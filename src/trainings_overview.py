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
    Ref,
    Row,
    ScrollMode,
    Tab,
    Tabs,
    Text,
    UserControl,
    alignment,
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
        self.resultsColumns = []
        self.resultRows = []
        self.dropDownOptions = []
        self.trainingDates = self.results.trainingdates(latest=False)

        if len(self.trainingDates) > 0:
            for trainingDate in self.trainingDates:
                date = datetime.strptime(trainingDate['training_date'], "%Y-%m-%d")
                self.dropDownOptions.append(
                    dropdown.Option(datetime.strftime(date, "%d. %B %Y"))
                )

            self.selectedDate = self.dropDownOptions[0].key
            self.resultTable = self.result_table(self.selectedDate)
        else:
            self.dropDownOptions.append(dropdown.Option("<Keine Ergebnisse>s"))
        

    def result_table(self, trainingsDate):
        results = Result(customer_id=self.customerID)
        resultColumns = [
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

        resultRows = []
        trainingData = results.byDate(trainingDate=datetime.strftime(datetime.strptime(trainingsDate, "%d. %B %Y"), "%Y-%m-%d"))
        print(len(trainingData))
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
            columns=resultColumns,
            rows=resultRows,
        )

    def setDate(self, e):
        self.selectedDate = e.control.value
        self.resultTable = self.result_table(self.selectedDate)
        self.page.clean()
        self.page.add(
            Row(
                alignment=alignment.center_left,
                controls=[
                    Text(
                        "Datum des Trainings",
                        size=16,
                        weight=FontWeight.BOLD,
                        bgcolor=colors.WHITE,
                        color=colors.BLUE,
                    ),
                    Dropdown(
                        value=self.dropDownOptions[0].key,
                        width=170,
                        options=self.dropDownOptions,
                        on_change=self.setDate
                    )
                ]
            ),
        )
        self.page.add(
            Divider(
                color=colors.BLUE,
                thickness=2,
            )
        )
        self.page.add(
            self.resultTable
        )
    
    def build(self):
        return self.page
    