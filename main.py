from flet import (
    Column,
    Container,
    CrossAxisAlignment,
    ElevatedButton,
    MainAxisAlignment,
    Page,
    View,
    app,
    colors,
    theme,
    WEB_BROWSER
)

from src.login import Login
from src.trainings_plan import TrainingsPlan
from src.helper import getAppBar

APP_TITLE = "Dein Trainingsbegleiter"

def main(page: Page):
    page.window_bgcolor = colors.BLUE_GREY_100,
    page.fonts = {
        "Raleway": "fonts/Raleway-Regular.ttf",
        "Kieser": "fonts/KieserApp.ttf",
        "OpenSans": "fonts/OpenSans-Regular.ttf"
    }
    page.theme = theme.Theme(
        color_scheme_seed=colors.BLACK,
        font_family="Raleway",
        use_material3=True
    )
    page.title = APP_TITLE
    # page.add(TrainingsPlan(page=page, customerID=19711))
    # page.route = "/trainingsPlan"
    page.window_max_height= 1200
    page.window_max_width=540
    page.window_height=1200
    page.window_width=540

    customerID = 19711

    def route_change(e):
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    Container(
                        width=page.window_width,
                        height=page.window_height - 125,
                        bgcolor=colors.WHITE10,
                        content=Column(
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            ElevatedButton(
                                "Login",
                                on_click=doLogin,
                                bgcolor=colors.BLUE,
                                color=colors.WHITE
                            )
                        ]
                    ))
                ],
                appbar=getAppBar(APP_TITLE)
            )
        )
        if page.route == "/login":
            login = Login(page)
            page.views.append(
                View(
                    "/login",
                    [
                        login
                    ],
                    appbar=getAppBar("Login")
                )
            )

        if page.route == "/trainingsplan":
            training = TrainingsPlan(page=page, customerID=customerID)
            page.views.append(
                View(
                    "/trainingsplan",
                    [
                      training
                    ],
                    appbar=getAppBar("Dein Trainingsplan")
                )
            )

        # page.update()

    def doLogin(e):
        login=Login(page)
        page.go("/trainingsplan")

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


app(target=main, assets_dir="./assets", view=WEB_BROWSER)