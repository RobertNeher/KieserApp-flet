from datetime import datetime
from flet import (
    ElevatedButton,
    Page,
    app,
)
from src.trainings_overview import TrainingsOverview
from src.confirm import ConfirmDialog


def main(page: Page):
    def open_dialog(e):
        t.open_confirm_dialog()

    def action(what):
        print(f"Action at {datetime.strftime(datetime.now(), '%H:%M:%S')}")

    page.add(ElevatedButton("OK", on_click=open_dialog))
    t = ConfirmDialog(page=page, confirmed_action=action)

if __name__ == "__main__":
    app(target=main)