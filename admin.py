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


class Admin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def addBook(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        book_title = self.book_Title.text()
        book_code = self.book_ID.text()
        book_subject = self.book_Subject.text()
        book_author = self.book_Author.text()
        book_description = self.book_Description.toPlainText()
        book_price = self.book_Price.text()
        if book_title == "" or book_code == "" or book_subject == "" or book_author == "" or book_description == "" or book_price == "" == "":
            QMessageBox.warning(self, 'Error', "Please enter a valid input", QMessageBox.Close)

        else:
            self.cur.execute('''
                INSERT INTO book (book_code,book_name,book_subject,book_author,book_description,book_price)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (book_code, book_title, book_subject, book_author, book_description, book_price))

            self.db.commit()
            # we can change this to the message boxes used everywhere else
            QMessageBox.information(self, 'Done', "New Book Added", QMessageBox.Close)

    def removeBook(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        book_code = self.first_13.text()
        if book_code == "":
            QMessageBox.warning(self, 'Error', "Please enter a valid book ID", QMessageBox.Close)
        else:
            # we can change this message box for another one
            warning = QMessageBox.warning(self, 'Delete Book', "Are you sure you want to delete this book?",
                                          QMessageBox.Yes | QMessageBox.No)
            if warning == QMessageBox.Yes:
                delete = '''DELETE FROM book WHERE book_code = %s '''
                self.cur.execute(delete, [(book_code)])
                self.db.commit()
                QMessageBox.information(self, 'Done', "Book Deleted", QMessageBox.Close)




class Admin_Add(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def NewLibrarian(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        user_name = self.lineEdit_45.text()
        user_password = self.lineEdit_48.text()
        user_retype = self.lineEdit_49.text()
        user_phone = self.lineEdit_46.text()
        user_email = self.lineEdit_47.text()

        if user_name == "" or user_password == "" or user_email == "" or user_phone == "" or user_retype == "":
            QMessageBox.warning(self, 'Error', "Please enter a valid input", QMessageBox.Close)

        else:
            # checking for matching passwords
            if user_password == user_retype:
                self.cur.execute('''
                           INSERT INTO user (user_name, user_email, user_phone, user_password) 
                           VALUES (%s , %s , %s , %s)
                       ''', (user_name, user_email, user_phone, user_password))
                self.label_36.setText('Account Created')
                self.db.commit()

            else:
                self.label_36.setText('Please enter a valid password twice')
                Messages_passsword.show_invalid_password(self)

    def selection(self):
        selection_type = self.comboBox_7.currentText()
        if selection_type == "Modify":
            self.groupBox_37.setEnabled(True)
        elif selection_type == "Delete Account":
            UserReset.deleteAdmin(self)

    def displayLib(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        user_name = self.librarian.text()

        if user_name == "":
            print("Error")
            Messages_username.show_username_empty(self)
            self.label_31.setText("Enter a Librarian name")
        else:
            self.label_31.clear()
            sql = ''' SELECT * FROM user WHERE user_name = %s '''
            self.cur.execute(sql, [(user_name)])
            data = self.cur.fetchone()
            if data == ():
                Messages_username.show_username_empty(self)
                self.label_31.setText("Librarian name not found")

            else:
                print(data[1])
                self.lineEdit_name2_2.setText(data[1])
                self.lineEdit_email2_2.setText(data[2])
                self.lineEdit_phone2_2.setText(data[3])
                self.label_31.clear()

    def modify(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        user_name = self.lineEdit_name2_2.text()
        email = self.lineEdit_email2_2.text()
        phone = self.lineEdit_phone2_2.text()
        new_pass = self.lineEdit_passL_2.text()
        confirm_pass = self.lineEdit_passL2_2.text()

        if new_pass == "" or confirm_pass == "":
            self.label_31.setText("Enter a valid password")
            Messages_passsword.show_invalid_password(self)

        else:
            if new_pass == confirm_pass:
                self.cur.execute(
                    '''UPDATE user SET user_password = %s, user_email = %s, user_phone = %s WHERE user_name = %s''',
                    (new_pass, email, phone, user_name))
                self.db.commit()
                print('Success')
                self.label_31.setText("Success")
            else:
                self.label_31.setText("Passwords must match")
                Messages_passsword.show_invalid_password(self)