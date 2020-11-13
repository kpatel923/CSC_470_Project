import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from borrower import *
from librarian import *
from search import *
from admin import *


# GUI FILE
##from Test import *

class Animation():
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70
            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            # ANIMATION
            self.animation = QPropertyAnimation(self.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()


class common_Buttons(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def home_screen(self):
        # PAGE home
        self.btn_home.clicked.connect(lambda: self.Pages_Widget.setCurrentWidget(self.page_home))
    def search_screen(self):
        # PAGE search
        self.btn_search.clicked.connect(lambda: self.Pages_Widget.setCurrentWidget(self.page_search))
    def librarian_screen(self):
        # PAGE librarian
        self.btn_librarian.clicked.connect(lambda: self.Pages_Widget.setCurrentWidget(self.page_Employee_Login))
        self.btn_librarian.clicked.connect(lambda: self.label_13.setText("Librarian Login Page"))
    def Admin_page(self):
        # PAGE Admin
        self.btn_admin.clicked.connect(lambda: self.Pages_Widget.setCurrentWidget(self.page_Employee_Login))
        self.btn_admin.clicked.connect(lambda: self.label_13.setText("Admin Login Page"))

class user_Buttons(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def forgot_password(self):
        # PAGE forgot_password
        self.btn_password.clicked.connect(lambda: Borrower.handleForgotPassword(self))

    def forgot_email(self):
        # PAGE forgot_email
        self.btn_username.clicked.connect(lambda: Borrower.handleForgotUsername(self))

    def signup_screen(self):
        # PAGE signup
        self.btn_signup.clicked.connect(lambda: self.Pages_Widget.setCurrentWidget(self.page_signup))

    def signup_screen_2(self):
        # PAGE signup_2
        self.btn_signup_2.clicked.connect(lambda: Signup.addNewUser(self))

    def user_screen(self):
        # PAGE user_screen
        self.btn_login.clicked.connect(lambda: Borrower.handleLogin(self))
        self.btn_modify.clicked.connect(lambda: Borrower.selection(self))
        self.btn_modify_2.clicked.connect(lambda: Borrower.modify(self))
        # self.btn_request.clicked.connect(lambda: Borrower.bookHold(self))


    def logout_screen(self):
        # PAGE logout
        self.btn_logout.clicked.connect(lambda: self.Pages_Widget.setCurrentWidget(self.page_home))

    def cancel(self):
        self.btn_cancel.clicked.connect(lambda: self.Pages_Widget.setCurrentWidget(self.page_home))
        self.btn_cancel_3.clicked.connect(lambda: self.Pages_Widget.setCurrentWidget(self.page_home))


class librarian_Buttons(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def Librarian_password(self):
        # PAGE forgot_password
        self.btn_Employee_password.clicked.connect(lambda: Librarian.handleForgotPassword(self))

    def Librarian_email(self):
        # PAGE forgot_email
        self.btn_Employee_email.clicked.connect(lambda: Librarian.handleForgotUsername(self))

    def Librarian_screen(self):
        # PAGE user_screen
        self.btn_Employee_login.clicked.connect(lambda: Librarian.handleLogin(self))
        self.btn_Scan.clicked.connect(lambda: Librarian.displayUser(self))
        self.btn_Checkout.clicked.connect(lambda: Librarian.bookTransaction(self))
        self.btn_selection.clicked.connect(lambda: Librarian.selection(self))
        self.btn_modifyL.clicked.connect(lambda: Librarian.modify(self))
        self.btn_Logout_3.clicked.connect(lambda: Librarian.logout_user(self))
        self.btn_Hold.clicked.connect(lambda: Librarian.bookHold(self))
        # self.refresh_CO.clicked.connect(lambda: Search.displayCheckOutBooks(self))
        # self.refresh_CO.clicked.connect(lambda: Search.displayBooksOnHold(self))


    def Librarian_logout(self):
        # PAGE logout
        self.btn_Logout.clicked.connect(lambda: self.Pages_Widget.setCurrentWidget(self.page_Employee_Login))

class admin_Buttons(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def Admin_logout(self):
        # PAGE logout
        self.btn_Logout_2.clicked.connect(lambda: self.Pages_Widget.setCurrentWidget(self.page_Employee_Login))

    def Admin_add(self):
        self.btn_signup_4.clicked.connect(lambda: Admin_Add.NewLibrarian(self))
        self.btn_selection_2.clicked.connect(lambda: Admin_Add.selection(self))
        self.btn_Scan_2.clicked.connect(lambda: Admin_Add.displayLib(self))
        self.btn_modifyL_2.clicked.connect(lambda: Admin_Add.modify(self))

    def Admin_addBook(self):
        self.btn_Checkin_4.clicked.connect(lambda: Admin.addBook(self))

    def Admin_removeBook(self):
        self.btn_Checkin_3.clicked.connect(lambda: Admin.removeBook(self))

class search_Buttons(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def search(self):
        self.btn_search_2.clicked.connect(lambda: Search.search(self))

