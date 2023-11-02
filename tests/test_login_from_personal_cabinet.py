import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.mark.usefixtures("setup")
class testLoginFromPersonalCab:

    def testLoginFromPersonalCab(self):
        driver = self.driver
        driver.find_element_by_id(RegistrationPageLocators.LOGIN_BUTTON_PERSONAL_CABINET).click()

        driver.find_element_by_id(RegistrationPageLocators.LOGIN_EMAIL_INPUT).send_keys("example@example.com")
        driver.find_element_by_id(RegistrationPageLocators.LOGIN_PASSWORD_INPUT).send_keys("password123")
        driver.find_element_by_id(RegistrationPageLocators.LOGIN_SUBMIT_BUTTON).click()

        success_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "success-element"))
        )
        assert "Вход выполнен успешно" in success_element.text