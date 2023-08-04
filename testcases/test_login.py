from pageobj.pagelogin import Login


class Test_Credkart_Login():

    def test_login_001(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.LOGIN_URL()
        self.lp.Enter_Email("test@credence.in")
        self.lp.Enter_Password("test@123")
        self.lp.click_login()
        print(self.lp.login_status())
        if self.lp.login_status() == True :
            assert True
        else:
            assert False

