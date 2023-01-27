from flet import (
    AppBar,
    Container,
    ElevatedButton,
    FontWeight,
    Icon,
    IconButton,
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

def getAppBar(title):
    return AppBar(
            # leading=IconButton(icons.APPS_SHARP),
            # leading_width=50,
            # automatically_imply_leading=True,
            title=Text(
                title,
                style=TextThemeStyle(TextThemeStyle.HEADLINE_MEDIUM),
                color=colors.WHITE
            ),
            center_title=False,
            toolbar_height=50,
            bgcolor=colors.BLUE,
        )