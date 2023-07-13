from flet import (
    Column,
    MainAxisAlignment,
    Page,
    UserControl,

)

class EditTrainingsPlan(UserControl):
    def __init__(self, page, customerID):
        super.__init__()
        self.page = page
        self.customerID = customerID

    def build(self):
        return Column(

        )