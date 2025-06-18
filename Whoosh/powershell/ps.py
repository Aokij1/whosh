
import subprocess, os
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer

CREATE_NO_WINDOW = 0x08000000

timer = QTimer()

# передача прогесса бара с main
def set_progress_bar(bar):
    global progress_bar
    progress_bar = bar

# прогресс progress_bara
def update_progress_bar(va=1):
    val = progress_bar.value()+va
    progress_bar.setValue(val)
    if val >= 100:
        timer.stop()
        return
    timer.timeout.connect(lambda: update_progress_bar)
    timer.start(300)


def warning(text):
    message = QMessageBox()
    message.setWindowTitle("Выполнено")
    message.setText(complet)
    message.setIcon(QMessageBox.Information)
    message.exec_()

# Окно информации Ошибка или Выполнено
def warning(text):
    message = QMessageBox()
    message.setWindowTitle("Внимание!")
    message.setText(text)
    message.setIcon(QMessageBox.Information)
    message.exec_()

# Окно предупреждения что будет если нажать на кнопку
def message_warning(text):
    message = QMessageBox()
    message.setWindowTitle("Предупреждение")
    message.setText(text)
    message.setIcon(QMessageBox.Warning)
    message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    result = message.exec_()
    return result

# Частная сеть
def network_private():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Сеть будет переключена в частную \nОтключен IPv6 \nВключен DHCP \nВ КОНЦЕ ПЕРЕСТАВИТЬ КАБЕЛЬ')

    # Проверяем что нажал пользовтель
    if result == QMessageBox.Ok:

        commands = [

            ('переключении сети в частную', 'Get-NetConnectionProfile | Set-NetConnectionProfile -NetworkCategory Private'),
            ('отключении IPv6', 'Disable-NetAdapterBinding -Name "*" -ComponentID ms_tcpip6'),
            ('включении DHCP', 'Get-NetAdapter -Name "*" | Set-NetIPInterface -Dhcp Enabled')

        ]

        try:
            progress_bar.show()
            for name, command in commands:
                try:
                    subprocess.run(["powershell", "-Command", command],shell=True,check=True, creationflags=CREATE_NO_WINDOW)
                    warning(text=f'Выполнено {name}')
                    update_progress_bar(va=33)
                except subprocess.CalledProcessError:
                    warning(text=f"Ошибка при {name} ")

            progress_bar.hide()
            warning(text='Переставить кабель')

        except Exception as e:
            warning(text=f'Непредвиденная ошибка {e}')

    elif result == QMessageBox.Cancel:
        return


# Отключение брандмауэра
def braundmauer():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Отключение брандмауэра для приватного профиля')

    # Проверяем что нажал пользовтель
    if result == QMessageBox.Ok:

        command = 'Set-NetFirewallProfile -Profile Private -Enabled False'
        progress_bar.show()
        update_progress_bar()

        try:
            subprocess.run(['powershell', '-Command', command],check=True, creationflags=CREATE_NO_WINDOW)
            progress_bar.hide()
            warning(text='Брандмауэр отключен!')
        except subprocess.CalledProcessError:
            progress_bar.hide()
            warning(text=f'Ошибка при отключении брандмауэра')

    elif result == QMessageBox.Cancel:
        return

# Электропитание
def pitanie():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Отключение автоматического перехода компьютера в спящий режим')

    # Проверяем что нажал пользовтель
    if result == QMessageBox.Ok:

        commands = [
            ('отключении автоматическое выключение дисплея', 'powercfg -change -monitor-timeout-ac 0'),
            ('отключении автоматического перехода компьютера в спящий режим', 'powercfg -change -standby-timeout-ac 0')
            ]

        try:

            progress_bar.show()

            for name, command in commands:

                try:
                    subprocess.run(["powershell", "-Command", command],shell=True,check=True, creationflags=CREATE_NO_WINDOW)
                    warning(text=f'Выполнено {name}')
                    update_progress_bar(va=50)

                except subprocess.CalledProcessError:
                    warning(text=f'Ошибка при {name}')

            progress_bar.hide()

        except Exception as e:
            warning(text=f'Непредвиденная ошибка {e}')

    elif result == QMessageBox.Cancel:
        return

