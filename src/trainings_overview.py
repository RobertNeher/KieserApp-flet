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
    border,
    colors,
    dropdown
)
from model.result import Result

class TrainingsOverview(UserControl):
    def __init__(self, page, customer_id):
        super().__init__()
        self.page = page
        self.customerID = customer_id
        self.results = Result(customer_id=self.customerID)
        # self.resultsColumns = []
        # self.resultRows = []
        self.dropDownOptions = []
        self.trainingDates = self.results.trainingdates(latest=False)

        if len(self.trainingDates) > 0:
            for trainingDate in self.trainingDates:
                date = datetime.strptime(trainingDate['training_date'], "%Y-%m-%d")
                self.dropDownOptions.append(
                    dropdown.Option(datetime.strftime(date, "%d. %B %Y"))
                )

            self.selectedDate = self.dropDownOptions[0].key
            self.resultsTable = self.result_table(self.selectedDate)
        else:
            self.dropDownOptions.append(dropdown.Option("<Keine Daten>"))

    def formatDate(self, dBYdate):
        return datetime.strftime(datetime.strptime(dBYdate, "%d. %B %Y"), "%Y-%m-%d")

    def result_table(self, trainingsDate):
        resultColumns = [
            DataColumn(
                label=Text(
                    "Gerät",
                    size=14,
                    weight=FontWeight.BOLD,
                    color=colors.BLACK
                )
            ),
            DataColumn(
                numeric=True,
                label=Text(
                    "Dauer",
                    size=14,
                    weight=FontWeight.BOLD,
                    color=colors.BLACK
                )
            ),
            DataColumn(
                numeric=True,
                label=Text(
                    "aufgelegtes\nGewicht",
                    size=14,
                    weight=FontWeight.BOLD,
                    color=colors.BLACK
                )
            ),
            DataColumn(
                numeric=True,
                label=Text(
                    "geplantes\nGewicht",
                    size=14,
                    weight=FontWeight.BOLD,
                    color=colors.BLACK
                )
            ),
        ]

        resultRows = []
        trainingData = self.results.byDate(trainingDate=self.formatDate(trainingsDate))

        print(self.selectedDate, len(trainingData))

        for machine in trainingData:
            resultRows.append(DataRow(
                cells=[
                    DataCell(
                        content=Text(
                            machine["machine_id"],
                            size=14,
                            weight=FontWeight.NORMAL
                        ),
                    ),
                    DataCell(
                        content=Text(
                            machine["duration"],
                            size=14,
                            weight=FontWeight.NORMAL
                        ),
                    ),
                    DataCell(
                        content=Text(
                            machine["weight_done"],
                            size=14,
                            weight=FontWeight.NORMAL
                        ),
                    ),
                    DataCell(
                        content=Text(
                            machine["weight_planned"],
                            size=14,
                            weight=FontWeight.NORMAL
                        ),
                    )
                ]
            ))

        return DataTable(
            bgcolor=colors.WHITE,
            border_radius=10,
            vertical_lines=border.BorderSide(1, colors.BLACK12),
            horizontal_lines=border.BorderSide(1, colors.BLACK12),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color={"hovered": colors.BLACK12},
            heading_row_height=60,
            data_row_color={"hovered": "0x30FF0000"},
            divider_thickness=1,
            column_spacing=30,
            columns=resultColumns,
            rows=resultRows,
        )

    def setDate(self, e):
        self.selectedDate = e.control.value
        self.resultsTable = self.result_table(e.control.value)
        self.page.update()

    def deleteResults(self, e):
        self.results.deleteResults(self.selectedDate)

    def build(self):
        self.resultsTable = self.result_table(self.selectedDate)

        return Column(
            alignment=MainAxisAlignment.START,
            # horizontal_alignment=CrossAxisAlignment.START,
            # scroll=ScrollMode.AUTO,
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
                self.resultsTable,
                Divider(
                    color=colors.BLUE,
                    thickness=1,
                ),
                Row(
                    alignment=MainAxisAlignment.END,
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
