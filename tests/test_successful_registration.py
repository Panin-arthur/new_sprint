import fake
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
class testSuccessfulReg:

    def testSuccessfulReg(self):
        driver = self.driver
        name = "Имя"
        email = fake.email()
        driver.find_element_by_id(RegistrationPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element_by_id(RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element_by_id(RegistrationPageLocators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element_by_id(RegistrationPageLocators.REGISTER_BUTTON).click()

        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "success-message"))
        )
        assert "Регистрация прошла успешно" in success_message.text