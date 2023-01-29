from flet import (
    Column,
    Container,
    CrossAxisAlignment,
    ElevatedButton,
    MainAxisAlignment,
    Page,
    TextField,
    UserControl,
    colors,
)
from model.customer import Customer

class Login(UserControl):
    def loginClick(self, e):
        self.customerID = self.customerIDField.value
        if self.customers.lookUp(self.customerIDField.value) == None:
            self.customerIDField.value = ""
        else:
            self.page.go("/trainingsplan")

    def textChange(self, e):
        self.loginButton.disabled = (self.customers.lookUp(e.control.value) == None)
        self.update()

    # def onSubmit(self, e):
    #     self.loginButton.disabled = (self.customers.lookUp(e.control.value) == None)
    #     self.update()

    def __init__(self, page: Page):
        super().__init__()
        self.customers = Customer()
        self.customerID = 19711
        self.page = page

    def build(self):
        self.loginButton = ElevatedButton(
            "Login",
            on_click=self.loginClick,
            bgcolor=colors.BLUE,
            color=colors.WHITE,
        )
        self.customerIDField = TextField(
            label="Ihre Kundennummer",
            width=150,
            bgcolor=colors.BLUE_GREY_50,
            border_color=colors.BLUE,
            value=str(self.customerID),
            hint_text="Ihre Kieser-Kundennummer",
            on_change=self.textChange
        )
        return Container(
                width=500,
                height=300,
                content=Column(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        self.customerIDField,
                        self.loginButton
                    ]
                ),
                bgcolor=colors.WHITE24
            )


#-------------------------- TEST -------------------------#
# if __name__ == "__main__":
#     c = Login(Page page)
#     page.add(Login)