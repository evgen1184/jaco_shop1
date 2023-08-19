import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_clases import Base



class Cart_page(Base):



    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver

    # locators
    checkout_button = "//button[@id='checkout']"
    sous_plus_button = "//*[@id='app']/div/div[2]/div[3]/div[7]/table/tbody/tr[5]/td[2]/div/button[3]"
    imbir_plus_button = "//*[@id='app']/div/div[2]/div[3]/div[7]/table/tbody/tr[6]/td[2]/div/button[3]"
    word_1 = "//*[@id='app']/div/div[2]/div[3]/div[7]/table/tbody/tr[1]/td[1]/div/span[1]"
    word_2 = "//*[@id='app']/div/div[2]/div[3]/div[7]/table/tbody/tr[2]/td[1]/div/span[1]"
    word_3 = "//*[@id='app']/div/div[2]/div[3]/div[7]/table/tbody/tr[3]/td[1]/div/span[1]"
    word_price_product_1 = "//*[@id='app']/div/div[2]/div[3]/div[7]/table/tbody/tr[1]/td[3]/span"
    word_price_product_2 = "//*[@id='app']/div/div[2]/div[3]/div[7]/table/tbody/tr[2]/td[3]/span"
    word_price_product_3 = "//*[@id='app']/div/div[2]/div[3]/div[7]/table/tbody/tr[3]/td[3]/span"
    word_price_sous = "//*[@id='app']/div/div[2]/div[3]/div[7]/table/tbody/tr[5]/td[3]/span"
    word_price_imbir = "//*[@id='app']/div/div[2]/div[3]/div[7]/table/tbody/tr[6]/td[3]/span"
    word_itog = "//*[@id='app']/div/div[2]/div[3]/div[7]/table/tfoot/tr[2]/td[2]/span"




    #getters

    # def get_checkout_button(self):
    #     return WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_sous_plus_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.sous_plus_button)))

    def get_imbir_plus_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.imbir_plus_button)))

    def get_word_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.word_1)))

    def get_word_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.word_2)))

    def get_word_3(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.word_3)))

    def get_word_price_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.word_price_product_1)))

    def get_word_price_product_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.word_price_product_2)))

    def get_word_price_product_3(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.word_price_product_3)))

    def get_word_price_sous(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.word_price_sous)))

    def get_word_price_imbir(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.word_price_imbir)))

    def get_word_itog(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.word_itog)))





    # Actions

    # def click_checkout_button(self):
    #     self.get_checkout_button().click()
    #     print("Click checkout_button")

    """Добавляем соус"""
    def click_sous_plus_button(self):
        self.get_sous_plus_button().click()
        print("Click sous plus button")

    """Добавляем имбирь"""

    def click_imbir_plus_button(self):
        self.get_imbir_plus_button().click()
        print("Click imbir plus button")

    """Складываем цены трех товаров и возрваращем переменную для сравнения"""
    def summ_itog(self):
        text_price_product_1 = self.get_word_price_product_1().text
        text_price_product_2 = self.get_word_price_product_2().text
        text_price_product_3 = self.get_word_price_product_3().text
        summa_itog = int(text_price_product_1)+int(text_price_product_2)+int(text_price_product_3)
        return summa_itog

    """Складываем три товара, соус, имбирь и возвращаем переменную для сравнения"""
    def summ_itog_plus(self):
        text_price_product_1 = self.get_word_price_product_1().text
        text_price_product_2 = self.get_word_price_product_2().text
        text_price_product_3 = self.get_word_price_product_3().text
        text_price_sous = self.get_word_price_sous().text
        text_price_imbir = self.get_word_price_imbir().text
        summa_itog_plus = int(text_price_product_1)+int(text_price_product_2)+int(text_price_product_3)+int(text_price_sous)+int(text_price_imbir)
        return summa_itog_plus



    # Methods
    """На странице корзины проверяем ссылку, наличие товара и стоимость и возвращаемся назад"""
    def product_confirmation(self):
        self.get_current_url()
        # self.click_sous_plus_button()
        # self.click_imbir_plus_button()
        self.assert_url("https://jacofood.ru/togliatti/cart")
        self.assert_word(word=self.get_word_1(), result="Мадейра сет")
        self.assert_word(word=self.get_word_2(), result="Вулкан сет")
        self.assert_word(word=self.get_word_3(), result="Атлантида сет")
        self.assert_word(word=self.get_word_price_product_1(), result="829")
        self.assert_word(word=self.get_word_price_product_2(), result="905")
        self.assert_word(word=self.get_word_itog(), result="2659")
        self.assert_word(word=self.get_word_itog(), result=str(self.summ_itog()))
        self.driver.back()
        # self.assert_word(word=self.get_word_price_product_2(), result="1810")
        # self.click_checkout_button()

    """Проверяем по сумме что второй товар добавлен и добавляем соус и имбирь, проверяем общую сумму"""
    def product_confirmation_plus(self):
        self.get_current_url()
        self.click_sous_plus_button()
        self.click_imbir_plus_button()
        self.assert_word(word=self.get_word_1(), result="Мадейра сет")
        self.assert_word(word=self.get_word_2(), result="Вулкан сет")
        self.assert_word(word=self.get_word_3(), result="Атлантида сет")
        self.assert_word(word=self.get_word_price_product_1(), result="829")
        self.assert_word(word=self.get_word_price_product_2(), result="1810")
        self.assert_word(word=self.get_word_itog(), result="3592")
        self.assert_word(word=self.get_word_itog(), result=str(self.summ_itog_plus()))





