import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import MySQLdb
from messages import *



# Database connection
db_host = "localhost"
db_name = "library"
db_user = "lcs"
db_password = "root"



class UserReset(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

    def getResetCode(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        if self.lineEdit_username_2.text() == "":
            Messages_username.show_username_empty(self)

        else:
            self.cur.execute('''SELECT reset_code FROM codes''')
            codeFound = self.cur.fetchone()
            print(codeFound[0])
            Messages_passsword.code(self, codeFound[0])
            self.label_pass.clear()

    def insertCode(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()
        codeInput = self.lineEdit_username_code_2.text()

        self.cur.execute('''SELECT reset_code FROM codes''')
        match = self.cur.fetchone()

        if codeInput == match[0]:
            self.label_35.setText('Code accepted, Username displayed above.')
            username = self.lineEdit_username_2.text()
            print(match[0])
            self.label_username.setText(username)
            self.label_pass.clear()

        else:
            print('No Match')
            Messages_username.invalid_code(self)

    def cancelReset(self):
        self.Pages_Widget.setCurrentWidget(self.page_home)
        Messages_passsword.resetAll(self)

    def cancelResetEmployee(self):
        self.Pages_Widget.setCurrentWidget(self.page_Employee_Login)
        Messages_passsword.resetAll(self)

    def reset(self):
        Messages.show_checkSuccess(self)
        self.Pages_Widget.setCurrentWidget(self.page_home)
        Messages_passsword.resetAll(self)

    def reset_Employee(self):
        Messages.show_checkSuccess(self)
        self.Pages_Widget.setCurrentWidget(self.page_Employee_Login)
        Messages_passsword.resetAll(self)

    def delete(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()
        print('hello')
        user_name = self.lineEdit_name.text()
        print(user_name)

        warning = QMessageBox.warning(self, 'Delete', "Are you sure you want to delete?", QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            self.cur.execute('''DELETE FROM user WHERE user_name = %s ''', [(user_name)])
            self.db.commit()
            print('Success')
            self.Pages_Widget.setCurrentWidget(self.page_home)

    def deleteLib(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()
        print('hello')
        user_name = self.lbl_first_4.text()
        print(user_name)

        warning = QMessageBox.warning(self, 'Delete', "Are you sure you want to delete?", QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            self.cur.execute('''DELETE FROM user WHERE user_name = %s ''', [(user_name)])
            self.db.commit()
            print('Success')
            self.Pages_Widget.setCurrentWidget(self.page_home)

    def deleteAdmin(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()
        print('hello')
        user_name = self.librarian.text()
        print(user_name)

        warning = QMessageBox.warning(self, 'Delete', "Are you sure you want to delete?", QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            self.cur.execute('''DELETE FROM user WHERE user_name = %s ''', [(user_name)])
            self.db.commit()
            print('Success')
            self.Pages_Widget.setCurrentWidget(self.page_home)


class Signup(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)


    def addNewUser(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        user_name = self.lineEdit_11.text()
        user_password = self.lineEdit_14.text()
        user_retype = self.lineEdit_15.text()
        user_phone = self.lineEdit_12.text()
        user_email = self.lineEdit_13.text()

        # checking for matching passwords
        if user_password == user_retype:
            self.cur.execute('''
                INSERT INTO user (user_name, user_email, user_phone, user_password) 
                VALUES (%s , %s , %s , %s)
            ''', (user_name, user_email, user_phone, user_password))
            self.label_10.setText('Account Created')
            Messages.success(self)
            self.db.commit()
            self.Pages_Widget.setCurrentWidget(self.page_home)


        else:
            self.label_10.setText('Please enter a valid password twice')
            Messages_passsword.show_invalid_password(self)
