

import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.linear_model import LinearRegression 
import datetime
import calendar
import numpy as np

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

class SpendingAnalyzer:
    def __init__(self, book):
        self.book = book

 

    def predict_future(self):
        """회귀 분석(Linear Regression)을 이용한 월말 지출 예측"""
        tx_list = self.book.get_transactions()
        
        
        data = []
        for tx in tx_list:
            # 지출 내역(음수)만 가져오고, 절대값으로 변환
            if tx.amount < 0:
                data.append({'date': tx.date, 'amount': abs(tx.amount)})
        
        if not data:
            print(" 분석할 지출 데이터가 없습니다.")
            return

        df = pd.DataFrame(data)
        
        # 2. 날짜별로 합치기 
        daily_df = df.groupby('date')['amount'].sum().reset_index()
        
        # 3. '누적 지출액' 계산 
        daily_df['cumulative'] = daily_df['amount'].cumsum()
        
        # 4. 학습 데이터 준비 
        daily_df['day_num'] = daily_df['date'].apply(lambda x: x.day)
        
        # 데이터가 너무 적으면 회귀 분석 불가
        if len(daily_df) < 2:
            print(" 데이터가 너무 적어 추세를 분석할 수 없습니다. (최소 2일치 필요)")
            return

        X = daily_df[['day_num']] 
        y = daily_df['cumulative']

        # 5. 선형 회귀 모델 학습 
        model = LinearRegression()
        model.fit(X, y)

        # 6. 미래 예측 
        today = datetime.date.today()
        last_day = calendar.monthrange(today.year, today.month)[1]
        
        # 이번 달의 마지막 날의 누적 지출액 예측
        predicted_total = model.predict([[last_day]])[0]
        
        # 7. 결과 출력
        slope = model.coef_[0] 
        
        print("\n---  AI 회귀 분석 리포트 ---")
        print(f" 분석 기간: {daily_df['day_num'].min()}일 ~ {daily_df['day_num'].max()}일")
        print(f" 현재 누적 지출: {int(daily_df['cumulative'].iloc[-1]):,}원")
        print(f" 소비 가속도(기울기): 하루 약 {int(slope):,}원씩 쓰는 중")
        print(f"----------------------------------")
        print(f" 회귀 분석 결과 월말 예상: {int(predicted_total):,}원")
        
        # 8. 시각화 
        self.show_regression_graph(daily_df, model, last_day)

    def show_regression_graph(self, df, model, last_day):
        """실제 데이터(산점도)와 예측된 회귀선(라인)을 시각화"""
        plt.figure(figsize=(10, 6))
        
        # A. 실제 데이터 점 찍기
        plt.scatter(df['day_num'], df['cumulative'], color='blue', label='실제 지출(누적)')
        
        # B. 회귀선 그리기 (1일 ~ 말일)
        future_days = np.arange(1, last_day + 1).reshape(-1, 1) 
        future_predict = model.predict(future_days) 
        
        plt.plot(future_days, future_predict, color='red', linestyle='--', label='AI 예측 추세선')
        
        # C. 그래프 꾸미기
        plt.title(f'이번 달 지출 추세 및 예측 (Linear Regression)')
        plt.xlabel('날짜 (일)')
        plt.ylabel('누적 지출액 (원)')
        plt.legend()
        plt.grid(True, linestyle=':', alpha=0.6)
        
        # 월말 예측 지점 표시
        plt.scatter([last_day], [future_predict[-1]], color='red', marker='*', s=150, zorder=5)
        plt.text(last_day, future_predict[-1], f'{int(future_predict[-1]):,}원', 
                ha='right', va='bottom', fontsize=12, fontweight='bold', color='red')

        plt.show()
        
        
    def export_ceo_report(self):
            """전체 내역, 카테고리별 통계, 일별 통계를 엑셀 파일 하나로 예쁘게 저장"""
            tx_list = self.book.get_transactions()
            if not tx_list:
                print("데이터가 없어서 보고서를 만들 수 없습니다.")
                return

            # 1. 데이터 준비 (DataFrame 변환)
            data = []
            for tx in tx_list:
                data.append({
                    '날짜': tx.date,
                    '카테고리': tx.category,
                    '금액': tx.amount,
                    '메모': tx.note
                })
            df = pd.DataFrame(data)

            # 2. 통계 데이터 만들기
            # 카테고리별 합계 (지출만)
            cat_summary = df[df['금액'] < 0].groupby('카테고리')['금액'].sum().abs().reset_index()
            cat_summary.columns = ['카테고리', '지출합계']
            cat_summary = cat_summary.sort_values(by='지출합계', ascending=False)

            # 일별 합계
            daily_summary = df.groupby('날짜')['금액'].sum().reset_index()
            daily_summary.columns = ['날짜', '순수익(수입-지출)']

            # 3. 엑셀로 저장 
            filename = "CEO_Financial_Report.xlsx"
            
            try:
                
                with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                    # 시트 1: 원본 데이터
                    df.to_excel(writer, sheet_name='전체내역', index=False)
                    
                    # 시트 2: 카테고리 분석
                    cat_summary.to_excel(writer, sheet_name='카테고리별_분석', index=False)
                    
                    # 시트 3: 일별 흐름
                    daily_summary.to_excel(writer, sheet_name='일별_손익', index=False)
                
                print(f"\n [성공] '{filename}' 파일이 생성되었습니다!")
                print(f" 폴더를 열어서 엑셀 파일을 확인해보세요. 교수님이 감동하실 겁니다.")
                
            except Exception as e:
                print(f" 엑셀 저장 중 오류 발생: {e}")
                print("팁: 혹시 엑셀 파일을 열어놓고 계신가요? 끄고 다시 시도해보세요.")