class NavigationHelper:
    def __init__(self,app):
        self.app = app



    def open_empty_form_page(self):
        wd=self.app.wd
        while not len(wd.find_elements_by_xpath("//content-page//div[@class='block-designer-area ui-sortable designer-time']")) == 1:
            wd.find_element_by_xpath("//form-pagination//button//span[@class='glyphicon glyphicon-arrow-right']").click()



