import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MySQLdb
import datetime
from xlrd import *
from xlsxwriter import *
from messages import *
from forgot_password import *
from username import *

# Database connection
db_host = "localhost"
db_name = "library"
db_user = "lcs"
db_password = "root"

class Borrower(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def handleLogin(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        self.cur.execute('''
              SELECT * FROM user WHERE user_name = %s and user_password = %s
              ''', (username, password))
        found = self.cur.fetchone()
        print(found)

        if found == None:
            Messages.show_login_empty(self)

        else:
            print('User Match')
            #Messages.displayUser(self)
            self.lbl_first.setText(found[1])
            self.label_name.setText(found[1])
            self.lbl_email.setText(found[2])
            self.lbl_first_ID.setText(str(found[0]))
            self.toolButton_11.setText(found[1])
            self.lbl_fines.setText(str(found[5]))
            self.lineEdit_username.clear()
            self.lineEdit_password.clear()
            self.label_home.clear()
            self.Pages_Widget.setCurrentWidget(self.page_user)

            # setting modify to the user info
            self.lineEdit_name.setText(found[1])
            self.lineEdit_email.setText(found[2])
            self.lineEdit_phone.setText(found[3])
            self.password_11.setText(str(found[5]))

###############################################################################################
            ####### Table for Check Out Books Borrower #######

            borrower_ID = str(found[0])
            trans = "Check Out"
            self.cur.execute('''SELECT book_code, book_name, to_date FROM day_transactions
                WHERE type = %s AND borrower = %s''', (trans, borrower_ID))
            data = self.cur.fetchall()

            print(data)
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_pos = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_pos)

###############################################################################################
            ####### Table for Hold Books Borrower #######

            # borrower_ID = str(found[0])
            trans = "Request hold"
            self.cur.execute('''SELECT book_code, book_name FROM day_transactions
                WHERE type = %s AND borrower = %s''', (trans, borrower_ID))
            data = self.cur.fetchall()

            print(data)
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_pos = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_pos)

    def handleForgotPassword(self):
        if self.lineEdit_username.text() == "":
            Messages_passsword.show_password_empty_home(self)

        else:
            self.lineEdit_username.clear()
            self.label_pass.clear()
            self.Pages_Widget.setCurrentWidget(self.page_passwordreset)
            self.btn_code.clicked.connect(lambda: PasswordReset.getResetCode(self))
            self.btn_enter.clicked.connect(lambda: PasswordReset.insertCode(self))
            self.btn_cancel_2.clicked.connect(lambda: PasswordReset.cancelReset(self))
            self.btn_reset.clicked.connect(lambda: PasswordReset.resetPassword(self))

    def handleForgotUsername(self):
        self.lineEdit_username.clear()
        self.label_pass.clear()
        self.Pages_Widget.setCurrentWidget(self.page_email_reset)
        self.btn_code_3.clicked.connect(lambda: UserReset.getResetCode(self))
        self.btn_code_4.clicked.connect(lambda: UserReset.insertCode(self))
        self.btn_cancel_3.clicked.connect(lambda: UserReset.cancelReset(self))
        self.btn_user_reset.clicked.connect(lambda: UserReset.reset(self))

    def selection(self):
        selection_type = self.comboBox_3.currentText()
        if selection_type == "Logout":
            self.Pages_Widget.setCurrentWidget(self.page_home)
        elif selection_type == "Modify":
            self.groupBox_30.setEnabled(True)
        elif selection_type == "Delete Account":
            UserReset.delete(self)


    def modify(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()
        user_name = self.lineEdit_name.text()
        email = self.lineEdit_email.text()
        phone = self.lineEdit_phone.text()
        new_pass = self.lineEdit_pass.text()
        confirm_pass = self.lineEdit_pass_2.text()
        print('Hello')

        if new_pass == confirm_pass:
            self.cur.execute('''UPDATE user SET user_password = %s, user_email = %s, user_phone = %s 
                WHERE user_name = %s''', (new_pass, email, phone, user_name))
            self.db.commit()
            print('Success')
            user = self.label_name.text()
            print(user)
            mod = '''SELECT user_email FROM user WHERE user_name = %s'''

            self.cur.execute(mod, [(user)])
            new = self.cur.fetchone()
            print(new)
            self.label_18.setText("Success")

        else:
            self.label_18.setText("Passwords must match")
            Messages_passsword.show_invalid_password(self)

    def bookHold(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        book_ID = self.first_3.text()
        if book_ID == "":
            print("Error")
            self.label_16.setText("Enter a Book ID")
        borrower_ID = self.lbl_first_ID.text()
        trans_type = self.comboBox.currentText()

        if trans_type == 'Request hold':
            search = '''SELECT * FROM book WHERE book_code = %s'''
            self.cur.execute(search, [(book_ID)])
            status = self.cur.fetchone()
            days_number = 0
            today_date = datetime.date.today()
            to_date = today_date + datetime.timedelta(days=days_number)
            print(status)

            if status[7] == "":
                print("Book Available")
                self.label_16.setText("Book Available for Check Out")
            elif status[7] == 'Request hold':
                print("Book already on hold")
                self.label_16.setText("Book Not Available for Hold")
            elif status[7] == 'Check Out' or status[7] == 'Renew':
                self.cur.execute('''
                    INSERT INTO day_transactions(book_code, book_name, borrower, type, days, date, to_date)
                    VALUES (%s , %s , %s , %s , %s , %s, %s)''',
                                 (book_ID, status[2], borrower_ID, trans_type, days_number, today_date, to_date))
                self.cur.execute('''UPDATE book SET book_status = %s WHERE book_code = %s''', (trans_type, book_ID))
                self.label_16.setText("Book Hold Requested")
                self.db.commit()
        elif trans_type == 'Remove hold':
            search = '''SELECT * FROM book WHERE book_code = %s'''
            self.cur.execute(search, [(book_ID)])
            status = self.cur.fetchone()
            days_number = 0
            today_date = datetime.date.today()
            to_date = today_date + datetime.timedelta(days=days_number)
            print(status)
            if status[7] == 'Request hold':
                self.cur.execute('''UPDATE book SET book_status = NULL WHERE book_code = %s''', ([(book_ID)]))
                self.cur.execute('''
                    INSERT INTO day_transactions(book_code, book_name, borrower, type, days, date, to_date)
                    VALUES (%s , %s , %s , %s , %s , %s, %s)''',
                                 (book_ID, status[2], borrower_ID, trans_type, days_number, today_date, to_date))
                self.db.commit()
                self.label_16.setText("Book Hold Removed")
