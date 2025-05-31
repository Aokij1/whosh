from PyQt5.QtWidgets import QMessageBox
import os, subprocess, shutil



def processing(text):
    message = QMessageBox()
    message.setWindowTitle("Внимание")
    message.setText(text)
    message.setIcon(QMessageBox.Information)
    message.exec_()


def adob():
    exe_path = os.path.join(os.path.abspath(os.curdir), '_internal', 'AcroRdrDC2100520060_MUI.exe')

    if os.path.exists(exe_path):
        try:
            subprocess.run([exe_path], check=True)
            processing(text='Установка выполнена')
        except subprocess.CalledProcessError as e:
            processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
    else:
        processing(text='Файл не найдет')

def free_vimag():
    exe_path = os.path.join(os.path.abspath(os.curdir), '_internal', 'FreeVimager-9.9.19-Setup-Rus.exe')

    if os.path.exists(exe_path):
        try:
            subprocess.run([exe_path], check=True)
            processing(text='Установка выполнена')
        except subprocess.CalledProcessError as e:
            processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
    else:
        processing(text='Файл не найдет')

def zip():
    exe_path = os.path.join(os.path.abspath(os.curdir), '_internal', '7z2301-x64.exe')

    if os.path.exists(exe_path):
        try:
            subprocess.run([exe_path], check=True)
            processing(text='Установка выполнена')
        except subprocess.CalledProcessError as e:
            processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
    else:
        processing(text='Файл не найдет')

def sumart():
    exe_path = os.path.join(os.path.abspath(os.curdir), '_internal', 'SumatraPDF-3.2-64-install.exe')

    if os.path.exists(exe_path):
        try:
            subprocess.run([exe_path], check=True)
            processing(text='Установка выполнена')
        except subprocess.CalledProcessError as e:
            processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
    else:
        processing(text='Файл не найдет')

def java():
    exe_path = os.path.join(os.path.abspath(os.curdir), '_internal', 'jre-8u311-windows-x64.exe')

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

def komp():
    exe_path = os.path.join(os.path.abspath(os.curdir), '_internal', '3D_Viewer_V16_x64.msi')

    if os.path.exists(exe_path):
        try:
            subprocess.run([exe_path], check=True)
            processing(text='Установка выполнена')
        except subprocess.CalledProcessError as e:
            processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
    else:
        processing(text='Файл не найдет')

def pdf_sam():
    exe_path = os.path.join(os.path.abspath(os.curdir), '_internal', 'PDFsamBasic4Installer.exe')

    if os.path.exists(exe_path):
        try:
            subprocess.run([exe_path], check=True)
            processing(text='Установка выполнена')
        except subprocess.CalledProcessError as e:
            processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
    else:
        processing(text='Файл не найдет')

def chrom():
    exe_path = os.path.join(os.path.abspath(os.curdir), '_internal', 'ChromeStandaloneSetup64.exe')

    if os.path.exists(exe_path):
        try:
            subprocess.run([exe_path], check=True)
            processing(text='Установка выполнена')
        except subprocess.CalledProcessError as e:
            processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
    else:
        processing(text='Файл не найдет')

def framework():
    exe_path = os.path.join(os.path.abspath(os.curdir), '_internal', 'dotnetfx35.exe')

    if os.path.exists(exe_path):
        try:
            subprocess.run([exe_path], check=True)
            processing(text='Установка выполнена')
        except subprocess.CalledProcessError as e:
            processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
    else:
        processing(text='Файл не найдет')

def dame():
    exe_path = os.path.join(os.path.abspath(os.curdir), '_internal', 'DWRCSVista32.MSI')

    if os.path.exists(exe_path):
        try:
            subprocess.run([exe_path], check=True)
            processing(text='Установка выполнена')
        except subprocess.CalledProcessError as e:
            processing(text=f'Ошибка при выполнении команды \n{e} \nКод возврата: {e.returncode}')
    else:
        processing(text='Файл не найдет')