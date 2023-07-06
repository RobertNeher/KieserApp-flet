from datetime import datetime
from flet import (
    Container,
    Column,
    CrossAxisAlignment,
    DataCell,
    DataColumn,
    DataRow,
    DataTable,
    Divider,
    Dropdown,
    ElevatedButton,
    FontWeight,
    ListView,
    MainAxisAlignment,
    MaterialState,
    OutlinedButton,
    Row,
    ScrollMode,
    Text,
    UserControl,
    alignment,
    colors,
    dropdown
)
from model.result import Result

HEADER_BG_COLOR = colors.BLACK12
HEADER_HEIGHT = 50
ROW_HEIGHT = 20
COLUMN_SPACE = 15
WIDTH_MACHINE_COLUMN = 80
WIDTH_DURATION_COLUMN = 60
WIDTH_WEIGHT_COLUMN = 110

class TrainingsOverview(UserControl):
    def __init__(self, page, customer_id):
        super().__init__()
        self.page = page
        self.customerID = customer_id
        self.results = Result(customer_id=self.customerID)
        self.dropDownOptions = []
        self.trainingDates = self.results.trainingdates(latest=False)

        if len(self.trainingDates) > 0:
            for trainingDate in self.trainingDates:
                date = datetime.strptime(trainingDate['training_date'], "%Y-%m-%d")
                self.dropDownOptions.append(
                    dropdown.Option(datetime.strftime(date, "%d. %B %Y"))
                )

            self.selectedDate = self.dropDownOptions[0].key
        else:
            self.dropDownOptions.append(dropdown.Option("<Keine Daten>"))

        self.result_header = Row(
            spacing=0,
            controls=[
                Container(
                    width=WIDTH_MACHINE_COLUMN,
                    height=HEADER_HEIGHT,
                    alignment=alignment.center,
                    bgcolor=HEADER_BG_COLOR,
                    content=Text(
                        "Gerät",
                        size=14,
                        weight=FontWeight.BOLD,
                        color=colors.BLACK
                    )
                ),
                Container(
                    width=COLUMN_SPACE * 2,
                    height=HEADER_HEIGHT,
                    bgcolor=HEADER_BG_COLOR
                ),
                Container(
                    width=WIDTH_DURATION_COLUMN,
                    height=HEADER_HEIGHT,
                    alignment=alignment.center_right,
                    bgcolor=HEADER_BG_COLOR,
                    content=Text(
                        "Dauer",
                        size=14,
                        weight=FontWeight.BOLD,
                        color=colors.BLACK
                    )
                ),
                Container(
                    width=COLUMN_SPACE * 2,
                    bgcolor=HEADER_BG_COLOR,
                    height=HEADER_HEIGHT
                ),
                Container(
                    width=WIDTH_WEIGHT_COLUMN,
                    height=HEADER_HEIGHT,
                    alignment=alignment.center_right,
                    bgcolor=HEADER_BG_COLOR,
                    content=Text(
                        "aufgelegtes\nGewicht",
                        size=14,
                        weight=FontWeight.BOLD,
                        color=colors.BLACK
                    )
                ),
                Container(
                    width=COLUMN_SPACE * 2,
                    height=HEADER_HEIGHT,
                    bgcolor=HEADER_BG_COLOR
                ),
                Container(
                    width=WIDTH_WEIGHT_COLUMN,
                    height=HEADER_HEIGHT,
                    alignment=alignment.center_right,
                    bgcolor=HEADER_BG_COLOR,
                    content=Text(
                        "geplantes\nGewicht",
                        size=14,
                        weight=FontWeight.BOLD,
                        color=colors.BLACK
                    )
                ),
            ]
        )
        self.resultRows = []

    def result_rows(self, trainingsDate):
        resultRows = ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        trainingData = self.results.byDate(trainingDate=self.formatDate(trainingsDate))


        for machine in trainingData:
            resultRows.controls.append(Row(
                spacing=0,
                controls=[
                    Container(
                        width=WIDTH_MACHINE_COLUMN,
                        height=ROW_HEIGHT,
                        alignment=alignment.center_left,
                        bgcolor=colors.WHITE,
                        content=Text(
                            machine["machine_id"],
                            size=14,
                            weight=FontWeight.NORMAL,
                            color=colors.BLACK
                        )
                    ),
                    Container(
                        width=COLUMN_SPACE,
                        height=ROW_HEIGHT,
                        bgcolor=colors.WHITE
                    ),
                    Container(
                        width=WIDTH_DURATION_COLUMN,
                        height=ROW_HEIGHT,
                        alignment=alignment.center_right,
                        bgcolor=colors.WHITE,
                        content=Text(
                            machine["duration"],
                            size=14,
                            weight=FontWeight.NORMAL,
                            color=colors.BLACK
                        )
                    ),
                    Container(
                        width=COLUMN_SPACE,
                        height=ROW_HEIGHT,
                        bgcolor=colors.WHITE
                    ),
                    Container(
                        width=WIDTH_WEIGHT_COLUMN,
                        alignment=alignment.center_right,
                        bgcolor=colors.WHITE,
                        content=Text(
                            machine["weight_done"],
                            size=14,
                            weight=FontWeight.NORMAL
                        ),
                    ),
                    Container(
                        width=COLUMN_SPACE,
                        height=ROW_HEIGHT,
                        bgcolor=colors.WHITE
                    ),
                    Container(
                        width=WIDTH_WEIGHT_COLUMN,
                        height=ROW_HEIGHT,
                        alignment=alignment.center_right,
                        bgcolor=colors.WHITE,
                        content=Text(
                            machine["weight_planned"],
                            size=14,
                            weight=FontWeight.NORMAL
                        ),
                    ),
                ]))

            resultRows.controls.append(
                Divider(
                    color = HEADER_BG_COLOR,
                    thickness = 1
                )
            )

        return Container(
            height=600,
            content=resultRows
        )

    def formatDate(self, dBYdate):
        return datetime.strftime(datetime.strptime(dBYdate, "%d. %B %Y"), "%Y-%m-%d")

    def setDate(self, e):
        self.selectedDate = e.control.value
        self.resultRows = self.result_rows(trainingsDate=self.selectedDate)
        self.page.views[1].update()

    def deleteResults(self, e):
        self.results.deleteResults(self.selectedDate)

    def build(self):
        print("build")
        self.resultRows = self.result_rows(trainingsDate=self.selectedDate)

        return Column(
            controls=[
                Row(
                    alignment=alignment.center_left,
                    controls=[
                        Text(
                            "Trainingsdatum",
                            size=16,
                            weight=FontWeight.BOLD,
                            bgcolor=colors.WHITE,
                            color=colors.BLUE,
                        ),
                        Dropdown(
                            value=self.selectedDate,
                            width=170,
                            options=self.dropDownOptions,
                            on_change=self.setDate
                        )
                    ]
                ),
                Divider(
                    color=colors.BLUE,
                    thickness=1,
                ),
                self.result_header,
                Divider(
                    color=colors.BLUE,
                    thickness=1,
                ),
                self.resultRows,
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Container(expand=1),
                        Container(
                            padding=5,
                            bgcolor=colors.RED,
                            content=OutlinedButton(
                                text="Delete selected\nresult set",
                                on_click=self.deleteResults,
                                opacity=0.5,
                            )
                        )
                    ]
                )
            ]
        )
