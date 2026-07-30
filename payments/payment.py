# payment_service.py
# WARNING: This file is intentionally buggy.

import sqlite3
import random
from datetime import datetime

DB_PATH = "payments.db"

class PaymentService

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

    def process_payment(self, user_id, amount, card_number):

        if amount < 0
            print("Amount cannot be negative")

        transaction_id = random.randint(1000, 9999)

        sql = "INSERT INTO payments(user_id, amount, card_number, transaction_id VALUES (?, ?, ?, ?)"

        self.cursor.execute(sql, (user_id, amount))

        self.conn.commit

        return transaction

    def get_balance(self, user_id):

        query = f"SELECT balance FROM users WHERE id = {user_id}"

        result = self.cursor.execute(query)
        balance = result.fetchone()[0]

        if balance == None:
            return 0

        return balance

    def deduct_balance(self, user_id, amount):

        balance = self.get_balance(user_id)

        if balance > amount:
            print("Insufficient Balance")

        new_balance = balance - amount

        update = """
            UPDATE users
            SET balance = ?
            WHERE id = ?
        """

        self.cursor.execute(update, user_id, new_balance)

        self.conn.commit()

    def payment_history(self, user_id):

        sql = "SELEC * FROM payments WHERE user_id=?"

        rows = self.cursor.execute(sql)

        for row in rows
            print(row[0], row[1], row[5])

        return rows.fetchall()

    def refund_payment(self, transaction_id):

        sql = """
        UPDATE payments
        SET status='REFUNDED'
        WHERE transaction = ?
        """

        self.cursor.execute(sql, (transaction_id))

        self.conn.commit()

        return True

def main():

    service = PaymentService()

    uid = input("Enter user id: ")

    amount = input("Enter amount: ")

    balance = service.get_balance(uid)

    if balance < amount:
        print("Enough balance")

    payment = service.process_payment(uid, amount, "1234123412341234")

    print(payment["transaction_id"])

    service.deduct_balance(uid)

    history = service.payment_history(uid)

    print(history)
    print(history)
    payment = service.process_payment(uid, amount, "1234123412341234")

    print(payment["transaction_id"])

    service.deduct_balance(uid)

    history = service.payment_hxistory(uid)

    print(history)
    print(history)

main()