import csv
import random



class Account:
    def __init__(self,ID,name,balance = 0):
        self.ID = ID
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:

            return False
        else:
            self.balance -= amount
            return True

    def transfer_money(self,cus2,amount):
        if self.balance < amount:
            return
        else:
            self.balance -= amount
            cus2.balance += amount
            return


    def check_balance(self):
        print(f"บัญชี {self.name} มีเงินในบัญชีคงเหลือ {self.balance} บาท")
class Bank:
    def __init__(self,list):
        self.accounts = list
        self.ID_acc_l = []
        for data in self.accounts:
            self.ID_acc_l.append(int(data[0]))


    def open_account(self,ID,name,balance):
        new_customer = Account(ID,name,balance)

        return new_customer

    def perform_transaction(self, new_customer, transaction_type, amount=None):
        amount = int(input("จำนวนเงินเท่าไหร่ :"))
        if amount < 0:
            print("จำนวนเงินผิดพลาด\n")
            return

        if transaction_type == 'deposit':
            new_customer.deposit(amount)
            self.accounts[self.ID_acc_l.index(int(new_customer.ID))][2] = new_customer.balance
            print(f"ทำรายการฝาก {amount} บาท สำเร็จ")

        elif transaction_type == 'withdraw':
            new_customer.withdraw(amount)
            if new_customer.withdraw(amount):
                self.accounts[self.ID_acc_l.index(int(new_customer.ID))][2] = new_customer.balance
                print(f"ทำรายการถอน {amount} บาท สำเร็จ")

            else:
                print("ยอดเงินในบัญชีคุณไม่พอสำหรับการถอนเงิน")
        elif transaction_type == 'transfer':
            if new_customer.balance > amount:
                cus2 = int(input("โอนไปบัญชีหมายเลขอะไร :"))
                if cus2 in self.ID_acc_l:
                    for data in self.accounts:
                        if cus2 == int(data[0]):
                            cus2 = self.open_account(data[0],data[1],data[2])
                    new_customer.transfer_money(cus2,amount)
                    self.accounts[self.ID_acc_l.index(int(cus2.ID))][2] =  cus2.balance
                    self.accounts[self.ID_acc_l.index(int(new_customer.ID))][2] = new_customer.balance
                    print(f"ทำรายการโอนเงินจากบัญชี {new_customer.name} ไปยังบัญชี {cus2.name} จำนวน {amount} บาท  สำเร็จ")
                else:
                    print("ไม่พบบัญชีสำหรับโอนเงิน\n")
                    return
            else:
                print("ยอดเงินในบัญชีตุณไม่พอสำหรับโอนเงิน")


        else:
            print("ประเภทของธุรกรรมไม่ถูกต้อง")
        new_customer.check_balance()
        print()

    def view_all_account(self,list):

        for data in self.accounts:
            print(data[0],data[1],data[2])

    def find_acc(self,ID):
        for data in self.accounts:
            if ID == int(data[0]):
                print(data[0],data[1],data[2])
                return data

        print("ไม่พบบัญชี")

    def edit_acc(self,ID):
        for data in self.accounts:
            if ID == int(data[0]):
                print(data[0],data[1],data[2])
                money = int(input(f"ต้องการเปลี่ยนยอดเงินในบัญชีชื่อ{data[1]}เป็นจำนวนเท่าไหร่? :"))
                if money >= 0:
                    self.accounts[self.ID_acc_l.index(int(ID))][2] = money
                    print("แก้ไขข้อมูลสำเร็จ\n")

                else:
                    print("ผิดพลาด\n")

                return

        print("ไม่พบบัญชีที่จะแ้กไข")
    # def edit_account(self,ID):
    #     for data in


# bank =Bank()
# cus1 = bank.open_account(data[0],data[1],data[2])
# bank.perform_transaction()

def customer(ID):
    for i in list_cus:
        id = int(i[0])
        if ID == id:
            cus1 = bank.open_account(i[0], i[1], i[2])
            print(f"สวัสดีตุณ {cus1.name}")
    while True:
                e = int(input("ต้องการทำธุรกรรม กด 1 \nเช็คยอดเงินคงเหลือ กด 2 \nออกจากระบบ กด 0\n:"))
                if e == 1:
                    while True:
                        cus1.check_balance()
                        w = int(input("ฝากเงิน กด 1\nถอนเงิน กด 2\nโอนเงิน กด 3 \nกลับไปหน้าต่างก่อน กด 0\n:"))

                        if w == 1:
                            w = "deposit"
                            bank.perform_transaction(cus1, w, amount=None)
                        elif w == 2:
                            w = "withdraw"
                            bank.perform_transaction(cus1, w, amount=None)
                        elif w == 3:
                            w = "transfer"
                            bank.perform_transaction(cus1,w,amount=None)
                        elif w == 0:
                            break
                        else:
                            print("\nเลือกธุรกรรมผิดพลาด\n")




                elif e == 2:
                    cus1.check_balance()
                    print()

                elif e ==0:
                    print("ิออกจากระบบเรียบร้อยแล้ว")
                    break
                else:
                    print("ผิดพลาด")



def admin():
    print("คุณได้เข้าสู่ระบบแอดมินเรียบร้อยแล้ว")
    print()
    while True:
        x = int(input("ต้องการเห็นทุกบัญชี กด 1\nหาข้อมูลบัญชี กด 2\nต้องการแก้ไขเงินในบัญชีหมายเลข ID ที่ระบุ กด 3\nออกจากระบบ กด 0\n:"))
        if x == 1:
            bank.view_all_account(list_cus)
            print()
        elif x == 2:
            while True:
                ID = int(input("คุณต้องการหาข้อมูลหมายเลขบัญชี ID อะไร ? ,ID = 0 เพื่อกลับมาหน้าต่างก่อน:" ))
                if ID ==0:
                    break
                bank.find_acc(ID)
        elif x == 3:
            ID = int(input("คูณต้องการเปลี่ยนเงินคงเหลือในบัญชีหมายเลข ID อะไร? :" ))
            bank.edit_acc(ID)
        elif x == 0:
            print("ิออกจากระบบเรียบร้อยแล้ว")
            start()


def start():
    while True:
        id_ip = int(input("ID :"))
        if id_ip == -1:
            admin()
            start()
        elif id_ip in [int(ID) for ID in bank.ID_acc_l]:
            customer(id_ip)
            start()
        elif id_ip == 0:
            out(bank.accounts)
            exit()

        else:
            print("ไม่พบบัญชีในระบบ")


def out(list):
    with open("out_put.csv","w",newline= "",encoding="utf-8")as f:
        fw = csv.writer(f)
        fw.writerows(list)

list_cus =[]
with open("Book1.csv","r",newline= "",encoding="utf-8")as f:
    fr = csv.reader(f)
    for data in fr:
        data.append(random.randint(1000,9000))
        list_cus.append(data)
list_cus = list_cus[1:]


bank = Bank(list_cus)
start()
out(bank.accounts)