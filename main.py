from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sqlite3
import sys



class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        
        self.loadTable('coffee.sqlite')
        
    def loadTable(self, table_name):
        con = sqlite3.connect(table_name)
        cur = con.cursor()
        cur.execute("""
            SELECT * FROM coffee
        """)
        self.tableWidget.setRowCount(cur.rowcount)
        for row, form in enumerate(cur):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                print(str(item))
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
        self.tableWidget.resizeColumnsToContents()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    exit(app.exec_())