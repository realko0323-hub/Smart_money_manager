
# main.py
from Money_manager import AccountBook, SpendingAnalyzer, save_data, load_data, delete_data_file
import datetime


def get_user_input(book):
    print("\n---  스피드 한 줄 입력 모드 (종료: q) ---")
    print("입력 형식: [날짜] [카테고리] [금액] [메모] ***띄어 쓰기 한칸을 꼭 지켜주세요")
    print("예시 1: 2025-12-25 식비 -15000 크리스마스케이크")
    print("예시 2: . 용돈 50000 할머니 (날짜에 .을 찍으면 오늘 날짜!)")
    
    while True:
        
        user_line = input("\n입력 >> ")
        
        # 종료 조건
        if user_line.strip().lower() == 'q':
            print(" 입력을 마칩니다.")
            break
        
        # 1. 입력된 문자열을 공백(스페이스바) 기준으로 자르기
        parts = user_line.split()
        
        # 2. 개수 확인 (최소 4개 정보가 있어야 함)
        if len(parts) < 4:
            print(" 형식이 맞지 않습니다. 4가지 정보를 띄어쓰기로 입력해주세요.")
            continue
            
        # 3. 데이터 분배 (Parsing)
        date_str = parts[0]
        category = parts[1]
        amount_str = parts[2]
        
        note = " ".join(parts[3:]) 
        
        # 4. 날짜 처리
        input_date = None
        if date_str == '.': # 점(.)을 찍으면 오늘 날짜
            input_date = None 
        else:
            try:
                input_date = datetime.date.fromisoformat(date_str)
            except ValueError:
                print(" 날짜 형식이 올바르지 않습니다 (YYYY-MM-DD).")
                continue

        # 5. 금액 처리
        try:
            amount = int(amount_str)
        except ValueError:
            print(" 금액은 숫자만 입력해주세요.")
            continue
            
        # 6. 저장
        book.add(category, amount, note, date=input_date)
        print(f" [{category}] {amount}원 저장 완료!")

def main():
    print("===스마트 가계부 v2.0 (저장 기능 탑재)===")
    
    my_book = AccountBook()
    
    
    load_data(my_book)
    
    while True:
        print("\n---  메 뉴 ---")
        print("1. 스피드 한 줄 입력")
        print("2. 전체 내역 보기")
        print("3. 소비 패턴 분석 (텍스트)")
        print("4. 지출 그래프 (파이 차트)")
        print("5. AI 월말 예측 (회귀 분석)")
        print("6. CEO 엑셀 리포트 생성")
        print("7. 데이터 초기화")
        print("8. 저장하고 종료")
        choice = input("선택: ")
        if choice == '1':
            get_user_input(my_book)
        elif choice == '2':
            my_book.show_all()
        elif choice == '3':
            analyzer = SpendingAnalyzer(my_book)
            analyzer.report()
        elif choice == '4':
            analyzer = SpendingAnalyzer(my_book)
            analyzer.show_category_pie_chart()
        elif choice == '8': 
            save_data(my_book)
            print("프로그램을 종료합니다.")
            break
        elif choice == '7': 
            check = input("정말 모든 데이터를 삭제하시겠습니까? (y/n): ")
            if check.lower() == 'y':
                delete_data_file()
                my_book.clear_all()
                print(" 모든 데이터가 초기화되었습니다.")
        elif choice == '5':
            analyzer = SpendingAnalyzer(my_book)
            analyzer.predict_future()         
        elif choice == '6':
            analyzer = SpendingAnalyzer(my_book)
            analyzer.export_ceo_report()    
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()