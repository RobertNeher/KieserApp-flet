from flet import (
    Column,
    Container,
    CrossAxisAlignment,
    ElevatedButton,
    MainAxisAlignment,
    Page,
    SnackBar,
    Text,
    View,
    app,
    colors,
    theme,
    WEB_BROWSER
)

from src.about import About
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
    # print("Initial: %s" % page.route)
    customerID = 19711
    page.route="/about"

    login=Login(page=page)

    def route_change(e):
        if page.route == "/login":
            page.clean()
            page.add(getAppBar(page, "Login", "/trainingsplan"))
            page.add(login)

        if page.route == "/trainingsplan":
            page.clean()
            page.add(getAppBar(page, "Dein Trainingsplan", "/login"))
            page.add(TrainingsPlan(page=page, customerID=customerID))
            # page.go("/login")

        if page.route == "/about":
            page.clean()
            page.add(getAppBar(page, APP_TITLE, "/login"))
            page.add(About(page=page))

        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)
    page.update()


app(target=main, assets_dir="./assets")