import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get('https://www.ozon.ru/')

# Проверяет поиск по сайту
search_box = driver.find_element(By.XPATH,
                                 '//*[@id="chrome-search"]')
search_box.send_keys('Корзина')
time.sleep(1)
search_button = driver.find_element(By.XPATH,
                                    '//*[@id="chrome-sticky-header"]/div[1]/div/div/div/form/div/button')
search_button.click()

answer = driver.find_element(By.XPATH,
                             '//*[@id="search-term-banner"]/p[2]')

if answer.text != u'корзина':
    print(datetime.datetime.now(), "№1 Ожидаемый ответ верен =  %r" % answer.text)
else:
    print("Ожидаемый ответ ", answer.text, " не найден")

time.sleep(2)

# Проверяет сортировку товара
sort_button = driver.find_element(By.XPATH,
                                  '//*[@id="plp"]/div/div[2]/div/div/div/div[1]/ul/li[4]/div/button')
time.sleep(1)
sort_button.click()
time.sleep(1)
type_sort = driver.find_element(By.XPATH,
                                '//*[@id="plp"]/div/div[2]/div/div/div/div[1]/ul/li[4]/div/div/div/ul/li[1]/div/label/div')
type_sort.click()
time.sleep(1)
sort_button.click()
print(datetime.datetime.now(), '№2 Сортировка успешна')

# Проверяет добавление товара в избранное
sell_box = driver.find_element(By.XPATH,
                               '//*[@id="product-201308084"]/a')

sell_box.click()
time.sleep(1)
wish_button = driver.find_element(By.XPATH,
                                  '//*[@id="product-save"]/div/button')
wish_button.click()
time.sleep(1)
wish_list_button = driver.find_element(By.XPATH,
                                       '//*[@id="chrome-sticky-header"]/div[1]/div/ul/li[2]/a')
wish_list_button.click()

print(datetime.datetime.now(), '№3 Товар добавлен в список желаемого')
time.sleep(1)

# Проверяет добавление товара в корзину
sell_box2 = driver.find_element(By.XPATH,
                                '//*[@id="saved-lists-app"]/main/div/div[1]/section/ol/li/div/div/div/a')
sell_box2.click()
time.sleep(0.5)

add_bag_button = driver.find_element(By.XPATH,
                                     '//*[@id="product-add-button"]')
add_bag_button.click()
time.sleep(0.5)

bag_button = driver.find_element(By.XPATH,
                                 '//*[@id="chrome-sticky-header"]/div[1]/div/ul/li[3]/a')
bag_button.click()
time.sleep(3)
print(datetime.datetime.now(), '№4 Товар добавлен в корзину')

# Проверяет удаление товара из корзины
del_button = driver.find_element(By.XPATH,
                                 '//*[@id="bagApp"]/div[1]/div/div[1]/div[1]/bag-group-list/ul/li/bag-item-list/ul/li/div/div/div/bag-remove/div/button')

del_button.click()
time.sleep(5)
print(datetime.datetime.now(), '№5 Товар удален')

# Проверяет переход по ссылке на соц. сети сайта через кнопку
insta_button = driver.find_element(By.XPATH,
                                   '//*[@id="chrome-footer"]/footer/div[1]/div[1]/ul[1]/li[2]/a')
insta_button.click()
print(datetime.datetime.now(), '№6 Переход по кнопке успешен')
time.sleep(15)

driver.quit()