import time

from pageobj.checkoutpage import Checkout
from pageobj.pagelogin import Login


class Test_Checkout:

    def test_checkout_001(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.LOGIN_URL()
        self.lp.Enter_Email("test@credence.in")
        self.lp.Enter_Password("test@123")
        self.lp.click_login()
        self.ck = Checkout(self.driver)
        self.ck.click_mackbook()
        self.ck.add_to_card()
        time.sleep(2)
        self.ck.click_continue_button()
        self.ck.click_headphone()
        time.sleep(2)
        self.ck.add_to_card()
        self.ck.click_continue_button()
        self.ck.click_ipad()
        self.ck.add_to_card()
        time.sleep(2)
        self.ck.click_checkout()
        self.ck.enter_first_name('prajwal')
        self.ck.enter_last_name('Amrutkar')
        time.sleep(2)
        self.ck.enter_phone_no(8806625895)
        self.ck.enter_address('neel gagan socirty nagpur')
        self.ck.enter_zip(442701)
        self.ck.dropdown_state(2)
        self.ck.enter_owner_name('Prajwal Amrutkar')
        time.sleep(2)
        self.ck.enter_cvv_no(257)
        self.ck.enter_card_no(4716)
        self.ck.enter_card_no(1089)
        self.ck.enter_card_no(9971)
        self.ck.enter_card_no(6531)
        time.sleep(2)
        self.ck.drop_down_year(2)
        self.ck.drop_down_month(2)
        self.ck.click_checkout_end()
        if self.ck.process_success() == True:
            self.driver.save_screenshot("D:\\pageobject\\test_checkout_001_pass.PNG")
            assert True
        else:
            assert False




