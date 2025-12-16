# money_manager/utils.py (전체 코드)
import csv
import os
import datetime # 날짜 변환을 위해 필요
from .models import Transaction

FILENAME = "my_account_book.csv"

def save_data(book):
    try:
        with open(FILENAME, mode='w', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])
            for tx in book.transactions:
                writer.writerow([tx.date, tx.category, tx.amount, tx.note])
        print(f"💾 데이터가 '{FILENAME}'에 안전하게 저장되었습니다.")
    except Exception as e:
        print(f"❌ 저장 중 오류 발생: {e}")

def load_data(book):
    if not os.path.exists(FILENAME):
        print("📂 저장된 파일이 없어 새로 시작합니다.")
        return

    try:
        with open(FILENAME, mode='r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            next(reader) 
            
            count = 0
            for row in reader:
                date_str, category, amount_str, note = row
                amount = int(amount_str)
                
                # 📌 [핵심 변경] 문자열('2025-12-16')을 진짜 날짜 객체로 변환
                # fromisoformat은 'YYYY-MM-DD' 형식을 날짜로 바꿔줍니다.
                date_obj = datetime.date.fromisoformat(date_str)
                
                # 날짜 정보까지 함께 추가
                book.add(category, amount, note, date=date_obj)
                count += 1
            
        print(f"📂 지난 내역 {count}건을 성공적으로 불러왔습니다!")
    except Exception as e:
        print(f"❌ 불러오기 실패: {e}")

def delete_data_file():
    if os.path.exists(FILENAME):
        try:
            os.remove(FILENAME)
            print(f"🗑️ '{FILENAME}' 파일이 완전히 삭제되었습니다.")
        except Exception as e:
            print(f"❌ 삭제 중 오류 발생: {e}")
    else:
        print("⚠️ 삭제할 데이터 파일이 없습니다.")