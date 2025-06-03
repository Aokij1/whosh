import winreg, os
from PyQt5.QtWidgets import QMessageBox

def warning(text):
    message = QMessageBox()
    message.setWindowTitle("Ошибка!")
    message.setText(text)
    message.setIcon(QMessageBox.Information)
    message.exec_()

# Получение доступа
def dostup():
    try:
        # Добавление значений
        register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                      'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System', 0, winreg.KEY_WRITE)
        winreg.SetValueEx(register_key, 'ConsentPromptBehaviorAdmin', 0, winreg.REG_DWORD, 5)
        winreg.SetValueEx(register_key, 'ConsentPromptBehaviorUser', 0, winreg.REG_DWORD, 3)
        winreg.SetValueEx(register_key, 'DSCAutomationHostEnabled', 0, winreg.REG_DWORD, 2)
        winreg.SetValueEx(register_key, 'EnableCursorSuppression', 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(register_key, 'EnableInstallerDetection', 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(register_key, 'EnableLUA', 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(register_key, 'EnableSecureUIAPaths', 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(register_key, 'EnableUIADesktopToggle', 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(register_key, 'EnableVirtualization', 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(register_key, 'PromptOnSecureDesktop', 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(register_key, 'ValidateAdminCodeSignatures', 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(register_key, 'dontdisplaylastusername', 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(register_key, 'legalnoticecaption', 0, winreg.REG_SZ, '')
        winreg.SetValueEx(register_key, 'legalnoticetext', 0, winreg.REG_SZ, '')
        winreg.SetValueEx(register_key, 'scforceoption', 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(register_key, 'shutdownwithoutlogon', 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(register_key, 'undockwithoutlogon', 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(register_key, 'LocalAccountTokenFilterPolicy', 0, winreg.REG_DWORD, 1)
    
        # Создание новых каталогов
        winreg.CreateKey(register_key, 'Audit')
        winreg.CreateKey(register_key, 'UIPI')
        register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                      'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\UIPI', 0,
                                      winreg.KEY_WRITE)
        winreg.CreateKey(register_key, 'Clipboard')
        register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                      'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\UIPI\\Clipboard', 0,
                                      winreg.KEY_WRITE)
        winreg.CreateKey(register_key, 'ExceptionFormats')
    
        # Добавление значений
        register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                      'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\UIPI\\Clipboard\\ExceptionFormats',
                                      0, winreg.KEY_WRITE)
        winreg.SetValueEx(register_key, 'CF_BITMAP', 0, winreg.REG_DWORD, 2)
        winreg.SetValueEx(register_key, 'CF_DIB', 0, winreg.REG_DWORD, 8)
        winreg.SetValueEx(register_key, 'CF_DIBV5', 0, winreg.REG_DWORD, 17)
        winreg.SetValueEx(register_key, 'CF_OEMTEXT', 0, winreg.REG_DWORD, 7)
        winreg.SetValueEx(register_key, 'CF_PALETTE', 0, winreg.REG_DWORD, 9)
        winreg.SetValueEx(register_key, 'CF_TEXT', 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(register_key, 'CF_UNICODETEXT', 0, winreg.REG_DWORD, 0x0000000d)

        warning(text='Выполнено')
    
    except PermissionError:
        warning(text='Недостаточно прав для записи в реестр. Запустите скрипт с правами администратора.')
    except FileNotFoundError as e:
        warning(text=f'Указанный ключ реестра не найден: \n{e}')
    except OSError as e:
        warning(text=f'Ошибка работы с реестром: \n{e}')
    except CalledProcessError as e:
        warning(text=f'Непредвиденная ошибка: \n{e}')

# Отключаю автоматическое устранение неполадок и ее оповещение через политику
def ne_poladka():
    try:
        register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Windows\\Windows Error Reporting' ,0, winreg.KEY_WRITE)
        winreg.SetValueEx(register_key, 'Disabled', 0, winreg.REG_DWORD, 1)
    
        register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Policies\\Microsoft\\Windows',0,winreg.KEY_WRITE)
        winreg.CreateKey(register_key, 'ScriptedDiagnostics')
    
        register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Policies\\Microsoft\\Windows\\ScriptedDiagnostics' , 0, winreg.KEY_WRITE)
        winreg.SetValueEx(register_key, 'EnableDiagnostics', 0, winreg.REG_DWORD, 0)
    
        winreg.CreateKey(register_key, 'Policy')
        register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Policies\\Microsoft\\Windows\\ScriptedDiagnostics\\Policy' , 0, winreg.KEY_WRITE)
        winreg.SetValueEx(register_key, 'EnableDiagnostics', 0, winreg.REG_DWORD, 1)

        warning(text='Выполнено')
        
    except PermissionError:
        warning(text='Недостаточно прав для записи в реестр. Запустите скрипт с правами администратора.')
    except FileNotFoundError as e:
        warning(text=f'Указанный ключ реестра не найден: \n{e}')
    except OSError as e:
        warning(text=f'Ошибка работы с реестром: \n{e}')
    except CalledProcessError as e:
        warning(text=f'Непредвиденная ошибка: \n{e}')

#Скрытые папки
def data_invis(self):
    register_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(register_key, 'Hidden', 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(register_key, 'HideFileExt', 0, winreg.REG_DWORD, 0)
    winreg.SetValueEx(register_key, 'ShowSuperHidden', 0 , winreg.REG_DWORD, 1)

# Smart
def smart(self):
    register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Policies\\Microsoft\\Windows\\System', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(register_key, 'EnableSmartScreen', 0, winreg.REG_DWORD, 0)

# Панель задач
def panel(self):
    register_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced',0,winreg.KEY_WRITE)
    winreg.SetValueEx(register_key, 'TaskbarGlomLevel', 0, winreg.REG_DWORD, 1)

    winreg.SetValueEx(register_key, 'DontUsePowerShellOnWinX', 0, winreg.REG_DWORD, 1)

# Отключение Windows Defender
def win_def(self):
    register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Policies\\Microsoft\\Windows Defender', 0,
                                  winreg.KEY_WRITE)
    winreg.SetValueEx(register_key, 'DisableAntiSpyware', 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(register_key, 'AllowFastServiceStartup', 0, winreg.REG_DWORD, 0)
    winreg.SetValueEx(register_key, 'ServiceKeepAlive', 0, winreg.REG_DWORD, 0)

    winreg.CreateKey(register_key, 'Real-Time Protection')
    winreg.CreateKey(register_key, 'Spynet')

    register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                  'SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection', 0,
                                  winreg.KEY_WRITE)
    winreg.SetValueEx(register_key, 'DisableOAVProtection', 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(register_key, 'DisableRealtimeMonitoring', 0, winreg.REG_DWORD, 1)

    register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                  'SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Spynet', 0,
                                  winreg.KEY_WRITE)
    winreg.SetValueEx(register_key, 'DisableBlockAtFierstSeen', 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(register_key, 'DisableBlockAtFierstSeen', 0, winreg.REG_DWORD, 0)
    winreg.SetValueEx(register_key, 'SubmitSamplesConsent', 0, winreg.REG_DWORD, 2)

# Отображение иконок для юзера
def data_combo_user():
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                  "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\HideDesktopIcons\\NewStartPanel",
                                  0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, "{20D04FE0-3AEA-1069-A2D8-08002B30309D}", 0, winreg.REG_DWORD,
                      0)  # Мой Пк
    winreg.SetValueEx(registry_key, "{645FF040-5081-101B-9F08-00AA002F954E}", 0, winreg.REG_DWORD,
                      0)  # Корзина
    winreg.SetValueEx(registry_key, "{5399E694-6CE5-4D6C-8FCE-1D8870FDCBA0}", 0, winreg.REG_DWORD,
                      1)  # Убирает Панель управления
    winreg.SetValueEx(registry_key, "{59031a47-3f72-44a7-89c5-5595fe6b30ee}", 0, winreg.REG_DWORD,
                      0)  # Файлы пользователя

    def attention():
        message = QMessageBox()
        message.setWindowTitle("ВНИМАНИЕ!!!")
        message.setText('Обнови рабочий стол "F5"')
        message.setIcon(QMessageBox.Information)
        message.exec_()

    attention()

# Отображение иконок для админа
def data_combo_admin():
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                  "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\HideDesktopIcons\\NewStartPanel",
                                  0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, "{20D04FE0-3AEA-1069-A2D8-08002B30309D}", 0, winreg.REG_DWORD,
                      0)  # Мой Пк
    winreg.SetValueEx(registry_key, "{645FF040-5081-101B-9F08-00AA002F954E}", 0, winreg.REG_DWORD,
                      0)  # Корзина
    winreg.SetValueEx(registry_key, "{5399E694-6CE5-4D6C-8FCE-1D8870FDCBA0}", 0, winreg.REG_DWORD,
                      0)  # Панель управления
    winreg.SetValueEx(registry_key, "{59031a47-3f72-44a7-89c5-5595fe6b30ee}", 0, winreg.REG_DWORD,
                      0)  # Файлы пользователя
    def attention():
        message = QMessageBox()
        message.setWindowTitle("ВНИМАНИЕ!!!")
        message.setText('Обнови рабочий стол "F5"')
        message.setIcon(QMessageBox.Information)
        message.exec_()

    attention()

# Удаление иконок
def data_combo_del():
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                  "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\HideDesktopIcons\\NewStartPanel",
                                  0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, "{20D04FE0-3AEA-1069-A2D8-08002B30309D}", 0, winreg.REG_DWORD,
                      1)  # Мой Пк
    winreg.SetValueEx(registry_key, "{645FF040-5081-101B-9F08-00AA002F954E}", 0, winreg.REG_DWORD,
                      1)  # Корзина
    winreg.SetValueEx(registry_key, "{5399E694-6CE5-4D6C-8FCE-1D8870FDCBA0}", 0, winreg.REG_DWORD,
                      1)  # Панель управления
    winreg.SetValueEx(registry_key, "{59031a47-3f72-44a7-89c5-5595fe6b30ee}", 0, winreg.REG_DWORD,
                      1)  # Файлы пользователя
    def attention():
        message = QMessageBox()
        message.setWindowTitle("ВНИМАНИЕ!!!")
        message.setText('Обнови рабочий стол "F5"')
        message.setIcon(QMessageBox.Information)
        message.exec_()

    attention()


def save_FIO(text: str):
    register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion' ,0, winreg.KEY_WRITE)
    winreg.SetValueEx(register_key, 'RegisteredOwner', 0, winreg.REG_SZ, text)
    winreg.SetValueEx(register_key, 'RegisteredOrganization', 0, winreg.REG_SZ, 'ПАО Дорогобуж')

def disabled_wsh():
    registe_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows Script Host\\Settings" , 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registe_key, "Enabled", 0, winreg.REG_DWORD, 0)

#Обои, аватар, забавные факты
def wapper_avatar():
    register_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(register_key,'SubscribedContent-338387Enabled', 0, winreg.REG_DWORD, 0)

    # Обои
    dir = os.path.abspath(os.curdir) + '_internal\\User_sa.bmp'
    ctypes.windll.user32.SystemParametersInfoW(20, 0, dir, 0)

    #Экран блокировки
    dir = os.path.abspath(os.curdir) + '_internal\\start_pic.jpg'
    register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion')
    winreg.CreateKey(register_key, 'PersonalizationCSP')

    register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                  'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\PersonalizationCSP', 0,
                                  winreg.KEY_WRITE)
    winreg.SetValueEx(register_key, 'LockScreenImagePath', 0, winreg.REG_SZ, dir)
    winreg.SetValueEx(register_key, 'LockScreenImageStatus', 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(register_key, 'PersonalizationCSP', 0, winreg.REG_DWORD, 1)

    command = 'Stop-Process -Name explorer -Force'
    result = subprocess.run(['powershell', '-Command', command])
