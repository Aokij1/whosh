import subprocess
from PyQt5.QtWidgets import QMessageBox
CREATE_NO_WINDOW = 0x08000000

def err(text):
    message = QMessageBox()
    message.setWindowTitle("Ошибка!")
    message.setText(text)
    message.setIcon(QMessageBox.Information)
    message.exec_()

def done(complet):
    message = QMessageBox()
    message.setWindowTitle("Выполнено")
    message.setText(complet)
    message.setIcon(QMessageBox.Information)
    message.exec_()


def uninstall():
    commands = [
        r'Get-AppxPackage *xbox* | Remove-AppxPackage',
        'Get-AppxPackage *Game Bar* | Remove-AppxPackage',
        r'Get-AppxPackage *office* | Remove-AppxPackage',
        r'Get-AppxPackage *skype* | Remove-AppxPackage',
        r'Get-AppxPackage *Microsoft Teams* | Remove-AppxPackage',
        r'Get-AppxPackage *HP Smart* | Remove-AppxPackage',
        r'Get-AppxPackage *VMTools* | Remove-AppxPackage',
        r'Get-AppxPackage *yandex.music* | Remove-AppxPackage',

    ]

    command_1 = [
        r'taskkill /f /im OneDrive.exe',
        r'C:\Windows\SysWOW64\OneDriveSetup.exe /uninstall'
    ]


    try:
        for command in commands:
            subprocess.run(['powershell', '-Command', command])
        for command in command_1:
            subprocess.run(command, check=True, shell=True)
        done(complet='Приложения удалены!')

    except subprocess.CalledProcessError as e:
        err(text=f'Ошибка при выполнении команды:\n{e.cmd}\nКод возврата: {e.returncode}')



















