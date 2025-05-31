
import subprocess, os
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

# Частная сеть
def network_private(self):
        commands = [
            r"Get-NetConnectionProfile | Set-NetConnectionProfile -NetworkCategory Private",
            r'Disable-NetAdapterBinding -Name "*" -ComponentID ms_tcpip6',
            r'Get-NetAdapter -Name "*" | Set-NetIPInterface -Dhcp Enabled'
        ]
        try:
            for command in commands:
                subprocess.run(["powershell", "-Command", command],shell=True,check=True, creationflags=CREATE_NO_WINDOW)
            done(complet='Настройка сети выполнена \nПеревставить кабель')
        except subprocess.CalledProcessError as e:
            err(text=f"Ошибка при выполнении команды: \n{e.cmd} \nКод возврата :{e.returncode}")


# Отключение брандмауэра
def braundmauer():
    command = 'Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False'
    try:
        subprocess.run(['powershell', '-Command', command],check=True, creationflags=CREATE_NO_WINDOW)
        done(complet='Выполено!')
    except subprocess.CalledProcessError as e:
        err(text=f'Ошибка при выполнении команды:\n{e.cmd}\nКод возврата: {e.returncode}')


# Электропитание
def pitanie():
    commands = [
        r'powercfg -change -monitor-timeout-ac 0',
        r'powercfg -change -standby-timeout-ac 0'
        ]
    try:
        for command in commands:
            subprocess.run(["powershell", "-Command", command],shell=True,check=True, creationflags=CREATE_NO_WINDOW)
        done(complet='Выполено!')
    except subprocess.CalledProcessError as e:
        err(text=f'Ошибка при выполнении команды:\n{e.cmd}\nКод возврата: {e.returncode}')

# Запуск служб
def start_():
    # Запуск служб
    commands = [
    r'Set-Service -Name "upnphost" -StartupType Automatic',
    r'Start-Service -Name "upnphot"',
    r'Set-Service -Name "BITS" -StartupType Automatic',
    r'Start-Service -Name "BITS"',
    r'Set-Service -Name "RemoteRegistry" -StartupType Automatic',
    r'Start-Service -Name "RemoteRegistry"',
    r'Set-Service -Name "SSDPSRV" -StartupType Automatic',
    r'Start-Service -Name "SSDPSRV"',
    r'Set-Service -Name "PlugPlay" -StartupType Automatic',
    r'Start-Service -Name "PlugPlay"',
    r'Set-Service -Name "FDResPub" -StartupType Automatic',
    r'Start-Service -Name "FDResPub"'
    ]
    try:
        for command in commands:
            subprocess.run(['powershell', '-Command', command],shell=True, check=True, creationflags=CREATE_NO_WINDOW)
        done(complet='Службы запущены')
    except subprocess.SubprocessError as e:
        err(text=f'Ошибка при выполнении команды:\n{e.cmd}\nКод возврата: {e.returncode}')

# Остановка служб (чего-то уже нет на ОС 10 и одна не отключается из-за зависимости с RPC её не отключать, а то Active Directory будет не работать)
def stop_(self):
    # Выключение служб
    commands = [
    r'Set-Service -Name "WebClient" -StartupType disabled',
    r'Stop-Service -Name "WebClient"',
    r'Set-Service -Name "WbioSrvc" -StartupType disabled',
    r'Stop-Service -Name "WbioSrvc"',
    r'Set-Service -Name "BthHFSrv" -StartupType disabled',
    r'Stop-Service -Name "BthHFSrv"',
    r'Set-Service -Name "bthserv" -StartupType disabled',
    r'Stop-Service -Name "bthserv"',
    r'Set-Service -Name "TabletInputService" -StartupType disabled',
    r'Stop-Service -Name "TabletInputService"',
    r'Set-Service -Name "RetailDemo" -StartupType disabled',
    r'Stop-Service -Name "RetailDemo"',
    r'Set-Service -Name "XboxNetApiSvc" -StartupType disabled',
    r'Stop-Service -Name "XboxNetApiSvc"',
    r'Set-Service -Name "XblGameSave" -StartupType disabled',
    r'Stop-Service -Name "XblGameSave"',
    r'Set-Service -Name "XblAuthManager" -StartupType disabled',
    r'Stop-Service -Name "XblAuthManager"',
    r'Set-Service -Name "WalletService" -StartupType disabled',
    r'Stop-Service -Name "WalletService"',
    r'Set-Service -Name "DPS" -StartupType disabled',
    r'Stop-Service -Name "DPS"',
    r'Set-Service -Name "vmicheartbeat" -StartupType disabled',
    r'Stop-Service -Name "vmicheartbeat"',
    r'Set-Service -Name "vmickvpexchange" -StartupType disabled',
    r'Stop-Service -Name "vmickvpexchange"',
    r'Set-Service -Name "vmicvmsession" -StartupType disabled',
    r'Stop-Service -Name "vmicvmsession"',
    r'Set-Service -Name "vmictimesync" -StartupType disabled',
    r'Stop-Service -Name "vmictimesync"',
    r'Set-Service -Name "vmicvss" -StartupType disabled',
    r'Stop-Service -Name "vmicvss"',
    r'Set-Service -Name "vmicshutdown" -StartupType disabled',
    r'Stop-Service -Name "vmicshutdown"',
    r'Set-Service -Name "vmicrdv" -StartupType disabled',
    r'Stop-Service -Name "vmicrdv"'
    ]

    try:
        for command in commands:
            subprocess.run(["powershell", "-Command", command], shell=True,check=True, creationflags=CREATE_NO_WINDOW)
        done(complet='Службы остановлены!')
    except subprocess.CalledProcessError as e:
        err(text=f'Ошибка при выполнении команды:\n{e.cmd}\nКод возврата: {e.returncode}')


