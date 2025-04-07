from locators.login_locators import LoginLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self, base_url):
        self.driver.get(base_url)

    def enter_email(self, email):
        self.driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*LoginLocators.ERROR_MESSAGE).text
