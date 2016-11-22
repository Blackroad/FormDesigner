class NavigationHelper:
    def __init__(self,app):
        self.app = app



    def open_empty_form_page(self):
        wd=self.app.wd
        while not len(wd.find_elements_by_xpath("//content-page//div[@class='block-designer-area ui-sortable designer-time']")) == 1:
            wd.find_element_by_xpath("//form-pagination//button//span[@class='glyphicon glyphicon-arrow-right']").click()

    def select_next_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form-pagination//button//span[@class='glyphicon glyphicon-arrow-right']").click()

    def select_previous_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form-pagination//button//span[@class='glyphicon glyphicon-arrow-left']").click()

    def select_last_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form-pagination//button//span[@class='glyphicon glyphicon-step-forward']").click()

    def select_page_for_editing(self, page_number):
        wd = self.app.wd
        wd.find_element_by_xpath(
            "//div[@class='btn-group']//button[@class='btn dropdown-toggle btn-default']/span[@class='caret']").click()
        wd.find_element_by_xpath(
            "//div[@class='dropdown-menu']/ul[@class='dropdown-menu']/li[@ng-click='ddeCtrl.select(option)']/span[text()='%s']" % page_number).click()






