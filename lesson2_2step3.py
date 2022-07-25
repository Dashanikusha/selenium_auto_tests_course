from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Взять у этого элемента y и x для задачи^ находим элемент, содержащий текст
    x_elt = browser.find_element(By.CSS_SELECTOR, "#num1")
    # записываем в переменную x текст из элемента x_elt
    x = x_elt.text
    # находим элемент, содержащий текст
    y_elt = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_elt.text
    sum = str(int(x) + int(y))

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)  # ищем элемент с суммой

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)


    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
