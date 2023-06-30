from flet import (
    Page,
    app,
)
from src.trainings_overview import TrainingsOverview

def showSelection(e):
    print(e.control.value)

def main(page: Page):
    t = TrainingsOverview(page, 19711)
    page.controls.append(t)
    page.update()

if __name__ == "__main__":
    app(target=main)