# Запуск служб
def start_():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Запуск следующий служб: '
                             '\nUPnP-обеспечивает автоматическую настройку и обнаружение устройств в сети;'
                             '\nBITS-используется для передачи файлов в фоновом режиме;'
                             '\nRemoteRegistry-позволяет удалённым пользователям или программам получать доступ и управлять реестром Windows;'
                             '\nSSDPSRV-реализует протокол обнаружения устройств и сервисов в сети;'
                             '\nPlugPlay-автоматически обнаруживает, конфигурирует и управляет подключаемыми устройствами;'
                             '\nFDResPub-публикует ресурсы и службы компьютера в сети с помощью протоколов обнаружения функций;')

    if result == QMessageBox.Ok:
        # Запуск служб
        commands = [
            ('переключении типа службы UPnP на автоматический', 'Set-Service -Name "upnphost" -StartupType Automatic'),
            ('запуск службы UPnP','Start-Service -Name "upnphot"'),
            ('переключении типа службы BITS на автоматический','Set-Service -Name "BITS" -StartupType Automatic'),
            ('запуск службы BITS','Start-Service -Name "BITS"'),
            ('переключении типа службы RemoteRegistry на автоматический','Set-Service -Name "RemoteRegistry" -StartupType Automatic'),
            ('запуск службы RemoteRegistry','Start-Service -Name "RemoteRegistry"'),
            ('переключении типа службы SSDPSRV на автоматический','Set-Service -Name "SSDPSRV" -StartupType Automatic'),
            ('запуск службы SSDPSRV','Start-Service -Name "SSDPSRV"'),
            ('переключении типа службы PlugPlay на автоматический','Set-Service -Name "PlugPlay" -StartupType Automatic'),
            ('запуск службы PlugPlay','Start-Service -Name "PlugPlay"'),
            ('переключении типа службы FDResPub на автоматический','Set-Service -Name "FDResPub" -StartupType Automatic'),
            ('запуск службы FDResPub','Start-Service -Name "FDResPub"')
        ]
        try:

            progress_bar.show()

            for name, command in commands:
                try:
                    subprocess.run(['powershell', '-Command', command], shell=True, check=True, creationflags=CREATE_NO_WINDOW)
                    warning(text=f'Выполнено {name}')
                    update_progress_bar(va=9)

                except subprocess.SubprocessError as e:
                    warning(text=f'Ошибка при {name}')

            progress_bar.hide()

        except Exception as e:
            warning(text=f'Непредвиденная ошибка {e}')

    elif result == QMessageBox.Cancel:
        return

