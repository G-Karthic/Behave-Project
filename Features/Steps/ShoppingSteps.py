from behave import *
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given('I launch chrome browser')
def LaunchBrowser(context):
    try:
        context.driver = webdriver.Chrome()
    except:
        assert False, "Browser not invoked"


@when('I open ProtoCommerce home Page')
def OpenHomePage(context):
    try:
        context.driver.get("https://rahulshettyacademy.com/angularpractice/")
    except:
        context.driver.close()
        assert False, "Invalid Url"


@when('click on shop button')
def clickShopButton(context):
    try:
        context.driver.find_element(By.XPATH, "//a[contains(@href, 'shop')]").click()
    except NoSuchElementException:
        assert False, "Element not found"


@when('Select a product and add to cart')
def SelectProduct(context):
    products = context.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    try:
        assert len(products) > 0
    except:
        context.driver.close()
        assert False, "Test Failed: Product list empty"

    for productNameList in products:
        productName = productNameList.find_element(By.XPATH, "div/h4/a").text
        if productName == "iphone X":
            productNameList.find_element(By.XPATH, "div/button").click()


@when('click Check out on shopping page')
def clickCheckOutOnShopPage(context):
    try:
        text = context.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").text
        assert text != "Checkout ( 0 )"
    except:
        assert False, "Test failed, product not added to the cart"
    context.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()


@when('click check out on checkout page')
def clickCheckOutOnCheckoutPage(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()


@when('Enter country name')
def EnterCountryName(context):
    context.driver.find_element(By.ID, "country").send_keys("ind")
    wait = WebDriverWait(context.driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))


@when('click on country name')
def clickCountryName(context):
    context.driver.find_element(By.LINK_TEXT, "India").click()


@when('Enable Check box')
def EnableCheckbox(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()


@when('Click on Purchase button')
def ClickPurchaseButton(context):
    context.driver.find_element(By.CLASS_NAME, "btn-success").click()
    context.driver.implicitly_wait(5)


@then('Verify the success message')
def VerifyAlertMessage(context):
    try:
        alertText = context.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
    except:
        context.driver.close()
        assert False, "Success text not captured"
    if "Success" in alertText:
        context.driver.close()
        assert True, "Test Passed"

