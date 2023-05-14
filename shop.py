import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from login_registration import *#my_email, my_password, home_url#, 
from selenium.webdriver.support.select import Select

# test data
    #for shop_show_page_item
test_css_selector_item_1= ".post-181"
test_title_item = 'HTML5 Forms'
    #for  count_of_items_in_a_category
test_css_selector_cat = ".cat-item-19 > a"
test_exp_amount_item_int = 5
    #for display_discount_item
test_css_selector_item_2 = '.post-169'
test_exp_old_price = '₹600.00'
test_exp_new_price = '₹450.00'

#=========================================================================================================

def shop_show_page_item(css_selector_item, title_item):
    #4
    item =  driver.find_element("css selector", css_selector_item)
    item.click()
    #5 Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
    content_title = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.product_title.entry-title'),title))
    print('Заголовок книги "'+ title_item +'":', content_title)


def shop_count_of_items_in_a_category(css_selector_cat, exp_amount_int):
    #4
    category = driver.find_element("css selector", css_selector_cat)
    category.click()
    #5 
    amount_items = len(driver.find_elements('css selector','.products .product'))
    if (amount_items == exp_amount_int):
        print ("Количество товаров в категории верное")
    else:
        print ('Количество товаров в категории не верное:\nРезультат-', amount_items ,"\nОжидаемый результат-",exp_amount_int )
    

def shop_sort_items():
    # 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию • Используйте проверку по value
    sort_item_selector = driver.find_element("name","orderby")# .woocommerce-ordering > select
    selector_checked = sort_item_selector.get_attribute("value")#
    assert selector_checked == "menu_order"
    #5. Отсортируйте товары по цене от большей к меньшей • в селекторах используйте класс Select
    sort_item_selector.click()
    select = Select(sort_item_selector)
    select.select_by_value("price-desc")
    #6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
    sort_item_selector = driver.find_element("name","orderby")
    #7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей • Используйте проверку по value
    selector_checked = sort_item_selector.get_attribute("value")#
    assert selector_checked == "price-desc"

def shop_display_discount_item(css_selector_item, exp_old_price, exp_new_price):
    #4. Откройте книгу "Android Quick Start Guide"
    item =  driver.find_element("css selector", css_selector_item)
    item.click()
    #5. Добавьте тест, что содержимое старой цены = "₹600.00"
    wait = WebDriverWait(driver, 10)
    old_price_check =  wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.price del .woocommerce-Price-amount'),exp_old_price))
    print('Старая цена', old_price_check)
    #6. Добавьте тест, что содержимое новой цены = "₹450.00"
    new_price_check =  wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.price ins .woocommerce-Price-amount'),exp_new_price))
    print('Новая цена', new_price_check)
    #7. Добавьте явное ожидание и нажмите на обложку книги • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
    cover_book = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
    cover_book.click()
    #8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа) 
    close_view = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
    close_view.click()


def shop_check_price_in_cart():
    pass
    #3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
        # если эта книга будет out of stock - тогда вместо неё добавьте книгу HTML5 Forms и выполните тесты по аналогии
        # если все книги будут out of stock - тогда пропустите это и следующие два задания

    #4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00" • Используйте для проверки assert

    #5. Перейдите в корзину

    #6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость

    #7. Используя явное ожидание, проверьте что в Total отобразилась стоимость



def shop_actions_in_cart():
    pass
    # 1. Откройте https://practice.automationtesting.in/ # в этом тесте логиниться не нужно
    # 2. Нажмите на вкладку "Shop"
    # 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
        # • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
        # • После добавления 1-й книги добавьте sleep
    # 4. Перейдите в корзину
    # 5. Удалите первую книгу
        # • Перед удалением добавьте sleep
    # 6. Нажмите на Undo (отмена удаления)
    # 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
        # • Предварительно очистите поле с помощью локатор_поля.clear()
    # 8. Нажмите на кнопку "UPDATE BASKET"
    # 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
    # 10. Нажмите на кнопку "APPLY COUPON"
        # • Перед нажатимем добавьте sleep
    # 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
    # если эти книги будут out of stock - тогда вместо них добавьте книгу HTML5 Forms и любую доступную книгу по JS и выполните тесты по аналогии

def shop_buy_items():
    pass
    #1. Откройте https://practice.automationtesting.in/ # в этом тесте логиниться не нужно
    #2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
    #3. Добавьте в корзину книгу "HTML5 WebApp Development"
    #4. Перейдите в корзину
    #5. Нажмите "PROCEED TO CHECKOUT" • Перед нажатием, добавьте явное ожидание
    #6. Заполните все обязательные поля 
            #• Перед заполнением first name, добавьте явное ожидание 
            #• Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
            #• Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
    #7. Выберите способ оплаты "Check Payments"
        #• Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
    #8. Нажмите PLACE ORDER
    #9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
   #10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"


if __name__ == "__main__":
    login_shop(my_email, my_password, home_url)
    #3 Нажмите на вкладку "Shop"
    shop_pg = driver.find_element("id", "menu-item-40")
    shop_pg.click()
# ========================= ниже раскомментировать строку с нужной функцией , только  для функций shop_buy_items  и shop_buy_items дополнительно нужно заккоментировать вызов функции login_shop(my_email, my_password, home_url)
#==============================================================================================================================================================================================================
    #shop_show_page_item(test_css_selector_item_1, test_title_item)
    #shop_count_of_items_in_a_category(test_css_selector_cat, test_exp_amount_item_int)
    #shop_sort_items()
    #shop_display_discount_item(test_css_selector_item_2, test_exp_old_price, test_exp_new_price)
    #shop_check_price_in_cart()
    #shop_actions_in_cart()
    #shop_buy_items()
    #driver.quit()