# Перезапуск службы времени
def time():
    commands = [
        r'w32tm /config /manualpeerlist:"10.2.1.19" /syncfromflags:manual /reliable:yes /update',
        r'Start-Service w32time'
    ]
    try:
        for command in commands:
            subprocess.run(command, shell=True, check=True, creationflags=CREATE_NO_WINDOW)
        done(complet='Синхронизация времени выполнена')
    except subprocess.CalledProcessError as e:
        err(text=f'Ошибка при выполнении команды:\n{e.cmd}\nКод возврата: {e.returncode}')


# Активация виндовс
def act_win():
    commands = [
    r'slmgr /upk',
    r'slmgr /cpky',
    r'slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX',
    r'slmgr /skms WTC-KMS-01.acron.ru',
    r'slmgr /ato',
    ]

    try:
        for command in commands:
            result = subprocess.run(['powershell', '-Command', command], shell=True, check=True, creationflags=CREATE_NO_WINDOW)
        done(complet='Активация выполнена')
    except subprocess.CalledProcessError:
        err(text=f'Ошибка при выполнении команды:\n{e.cmd}\nКод возврата: {e.returncode}')


# Активация офиса
def act_off():
    commands = [
        r'cscript "C:\Program Files (x86)\Microsoft Office\Office16\ospp.vbs" /sethst:wtc-kms-01.acron.ru',
        r'cscript "C:\Program Files (x86)\Microsoft Office\Office16\ospp.vbs" /FXYTK-NJJ8C-GB6DW-3DYQT-6F7TH',
        r'cscript "C:\Program Files (x86)\Microsoft Office\Office16\ospp.vbs" /act',
    ]

    commands_1 = [
        r'cscript "C:\Program Files\Microsoft Office\Office16\ospp.vbs" /sethst:wtc-kms-01.acron.ru',
        r'cscript "C:\Program Files\Microsoft Office\Office16\ospp.vbs" /FXYTK-NJJ8C-GB6DW-3DYQT-6F7TH',
        r'cscript "C:\Program Files\Microsoft Office\Office16\ospp.vbs" /act',
    ]

    file_1 = r'cd "c:\Program Files (x86)\Microsoft Office\Office16\OSPP.VBS"'

    if os.path.exists(file_1):
        try:
            for command in commands:
                subprocess.run(command, shell=True,check=True, creationflags=CREATE_NO_WINDOW)
            done(complet='Office активирован')
        except subprocess.CalledProcessError as e:
            err(text=f'Ошибка при выполнении команды:\n{e.cmd}\nКод возврата: {e.returncode}')

    else:
        try:
            for command_1 in commands_1:
                subprocess.run(command_1, shell=True,check=True, creationflags=CREATE_NO_WINDOW)
            done(complet='Office активирован')
        except subprocess.CalledProcessError as e:
            err(text=f'Ошибка при выполнении команды:\n{e.cmd}\nКод возврата: {e.returncode}')

#Ассоциация файлов
def assoziazion_file():
    commands = [
        # 7z, rar, zip
        r'assoc .zip=zip_7',
        r'assoc .7z=zip_7',
        r'assoc .rar=zip_7',
        r'ftype zip_7="C:\Program Files\7-Zip\7zFM.exe" "%1"',

        # kompas
        r'assoc .cdw=kompas',
        r'assoc .dwg=kompas',
        r'ftype kompas="C:\Program Files\ASCON\KOMPAS-3D Viewer V16\Bin\kViewer.Exe" "%1"',

        # office
        r'assoc .doc=Word.Document.8',
        r'ftype Word.Document.8="C:\Program Files\Microsoft Office\Root\Office16\WINWORD.EXE" /n "%1" /o "%u"',

        r'assoc .docx=Word.Document.12',
        r'ftype Word.Document.12="C:\Program Files\Microsoft Office\Root\Office16\WINWORD.EXE" /n "%1" /o "%u"',

        r'assoc .ods=Excel.OpenDocumentSpreadsheet.12',
        r'ftype Excel.OpenDocumentSpreadsheet.12="C:\Program Files\Microsoft Office\Root\Office16\EXCEL.EXE" /dde',

        r'assoc .odt=Word.OpenDocumentText.12',
        r'ftype Word.OpenDocumentText.12="C:\Program Files\Microsoft Office\Root\Office16\WINWORD.EXE" /n "%1"',

        r'assoc .vsd=VisioViewer.Viewer',
        r'ftype VisioViewer.Viewer="%ProgramFiles%\Internet Explorer\iexplore.exe" -nohome',

        r'assoc .xls=Excel.Sheet.8',
        r'ftype Excel.Sheet.8="C:\Program Files\Microsoft Office\Root\Office16\EXCEL.EXE" /dde',

        r'assoc .xls=Excel.Sheet.12',
        r'ftype Excel.Sheet.12="C:\Program Files\Microsoft Office\Root\Office16\EXCEL.EXE" /dde',

        # pdf
        r'assoc .pdf=AcroExch.Document.DC',
        r'ftype AcroExch.Document.DC="C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe" "%1"',

        # sumatra
        r'assoc .djvu=sumatra',
        r'ftype sumatra="C:\Program Files\SumatraPDF\SumatraPDF.exe" "%1"'
    ]

    try:
        for cmd in commands:
            subprocess.run(cmd, shell=True,check=True, creationflags=CREATE_NO_WINDOW)
        done(complet='Ассоциация выполнена')

    except subprocess.CalledProcessError:
        err(text=f'Ошибка при выполнении команды:\n{e.cmd}\nКод возврата: {e.returncode}')