# Остановка служб (чего-то уже нет на ОС 10 и одна не отключается из-за зависимости с RPC её не отключать, а то Active Directory будет не работать)
def stop_():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Останавливаем следующие службы:'
                             '\nWebClient-позволяет приложениям получать доступ к ресурсам, расположенным по протоколам WebDAV, HTTP и HTTPS;'
                             '\nWbioSrvc-управляет биометрическими устройствами;'
                             '\nBthHFSrv-обеспечивает поддержку Bluetooth-гарнитур и устройств для handsfree;'
                             '\nbthserv-обеспечивает поддержку Bluetooth-устройств;'
                             '\nTabletInputService-управляет функциями сенсорных экранов;'
                             '\nRetailDemo-используется для демонстрации устройств и систем;'
                             '\nXboxNetApiSvc-обеспечивает сетевую интеграцию и поддержку Xbox Live;'
                             '\nXblGameSave-управляет автоматическим сохранением данных игр через Xbox Live;'
                             '\nXblAuthManager-отвечает за управление аутентификацией и авторизацией пользователей Xbox Live;'
                             '\nWalletService-управляет функциями цифрового кошелька;'
                             '\nDPS-управление политиками устройств и конфигурациями в Windows;'
                             '\nvmicheartbeat-связанна с компонентами виртуализации Windows;'
                             '\nvmickvpexchange- связанная с виртуализацией Hyper-V;'
                             '\nvmicvmsession-связанна с удалённым управлением и взаимодействием виртуальных машин;'
                             '\nvmictimesync-обеспечивает синхронизацию времени между виртуальной машиной и гипервизором;'
                             '\nvmicvss-необходима для корректной работы функций резервного копирования и восстановления виртуальных машин;'
                             '\nvmicshutdown-обеспечивает корректное завершение работы виртуальной машины;'
                             '\nvmicrdv-управляет удалёнными подключениями и взаимодействием с виртуальными машинами через протокол RDV;')

    if result == QMessageBox.Ok:

        # Выключение служб
        commands = [
        ('Переключении типа службы WebClient на "Disabled"','Set-Service -Name "WebClient" -StartupType disabled'),
        ('Остановка службы WebClient', 'Stop-Service -Name "WebClient"'),
        ('Переключении типа службы WbioSrvc на "Disabled"','Set-Service -Name "WbioSrvc" -StartupType disabled'),
        ('Остановка службы WbioSrvc','Stop-Service -Name "WbioSrvc"'),
        ('Переключении типа службы BthHFSrv на "Disabled"','Set-Service -Name "BthHFSrv" -StartupType disabled'),
        ('Остановка службы BthHFSrv','Stop-Service -Name "BthHFSrv"'),
        ('Переключении типа службы bthserv на "Disabled"','Set-Service -Name "bthserv" -StartupType disabled'),
        ('Остановка службы bthserv','Stop-Service -Name "bthserv"'),
        ('Переключении типа службы TabletInputService на "Disabled"','Set-Service -Name "TabletInputService" -StartupType disabled'),
        ('Остановка службы TabletInputService','Stop-Service -Name "TabletInputService"'),
        ('Переключении типа службы RetailDemo на "Disabled"','Set-Service -Name "RetailDemo" -StartupType disabled'),
        ('Остановка службы RetailDemo','Stop-Service -Name "RetailDemo"'),
        ('Переключении типа службы XboxNetApiSvc на "Disabled"','Set-Service -Name "XboxNetApiSvc" -StartupType disabled'),
        ('Остановка службы XboxNetApiSvc','Stop-Service -Name "XboxNetApiSvc"'),
        ('Переключении типа службы XblGameSave на "Disabled"','Set-Service -Name "XblGameSave" -StartupType disabled'),
        ('Остановка службы XblGameSave','Stop-Service -Name "XblGameSave"'),
        ('Переключении типа службы XblAuthManager на "Disabled"','Set-Service -Name "XblAuthManager" -StartupType disabled'),
        ('Остановка службы XblAuthManager','Stop-Service -Name "XblAuthManager"'),
        ('Переключении типа службы WalletService на "Disabled"','Set-Service -Name "WalletService" -StartupType disabled'),
        ('Остановка службы WalletService','Stop-Service -Name "WalletService"'),
        ('Переключении типа службы DPS на "Disabled"','Set-Service -Name "DPS" -StartupType disabled'),
        ('Остановка службы DPS','Stop-Service -Name "DPS"'),
        ('Переключении типа службы vmicheartbeat на "Disabled"','Set-Service -Name "vmicheartbeat" -StartupType disabled'),
        ('Остановка службы vmicheartbeat','Stop-Service -Name "vmicheartbeat"'),
        ('Переключении типа службы vmickvpexchange на "Disabled"','Set-Service -Name "vmickvpexchange" -StartupType disabled'),
        ('Остановка службы vmickvpexchange','Stop-Service -Name "vmickvpexchange"'),
        ('Переключении типа службы vmicvmsession на "Disabled"','Set-Service -Name "vmicvmsession" -StartupType disabled'),
        ('Остановка службы vmicvmsession','Stop-Service -Name "vmicvmsession"'),
        ('Переключении типа службы vmictimesync на "Disabled"','Set-Service -Name "vmictimesync" -StartupType disabled'),
        ('Остановка службы vmictimesync','Stop-Service -Name "vmictimesync"'),
        ('Переключении типа службы vmicvss на "Disabled"','Set-Service -Name "vmicvss" -StartupType disabled'),
        ('Остановка службы vmicvss','Stop-Service -Name "vmicvss"'),
        ('Переключении типа службы vmicshutdown на "Disabled"','Set-Service -Name "vmicshutdown" -StartupType disabled'),
        ('Остановка службы vmicshutdown','Stop-Service -Name "vmicshutdown"'),
        ('Переключении типа службы vmicrdv на "Disabled"','Set-Service -Name "vmicrdv" -StartupType disabled'),
        ('Остановка службы vmicrdv','Stop-Service -Name "vmicrdv"')
        ]

        try:

            progress_bar.show()

            for name, command in commands:
                try:
                    subprocess.run(["powershell", "-Command", command], shell=True,check=True, creationflags=CREATE_NO_WINDOW)
                    warning(text=f'Выполнено {name}')

                except subprocess.CalledProcessError:
                    warning(text=f'Ошибка при {name}')

            progress_bar.hide()

        except Exception as e:
            warning(text=f'Непредвиденная ошибка {e}')


    elif result == QMessageBox.Cancel:
        return

