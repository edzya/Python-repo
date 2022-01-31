from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import readFiles
import sqlite3
from sqlite3 import Error


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 800, 600)
        self.setFixedSize(800, 600)
        self.setWindowTitle("MBI SE 2022")
        self.initUI()

    def initUI(self):
        self.statusBar = self.statusBar()
        self.statusBar.showMessage('Ready')
        self.label = QtWidgets.QLabel(self)
        # self.label.setGeometry(250, 20, 300, 40)
        self.label.setText("Warranty processing application")
        self.label.adjustSize()
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Export GAP file")
        self.b1.move(220, 450)
        self.b1.clicked.connect(self.chooseFiles)  # readFiles
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Generate credit notes")
        self.b2.setGeometry(350, 450, 150, 30)
        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Import file(s) to DB")
        self.b3.move(530, 450)

    def chooseFiles(self):
        self.allFiles = QtWidgets.QFileDialog.getOpenFileNames(
            self, 'All files', "C:/", '*.0*')

        if not self.allFiles[0] == []:
            readFiles.readFiles(self.allFiles[0][0])
            self.statusBar.showMessage('Excel file ready')

    def update(self):
        self.label.adjustSize()


stylesheet = """
    MyWindow {
        background-image: url("C:/Users/edgar/Documents/Python/Warranty tool/img/etron.jpg");
        background-repeat: no-repeat;
        background-position: center;
    }    
"""
create_start_table = '''CREATE TABLE IF NOT EXISTS ALLDATA (
importer_no INTEGER,
dealer_no INTEGER,
claim_number TEXT,
claim_serial INTEGER,
claim_date TEXT,
brand TEXT,
international TEXT,
vehicle_coding TEXT,
vehicle_type TEXT,
check_digit TEXT,
model_year TEXT,
production_plant TEXT,
vin_serial_no TEXT,
vehicle_class TEXT,
body TEXT,
variation_of_car_equipment TEXT,
units_engine_gearbox TEXT,
mileage INTEGER,
version INTEGER,
service_id TEXT,
manufacturer_code TEXT,
damage_type INTEGER,
claim_type_1 TEXT,
claim_type_2 TEXT,
rep_code INTEGER,
production_date TEXT,
delivery_date TEXT,
repair_date TEXT,
claim_control_data TEXT,
claim_authorization_date TEXT,
time_units REAL,
labour_rate REAL,
labour_costs REAL,
outside_labour_costs REAL,
material_costs REAL,
outside_material_costs REAL,
vat_factor REAL,
total_costs REAL,
currency TEXT,
material_factor_1 REAL,
material_factor_2 REAL,
labour_rate_WF2 REAL,
labour_costs_WF2 REAL,
outside_labour_WF2 REAL,
material_costs_WF2 REAL,
outside_materials_WF2 REAL,
total_costs_WF2 REAL,
credit_note_from TEXT,
credit_note_to TEXT,
credit_note_date TEXT,
credit_note_number TEXT,
claim_type_1_WF2 TEXT,
claim_type_2_WF2 TEXT,
time_units_WF2 REAL,
req_time_units_partner REAL,
req_labour_costs REAL,
req_outside_labour_costs REAL,
req_material_costs REAL,
req_outside_material_costs REAL,
data_id INTEGER,
tow_in INTEGER,
key TEXT
);
'''


def execute_query(connection, query, variable=''):
    cur = con.cursor()
    try:
        cur.execute(query, variable)
        connection.commit()
        print('Query executed successful\n')
    except Error as e:
        print(f'The error {e} occured')


if __name__ == "__main__":
    import sys
    con = sqlite3.connect('Warranty_DB.db')
    execute_query(con, create_start_table)
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())
