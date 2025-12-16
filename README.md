# Smart_money_manager
대학생들의 늘어나는 돈 낭비를 줄이기 위해 만든 스마트 가계부
기능은 다음과 같다.
1. 지출 및 수익 입력 기능( 날짜 카테고리 금액 메모) 의 형식으로 입력을 받는다.
2. 전체 내역 보기.
3. 소비 패턴 분석(텍스트)
4. 지출 그래프 (파이차트)
5. 회귀 분석을 통한 월말 총 지출 예상
6. 위의 내용들을 종합적으로 알려주는 엑셀 리포트 생성
7. 데이터 초기화
8. 저장하고 종료

실행 결과
1. 지출 및 수익 입력 기능: 1을 누르고 엔터. 날짜 카테고리 금액 메모 형식에 맞춰서 입력. 입력을 그만하고 싶을 때는 입력창에 q를 입력
   <img width="871" height="1277" alt="image" src="https://github.com/user-attachments/assets/fd6837d3-2c26-46b9-a13c-f6b0bbe6e11f" />
2. 전체 내역 보기 기능: 2를 누르고 엔터.

   <img width="498" height="582" alt="image" src="https://github.com/user-attachments/assets/b13fcd5e-cf00-4650-ad8f-a5d85d723049" />
3. 소비 패턴 분석(텍스트): 수익보다 지출이 높다면 경고 멘트가, 수익이 지출보다 높다면 칭찬멘트가 나온다

   <img width="414" height="436" alt="image" src="https://github.com/user-attachments/assets/90680be9-3041-442a-a7f4-c261d7ba7150" />
4. 지출 그래프(파이 차트) 카테고리별로 총 지출의 몇 퍼세트를 차지하는 지를 파티차트로 보여준다

   <img width="1198" height="1172" alt="image" src="https://github.com/user-attachments/assets/f522122e-a730-42ee-adad-795ac8d39556" />
5. 회귀 분석을 통한 월말 총 지출 예상: 날짜 별로 지출을 묶어서 선형회귀 분석을 진행. 월말 최종 지출을 예상하는 그래프를 보여줌

   <img width="1501" height="996" alt="image" src="https://github.com/user-attachments/assets/1435d68d-02bb-4089-850f-f25bd3304d48" />
6. 엑셀 리포트: 자신이 입력한 값들을 엑셀파일로 만들어준다.

<img width="416" height="282" alt="image" src="https://github.com/user-attachments/assets/fe6b9bad-ccec-469a-8058-f8d8a1092eb9" />

7. 데이터 초기화: 월초가 되면 지금까지 저장해 두었던 값들을 초기화 해야하므로 추가하였다.
   
   <img width="592" height="122" alt="image" src="https://github.com/user-attachments/assets/c678daa1-90f0-4c40-971f-afb8fa569ac0" />

8. 저장하고 종료: 입력한 값들을 저장하고 프로그램을 종료한다.




