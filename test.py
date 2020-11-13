import sys
import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import MySQLdb


#Files
from actions import *
from search import *


# GUI FILE
# Database connection
db_Host = "localhost"
db_Name = "library"
db_User = "lcs"
db_Password = "root"


ui,_ = loadUiType('ui_main.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # Search.displayCheckOutBooks(self)
        # Search.displayBooksOnHold(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.Btn_Toggle.clicked.connect(lambda: Animation.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE Common
        common_Buttons.home_screen(self)
        common_Buttons.search_screen(self)
        common_Buttons.librarian_screen(self)
        common_Buttons.Admin_page(self)

        # PAGE user_login
        user_Buttons.forgot_password(self)
        user_Buttons.forgot_email(self)


        # PAGE signup
        user_Buttons.signup_screen(self)
        user_Buttons.signup_screen_2(self)

        # PAGE user
        user_Buttons.user_screen(self)
        user_Buttons.logout_screen(self)
        user_Buttons.cancel(self)

        # PAGE Librarian
        librarian_Buttons.Librarian_screen(self)
        librarian_Buttons.Librarian_password(self)
        librarian_Buttons.Librarian_email(self)
        librarian_Buttons.Librarian_logout(self)


        # PAGE Admin
        admin_Buttons.Admin_logout(self)
        admin_Buttons.Admin_add(self)
        admin_Buttons.Admin_addBook(self)
        admin_Buttons.Admin_removeBook(self)

        # PAGE Search
        search_Buttons.search(self)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


    def darkBlueTheme(self):
        style = open('themes/darkstyle.css', 'r')
        style = style.read()
        self.setStyleSheet(style)
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    window.setFixedHeight(700)
    window.setFixedWidth(992)
    app.exec_()

if __name__ == '__main__':
    main()


