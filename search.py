import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MySQLdb
import datetime
from xlrd import *
from xlsxwriter import *
from messages import *

# Database connection
db_host = "localhost"
db_name = "library"
db_user = "lcs"
db_password = "root"

class Search(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.displayCheckOutBooks()


    def search(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()

        book_search = self.line_author_2.text()
        search_criteria = self.comboBox_2.currentText()

        if search_criteria == 'Title':
            search = '''SELECT book_code, book_name,book_status FROM book WHERE book_name = %s'''
            self.cur.execute(search, [(book_search)])
            data = self.cur.fetchall()

            if data == ():
                self.label_8.setText("No Book Found")
                # place code for calling the correct message
                Messages.show_bookNotFound(self)

            else:
                self.label_8.setText("Book Found")
                print(data)
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)

                for row, form in enumerate(data):
                    for column, item in enumerate(form):
                        self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                        column += 1

                    row_pos = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_pos)
            # self.db.close()

        elif search_criteria == 'Subject':
            search = '''SELECT book_code, book_name,book_status FROM book WHERE book_subject = %s'''
            self.cur.execute(search, [(book_search)])
            data = self.cur.fetchall()

            if data == ():
                self.label_8.setText("No Book Found")
                # place code for calling the correct message
                Messages.show_bookNotFound(self)

            else:
                self.label_8.setText("Book Found")
                print(data)
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)

                for row, form in enumerate(data):
                    for column, item in enumerate(form):
                        self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                        column += 1

                    row_pos = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_pos)
            # self.db.close()

        elif search_criteria == 'Author':
            search = '''SELECT book_code, book_name,book_status FROM book WHERE book_author = %s'''
            self.cur.execute(search, [(book_search)])
            data = self.cur.fetchall()

            if data == ():
                self.label_8.setText("No Book Found")
                # place code for calling the correct message
                Messages.show_bookNotFound(self)
            else:
                self.label_8.setText("Book Found")
                print(data)
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)

                for row, form in enumerate(data):
                    for column, item in enumerate(form):
                        self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                        column += 1

                    row_pos = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_pos)
            # self.db.close()

        else:
            # place code for calling the correct message
            Messages.select(self)

    def displayCheckOutBooks(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()
        trans = 'Check Out'
        trans2 = 'Renew'
        search = '''SELECT borrower, book_code, book_name, to_date FROM day_transactions WHERE type = %s OR type = %s'''
        self.cur.execute(search, trans, trans2)
        data = self.cur.fetchall()
        self.tableWidget_9.setRowCount(0)
        self.tableWidget_9.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_9.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_pos = self.tableWidget_9.rowCount()
            self.tableWidget_9.insertRow(row_pos)

    def displayBooksOnHold(self):
        self.db = MySQLdb.connect(host=db_host, db=db_name, user=db_user, password=db_password)
        self.cur = self.db.cursor()
        trans = "Request Hold"
        search = '''SELECT book_code, borrower, book_name FROM day_transactions WHERE type = %s'''
        self.cur.execute(search, [(trans)])
        data = self.cur.fetchall()

        self.tableWidget_8.setRowCount(0)
        self.tableWidget_8.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_8.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_pos = self.tableWidget_8.rowCount()
            self.tableWidget_8.insertRow(row_pos)
