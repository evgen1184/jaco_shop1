import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_clases import Base


class Login_page(Base):

    url = 'https://jacofood.ru/togliatti'

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver

    # locators
    button_togliatti = "/html/body/div[3]/div[3]/div/a[1]"
    button_samara = "/html/body/div[4]/div[3]/div/a[2]"
    button_close = "/html/body/div[4]/div[3]/div/button"
    button_enter = "//*[@id='headerNew']/div/a[10]/span"
    telephone_number = "//input[@id='mui-1']"
    password = "//input[@id='mui-2']"
    login_button = "//div[@class='loginLogin']"


    #getters

    """Получаем Xpath всех кнопок"""

    def get_button_togliatti(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_togliatti)))

    def get_button_samara(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_samara)))

    def get_button_close(self):
        return WebDriverWait(self.driver, 90).until(
            EC.element_to_be_clickable((By.XPATH, self.button_close)))

    def get_button_enter(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.button_enter)))

    def get_telephone_number(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.telephone_number)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))
    # Actions


    def click_button_togliatti(self):
        self.get_button_togliatti().click()
        print("Click button togliatti")

    def click_button_samara(self):
        self.get_button_samara().click()
        print("Click button samara")

    def click_button_close(self):
        self.get_button_close().click()
        print("Click button close")

    def click_button_enter(self):
        self.get_button_enter().click()
        print("Click button enter")

    def input_telephone_number(self, telephone_number):
        self.get_telephone_number().send_keys(telephone_number)
        print("Input telephone number")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login button")


    # Methods
    """ Нажимаем на кнопку close и авторизуемся на сайте"""
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_button_close()
        self.click_button_enter()
        self.input_telephone_number("89022376818")
        self.input_password("secret_sauce")
        self.click_login_button()



