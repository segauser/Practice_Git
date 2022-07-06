"""
Задание 25.3.1
Написать тест, который проверяет, что на странице со списком питомцев пользователя:

1.Присутствуют все питомцы.
2.Хотя бы у половины питомцев есть фото.
3.У всех питомцев есть имя, возраст и порода.
4.У всех питомцев разные имена.
5.В списке нет повторяющихся питомцев. (Сложное задание).
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from collections import Counter


def chrome_options(chrome_options):
    chrome_options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    chrome_options.add_argument('--kiosk')
    return chrome_options


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('../Module_24/chromedriver.exe')
    # неявное ожидание
    pytest.driver.implicitly_wait(10)

    # Без увеличения размера экрана тест падает, так как не видит кнопку мои питомцы
    pytest.driver.set_window_size(1400, 1000)

    # Переходим на страницу авторизации
    pytest.driver.get('https://petfriends.skillfactory.ru/login')
    yield
    pytest.driver.quit()


# Проверка страницы "мои питомцы"
def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('abuser@abuser.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('abuser')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на странице "все питомцы"
    assert WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located([By.CLASS_NAME, "card-deck"]))
    # Нажимаем на кнопку "мои питомцы"
    pytest.driver.find_element_by_xpath("//a[@class='nav-link']").click()
    # time.sleep(5) # плохая практика использования
    # Проверяем, что мы оказались на странице "мои питомцы"
    assert WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located([By.CLASS_NAME, "table-hover"]))
    # Получаем все фотографии питомцев на странице
    images = pytest.driver.find_elements_by_css_selector('th img')
    # Получаем всю информацию о питомцах на странице
    pets_info = pytest.driver.find_elements_by_css_selector('div td')

    # Сортируем информацию о питомцах и записываем в отдельные переменные
    names = pets_info[::4] #  создаём новый список элементов с соответствующими полями
    breeds = pets_info[1::4]
    ages = pets_info[2::4]

    # Получаем информацию профиля и записываем в переменную
    amount = pytest.driver.find_elements_by_css_selector('div.\.col-sm-4.left')
    # Подсчёт питомцев с фото
    pets_with_photo = 0
    # Список имён питомцев
    list_names = []
    # Инфа о питомцах
    all_pets = []

    for i in range(len(names)):
        # Записываем количество питомце, у которых есть фото
        if len(images[i].get_attribute('src')) > 1:
            pets_with_photo += 1
        # 3 Проверяем, что у всех питомцев есть имя
        assert names[i].text != ''
        # 3 Проверяем, что у всех питомцев есть порода
        assert breeds[i].text != ''
        # 3 Проверяем, что у всех питомцев есть возраст
        assert ages[i].text != ''
        # Добавляем имена питомцев в список
        list_names.append(names[i].text)
        # Добавляем имена + породы + возраст каждого питомца в список
        all_pets.append(names[i].text + breeds[i].text + ages[i].text)


    # 1 Проверяем, что присутствуют все питомцы
    assert f"Питомцев: {len(names)}" in amount[0].text
    # 2 Проверяем, что минимум у половины питомцев есть фото
    assert pets_with_photo >= len(names) / 2
    # 4 Проверяем, что имена уникальны
    assert len(Counter(list_names)) == len(list_names)
    # 5 Проверяем, что нет повторяющихся питомцев
    assert len(Counter(all_pets)) == len(all_pets)
