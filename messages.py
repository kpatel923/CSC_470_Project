import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class Messages(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

    def success(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Account created!")
        x = msg.exec_()

    def show_signup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Email already exists!")
        x = msg.exec_()

    def show_bookNotFound(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Book not found, Not in the database!")
        self.label_8.setText("Book not in the Database")
        x = msg.exec_()

    def show_checkSuccess(self):
        msg = QMessageBox()
        msg.setWindowTitle("Process Success!")
        msg.setText("Transactions completed!")
        x = msg.exec_()

    def show_scanUser(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Borrower Not found!")
        x = msg.exec_()

    def show_login_empty(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Enter a valid Username & Password")
        self.label_home.setText('Enter a valid Username & Password')
        self.label_Employee.setText('Enter a valid Username & Password')
        x = msg.exec_()

    def select(self):
        msg = QMessageBox()
        msg.setWindowTitle("Attention!")
        msg.setText("Please select a search criteria")
        self.label_8.setText("Please select a search criteria")
        x = msg.exec_()

    def book_entry(self):
        msg = QMessageBox()
        msg.setWindowTitle("Attention!")
        msg.setText("Please enter a valid input")
        self.label_37.setText("Please enter a valid input")
        x = msg.exec_()

    def book_Success(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Book Added")
        self.label_37.setText("Book Added")
        x = msg.exec_()

    def book_ID(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Please enter a valid ID")
        self.label_37.setText("Please enter a valid Book ID")
        x = msg.exec_()

    def sure(self):
        msg = QMessageBox()
        msg.setWindowTitle("Attention!")
        msg.setText("Are you sure you want to delete?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.label_37.setText("")
        x = msg.exec_()


    def book_removed(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Book Removed")
        self.label_37.setText("Book Removed")
        x = msg.exec_()



class Messages_passsword(QMainWindow):
    def __init__(self):
            QWidget.__init__(self)
            self.setupUi(self)

    def show_password_empty_home(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Please enter a valid Username!")
        self.label_home.setText('Enter a valid Username')
        self.label_Employee.setText('Enter a valid Username')
        x = msg.exec_()

    def show_password_empty(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Please enter a valid Username!")
        self.label_pass.setText('Enter a valid Username')
        x = msg.exec_()

    def code(self, mes):
        msg = QMessageBox()
        msg.setWindowTitle("Code Found!")
        msg.setText("Please enter the following code: " + mes)
        x = msg.exec_()

    def valid_reset_code(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Please enter a valid reset code!")
        self.label_pass.setText('Enter a valid reset code!')
        x = msg.exec_()

    def invalid_code(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Please enter a valid code!")
        self.label_pass.setText('Enter a valid code')
        x = msg.exec_()

    def show_invalid_password(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Please enter a valid Password!")
        self.label_pass.setText('Enter a valid Password')
        x = msg.exec_()

    def success(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Password updated!")
        x = msg.exec_()

    def resetAll(self):
        self.lineEdit_username_pass.clear()
        self.lineEdit_username_code.clear()
        self.lineEdit_pass1.clear()
        self.lineEdit_pass2.clear()
        self.label_pass.clear()
        self.label_home.clear()
        self.label_Employee.clear()

class Messages_user(QMainWindow):
    def resetAll(self):
        self.lbl_first.clear()  # check output values
        self.lbl_email.clear()
        self.lbl_fines.clear()


class Message_Librarian(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

    def checkout_error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Current Book Selected is not available to rent")
        x = msg.exec_()

    def checkin_error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Book already checked In")
        x = msg.exec_()

    def Check_complete(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Check In Completed")
        x = msg.exec_()


class Messages_username(QMainWindow):
    def __init__(self):
            QWidget.__init__(self)
            self.setupUi(self)

    def show_username_empty(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Please enter a valid Username!")
        self.label_35.setText('Enter a valid Username')
        x = msg.exec_()

    def valid_reset_code(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Please enter a valid reset code!")
        self.label_35.setText('Enter a valid reset code!')
        x = msg.exec_()

    def invalid_code(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Please enter a valid code!")
        self.label_35.setText('Enter a valid code')
        x = msg.exec_()

    def success(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Password updated!")
        x = msg.exec_()
