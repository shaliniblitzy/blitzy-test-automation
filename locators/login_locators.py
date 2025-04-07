from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[span[text()='Sign in']]")
    ERROR_MESSAGE = (By.XPATH, "//ol//li//div[contains(text(), 'Invalid email or password')]")

