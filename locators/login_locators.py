from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[span[text()='Sign in']]")
    ERROR_MESSAGE = (By.XPATH, "//ol//li//div[contains(text(), 'Invalid email or password')]")
    ERROR_REQUIRED_EMAIL = (By.XPATH, "//div[@class='form-error-note' and contains(text(), 'Email is required')]")
    ERROR_REQUIRED_PASSWORD = (By.XPATH, "//div[@class='form-error-note' and contains(text(), 'Password is required')]")

