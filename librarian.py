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
from search import *
from username import *

# Database connection
db_host = "localhost"
db_name = "library"
db_user = "lcs"
db_password = "root"


class Librarian(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def handleLogin(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        username = self.lineEdit_U_L.text()
        password = self.lineEdit_P_L.text()

        self.cur.execute('''
            SELECT * FROM user WHERE user_name = %s and user_password = %s
            ''', (username, password))
        found = self.cur.fetchone()
        print(found)

        if found == None:
            Messages.show_login_empty(self)

        else:
            if username == "Jean":
                self.Pages_Widget.setCurrentWidget(self.page_Admin)
                print('User Match')
                self.toolButton_12.setText(found[1])
                self.lineEdit_U_L.clear()
                self.lineEdit_P_L.clear()
                self.label_Employee.clear()

            else:
                print('User Match')
                self.toolButton_10.setText(found[1])
                self.lineEdit_U_L.clear()
                self.lineEdit_P_L.clear()
                self.label_Employee.clear()
                self.Pages_Widget.setCurrentWidget(self.page_Librarian)

    def handleForgotPassword(self):
        if self.lineEdit_U_L.text() == "":
            Messages_passsword.show_password_empty_home(self)

        else:
            self.lineEdit_U_L.clear()
            self.label_pass.clear()

            self.Pages_Widget.setCurrentWidget(self.page_passwordreset)
            self.btn_code.clicked.connect(lambda: PasswordReset.getResetCode(self))
            self.btn_enter.clicked.connect(lambda: PasswordReset.insertCode(self))
            self.btn_cancel_2.clicked.connect(lambda: PasswordReset.cancel_Employee(self))
            self.btn_reset.clicked.connect(lambda: PasswordReset.reset_Employee(self))

    def handleForgotUsername(self):
        self.lineEdit_username.clear()
        self.label_pass.clear()
        self.Pages_Widget.setCurrentWidget(self.page_email_reset)
        self.btn_code_3.clicked.connect(lambda: UserReset.getResetCode(self))
        self.btn_code_4.clicked.connect(lambda: UserReset.insertCode(self))
        self.btn_cancel_3.clicked.connect(lambda: UserReset.cancelResetEmployee(self))
        self.btn_user_reset.clicked.connect(lambda: UserReset.reset_Employee(self))

    def displayUser(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        borrower_ID = self.first_6.text()

        if borrower_ID == "":
            print("Error")
            self.label_26.setText("Enter a Borrower ID")
        else:
            self.label_26.clear()
            sql = ''' SELECT * FROM user WHERE id_user = %s '''
            self.cur.execute(sql, [(borrower_ID)])
            data = self.cur.fetchone()
            print(data[1])

            self.lbl_first_2.setText(data[1])
            self.lbl_first_4.setText(data[1])
            self.lbl_email_2.setText(data[2])
            self.lbl_fines_2.setText(str(data[5]))

            # setting modify to the user info
            self.lineEdit_name2.setText(data[1])
            self.lineEdit_email2.setText(data[2])
            self.lineEdit_phone2.setText(data[3])
            self.password_12.setText(str(data[5]))

            trans = "Check Out"
            self.cur.execute('''SELECT book_code, book_name, to_date FROM day_transactions 
                WHERE type = %s AND borrower = %s''', (trans, borrower_ID))
            data = self.cur.fetchall()

            print(data)
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_pos = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_pos)

            trans = "Request hold"
            self.cur.execute('''SELECT book_code, book_name, to_date FROM day_transactions 
                            WHERE type = %s AND borrower = %s''', (trans, borrower_ID))
            data = self.cur.fetchall()

            print(data)
            self.tableWidget_5.setRowCount(0)
            self.tableWidget_5.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_pos = self.tableWidget_5.rowCount()
                self.tableWidget_5.insertRow(row_pos)

    def logout_user(self):
        self.first_6.clear()
        self.lbl_first_2.clear()
        self.lbl_first_4.clear()
        self.lbl_email_2.clear()
        self.lbl_fines_2.clear()
        # setting modify to the user info
        self.lineEdit_name2.clear()
        self.lineEdit_email2.clear()
        self.lineEdit_phone2.clear()
        self.password_12.clear()
        self.tableWidget_4.clear()

    def selection(self):
        selection_type = self.comboBox_4.currentText()
        if selection_type == "Logout":
            self.Pages_Widget.setCurrentWidget(self.page_Employee_Login)
        elif selection_type == "Modify":
            self.groupBox_35.setEnabled(True)
        elif selection_type == "Report":
            borrowerBookReport(self)
        elif selection_type == "Delete Account":
            UserReset.deleteLib(self)
        elif selection_type == "Add Borrower":
            self.Pages_Widget.setCurrentWidget(self.page_signup)


    def modify(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()
        user_name = self.lbl_first_4.text()
        email = self.lineEdit_email2.text()
        phone = self.lineEdit_phone2.text()
        new_pass = self.lineEdit_passL.text()
        confirm_pass = self.lineEdit_passL2.text()

        if new_pass == confirm_pass:
            self.cur.execute(
                '''UPDATE user SET user_password = %s, user_email = %s, user_phone = %s WHERE user_name = %s''',
                (new_pass, email, phone, user_name))
            self.db.commit()
            print('Success')
            self.label_29.setText("Success")
        else:
            self.label_29.setText("Passwords must match")
            Messages_passsword.show_invalid_password(self)

    def bookTransaction(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        book_ID = self.first_7.text()
        if book_ID == "":
            print("Error")
            self.label_20.setText("Enter a Book ID")
        borrower_ID = self.first_6.text()
        trans_type = self.comboBox_5.currentText()

        if trans_type == 'Check Out':
            search = '''SELECT * FROM book WHERE book_code = %s'''
            self.cur.execute(search, [(book_ID)])
            status = self.cur.fetchone()
            days_number = 21
            today_date = datetime.date.today()
            to_date = today_date + datetime.timedelta(days=days_number)
            print(status)
            if status[7] == 'Check Out' or status[7] == 'Renew' or status[7] == 'Request hold':
                self.label_20.setText("Book Selected is not available")
                Message_Librarian.checkout_error(self)
            else:  # status == 'Check In':
                self.label_20.clear()
                self.cur.execute('''UPDATE book SET book_status = %s WHERE book_code = %s''', (trans_type, book_ID))
                print(book_ID, " Checked out from: ", today_date, "to ", to_date)
                self.cur.execute('''
                    INSERT INTO day_transactions(book_code, book_name, borrower, type, days, date, to_date)
                    VALUES (%s , %s , %s , %s , %s , %s, %s)''',
                                 (book_ID, status[2], borrower_ID, trans_type, days_number, today_date, to_date))

                self.db.commit()
                Messages.show_checkSuccess(self)

        elif trans_type == 'Renew':
            search = '''SELECT * FROM book WHERE book_code = %s'''
            self.cur.execute(search, [(book_ID)])
            status = self.cur.fetchone()
            days_number = 21
            today_date = datetime.date.today()
            to_date = today_date + datetime.timedelta(days=days_number)
            print(status)
            if status[7] == 'Check Out' or status[7] == 'Renew' or status[7] == 'Request hold':
                self.label_20.setText("Book Selected is not available")
                Message_Librarian.checkout_error(self)
            else:  # status == 'Check In':
                self.label_20.clear()
                self.cur.execute('''UPDATE book SET book_status = %s WHERE book_code = %s''', (trans_type, book_ID))
                print(book_ID, " Checked out from: ", today_date, "to ", to_date)
                self.cur.execute('''
                    INSERT INTO day_transactions(book_code, book_name, borrower, type, days, date, to_date)
                    VALUES (%s , %s , %s , %s , %s , %s, %s)''',
                                 (book_ID, status[2], borrower_ID, trans_type, days_number, today_date, to_date))

                self.db.commit()
                Messages.show_checkSuccess(self)



        elif trans_type == 'Check In':
            days_number = 0
            today_date = datetime.date.today()
            to_date = today_date + datetime.timedelta(days=days_number)
            search = '''SELECT * FROM book WHERE book_code = %s'''
            self.cur.execute(search, [(book_ID)])
            status = self.cur.fetchone()
            if status[7] == 'Check Out' or status[7] == 'Renew':
                self.cur.execute('''DELETE FROM day_transactions WHERE book_code = %s''', [(book_ID)])
                self.cur.execute('''UPDATE book SET book_status = NULL WHERE book_code = %s''', [(book_ID)])
                print(book_ID, " Checked In: ", today_date)
                self.cur.execute('''
                    INSERT INTO day_transactions(book_code, book_name, borrower, type, days, date, to_date)
                    VALUES (%s , %s , %s , %s , %s , %s, %s)''',
                                 (book_ID, status[2], borrower_ID, trans_type, days_number, today_date, to_date))
                self.label_20.setText("Checked In")
                self.db.commit()
                Message_Librarian.Check_complete(self)
            else:
                self.label_20.setText("Book Returned Already")
                Message_Librarian.checkin_error(self)

    def bookHold(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        book_ID = self.first_9.text()
        if book_ID == "":
            print("Error")
            self.label_21.setText("Enter a Book ID")
        borrower_ID = self.first_6.text()
        trans_type = self.comboBox_6.currentText()

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
                self.label_21.setText("Book Available for Check Out")
            elif status[7] == 'Request hold':
                print("Book already on hold")
                self.label_21.setText("Book Not Available for Hold")
            elif status[7] == 'Check Out' or status[7] == 'Renew':
                self.cur.execute('''
                    INSERT INTO day_transactions(book_code, book_name, borrower, type, days, date, to_date)
                    VALUES (%s , %s , %s , %s , %s , %s, %s)''',
                                 (book_ID, status[2], borrower_ID, trans_type, days_number, today_date, to_date))
                self.cur.execute('''UPDATE book SET book_status = %s WHERE book_code = %s''', (trans_type, book_ID))
                self.label_21.setText("Book Hold Requested")
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
                self.cur.execute('''UPDATE book SET book_status = %s WHERE book_code = %s''', (trans_type, book_ID))
                self.cur.execute('''
                    INSERT INTO day_transactions(book_code, book_name, borrower, type, days, date, to_date)
                    VALUES (%s , %s , %s , %s , %s , %s, %s)''',
                                 (book_ID, status[2], borrower_ID, trans_type, days_number, today_date, to_date))
                self.db.commit()
                self.label_21.setText("Book Hold Removed")



def borrowerBookReport(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        borrower_ID = self.first_6.text()

        self.cur.execute('''SELECT book_name,borrower,type,date,to_date 
            FROM day_transactions WHERE borrower = %s''', [(borrower_ID)])

        data = self.cur.fetchall()

        wb = Workbook('borrower_checkout.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0,0,'book title')
        sheet1.write(0,1,'borrower ID')
        sheet1.write(0,2,'type')
        sheet1.write(0,3,'from date')
        sheet1.write(0,4,'to date')

        row_num = 1
        for row in data:
            column_num = 0
            for item in row:
                sheet1.write(row_num,column_num,str(item))
                column_num += 1
            row_num += 1

        wb.close()
        QMessageBox.information(self,'Done',"Report Created Successfully", QMessageBox.Ok)

