from selenium.webdriver.common.by import By


class Login:
    Text_Email_XPATH = (By.XPATH,"//input[@id='email']")
    Text_password_XPATH = (By.XPATH,"//input[@id='password']")
    Click_Login_Button_XPATH = (By.XPATH,"//button[@type='submit']")
    Login_Status_XPATH =[By.XPATH,"//h2[normalize-space()='CredKart']"]

    def __init__(self,driver):
        self.driver = driver

    def LOGIN_URL(self):
        self.driver.get("https://automation.credence.in/login")

    def Enter_Email(self,email):
        self.driver.find_element(*Login.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self,password):
        self.driver.find_element(*Login.Text_password_XPATH).send_keys(password)

    def click_login(self):
        self.driver.find_element(*Login.Click_Login_Button_XPATH).click()

    def login_status(self):
        try:
            self.driver.find_element(*Login.Login_Status_XPATH)
            return True
        except:
            return False
