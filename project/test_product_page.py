import pytest
from selenium import webdriver
from pages.product_page import ProductPage

# Пример: http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    
    page.add_product_to_basket()
    page.should_be_correct_product_name_in_message(product_name)
    page.should_be_correct_basket_total(product_price)
