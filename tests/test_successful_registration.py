import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


# Ваши локаторы
class RegistrationPageLocators:
    NAME_INPUT = "name"
    EMAIL_INPUT = "email"
    PASSWORD_INPUT = "password"
    REGISTER_BUTTON = "register-button"
    LOGIN_BUTTON_HOMEPAGE = "login-button-homepage"
    LOGIN_BUTTON_REGISTRATION_FORM = "login-button-registration-form"
    LOGIN_BUTTON_PASSWORD_RECOVERY_FORM = "login-button-password-recovery-form"
    LOGIN_BUTTON_PERSONAL_CABINET = "login-button-personal-cabinet"
    LOGIN_EMAIL_INPUT = "login-email"
    LOGIN_PASSWORD_INPUT = "login-password"
    LOGIN_SUBMIT_BUTTON = "login-submit-button"


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestStellarBurgers:

    def test_successful_registration(self):
        driver = self.driver
        driver.find_element_by_id(RegistrationPageLocators.NAME_INPUT).send_keys("Имя")
        driver.find_element_by_id(RegistrationPageLocators.EMAIL_INPUT).send_keys("example@example.com")
        driver.find_element_by_id(RegistrationPageLocators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element_by_id(RegistrationPageLocators.REGISTER_BUTTON).click()

        # Проверка на успешную регистрацию
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "success-message"))
        )
        assert "Регистрация прошла успешно" in success_message.text