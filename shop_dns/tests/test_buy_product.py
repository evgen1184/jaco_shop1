import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
# from pages.cart_page import Cart_page
# from pages.client_information_page import Client_information_page
# from pages.finish_page import Finish_page
from pages.login_page import Login_page
# from pages.main_page import Main_page
# from pages.payment_page import Payment_page
import undetected_chromedriver as uc

from pages.main_page import Main_page


# @pytest.mark.run(order=3)
def test_buy_product_1():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    # patch = "C:\\Users\\Егор\\PycharmProjects\\resource\\chromedriver.exe"
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)


    print("Start test 1")



    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products()

    cp = Cart_page(driver)
    cp.product_confirmation()

    mp = Main_page(driver)
    mp.select_products_plus()

    cp = Cart_page(driver)
    cp.product_confirmation_plus()






    print("Finish test 1")


# @pytest.mark.run(order=1)






