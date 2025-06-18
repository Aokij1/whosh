import winreg, os
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer


timer = QTimer()

def set_progress_bar(bar):
    global progress_bar
    progress_bar = bar

def update_progress_bar():
    progress_bar.setValue()
    val = progress_bar.value()+10
    progress_bar.setValue(val)
    if val >= 99:
        timer.stop()

    timer.timeout.connect(update_progress_bar)
    timer.start(300)

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

# Получение доступа
def dostup():
    result = message_warning('Меняются следующие значения в реестре:'
                             '\nConsentPromptBehaviorAdmin'
                             '\nConsentPromptBehaviorUser'
                             '\nDSCAutomationHostEnabled'
                             '\nEnableCursorSuppression'
                             '\nEnableInstallerDetection'
                             '\nEnableLUA'
                             '\nEnableSecureUIAPaths'
                             '\nEnableVirtualization'
                             '\nPromptOnSecureDesktop'
                             '\nValidateAdminCodeSignatures'
                             '\ndontdisplaylastusername'
                             '\nlegalnoticecaption'
                             '\nlegalnoticetext'
                             '\nscforceoption'
                             '\nshutdownwithoutlogon'
                             '\nundockwithoutlogon'
                             '\nLocalAccountTokenFilterPolicy'
                             '\nСоздано 3 каталога:'
                             '\nAudit'
                             '\nUIPI'
                             '\nClipboard')

    if result == QMessageBox.Ok:

        progress_bar.show()
        update_progress_bar()
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
            winreg.CloseKey(register_key)
            progress_bar.hide()
            warning(text='Выполнено!')

        except PermissionError:
            progress_bar.hide()
            warning(text='Недостаточно прав для записи в реестр. Запустите скрипт с правами администратора.')

        except FileNotFoundError as e:
            progress_bar.hide()
            warning(text=f'Указанный ключ реестра не найден: \n{e}')

        except OSError as e:
            progress_bar.hide()
            warning(text=f'Ошибка работы с реестром: \n{e}')

        except CalledProcessError as e:
            progress_bar.hide()
            warning(text=f'Непредвиденная ошибка: \n{e}')

    elif result == QMessageBox.Cancel:
        return


# Отключаю автоматическое устранение неполадок и ее оповещение через политику
def ne_poladka():
    result = message_warning('Будет отключено устранение неполадок и ее оповещения через политику')
    if result == QMessageBox.Ok:
        progress_bar.show()
        update_progress_bar()
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
            winreg.CloseKey(register_key)
            progress_bar.hide()
            warning(text='Выполнено!')

        except PermissionError:
            progress_bar.hide()
            warning(text='Недостаточно прав для записи в реестр. Запустите скрипт с правами администратора.')

        except FileNotFoundError as e:
            progress_bar.hide()
            warning(text=f'Указанный ключ реестра не найден: \n{e}')

        except OSError as e:
            progress_bar.hide()
            warning(text=f'Ошибка работы с реестром: \n{e}')

        except CalledProcessError as e:
            progress_bar.hide()
            warning(text=f'Непредвиденная ошибка: \n{e}')

    elif result == QMessageBox.Cancel:
        return

