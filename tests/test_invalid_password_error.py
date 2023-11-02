import driver
import pytest
import locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.confest()
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.mark.usefixtures("setup")
class testInvalidPasswordEr:

    def testInvalidPasswordEr(self):
        driver = self.driver
        driver.find_element_by_id(RegistrationPageLocators.NAME_INPUT).send_keys("Имя")
        driver.find_element_by_id(RegistrationPageLocators.EMAIL_INPUT).send_keys("example@example.com")
        driver.find_element_by_id(RegistrationPageLocators.PASSWORD_INPUT).send_keys("short")
        driver.find_element_by_id(RegistrationPageLocators.REGISTER_BUTTON).click()

        error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locators.HomePageLocators.ERROR_MESSAGE))
        assert "Пароль слишком короткий" in error_message.text