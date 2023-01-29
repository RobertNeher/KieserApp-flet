from flet import (
    AppBar,
    Container,
    ElevatedButton,
    FontWeight,
    Icon,
    IconButton,
    NavigationBar,
    NavigationDestination,
    Page,
    Text,
    TextField,
    TextStyle,
    TextThemeStyle,
    UserControl,
    app,
    colors,
    icons,
    margin,
)

def getAppBar(page: Page, title:str, backRoute:str):
    def onClick(e):
        page.go(backRoute)

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
        )