# Перезапуск службы времени
def time():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Синхронизация времени с сервером 10.2.1.19 \nЗапуск службы времени w32time')
    commands = [
        ('Синхронизация времени с сервером 10.2.1.19', 'w32tm /config /manualpeerlist:"10.2.1.19" /syncfromflags:manual /reliable:yes /update'),
        ('Запуск службы w32time', 'Start-Service w32time')
    ]
    if result == QMessageBox.Ok:
        try:
            progress_bar.show()

            for name, command in commands:
                try:
                    subprocess.run(command, shell=True, check=True, creationflags=CREATE_NO_WINDOW)
                    warning(text=f'Выполнено {name}')
                    update_progress_bar(va=50)

                except subprocess.CalledProcessError:
                    warning(text=f'Ошибка {name}')

            progress_bar.hide()

        except Exception as e:
            warning(text=f'Непредвиденная ошибка {e}')

    elif result == QMessageBox.Cancel:
        return

# Активация виндовс
def act_win():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Активация Windows через kms')

    if result == QMessageBox.Ok:
        commands = [
        r'slmgr /upk',
        r'slmgr /cpky',
        r'slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX',
        r'slmgr /skms WTC-KMS-01.acron.ru',
        r'slmgr /ato'
        ]


        progress_bar.show()

        try:
            for command in commands:
                result = subprocess.run(['powershell', '-Command', command], shell=True, check=True, creationflags=CREATE_NO_WINDOW)
                update_progress_bar(va=10)
            progress_bar.hide()
            warning(text='Активация выполнена')

        except subprocess.CalledProcessError:
            progress_bar.hide()
            warning(text=f'Ошибка при активации Windows')

    elif result == QMessageBox.Cancel:
        return

# Активация офиса
def act_off():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Активация Office через kms')

    if result == QMessageBox.Ok:
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
            progress_bar.show()

            try:
                for command in commands:
                    subprocess.run(command, shell=True,check=True, creationflags=CREATE_NO_WINDOW)
                    update_progress_bar(va=33)
                progress_bar.hide()
                warning(text='Office активирован')
            except subprocess.CalledProcessError:
                progress_bar.hide()
                warning(text=f'Ошибка при активации Office')

        else:
            progress_bar.show()
            try:
                for command_1 in commands_1:
                    subprocess.run(command_1, shell=True,check=True, creationflags=CREATE_NO_WINDOW)
                    update_progress_bar(va=33)
                progress_bar.hide()
                warning(text='Office активирован')
            except subprocess.CalledProcessError as e:
                progress_bar.hide()
                warning(text=f'Ошибка при активации Office')

    elif result == QMessageBox.Cancel:
        return

#Ассоциация файлов
def assoziazion_file():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Ассоциация будет со следующими расширениями:'
                             '\n7Zip-7z'
                             '\nRar-7z'
                             '\nZip-7z'
                             '\ncdw-Компас'
                             '\ndwg-Компас'
                             '\npdf-Adobe'
                             '\ndjvu-SumatraPDF'
                             '\ndoc,docx,ods,odt,vsd,xls-Office'
                             '\nАссоциация настраивается через powershell')



    if result == QMessageBox.Ok:

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

        def get_error_message(command):
            """Определяет сообщение об ошибке по команде."""
            if '.rar' in command:
                return 'Ошибка при ассоциации rar'
            elif '.docx' in command:
                return 'Ошибка при ассоциации docx'
            elif '.zip' in command:
                return 'Ошибка при ассоциации zip'
            elif '.pdf' in command:
                return 'Ошибка при ассоциации pdf'
            elif '.dwg' in command:
                return 'Ошибка при ассоциации dwg'
            elif '.cdw' in command:
                return 'Ошибка при ассоциации cdw'
            elif '.odt' in command:
                return 'Ошибка при ассоциации odt'
            elif '.xls' in command:
                return 'Ошибка при ассоциации xls'
            # добавьте другие расширения по необходимости
            else:
                return 'Общая ошибка'


        try:
            for cmd in commands:
                subprocess.run(cmd, shell=True,check=True, creationflags=CREATE_NO_WINDOW)
            progress_bar.hide()
            warning(text='Ассоциация выполнена')

        except subprocess.CalledProcessError as e:
            progress_bar.hide()

            error_message = get_error_message(e.cmd)

            warning(text=f'{error_message}')

