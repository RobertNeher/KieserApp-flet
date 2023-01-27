from flet import (
    AppBar,
    Column,
    Container,
    CrossAxisAlignment,
    ElevatedButton,
    Icon,
    MainAxisAlignment,
    Page,
    Text,
    TextButton,
    TextField,
    UserControl,
    alignment,
    app,
    colors,
    icons,
    margin,
)
from model.customer import Customer

class Login(UserControl):
    def loginClick(self, e):
        self.customerID = self.customerIDField.value
        
        if self.customers.lookUp(self.customerIDField.value) != None:
            self.page.route = "/trainingsplan"
        else:
            self.page.route = "/"

        self.page.update()

    def textChange(self, e):
        self.loginButton.disabled = (self.customers.lookUp(e.control.value) == None)
        self.update()

    def onSubmit(self, e):
        self.loginButton.disabled = (self.customers.lookUp(e.control.value) == None)
        self.update()

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
            value=self.customerID,
            hint_text="Ihre Kieser-Kundennummer",
            on_change=self.textChange
        )
        return Container(
                width=500,
                height=400,
                content=Column(
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        self.customerIDField,
                        Container(height=300),
                        self.loginButton
                    ]
                ),
                bgcolor=colors.WHITE24
            )


#-------------------------- TEST -------------------------#
# if __name__ == "__main__":
#     c = Login(Page page)
#     page.add(Login)