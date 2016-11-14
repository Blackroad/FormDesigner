class FormsHelper:
    def __init__(self,app):
        self.app = app


    def insert_new_form_page(self):
        wd=self.app.wd
        if self.is_avaialble("//div/div[@class='btn-group split-button pull-right form-page-change-control']/button"):
            self.select_previous_page()
            wd.find_element_by_xpath("//div/div[@class='btn-group split-button pull-right form-page-change-control']/button[text()='Insert Page']").click()

    def is_avaialble(self,element_xpath):
        wd = self.app.wd
        try:
            element_availability = wd.find_element_by_xpath("%s" % element_xpath).get_attribute('disabled')
            return element_availability
        except:
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


    def delete_form_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='btn-group split-button pull-right form-page-change-control']//button[@class='btn btn-default dropdown-toggle']//span[@class='caret']").click()
        if not self.is_avaialble("//div[@class='btn-group split-button pull-right form-page-change-control open']//li"):
            wd.find_element_by_xpath("//div[@class='btn-group split-button pull-right form-page-change-control open']//li//a[text()='Delete Page']").click()
            self.wait_for_allert_window("")



    def allert_for_delete_form(self,Delete=None):
        wd = self.app.wd
        if Delete == True:
            wd.find_element_by_xpath("//div//button[@class='btn btn-default ng-binding ng-scope' and text()='%s']"%Delete).click()
        wd.find_element_by_xpath("//div//button[@class='btn btn-default ng-binding ng-scope' and text()='Cancel']").click()

    def wait_for_allert_window(self, allert_widnow):
        
