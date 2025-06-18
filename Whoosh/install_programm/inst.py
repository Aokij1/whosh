from PyQt5.QtWidgets import QMessageBox
import os, subprocess, shutil

install_path = ""

def do_install(path):
    global install_path
    install_path = path
    print(install_path)

def processing(text):
    message = QMessageBox()
    message.setWindowTitle("Внимание")
    message.setText(text)
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

# Устанавливаем Adobe
def adob():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Запустит файл установки Adobe. \n(ПрогрессБар не будет отображаться)')

    # Проверяем что нажал пользовтель
    if result == QMessageBox.Ok:


        exe_path = (install_path + '/AcroRdrDC2100520060_MUI.exe')
        if os.path.exists(exe_path):
            try:
                subprocess.run([exe_path], check=True)
                processing(text='Установка выполнена')
            except subprocess.CalledProcessError as e:
                processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
        else:
            processing(text='Файл не найдет')


    elif result == QMessageBox.Cancel:
        return

# Устанавливаем Free_vimage
def free_vimag():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Запустит файл установки Free Vimage. \n(ПрогрессБар не будет отображаться)')

    # Проверяем что нажал пользовтель
    if result == QMessageBox.Ok:


        exe_path = (install_path +  '/FreeVimager-9.9.19-Setup-Rus.exe')

        if os.path.exists(exe_path):
            try:
                subprocess.run([exe_path], check=True)
                processing(text='Установка выполнена')
            except subprocess.CalledProcessError as e:
                processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
        else:
            processing(text='Файл не найдет')



    elif result == QMessageBox.Cancel:
        return
#

# Устанавливаем 7Zip
def zip():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Запустит файл установки 7Zip. \n(ПрогрессБар не будет отображаться)')

    # Проверяем что нажал пользовтель
    if result == QMessageBox.Ok:

        exe_path = (install_path + '/7z2301-x64.exe')

        if os.path.exists(exe_path):
            try:
                subprocess.run([exe_path], check=True)
                processing(text='Установка выполнена')
            except subprocess.CalledProcessError as e:
                processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
        else:
            processing(text='Файл не найдет')



    elif result == QMessageBox.Cancel:
            return
#

# Устанавливаем Sumatra
def sumart():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Запустит файл установки Sumatra. \n(ПрогрессБар не будет отображаться)')

    # Проверяем что нажал пользовтель
    if result == QMessageBox.Ok:


        exe_path = (install_path + '/SumatraPDF-3.2-64-install.exe')

        if os.path.exists(exe_path):
            try:
                subprocess.run([exe_path], check=True)
                processing(text='Установка выполнена')
            except subprocess.CalledProcessError as e:
                processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
        else:
            processing(text='Файл не найдет')



    elif result == QMessageBox.Cancel:
        return
#

# Установка java и копирование файла javaw.exe в C:\Windows\ и C:\Windows\System32\
def java():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Запустит файл установки java. \nКопируем файл "javaw.exe" в "C:\Windows\" и "C:\Windows\System32\" \n(ПрогрессБар не будет отображаться)')

    # Проверяем что нажал пользовтель
    if result == QMessageBox.Ok:


        exe_path = (install_path + '/jre-8u311-windows-x64.exe')

        if os.path.exists(exe_path):
            try:
                result = subprocess.run([exe_path],  check=True)
                if result.returncode == 0:
                # Копирование файла
                    url_1 = 'C:\\Program Files\\Java\\jre1.8.0_311\\bin\\javaw.exe'
                    url_2 = 'C:\\Windows\\'
                    url_3 = 'C:\\Windows\\System32\\'
                    try:
                        result_1 = subprocess.run(shutil.copy(url_1, url_2))
                        result_2 = subprocess.run(shutil.copy(url_1, url_3))
                        processing(text='Установка и копироване выполнено!')
                    except subprocess.CalledProcessError as e:
                        processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')

                else:
                    processing(text='Копирование не выполнено!')
            except subprocess.CalledProcessError as e:
                processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
        else:
            processing(text='Файл не найден')



    elif result == QMessageBox.Cancel:
        return
#

# Установка КОМПАСА
def komp():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Запустит файл установки КОМПАСА. \n(ПрогрессБар не будет отображаться)')

    # Проверяем что нажал пользовтель
    if result == QMessageBox.Ok:


        exe_path = (install_path + '/3D_Viewer_V16_x64.msi')

        if os.path.exists(exe_path):
            try:
                subprocess.run([exe_path], check=True)
                processing(text='Установка выполнена')
            except subprocess.CalledProcessError as e:
                processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
        else:
            processing(text='Файл не найдет')



    elif result == QMessageBox.Cancel:
        return
#

# Установка PDFSam
def pdf_sam():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Запустит файл установки PDFSam. \n(ПрогрессБар не будет отображаться)')

    # Проверяем что нажал пользовтель
    if result == QMessageBox.Ok:


        exe_path = (install_path + '/PDFsamBasic4Installer.exe')

        if os.path.exists(exe_path):
            try:
                subprocess.run([exe_path], check=True)
                processing(text='Установка выполнена')
            except subprocess.CalledProcessError as e:
                processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
        else:
            processing(text='Файл не найдет')



    elif result == QMessageBox.Cancel:
        return
#

# Установка Google Chrome
def chrom():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Запустит файл установки Google Chrome. \n(ПрогрессБар не будет отображаться)')

    # Проверяем что нажал пользовтель
    if result == QMessageBox.Ok:


        exe_path = (install_path + '/ChromeStandaloneSetup64.exe')

        if os.path.exists(exe_path):
            try:
                subprocess.run([exe_path], check=True)
                processing(text='Установка выполнена')
            except subprocess.CalledProcessError as e:
                processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
        else:
            processing(text='Файл не найдет')



    elif result == QMessageBox.Cancel:
        return
#

# Установка FrameWork
def framework():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Запустит файл установки PDFSam. \n(ПрогрессБар не будет отображаться)')

    # Проверяем что нажал пользовтель
    if result == QMessageBox.Ok:


        exe_path = (install_path + '/dotnetfx35.exe')

        if os.path.exists(exe_path):
            try:
                subprocess.run([exe_path], check=True)
                processing(text='Установка выполнена')
            except subprocess.CalledProcessError as e:
                processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
        else:
            processing(text='Файл не найдет')



    elif result == QMessageBox.Cancel:
        return
#

# Установка DWRCS
def dame():
    # Получаем значение из окна предупреждений попутно вызывая его с текстом
    result = message_warning('Запустит файл установки PDFSam. \n(ПрогрессБар не будет отображаться)')

    # Проверяем что нажал пользовтель
    if result == QMessageBox.Ok:


        exe_path = (install_path + '/DWRCSVista32.MSI')

        if os.path.exists(exe_path):
            try:
                subprocess.run([exe_path], check=True)
                processing(text='Установка выполнена')
            except subprocess.CalledProcessError as e:
                processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
        else:
            processing(text='Файл не найдет')



    elif result == QMessageBox.Cancel:
        return
