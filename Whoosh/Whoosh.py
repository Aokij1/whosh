import sys

from powershell import ps
from regedit import reg
from install_programm import inst
from uninstall import uni
from drivers import drivers

from PyQt5 import QtCore, QtWidgets

from elevate import elevate

elevate()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(671, 370)
        MainWindow.setStyleSheet("background-color: rgb(152, 152, 152);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        # Выподающий список для выбора админа или пользователя
        self.combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.combo_box.setGeometry(QtCore.QRect(10, 10, 70, 25))
        self.combo_box.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.combo_box.setObjectName("combo_box")
        self.combo_box_item = ['User', 'Admin', 'Del']
        self.combo_box.addItems(self.combo_box_item)



        # Кнопка для вывода иконок на рабочий стол
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 10, 75, 25))
        self.pushButton.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.data_combo)

        # Настройка сети
        self.button_network = QtWidgets.QPushButton(self.centralwidget)
        self.button_network.setGeometry(QtCore.QRect(10, 50, 150, 25))
        self.button_network.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.button_network.setObjectName("button_network")
        self.button_network.clicked.connect(ps.network_private)

        # Синхронизация времени
        self.button_time = QtWidgets.QPushButton(self.centralwidget)
        self.button_time.setGeometry(QtCore.QRect(10, 90, 150, 25))
        self.button_time.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.button_time.setObjectName("button_time")
        self.button_time.clicked.connect(ps.time)

        # Доступ
        self.button_dostup = QtWidgets.QPushButton(self.centralwidget)
        self.button_dostup.setGeometry(QtCore.QRect(10, 130, 150, 25))
        self.button_dostup.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.button_dostup.setObjectName("button_dostup")
        self.button_dostup.clicked.connect(reg.dostup)


        # Отключение брандмауэра
        self.button_mauer = QtWidgets.QPushButton(self.centralwidget)
        self.button_mauer.setGeometry(QtCore.QRect(10, 170, 150, 25))
        self.button_mauer.setStyleSheet("background-color: rgb(255, 242, 245);\n"
                                        "font: 25 8pt \"Bahnschrift\";")
        self.button_mauer.setObjectName("button_mauer")
        self.button_mauer.clicked.connect(ps.braundmauer)

        # Обои, аватар, забавные факты
        self.button_warpper = QtWidgets.QPushButton(self.centralwidget)
        self.button_warpper.setGeometry(QtCore.QRect(10, 210, 150, 25))
        self.button_warpper.setStyleSheet("background-color: rgb(255, 242, 245);\n"
                                          "font: 25 8pt \"Bahnschrift\";")
        self.button_warpper.setObjectName("button_warpper")
        self.button_warpper.clicked.connect(reg.wapper_avatar)

        # Скрытые папки
        self.button_invis = QtWidgets.QPushButton(self.centralwidget)
        self.button_invis.setGeometry(QtCore.QRect(10, 250, 150, 25))
        self.button_invis.setStyleSheet("background-color: rgb(255, 242, 245);\n"
                                        "font: 25 8pt \"Bahnschrift\";")
        self.button_invis.setObjectName("button_invis")
        self.button_invis.clicked.connect(reg.data_invis)

        # Электропитание
        self.button_electro = QtWidgets.QPushButton(self.centralwidget)
        self.button_electro.setGeometry(QtCore.QRect(170, 50, 150, 25))
        self.button_electro.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.button_electro.setObjectName("button_electro")
        self.button_electro.clicked.connect(ps.pitanie)

        # Поле для ввода ФИО юзера
        self.line_FIO = QtWidgets.QLineEdit(self.centralwidget)
        self.line_FIO.setGeometry(QtCore.QRect(170, 10, 150, 25))
        self.line_FIO.setStyleSheet("background-color: rgb(255, 242, 245);\n"
                                    "font: 25 8pt \"Bahnschrift\";")
        self.line_FIO.setText("")
        self.line_FIO.setObjectName("line_FIO")

        # Кнопка для ФИО юзера
        self.button_FIO = QtWidgets.QPushButton(self.centralwidget)
        self.button_FIO.setGeometry(QtCore.QRect(330, 10, 150, 25))
        self.button_FIO.setStyleSheet("background-color: rgb(255, 242, 245);\n"
                                      "font: 25 8pt \"Bahnschrift\";")
        self.button_FIO.setObjectName("button_FIO")
        self.button_FIO.clicked.connect(self.teext)



        # Запуск служб
        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(170, 90, 150, 25))
        self.button_start.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.button_start.setObjectName("button_start")
        self.button_start.clicked.connect(ps.start_)

        # Остановка служб (половины из которых уже нет на ОС 10)
        self.button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_stop.setGeometry(QtCore.QRect(170, 130, 150, 25))
        self.button_stop.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.button_stop.setObjectName("button_stop")
        self.button_stop.clicked.connect(ps.stop_)

        # Устранение неполадок
        self.button_nepoladka = QtWidgets.QPushButton(self.centralwidget)
        self.button_nepoladka.setGeometry(QtCore.QRect(170, 170, 150, 25))
        self.button_nepoladka.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.button_nepoladka.setObjectName("button_nepoladka")
        self.button_nepoladka.clicked.connect(reg.ne_poladka)

        # SMART
        self.button_smart = QtWidgets.QPushButton(self.centralwidget)
        self.button_smart.setGeometry(QtCore.QRect(170, 210, 150, 25))
        self.button_smart.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.button_smart.setObjectName("button_smart")
        self.button_smart.clicked.connect(reg.smart)

        # Панель задач
        self.button_panel = QtWidgets.QPushButton(self.centralwidget)
        self.button_panel.setGeometry(QtCore.QRect(170, 250, 150, 25))
        self.button_panel.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.button_panel.setObjectName("button_panel")
        self.button_panel.clicked.connect(reg.panel)

        # Виндовс defender))
        self.button_defender = QtWidgets.QPushButton(self.centralwidget)
        self.button_defender.setGeometry(QtCore.QRect(170, 290, 150, 25))
        self.button_defender.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.button_defender.setObjectName("button_defender")
        self.button_defender.clicked.connect(reg.win_def)

        # Установка adobe
        self.butten_setup_adobe = QtWidgets.QPushButton(self.centralwidget)
        self.butten_setup_adobe.setGeometry(QtCore.QRect(330, 50, 150, 25))
        self.butten_setup_adobe.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.butten_setup_adobe.setObjectName("butten_setup_adobe")
        self.butten_setup_adobe.clicked.connect(inst.adob)

        # Установка vimage
        self.butten_setup_vimage = QtWidgets.QPushButton(self.centralwidget)
        self.butten_setup_vimage.setGeometry(QtCore.QRect(330, 90, 150, 25))
        self.butten_setup_vimage.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.butten_setup_vimage.setObjectName("butten_setup_vimage")
        self.butten_setup_vimage.clicked.connect(inst.free_vimag)

        # Установка zip
        self.butten_setup_zip = QtWidgets.QPushButton(self.centralwidget)
        self.butten_setup_zip.setGeometry(QtCore.QRect(330, 130, 150, 25))
        self.butten_setup_zip.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.butten_setup_zip.setObjectName("butten_setup_zip")
        self.butten_setup_zip.clicked.connect(inst.zip)

        # Установка Sumatra
        self.butten_setup_sumartra = QtWidgets.QPushButton(self.centralwidget)
        self.butten_setup_sumartra.setGeometry(QtCore.QRect(330, 170, 150, 25))
        self.butten_setup_sumartra.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.butten_setup_sumartra.setObjectName("butten_setup_sumartra")
        self.butten_setup_sumartra.clicked.connect(inst.sumart)

        # Установка java
        self.butten_setup_java = QtWidgets.QPushButton(self.centralwidget)
        self.butten_setup_java.setGeometry(QtCore.QRect(330, 210, 150, 25))
        self.butten_setup_java.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.butten_setup_java.setObjectName("butten_setup_java")
        self.butten_setup_java.clicked.connect(inst.java)

        # Установка dameWare
        self.butten_setup_dameWare = QtWidgets.QPushButton(self.centralwidget)
        self.butten_setup_dameWare.setGeometry(QtCore.QRect(330, 250, 150, 25))
        self.butten_setup_dameWare.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.butten_setup_dameWare.setObjectName("butten_setup_dameWare")
        self.butten_setup_dameWare.clicked.connect(inst.dame)

        # Установка Kompas
        self.butten_setup_kompas = QtWidgets.QPushButton(self.centralwidget)
        self.butten_setup_kompas.setGeometry(QtCore.QRect(330, 290, 150, 25))
        self.butten_setup_kompas.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.butten_setup_kompas.setObjectName("butten_setup_kompas")
        self.butten_setup_kompas.clicked.connect(inst.komp)



        # Установка PdfSam
        self.butten_setup_pdfSam = QtWidgets.QPushButton(self.centralwidget)
        self.butten_setup_pdfSam.setGeometry(QtCore.QRect(490, 10, 150, 25))
        self.butten_setup_pdfSam.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.butten_setup_pdfSam.setObjectName("butten_setup_pdfSam")
        self.butten_setup_pdfSam.clicked.connect(inst.pdf_sam)

        # Установка googl
        self.butten_setup_chrome = QtWidgets.QPushButton(self.centralwidget)
        self.butten_setup_chrome.setGeometry(QtCore.QRect(490, 50, 150, 25))
        self.butten_setup_chrome.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.butten_setup_chrome.setObjectName("butten_setup_chrome")
        self.butten_setup_chrome.clicked.connect(inst.chrom)

        # Установка framwork
        self.butten_setup_framework = QtWidgets.QPushButton(self.centralwidget)
        self.butten_setup_framework.setGeometry(QtCore.QRect(490, 90, 150, 25))
        self.butten_setup_framework.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.butten_setup_framework.setObjectName("butten_setup_framework")
        self.butten_setup_framework.clicked.connect(inst.framework)

        # Удаление шлюпы
        self.butten_uninstall = QtWidgets.QPushButton(self.centralwidget)
        self.butten_uninstall.setGeometry(QtCore.QRect(490, 130, 150, 25))
        self.butten_uninstall.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.butten_uninstall.setObjectName("butten_uninstall")
        self.butten_uninstall.clicked.connect(uni.uninstall)

        # Активация ввиндовс
        self.butten_windows = QtWidgets.QPushButton(self.centralwidget)
        self.butten_windows.setGeometry(QtCore.QRect(490, 170, 150, 25))
        self.butten_windows.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.butten_windows.setObjectName("butten_windows")
        self.butten_windows.clicked.connect(ps.act_win)

        # Актвация офис
        self.butten_offic = QtWidgets.QPushButton(self.centralwidget)
        self.butten_offic.setGeometry(QtCore.QRect(490, 210, 150, 25))
        self.butten_offic.setStyleSheet("background-color: rgb(255, 242, 245);\n"
                                          "font: 25 8pt \"Bahnschrift\";")
        self.butten_offic.setObjectName("butten_offic")
        self.butten_offic.clicked.connect(ps.act_off)

        self.butten_assoziazia = QtWidgets.QPushButton(self.centralwidget)
        self.butten_assoziazia.setGeometry(QtCore.QRect(490, 250, 150, 25))
        self.butten_assoziazia.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.butten_assoziazia.setObjectName("butten_assoziazia")
        self.butten_assoziazia.clicked.connect(ps.assoziazion_file)

        self.butten_drivers = QtWidgets.QPushButton(self.centralwidget)
        self.butten_drivers.setGeometry(QtCore.QRect(170, 320, 310, 25))
        self.butten_drivers.setStyleSheet("background-color: rgb(255, 242, 245);\n"
"font: 25 8pt \"Bahnschrift\";")
        self.butten_drivers.setObjectName("butten_drivers")
        self.butten_drivers.clicked.connect(drivers.all_drivers)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Whoosh"))
        self.pushButton.setText(_translate("MainWindow", "Значки РС"))
        self.button_network.setText(_translate("MainWindow", "Настройка сети"))
        self.button_time.setText(_translate("MainWindow", "Время"))
        self.button_dostup.setText(_translate("MainWindow", "Удаленка"))
        self.button_electro.setText(_translate("MainWindow", "Электропитание"))
        self.button_start.setText(_translate("MainWindow", "StartServices"))
        self.button_stop.setText(_translate("MainWindow", "StopServices"))
        self.button_nepoladka.setText(_translate("MainWindow", "Выкл. неполадок"))
        self.button_smart.setText(_translate("MainWindow", "Выкл. SmartScreen"))
        self.button_panel.setText(_translate("MainWindow", "Панель задач"))
        self.button_mauer.setText(_translate("MainWindow", "Брандмауэр "))
        self.button_warpper.setText(_translate("MainWindow", "Обои, аватар"))
        self.button_invis.setText(_translate("MainWindow", "Скрытые папки"))
        self.button_defender.setText(_translate("MainWindow", "WindowsDefender"))
        self.button_FIO.setText(_translate("MainWindow", "ФИО пользователя"))
        self.butten_setup_adobe.setText(_translate("MainWindow", "Adobe Reader DC"))
        self.butten_setup_vimage.setText(_translate("MainWindow", "FreeVimager-5.0.9"))
        self.butten_setup_zip.setText(_translate("MainWindow", "7-Zip"))
        self.butten_setup_sumartra.setText(_translate("MainWindow", "SumatraPDF"))
        self.butten_setup_java.setText(_translate("MainWindow", "Java"))
        self.butten_setup_dameWare.setText(_translate("MainWindow", "DameWare"))
        self.butten_setup_kompas.setText(_translate("MainWindow", " KOMPAS"))
        self.butten_setup_pdfSam.setText(_translate("MainWindow", "PdfSam"))
        self.butten_setup_chrome.setText(_translate("MainWindow", " Google Chrome"))
        self.butten_setup_framework.setText(_translate("MainWindow", "NET Framework 3.5"))
        self.butten_uninstall.setText(_translate("MainWindow", "Uninstall"))
        self.butten_windows.setText(_translate("MainWindow", "Активация Виндовс"))
        self.butten_offic.setText(_translate("MainWindow", "Активация Оффиса"))
        self.butten_assoziazia.setText(_translate('MainWindows', 'Ассоциация'))
        self.butten_drivers.setText(_translate('MainWindow', 'Drivers'))

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

    def activation(self):
        ps.act_win()
        ps.act_off()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