#Скрытые папки
def data_invis():
    result = message_warning('Будет включено отображение скрытых файлов и системных файлов')

    if result == QMessageBox.Ok:

        progress_bar.show()
        update_progress_bar()
        try:

            register_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 0, winreg.KEY_WRITE)
            winreg.SetValueEx(register_key, 'Hidden', 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(register_key, 'HideFileExt', 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(register_key, 'ShowSuperHidden', 0 , winreg.REG_DWORD, 1)
            winreg.CloseKey(register_key)
            progress_bar.hide()
            warning(text='Выполнено!')

        except PermissionError:
            progress_bar.hide()
            warning(text='Недостаточно прав для записи в реестр. Запустите скрипт с правами администратора.')

        except FileNotFoundError as e:
            progress_bar.hide()
            warning(text=f'Указанный ключ реестра не найден: \n{e}')

        except OSError as e:
            progress_bar.hide()
            warning(text=f'Ошибка работы с реестром: \n{e}')

        except CalledProcessError as e:
            progress_bar.hide()
            warning(text=f'Непредвиденная ошибка: \n{e}')

    elif result == QMessageBox.Cancel:
        return

# Smart
def smart():
    result = message_warning('Будет отключена функция SmartScreen')

    if result == QMessageBox.Ok:

        progress_bar.show()
        update_progress_bar()
        try:

            register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Policies\\Microsoft\\Windows\\System', 0, winreg.KEY_WRITE)
            winreg.SetValueEx(register_key, 'EnableSmartScreen', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(register_key)

            progress_bar.hide()
            warning(text='Выполнено!')

        except PermissionError:
            progress_bar.hide()
            warning(text='Недостаточно прав для записи в реестр. Запустите скрипт с правами администратора.')

        except FileNotFoundError as e:
            progress_bar.hide()
            warning(text=f'Указанный ключ реестра не найден: \n{e}')

        except OSError as e:
            progress_bar.hide()
            warning(text=f'Ошибка работы с реестром: \n{e}')

        except CalledProcessError as e:
            progress_bar.hide()
            warning(text=f'Непредвиденная ошибка: \n{e}')

    elif result == QMessageBox.Cancel:
        return


# Панель задач + забавные факты
def panel():
    result = message_warning('Будут применены следующие изменения:'
                             '\nГруппировка кнопок на панели задач при переполнении'
                             '\nУбираем галочку "Заменить командную строку PowerShell"')

    if result == QMessageBox.Ok:

        progress_bar.show()
        update_progress_bar()
        try:


            register_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced',0,winreg.KEY_WRITE)
            winreg.SetValueEx(register_key, 'TaskbarGlomLevel', 0, winreg.REG_DWORD, 1)

            winreg.SetValueEx(register_key, 'DontUsePowerShellOnWinX', 0, winreg.REG_DWORD, 1)

            # Отключение фактов
            register_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                          'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager', 0,
                                          winreg.KEY_WRITE)
            winreg.SetValueEx(register_key, 'SubscribedContent-338387Enabled', 0, winreg.REG_DWORD, 0)

            progress_bar.hide()
            warning(text='Выполнено!')

        except PermissionError:
            progress_bar.hide()
            warning(text='Недостаточно прав для записи в реестр. Запустите скрипт с правами администратора.')

        except FileNotFoundError as e:
            progress_bar.hide()
            warning(text=f'Указанный ключ реестра не найден: \n{e}')

        except OSError as e:
            progress_bar.hide()
            warning(text=f'Ошибка работы с реестром: \n{e}')

        except CalledProcessError as e:
            progress_bar.hide()
            warning(text=f'Непредвиденная ошибка: \n{e}')

    elif result == QMessageBox.Cancel:
        return

# Отключение Windows Defender
def win_def():
    result = message_warning('Отключение windows defender посредством реестра.')

    if result == QMessageBox.Ok:

        progress_bar.show()
        update_progress_bar()
        try:

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

            progress_bar.hide()
            warning(text='Выполнено!')

        except PermissionError:
            progress_bar.hide()
            warning(text='Недостаточно прав для записи в реестр. Запустите скрипт с правами администратора.')

        except FileNotFoundError as e:
            progress_bar.hide()
            warning(text=f'Указанный ключ реестра не найден: \n{e}')

        except OSError as e:
            progress_bar.hide()
            warning(text=f'Ошибка работы с реестром: \n{e}')

        except CalledProcessError as e:
            progress_bar.hide()
            warning(text=f'Непредвиденная ошибка: \n{e}')

    elif result == QMessageBox.Cancel:
        return

# Отображение иконок для юзера
def data_combo_user():
    result = message_warning('Выводим на рабочий стол иконки: \nМой компьютер; \nМои документы; \nКорзина')

    if result == QMessageBox.Ok:
        progress_bar.show()
        update_progress_bar()
        try:

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

            progress_bar.hide()
            warning(text='Выполнено! \nОбновите рабочий стол')

        except PermissionError:
            progress_bar.hide()
            warning(text='Недостаточно прав для записи в реестр. Запустите скрипт с правами администратора.')

        except FileNotFoundError as e:
            progress_bar.hide()
            warning(text=f'Указанный ключ реестра не найден: \n{e}')

        except OSError as e:
            progress_bar.hide()
            warning(text=f'Ошибка работы с реестром: \n{e}')

        except CalledProcessError as e:
            progress_bar.hide()
            warning(text=f'Непредвиденная ошибка: \n{e}')

    elif result == QMessageBox.Cancel:
        return

# Отображение иконок для админа
def data_combo_admin():
    result = message_warning('Выводим на рабочий стол иконки: \nМой компьютер; \nМои документы; \nКорзина; \nПанель управления')

    if result == QMessageBox.Ok:

        progress_bar.show()
        update_progress_bar()
        try:

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

            progress_bar.hide()
            warning(text='Выполнено! \nОбновите рабочий стол')

        except PermissionError:
            progress_bar.hide()
            warning(text='Недостаточно прав для записи в реестр. Запустите скрипт с правами администратора.')

        except FileNotFoundError as e:
            progress_bar.hide()
            warning(text=f'Указанный ключ реестра не найден: \n{e}')

        except OSError as e:
            progress_bar.hide()
            warning(text=f'Ошибка работы с реестром: \n{e}')

        except CalledProcessError as e:
            progress_bar.hide()
            warning(text=f'Непредвиденная ошибка: \n{e}')

    elif result == QMessageBox.Cancel:
        return


# Удаление иконок
def data_combo_del():
    result = message_warning('Убираем следующие иконки с рабочего стола: \nМой компьютер; \nМои документы; \nКорзина; \nПанель управления')

    if result == QMessageBox.Ok:
        progress_bar.show()
        update_progress_bar()
        try:


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

            progress_bar.hide()
            warning(text='Выполнено! \nОбновите рабочий стол')

        except PermissionError:
            progress_bar.hide()
            warning(text='Недостаточно прав для записи в реестр. Запустите скрипт с правами администратора.')

        except FileNotFoundError as e:
            progress_bar.hide()
            warning(text=f'Указанный ключ реестра не найден: \n{e}')

        except OSError as e:
            progress_bar.hide()
            warning(text=f'Ошибка работы с реестром: \n{e}')

        except CalledProcessError as e:
            progress_bar.hide()
            warning(text=f'Непредвиденная ошибка: \n{e}')

    elif result == QMessageBox.Cancel:
        return


#save
def save_FIO(text: str):
    result = message_warning(f'Записать пользователя {text} в реестр?')

    if result == QMessageBox.Ok:
        progress_bar.show()
        update_progress_bar()
        try:


            register_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion' ,0, winreg.KEY_WRITE)
            winreg.SetValueEx(register_key, 'RegisteredOwner', 0, winreg.REG_SZ, text)
            winreg.SetValueEx(register_key, 'RegisteredOrganization', 0, winreg.REG_SZ, 'ПАО Дорогобуж')

            progress_bar.hide()
            warning(text='Выполнено!')

        except PermissionError:
            progress_bar.hide()
            warning(text='Недостаточно прав для записи в реестр. Запустите скрипт с правами администратора.')

        except FileNotFoundError as e:
            progress_bar.hide()
            warning(text=f'Указанный ключ реестра не найден: \n{e}')

        except OSError as e:
            progress_bar.hide()
            warning(text=f'Ошибка работы с реестром: \n{e}')

        except CalledProcessError as e:
            progress_bar.hide()
            warning(text=f'Непредвиденная ошибка: \n{e}')

    elif result == QMessageBox.Cancel:
        return


def disabled_wsh():
    result = message_warning('Отключение Windows Script Host')

    if result == QMessageBox.Ok:
        progress_bar.show()
        update_progress_bar()
        try:

            registe_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows Script Host\\Settings" , 0, winreg.KEY_WRITE)
            winreg.SetValueEx(registe_key, "Enabled", 0, winreg.REG_DWORD, 0)

            progress_bar.hide()
            warning(text='Выполнено!')

        except PermissionError:
            progress_bar.hide()
            warning(text='Недостаточно прав для записи в реестр. Запустите скрипт с правами администратора.')

        except FileNotFoundError as e:
            progress_bar.hide()
            warning(text=f'Указанный ключ реестра не найден: \n{e}')

        except OSError as e:
            progress_bar.hide()
            warning(text=f'Ошибка работы с реестром: \n{e}')

        except CalledProcessError as e:
            progress_bar.hide()
            warning(text=f'Непредвиденная ошибка: \n{e}')

    elif result == QMessageBox.Cancel:
        return

