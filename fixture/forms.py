class FormsHelper:
    def __init__(self,app):
        self.app = app


    def insert_new_form_page(self):
        wd=self.app.wd
        wd.implicitly_wait(5)
        if self.is_avaialble("//div/div[@class='btn-group split-button pull-right form-page-change-control']/button[text()='Insert Page']"):
            self.select_page_for_editing('2')
        wd.find_element_by_xpath("//div/div[@class='btn-group split-button pull-right form-page-change-control']/button[text()='Insert Page']").click()

    def is_avaialble(self,element_xpath):
        wd = self.app.wd
        if wd.find_element_by_xpath("%s" % element_xpath).get_attribute('disabled'):
            return True
        else:
            return False

    def select_next_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form-pagination//button//span[@class='glyphicon glyphicon-arrow-right']").click()

    def select_previous_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form-pagination//button//span[@class='glyphicon glyphicon-arrow-left']").click()

    def select_last_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form-pagination//button//span[@class='glyphicon glyphicon-step-forward']").click()

    def select_page_for_editing(self,page_number):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='btn-group']//button[@class='btn dropdown-toggle btn-default']/span[@class='caret']").click()
        wd.find_element_by_xpath("//div[@class='dropdown-menu']/ul[@class='dropdown-menu']/li[@ng-click='ddeCtrl.select(option)']/span[text()='%s']" % page_number).click()

    def delete_form_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='btn-group split-button pull-right form-page-change-control']//button[@class='btn btn-default dropdown-toggle']//span[@class='caret']").click()
        if not self.is_avaialble("//div[@class='btn-group split-button pull-right form-page-change-control open']//li"):
            wd.find_element_by_xpath("//div[@class='btn-group split-button pull-right form-page-change-control open']//li//a[text()='Delete Page']").click()
            wd.switch_to_alert()
            try:
                wd.find_element_by_xpath("//div[@class='modal-content']//button[@ng-repeat='button in popUpContentCtrl.buttons']").click()
            except:
                return False


    def wait(self,main_page_element):
        wd = self.app.wd
        while len(wd.find_elements_by_xpath("%s']" % main_page_element)) > 0:
            pass
        wd.implicitly_wait(5)
        return


