from flet import (
    AppBar,
    IconButton,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    Text,
    TextThemeStyle,
    colors,
    icons,
)

def kieserAppBar(page:Page, title:str, backRoute:str):
    def onClick(e):
        page.go(backRoute)
    def openEditPreferences(e):
        page.go("/editPreferences")
    def openTrainingsOverview(e):
        page.go("/trainingsOverview")

    return AppBar(
        leading=IconButton(
            icons.ARROW_BACK, on_click=onClick),
        leading_width=40,
        automatically_imply_leading=True,
        title=Text(
            title,
            style=TextThemeStyle(TextThemeStyle.HEADLINE_MEDIUM),
            color=colors.WHITE
        ),
        center_title=False,
        toolbar_height=50,
        bgcolor=colors.BLUE,
        actions=[
            PopupMenuButton(
                items=[
                    PopupMenuItem(
                        text="Einstellungen", on_click=openEditPreferences
                    ),
                    PopupMenuItem(
                        text="Trainings-\nübersicht", on_click=openTrainingsOverview
                    ),
                ]
            )
        ]
    )
