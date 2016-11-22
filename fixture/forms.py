import time

class FormsHelper:
    def __init__(self,app):
        self.app = app


    def insert_new_form_page(self):
        wd=self.app.wd
        if self.is_avaialble("//div/div[@class='btn-group split-button pull-right form-page-change-control']/button[text()='Insert Page']"):
            self.app.navigation.select_page_for_editing('2')
            return
        wd.find_element_by_xpath("//div/div[@class='btn-group split-button pull-right form-page-change-control']/button[text()='Insert Page']").click()

    def is_avaialble(self,element_xpath):
        wd = self.app.wd
        if wd.find_element_by_xpath("%s" % element_xpath).get_attribute('disabled'):
            return True
        else:
            return False



    def delete_form_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='btn-group split-button pull-right form-page-change-control']//button[@class='btn btn-default dropdown-toggle']//span[@class='caret']").click()
        if not self.is_avaialble("//div[@class='btn-group split-button pull-right form-page-change-control open']//li"):
            wd.find_element_by_xpath("//div[@class='btn-group split-button pull-right form-page-change-control open']//li//a[text()='Delete Page']").click()
        self.app.wait("//div[@class='modal-content']//button[text()='Delete']")
        wd.find_element_by_xpath("//div[@class='modal-content']//button[text()='Delete']").click()
        time.sleep(0.5)


    def wait(self,main_page_element):
        wd = self.app.wd
        while len(wd.find_elements_by_xpath("%s" % main_page_element)) == 0:
            wd.implicitly_wait(5)
        pass
        return


    def get_page_value(self):
        wd = self.app.wd
        current_page = wd.find_element_by_xpath("//form-pagination//button[@class='btn dropdown-toggle btn-default']/span").text
        return int(current_page)

    def get_number_of_pages(self):
        wd = self.app.wd
        elements = wd.find_elements_by_xpath("//div[@class='designer-pagination']//div[@class='btn-group']/div[@class='dropdown-menu']//ul/li//span")
        return len(elements)




