from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Checkout:

    Click_Mackbook_XPATH = (By.XPATH,"//h3[normalize-space()='Apple Macbook Pro']")
    Click_Add_to_card_XPATH = (By.XPATH,"//input[@value='Add to Cart']")
    Click_Continue_Shopping_XPATH =(By.XPATH,"//a[@class='btn btn-primary btn-lg']")
    Click_Headphone_XPATH = (By.XPATH,"//h3[normalize-space()='Headphones']")
    Click_Ipad_XPATH = (By.XPATH,"//h3[normalize-space()='Apple iPad Retina']")
    Click_Proceed_to_checkout_XPATH=(By.XPATH,"//a[@class='btn btn-success btn-lg']")
    Enter_First_Name_XPATH =(By.XPATH,"//input[@id='first_name']")
    Enter_Last_Name_Xpath = (By.XPATH,"//input[@id='last_name']")
    Enter_Phone_No_XPATH = (By.XPATH,"//input[@id='phone']")
    Enter_Address_XPATH =(By.XPATH,"//textarea[@id='address']")
    Enter_Zip_XPATH = (By.XPATH,"//input[@id='zip']")
    DROPDOWN_State_XPATH =(By.XPATH,"//select[@id='state']")
    Enter_Owner_Name_XPATH = (By.XPATH,"//input[@id='owner']")
    Enter_CVV_XPATH =(By.XPATH,"//input[@id='cvv']")
    Enter_CardNo_XPATH = (By.XPATH,"//input[@id='cardNumber']")
    DROPDOWN_Year_XPATH =(By.XPATH,"//select[@id='exp_year']")
    DROPDOWN_Month_XPATH = (By.XPATH,"//select[@id='exp_month']")
    Click_Checkout_XPATH = (By.XPATH,"//button[@id='confirm-purchase']")
    Success_Massage_XPATH = (By.XPATH, "//h2[normalize-space()='CredKart']")

    def __init__(self, driver):
        self.driver = driver

    def click_mackbook(self):
        self.driver.find_element(*Checkout.Click_Mackbook_XPATH).click()

    def add_to_card(self):
        self.driver.find_element(*Checkout.Click_Add_to_card_XPATH).click()

    def click_continue_button(self):
        self.driver.find_element(*Checkout.Click_Continue_Shopping_XPATH).click()

    def click_headphone(self):
        self.driver.find_element(*Checkout.Click_Headphone_XPATH).click()

    def click_ipad(self):
        self.driver.find_element(*Checkout.Click_Ipad_XPATH).click()

    def click_checkout(self):
        self.driver.find_element(*Checkout.Click_Proceed_to_checkout_XPATH).click()

    def enter_first_name(self,first_name):
        self.driver.find_element(*Checkout.Enter_First_Name_XPATH).send_keys(first_name)

    def enter_last_name(self,last_name):
        self.driver.find_element(*Checkout.Enter_Last_Name_Xpath).send_keys(last_name)

    def enter_phone_no(self,phone_no):
        self.driver.find_element(*Checkout.Enter_Phone_No_XPATH).send_keys(phone_no)

    def enter_address(self,address):
        self.driver.find_element(*Checkout.Enter_Address_XPATH).send_keys(address)

    def enter_zip(self,zip):
        self.driver.find_element(*Checkout.Enter_Zip_XPATH).send_keys(zip)

    def dropdown_state(self,state_name):
        sate= Select(self.driver.find_element(By.XPATH, "//select[@id='state']"))
        sate.select_by_index(state_name)

    def enter_owner_name(self,owner_name):
        self.driver.find_element(*Checkout.Enter_Owner_Name_XPATH).send_keys(owner_name)

    def enter_cvv_no(self,cvv):
        self.driver.find_element(*Checkout.Enter_CVV_XPATH).send_keys(cvv)

    def enter_card_no(self,card_no):
        self.driver.find_element(*Checkout.Enter_CardNo_XPATH).send_keys(card_no)

    def drop_down_year(self,year):
        Eyear = Select(self.driver.find_element(*Checkout.DROPDOWN_Year_XPATH))
        Eyear.select_by_index(year)

    def drop_down_month(self,month):
        Emonth = Select(self.driver.find_element(*Checkout.DROPDOWN_Month_XPATH))
        Emonth.select_by_index(month)

    def click_checkout_end(self):
        self.driver.find_element(*Checkout.Click_Checkout_XPATH).click()

    def process_success(self):
        try:
            self.driver.find_element(*Checkout.Success_Massage_XPATH)
            return True
        except:
            return False






