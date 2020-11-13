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



class PasswordReset(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

    def getResetCode(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        if self.lineEdit_username_pass.text() == "":
            Messages_passsword.show_password_empty(self)

        else:
            self.cur.execute('''SELECT reset_code FROM codes''')
            codeFound = self.cur.fetchone()
            print(codeFound[0])
            Messages_passsword.code(self, codeFound[0])
            self.label_pass.clear()

    def insertCode(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()
        codeInput = self.lineEdit_username_code.text()

        self.cur.execute('''SELECT reset_code FROM codes''')
        match = self.cur.fetchone()

        if codeInput == match[0]:
            Messages.show_checkSuccess(self)
            print(match[0])
            self.lineEdit_pass1.setEnabled(True)
            self.lineEdit_pass2.setEnabled(True)
            self.label_pass.clear()

        else:
            print('No Match')
            Messages_passsword.invalid_code(self)

    def resetPassword(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        user_name = self.lineEdit_username_pass.text()
        new_pass = self.lineEdit_pass1.text()
        confirm_pass = self.lineEdit_pass2.text()

        if new_pass == confirm_pass:
            self.cur.execute('''UPDATE user SET user_password = %s WHERE user_name = %s''', (new_pass,user_name))
            self.db.commit()
            Messages_passsword.success(self)
            self.Pages_Widget.setCurrentWidget(self.page_home)
            Messages_passsword.resetAll(self)

        else:
            Messages_passsword.show_invalid_password(self)

    def cancelReset(self):
        self.Pages_Widget.setCurrentWidget(self.page_home)
        Messages_passsword.resetAll(self)

    def reset_Employee(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        user_name = self.lineEdit_username_pass.text()
        new_pass = self.lineEdit_pass1.text()
        confirm_pass = self.lineEdit_pass2.text()

        if new_pass == confirm_pass:
            self.cur.execute('''UPDATE user SET user_password = %s WHERE user_name = %s''', (new_pass, user_name))
            self.db.commit()
            Messages_passsword.success(self)
            self.Pages_Widget.setCurrentWidget(self.page_Employee_Login)
            Messages_passsword.resetAll(self)

        else:
            Messages_passsword.show_invalid_password(self)

    def cancel_Employee(self):
        self.Pages_Widget.setCurrentWidget(self.page_Employee_Login)
        Messages_passsword.resetAll(self)


