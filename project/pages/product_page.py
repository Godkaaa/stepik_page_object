from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_correct_product_name_in_message(self, expected_name):
        actual_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert actual_name == expected_name, \
            f"Expected product name in message '{expected_name}', but got '{actual_name}'"

    def should_be_correct_basket_total(self, expected_price):
        actual_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert actual_total == expected_price, \
            f"Expected basket total '{expected_price}', but got '{actual_total}'"
