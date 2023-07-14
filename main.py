import locale

from flet import (
    Page,
    Theme,
    View,
    app,
    colors
)
from src.trainings_overview import TrainingsOverview
from src.about import About
from src.login import Login
from src.trainings_plan import TrainingsPlan
from edit_trainings_plan import EditTrainingsPlan
from src.app_bar import kieserAppBar
from src.edit_preferences import EditPreferences
from model.preferences import Preferences

APP_TITLE = "Dein Trainingsbegleiter"

def main(page: Page):
    customerid = 0
    prefs = Preferences()
    locale.setlocale(locale.LC_TIME, "de_DE")
    page.window_bgcolor = colors.BLUE_GREY_100,
    page.fonts = {
        "Raleway": "fonts/Raleway-Regular.ttf",
        "Kieser": "fonts/KieserApp.ttf",
        "OpenSans": "fonts/OpenSans-Regular.ttf"
    }
    page.theme = Theme(
        color_scheme_seed=colors.BLACK,
        font_family="Raleway",
        use_material3=True
    )
    page.title = APP_TITLE
    page.window_max_height= 1000
    page.window_max_width=500
    page.window_height=1000
    page.window_width=500
    page.route="/login"

    def setCustomerID(customerID):
        customerID = customerID

    def route_change(route):
        if page.route == "/login":
            page.views.clear()
            page.views.append(
                View(
                    "/",
                    [
                        kieserAppBar(page, "Login", "/trainingsplan"),
                        Login(page=page, setCustomerID=setCustomerID)
                    ]
                )
            )

        if page.route == "/trainingsplan":
            page.views.append(
                View(
                    "/trainingsplan",
                    [
                        kieserAppBar(page, "Dein Trainingsplan", "/login"),
                        TrainingsPlan(page, customerID=19711)
                    ]
                )
            )

        if page.route == "/editPreferences":
            page.views.append(
                View(
                    "/editPreferences",
                    [
                        kieserAppBar(page, "Einstellungen", "/login"),
                        EditPreferences(page, "/login")
                    ]
                )
            )

        if page.route == "/trainingsPlanOverview":
            page.views.append(
                View(
                    "/trainingsPlanOverview",
                    [
                        kieserAppBar(page, "Bearbeitung Trainingspläne", "/login"),
                        EditTrainingsPlan(page, customerID=19711)
                    ]
                )
            )

        if page.route == "/trainingsOverview":
            page.views.append(
                View(
                    "/trainingsOverview",
                    [
                        kieserAppBar(page, "Letzte Trainings", "/login"),
                        TrainingsOverview(page, customerID=19711)
                    ]
                )
            )

        if page.route == "/about":
            page.views.append(
                View(
                    "/about",
                    [
                        kieserAppBar(page, APP_TITLE, "/login"),
                        About(page)
                    ]
                )
            )
        page.go(page.route)

    def view_pop():
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.update()


app(target=main, assets_dir="./assets")
