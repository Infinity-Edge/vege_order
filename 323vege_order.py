from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from sort_processor import total_excecuter
import sys
import os
import traceback

def exception_hook(exctype, value, tb):
    # 예외 정보 출력
    print("Exception type:", exctype)
    print("Exception value:", value)
    print("Traceback:", ''.join(traceback.format_tb(tb)))

    # 예외 발생 시 메세지 박스 표시
    error_message = ''.join(traceback.format_exception(exctype, value, tb))
    QMessageBox.critical(None, "Exception", f"An error occurred:\n{error_message}\n프로그램이 재실행됩니다.")

    # 데이터 저장 및 프로그램 재시작 등의 추가 처리
    restart_program()

    # 프로그램 종료
    sys.exit(1)

sys.excepthook = exception_hook

def get_desktop_path():
    # OneDrive 바탕화면 경로 확인
    onedrive_path = os.environ.get('OneDrive') or os.environ.get('OneDriveCommercial')
    
    if onedrive_path:
        desktop_path = os.path.join(onedrive_path, 'Desktop')
    else:
        # OneDrive 경로가 없으면 기본 사용자 바탕화면 경로 사용
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    
    return desktop_path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 파일 경로 리스트 초기화
        self.file_paths = []

        # 버튼 연결
        self.pushButton.clicked.connect(self.select_file)
        self.pushButton_2.clicked.connect(self.remove_file)
        self.pushButton_3.clicked.connect(self.run_algorithm)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "323 야채 정리기"))
        self.pushButton_2.setText(_translate("MainWindow", "파일 삭제"))
        self.pushButton.setText(_translate("MainWindow", "파일 선택"))
        self.pushButton_3.setText(_translate("MainWindow", "출력"))
        self.label.setText(_translate("MainWindow", "장부 목록"))

    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        files, _ = QFileDialog.getOpenFileNames(None, "파일 선택", "", "엑셀 파일 (*.xlsm *.xlsx *.xls)", options=options)
        if files:
            for file in files:
                self.file_paths.append(file)
                self.listWidget.addItem(os.path.basename(file))  # 파일 이름만 리스트에 추가

    def remove_file(self):
        selected_items = self.listWidget.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            row = self.listWidget.row(item)
            self.listWidget.takeItem(row)  # 리스트에서 항목 제거
            del self.file_paths[row]  # 파일 경로 리스트에서도 제거

    def run_algorithm(self):
        if not self.file_paths:
            QMessageBox.warning(None, "경고", "파일이 선택되지 않았습니다.")
            return
        
        #out_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive/Desktop')
        out_path = os.path.dirname(sys.executable)
        #out_path = get_desktop_path()
        total_excecuter(self.file_paths, out_path)
        QMessageBox.information(None, "완료", "작업이 완료되었습니다.")

def restart_program():
    # 프로그램을 재실행하는 함수
    python = sys.executable
    os.execl(python, python, *sys.argv)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
