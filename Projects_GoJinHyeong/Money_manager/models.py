
import datetime

class Transaction:
    
    def __init__(self, category, amount, note, date=None):
        if date is None:
            self.date = datetime.date.today() # 날짜 없으면 오늘
        else:
            self.date = date # 입력받은 날짜 저장
        
        self.category = category
        self.amount = amount
        self.note = note
    
    def __str__(self):
        return f"[{self.date}] {self.category}: {self.amount}원 ({self.note})"

class AccountBook:
    def __init__(self):
        self.transactions = []

    
    def add(self, category, amount, note, date=None):
        self.transactions.append(Transaction(category, amount, note, date))
        
        self.transactions.sort(key=lambda x: x.date)
    
    def get_transactions(self):
        return self.transactions

    def show_all(self):
        if not self.transactions:
            print("아직 등록된 거래 내역이 없습니다.")
            return

        print("\n---  전체 거래 내역 (날짜순) ---")
        for i, tx in enumerate(self.transactions):
            print(f"{i+1}. {tx}")
        print(f" 현재 잔액: {self.get_balance()}원")

    def get_balance(self):
        total = sum([tx.amount for tx in self.transactions])
        return total

    def clear_all(self):
        self.transactions = []