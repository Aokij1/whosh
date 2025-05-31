import wmi,time, os, subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PyQt5.QtWidgets import QMessageBox
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

CREATE_NO_WINDOW = 0x08000000

def warning(text):
    message = QMessageBox()
    message.setWindowTitle("Ошибка!")
    message.setText(text)
    message.setIcon(QMessageBox.Information)
    message.exec_()

def all_drivers():

    prefixes = (
            "PCI\\",
            "ACPI\\VEN",
            "USB\\VID",
            "HDAUDIO\\",
            "HID\\VID"
        )
    found = False
    c = wmi.WMI()

    driver = []

    for driver in c.Win32_PnPSignedDriver():
        if driver.IsSigned == False or not driver.IsSigned:
            Name_Device = driver.DeviceName
            ID_Device = driver.HardwareID
            Version_Device = driver.DriverVersion

            if isinstance(ID_Device, str):
                ID_Device = [ID_Device]
            elif ID_Device is None:
                ID_Device = []

            for hwid in ID_Device:
                if hwid.startswith(prefixes):
                    Driver_ID = hwid

                    # Настройки для Chrome
                    chrome_options = Options()
                    chrome_options.add_argument("--start-maximized")

                    # Запуск Chrome
                    driver = webdriver.Chrome(options=chrome_options)

                    # Сайт который парсим
                    driver.get('https://www.catalog.update.microsoft.com/home.aspx')
                    # Ищем это поле
                    elem = driver.find_element(By.NAME, 'searchTextBox')

                    # Отпрaвляем ключи
                    elem.clear()  # На всякий случай очищаем ключ
                    elem.send_keys(Driver_ID)  # Что будем отпрaвлять
                    elem.send_keys(Keys.RETURN)
                    time.sleep(2)

                    try:
                        # Находим и кликаем на кнопку для скачивания
                        link_elem = driver.find_element(By.CLASS_NAME, 'flatBlueButtonDownload')
                        link_elem.click()
                        time.sleep(2)

                        # Получаем список всех окон
                        windows = driver.window_handles

                        # Переключаемся на новое окно
                        driver.switch_to.window(windows[-1])
                        time.sleep(2)

                        try:
                            # Находим и кликаем на кнопку для скачивания
                            link_down_elem = driver.find_element(By.CLASS_NAME, 'contentTextItemSpacerNoBreakLink')
                            link_down_elem.click()

                            # Закрытие нового окна
                            driver.close()
                            # Переключаемся обратно на главное окно
                            driver.switch_to.window(windows[0])
                            time.sleep(5)
                        except NoSuchElementException:
                            warning(text='Ошибка! \nДрайвер {0} не удалось скачать'.format(Driver_ID))

                    except NoSuchElementException:
                        warning(text='Ошибка! \nДрайвер {0} не найден'.format(Driver_ID))


                    # закрываем браузер
                    driver.close()


                    file_cab = os.path.join(os.path.expanduser("~"), "Downloads", Driver_ID)
                    print(file_cab)
                    command = ["pnputil", "/add-driver", file_cab, "/install"]

                    try:
                        subprocess.run(command, check=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=CREATE_NO_WINDOW)
                        warning(text='Драйвер установлен')
                    except subprocess.CalledProcessError as e:
                        if e.returncode == 2:
                            warning(text=f'Драйвер {Driver_ID} уже установлен')
                        else:
                            warning(text=f'Ошибка при установке драйвера \n{e.cmd}')