import sys, os

from powershell import ps
from regedit import reg
from uninstall import uni
from drivers import drivers

from PyQt5 import QtCore, QtGui, QtWidgets
from elevate import elevate

sys.path.append(os.path.join(os.path.dirname(__file__), 'install_programm'))
import inst

elevate()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 338)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 871, 341))
        self.tabWidget.setMinimumSize(QtCore.QSize(871, 0))
        self.tabWidget.setObjectName("tabWidget")

        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab")

        self.listView = QtWidgets.QListView(self.tab_6)
        self.listView.setGeometry(QtCore.QRect(20, 10, 271, 261))
        self.listView.setObjectName("listView")

        self.button_pitanie = QtWidgets.QPushButton(self.tab_6)
        self.button_pitanie.setGeometry(QtCore.QRect(30, 200, 251, 23))
        self.button_pitanie.setObjectName("button_pitanie")
        self.button_pitanie.clicked.connect(ps.pitanie)

        self.button_brandmaura = QtWidgets.QPushButton(self.tab_6)
        self.button_brandmaura.setGeometry(QtCore.QRect(30, 110, 251, 23))
        self.button_brandmaura.setObjectName("button_brandmaura")
        self.button_brandmaura.clicked.connect(ps.braundmauer)

        self.button_network = QtWidgets.QPushButton(self.tab_6)
        self.button_network.setGeometry(QtCore.QRect(30, 20, 251, 23))
        self.button_network.setObjectName("button_network")
        self.button_network.clicked.connect(ps.network_private)

        self.button_invisibal_files = QtWidgets.QPushButton(self.tab_6)
        self.button_invisibal_files.setGeometry(QtCore.QRect(30, 170, 251, 23))
        self.button_invisibal_files.setObjectName("button_invisibal_files")
        self.button_invisibal_files.clicked.connect(reg.data_invis)

        self.button_start_sluzb = QtWidgets.QPushButton(self.tab_6)
        self.button_start_sluzb.setGeometry(QtCore.QRect(30, 230, 251, 23))
        self.button_start_sluzb.setObjectName("button_start_sluzb")
        self.button_start_sluzb.clicked.connect(ps.start_)

        self.button_panel_zadac = QtWidgets.QPushButton(self.tab_6)
        self.button_panel_zadac.setGeometry(QtCore.QRect(30, 140, 251, 23))
        self.button_panel_zadac.setObjectName("button_panel_zadac")
        self.button_panel_zadac.clicked.connect(reg.panel)

        self.button_dostup = QtWidgets.QPushButton(self.tab_6)
        self.button_dostup.setGeometry(QtCore.QRect(30, 80, 251, 23))
        self.button_dostup.setObjectName("button_dostup")
        self.button_dostup.clicked.connect(reg.dostup)


        self.button_time = QtWidgets.QPushButton(self.tab_6)
        self.button_time.setGeometry(QtCore.QRect(30, 50, 251, 23))
        self.button_time.setObjectName("button_time")
        self.button_time.clicked.connect(ps.time)

        self.listView_2 = QtWidgets.QListView(self.tab_6)
        self.listView_2.setGeometry(QtCore.QRect(580, 60, 256, 71))
        self.listView_2.setObjectName("listView_2")

        self.znacki = QtWidgets.QPushButton(self.tab_6)
        self.znacki.setGeometry(QtCore.QRect(710, 90, 111, 23))
        self.znacki.setObjectName("pushButton")
        self.znacki.clicked.connect(self.data_combo)

        self.combo_box = QtWidgets.QComboBox(self.tab_6)
        self.combo_box.setGeometry(QtCore.QRect(590, 90, 111, 22))
        self.combo_box.setObjectName("combo_box")
        self.combo_box_item = ['User', 'Admin', 'Del']
        self.combo_box.addItems(self.combo_box_item)



        self.label_znacki = QtWidgets.QLabel(self.tab_6)
        self.label_znacki.setGeometry(QtCore.QRect(590, 60, 191, 21))
        self.label_znacki.setObjectName("label_znacki")


        self.listView_3 = QtWidgets.QListView(self.tab_6)
        self.listView_3.setGeometry(QtCore.QRect(580, 180, 256, 91))
        self.listView_3.setObjectName("listView_3")

        self.line_FIO = QtWidgets.QLineEdit(self.tab_6)
        self.line_FIO.setGeometry(QtCore.QRect(590, 210, 231, 20))
        self.line_FIO.setText("")
        self.line_FIO.setObjectName("line_FIO")

        self.button_FIO = QtWidgets.QPushButton(self.tab_6)
        self.button_FIO.setGeometry(QtCore.QRect(650, 240, 111, 23))
        self.button_FIO.setObjectName("button_FIO")
        self.button_FIO.clicked.connect(self.teext)

        self.label_FIO = QtWidgets.QLabel(self.tab_6)
        self.label_FIO.setGeometry(QtCore.QRect(590, 180, 191, 21))
        self.label_FIO.setObjectName("label_FIO")

        self.listView_4 = QtWidgets.QListView(self.tab_6)
        self.listView_4.setGeometry(QtCore.QRect(300, 10, 271, 261))
        self.listView_4.setObjectName("listView_4")

        self.button_disabled_smart = QtWidgets.QPushButton(self.tab_6)
        self.button_disabled_smart.setGeometry(QtCore.QRect(310, 80, 251, 23))
        self.button_disabled_smart.setObjectName("button_disabled_smart")
        self.button_disabled_smart.clicked.connect(reg.smart)

        self.button_disabled_nepoladka = QtWidgets.QPushButton(self.tab_6)
        self.button_disabled_nepoladka.setGeometry(QtCore.QRect(310, 50, 251, 23))
        self.button_disabled_nepoladka.setObjectName("button_disabled_nepoladka")
        self.button_disabled_nepoladka.clicked.connect(reg.ne_poladka)

        self.button_office = QtWidgets.QPushButton(self.tab_6)
        self.button_office.setGeometry(QtCore.QRect(310, 170, 251, 23))
        self.button_office.setObjectName("button_office")
        self.button_office.clicked.connect(ps.act_off)

        self.button_windows_defender = QtWidgets.QPushButton(self.tab_6)
        self.button_windows_defender.setGeometry(QtCore.QRect(310, 110, 251, 23))
        self.button_windows_defender.setObjectName("button_windows_defender")
        self.button_windows_defender.clicked.connect(reg.win_def)


        self.button_stop_slusb = QtWidgets.QPushButton(self.tab_6)
        self.button_stop_slusb.setGeometry(QtCore.QRect(310, 20, 251, 23))
        self.button_stop_slusb.setObjectName("button_stop_slusb")
        self.button_stop_slusb.clicked.connect(ps.stop_)

        self.button_assazion_files = QtWidgets.QPushButton(self.tab_6)
        self.button_assazion_files.setGeometry(QtCore.QRect(310, 200, 251, 23))
        self.button_assazion_files.setObjectName("button_assazion_files")
        self.button_assazion_files.clicked.connect(ps.assoziazion_file)

        self.button_windows = QtWidgets.QPushButton(self.tab_6)
        self.button_windows.setGeometry(QtCore.QRect(310, 140, 251, 23))
        self.button_windows.setObjectName("button_windows")
        self.button_windows.clicked.connect(ps.act_win)

        self.progressBar = QtWidgets.QProgressBar(self.tab_6)
        self.progressBar.setGeometry(QtCore.QRect(580, 10, 221, 31))
        self.progressBar.setObjectName("progressBar")

        self.progressBar.hide()
        ps.set_progress_bar(self.progressBar)
        reg.set_progress_bar(self.progressBar)
        drivers.set_progress_bar(self.progressBar)

        self.button_drivers = QtWidgets.QPushButton(self.tab_6)
        self.button_drivers.setGeometry(QtCore.QRect(310, 230, 251, 23))
        self.button_drivers.setObjectName("button_drivers")
        self.button_drivers.clicked.connect(drivers.all_drivers)


        self.tabWidget.addTab(self.tab_6, "")

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")

        self.progressBar_1 = QtWidgets.QProgressBar(self.tab_5)
        self.progressBar_1.setGeometry(QtCore.QRect(700, 30, 121, 31))
        self.progressBar_1.setObjectName("progressBar_1")

        self.progressBar_1.hide()
        uni.set_progress_bar(self.progressBar_1)

        self.listView_5 = QtWidgets.QListView(self.tab_5)
        self.listView_5.setGeometry(QtCore.QRect(110, 10, 581, 71))
        self.listView_5.setObjectName("listView_5")

        self.combo_box_intall = QtWidgets.QComboBox(self.tab_5)
        self.combo_box_intall.setGeometry(QtCore.QRect(120, 40, 461, 31))
        self.combo_box_intall.setObjectName("combo_box_intall")
        self.combo_box_intall.addItem("Путь не выбран")



        self.button_install = QtWidgets.QPushButton(self.tab_5)
        self.button_install.setGeometry(QtCore.QRect(590, 40, 91, 31))
        self.button_install.setObjectName("button_install")
        self.button_install.clicked.connect(self.select_install_path)



        self.label_install = QtWidgets.QLabel(self.tab_5)
        self.label_install.setGeometry(QtCore.QRect(120, 10, 211, 21))
        self.label_install.setObjectName("label_install")

        self.listView_6 = QtWidgets.QListView(self.tab_5)
        self.listView_6.setGeometry(QtCore.QRect(130, 90, 271, 201))
        self.listView_6.setObjectName("listView_6")

        self.button_adobe = QtWidgets.QPushButton(self.tab_5)
        self.button_adobe.setGeometry(QtCore.QRect(140, 100, 251, 23))
        self.button_adobe.setObjectName("button_adobe")
        self.button_adobe.clicked.connect(inst.adob)

        self.button_free_vimager = QtWidgets.QPushButton(self.tab_5)
        self.button_free_vimager.setGeometry(QtCore.QRect(140, 130, 251, 23))
        self.button_free_vimager.setObjectName("button_free_vimager")
        self.button_free_vimager.clicked.connect(inst.free_vimag)

        self.button_zip = QtWidgets.QPushButton(self.tab_5)
        self.button_zip.setGeometry(QtCore.QRect(140, 160, 251, 23))
        self.button_zip.setObjectName("button_zip")
        self.button_zip.clicked.connect(inst.zip)

        self.button_sumatra = QtWidgets.QPushButton(self.tab_5)
        self.button_sumatra.setGeometry(QtCore.QRect(140, 190, 251, 23))
        self.button_sumatra.setObjectName("button_sumatra")
        self.button_sumatra.clicked.connect(inst.sumart)

        self.button_java = QtWidgets.QPushButton(self.tab_5)
        self.button_java.setGeometry(QtCore.QRect(140, 220, 251, 23))
        self.button_java.setObjectName("button_java")
        self.button_java.clicked.connect(inst.java)

        self.button_Dame_Ware = QtWidgets.QPushButton(self.tab_5)
        self.button_Dame_Ware.setGeometry(QtCore.QRect(140, 250, 251, 23))
        self.button_Dame_Ware.setObjectName("button_Dame_Ware")
        self.button_Dame_Ware.clicked.connect(inst.dame)

        self.listView_7 = QtWidgets.QListView(self.tab_5)
        self.listView_7.setGeometry(QtCore.QRect(410, 90, 271, 201))
        self.listView_7.setObjectName("listView_7")


        self.button_kompas = QtWidgets.QPushButton(self.tab_5)
        self.button_kompas.setGeometry(QtCore.QRect(420, 130, 251, 23))
        self.button_kompas.setObjectName("button_kompas")
        self.button_kompas.clicked.connect(inst.komp)

        self.button_pdf_sam = QtWidgets.QPushButton(self.tab_5)
        self.button_pdf_sam.setGeometry(QtCore.QRect(420, 160, 251, 23))
        self.button_pdf_sam.setObjectName("button_pdf_sam")
        self.button_pdf_sam.clicked.connect(inst.pdf_sam)

        self.button_google = QtWidgets.QPushButton(self.tab_5)
        self.button_google.setGeometry(QtCore.QRect(420, 190, 251, 23))
        self.button_google.setObjectName("button_google")
        self.button_google.clicked.connect(inst.chrom)

        self.button_uninstall = QtWidgets.QPushButton(self.tab_5)
        self.button_uninstall.setGeometry(QtCore.QRect(420, 220, 251, 23))
        self.button_uninstall.setObjectName("button_uninstall")
        self.button_uninstall.clicked.connect(uni.uninstall)



        self.tabWidget.addTab(self.tab_5, "")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_pitanie.setText(_translate("MainWindow", "Электропитание"))
        self.button_brandmaura.setText(_translate("MainWindow", "Отключение брандмауэра"))
        self.button_network.setText(_translate("MainWindow", "Частная сеть"))
        self.button_invisibal_files.setText(_translate("MainWindow", "Скрытые папки"))
        self.button_start_sluzb.setText(_translate("MainWindow", "Запуск служб"))
        self.button_panel_zadac.setText(_translate("MainWindow", "Панель задач"))
        self.button_dostup.setText(_translate("MainWindow", "Удаленый доступ"))
        self.button_time.setText(_translate("MainWindow", "Синхронизация времени"))
        self.znacki.setText(_translate("MainWindow", "Значки"))
        self.label_znacki.setText(_translate("MainWindow", "Вывод значков на рабочий стол"))
        self.button_FIO.setText(_translate("MainWindow", "ФИО"))
        self.label_FIO.setText(_translate("MainWindow", "Запись ФИО и организации в реестр"))
        self.button_disabled_smart.setText(_translate("MainWindow", "Отключение SmartScreen"))
        self.button_disabled_nepoladka.setText(_translate("MainWindow", "Устранение неполадок"))
        self.button_office.setText(_translate("MainWindow", "Активация оффиса"))
        self.button_windows_defender.setText(_translate("MainWindow", "Windows Defender"))
        self.button_stop_slusb.setText(_translate("MainWindow", "Остановка служб"))
        self.button_assazion_files.setText(_translate("MainWindow", "Ассоциация файлов"))
        self.button_windows.setText(_translate("MainWindow", "Активация виндовс"))
        self.button_drivers.setText(_translate("MainWindow", "Обновить драйвера"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "PS"))
        self.button_install.setText(_translate("MainWindow", "Указать путь"))
        self.label_install.setText(_translate("MainWindow", "Указать путь к установщикам"))
        self.button_adobe.setText(_translate("MainWindow", "Adobe Reader"))
        self.button_free_vimager.setText(_translate("MainWindow", "FreeVimager"))
        self.button_zip.setText(_translate("MainWindow", "7-Zip"))
        self.button_sumatra.setText(_translate("MainWindow", "SumatraPDF"))
        self.button_java.setText(_translate("MainWindow", "Java"))
        self.button_Dame_Ware.setText(_translate("MainWindow", "DameWare"))
        self.button_kompas.setText(_translate("MainWindow", "KOMPAS "))
        self.button_pdf_sam.setText(_translate("MainWindow", "PdfSam"))
        self.button_google.setText(_translate("MainWindow", " Google Chrome"))
        self.button_uninstall.setText(_translate("MainWindow", "Удаление мусора"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Install"))

    # Вывод иконок на рабочий сто
    def data_combo(self):
        text_combo = self.combo_box.currentText()
        if text_combo == 'User':
            reg.data_combo_user()

        elif text_combo == 'Admin':
            reg.data_combo_admin()

        elif text_combo == 'Del':
            reg.data_combo_del()

    # ФИО Пользователя, сохранение и запись
    def teext(self):
        text = self.line_FIO.text()
        reg.save_FIO(text)

    #Сохранение путь к установке программ
    def select_install_path(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory()
        if directory:
            self.combo_box_intall.addItem(directory)
            self.combo_box_intall.setCurrentText(directory)
            path = directory
            inst.do_install(path)  # передаем путь напрямую


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
