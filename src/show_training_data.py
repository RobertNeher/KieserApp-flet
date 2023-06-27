from datetime import datetime
from flet import (
    Column,
    Container,
    DataCell,
    DataColumn,
    DataRow,
    DataTable,
    Divider,
    Dropdown,
    FontWeight,
    MainAxisAlignment,
    Page,
    Row,
    Tab,
    Tabs,
    Text,
    UserControl,
    alignment,
    colors,
)
from model.result import Result

class ShowTrainingData(UserControl):
    def __init__(self, page: Page, backRoute, customerID):
        super().__init__()
        self.page = page
        self.customerID = customerID
        self.backRoute = backRoute
        self.results = Result(customer_id=customerID)
        self.trainingDates=self.results.trainingdates(latest=False)
        self.results_tabs = []
        self.resultsColumns = []
        self.resultRows = []
        self.dropDownOptions = []
        for trainingDate in self.trainingDates:
            date = datetime.strptime(trainingDate['training_date'], "%Y-%m-%d")
            self.dropDownOptions.append(
                datetime.strftime(date, "%d. %B %Y")
            )
            self.dropDownOptions.append("all")

        self.dateSelection=Dropdown(
            width=100,
            options=self.dropDownOptions,
        )

    def resultsTabs(self):
        self.results_tabs = []

        for training_date in self.trainingDates:
            self.results_tabs.append(
                self.resultTabContent(trainingDate=training_date)
            )

        return self.results_tabs

    def resultTabContent(self, trainingDate):
        return Tab(
            content=self.resultTable(trainingDate=trainingDate),
            text=Text(
                trainingDate,
                size=18,
                weight=FontWeight.BOLD,
                color=colors.WHITE,
                bgcolor=colors.BLUE,
            )
        )

    def resultTable(self, trainingDate):
        trainingData = self.results.byDate(trainingDate=trainingDate)

        self.resultsColumns = [
            DataColumn(
                label=Text(
                    "Gerät",
                )
            ),
            DataColumn(
                label=Text(
                    "Dauer",
                )
            ),
            DataColumn(
                label=Text(
                    "aufgelegtes\nGewicht",
                )
            ),
            DataColumn(
                label=Text(
                    "geplantes\nGewicht",
                )
            ),
        ]
        self.resultRows = []

        for machine in trainingData:
            self.resultRows.append(DataRow(
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
            columns=self.resultsColumns,
            rows=self.resultRows,
        )

    def routeBack(self, e):
        self.page.go(self.backRoute)
        return

    def setDate(self, e):
        self.selectedDate = e.control.value

    def build(self):
        return Container(
                width=500,
                height=600,
                bgcolor=colors.WHITE,
                content=Column(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Row(
                            alignment=alignment.center_left,
                            controls=[
                                Text(
                                    "Datum des\nTrainings",
                                    size=18,
                                    weight=FontWeight.BOLD,
                                    bgcolor=colors.WHITE,
                                    color=colors.BLUE,
                                ),
                                Dropdown(
                                    alignment=alignment.top_center,
                                    options=self.dropDownOptions,
                                    on_change=self.setDate
                                ),
                            ]
                        ),
                        Divider(
                            color=colors.BLUE,
                            thickness=2,
                        ),
                        Tabs(
                            selected_index = 0,
                            tabs=self.results_tabs,
                        )
                    ]
                )
            )
