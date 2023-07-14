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
    OutlinedButton,
    Page,
    Row,
    SnackBar,
    Text,
    TextStyle,
    UserControl,
    alignment,
    border,
    colors,
    dropdown,
)
from src.confirm import ConfirmDialog
from src.helper import extract_list, formatDate
from model.machine import Machine
from model.plan import Plan

class EditTrainingsPlan(UserControl):
    def __init__(self, page, customerID):
        super().__init__()
        self.page = page
        self.customerID = customerID
        self.trainingPlans = Plan(customerID=self.customerID)
        self.dropDownOptions = []
        self.trainingDates = self.trainingPlans.get_valid_from_dates(customerID=self.customerID)
        self.confirmDialog = ConfirmDialog(
            page=self.page,
            title="Bitte bestätige das Löschen",
            question= "Möchtest du den ausgewählten Trainingsplan löschen?",
            confirmed_action=self.delete_record
        )
        self.page.snack_bar = SnackBar(
            content=Text(""),
            bgcolor=colors.RED
        )

        if len(self.trainingDates) > 0:
            for plan_date in self.trainingDates:
                date = datetime.strptime(plan_date['valid_from'], "%Y-%m-%d")
                self.dropDownOptions.append(
                    dropdown.Option(datetime.strftime(date, "%d. %B %Y"))
                )

            self.selectedDate = self.dropDownOptions[0].key
            self.planRows = []
        else:
            self.dropDownOptions.append(dropdown.Option("<Keine Daten>"))

        self.planColumns = [
            DataColumn(
                label=Text(
                    "Gerät",
                )
            ),
            DataColumn(
                numeric=True,
                label=Text(
                    "Parameter",
                )
            ),
            DataColumn(
                numeric=True,
                label=Text(
                    "Bewegung",
                )
            ),
            DataColumn(
                numeric=True,
                label=Text(
                    "Hinweise",
                )
            ),
        ]

        self.ParameterTableColumns = [
            DataColumn(
                label=Text(
                    "Parameter",
                )
            ),
            DataColumn(
                numeric=True,
                label=Text(
                    "Einstellung",
                )
            ),
        ]

    def plan_rows(self):
        self.planRows = []

        for machine in self.trainingPlans.get_machines(self.customerID, self.selectedDate):
            self.planRows.append(DataRow(
                cells=[
                    DataCell(
                        content=Text(
                            machine["machine_id"],
                        ),
                    ),
                    DataCell(
                        content=self.ParameterTable(machine["machine_id"], machine["machine_parameters"]),
                    ),
                    DataCell(
                        content=Text(
                            machine["machine_movement"],
                        ),
                    ),
                    DataCell(
                        content=Text(
                            machine["machine_comments"],
                        ),
                    )
                ]
            ))

        return self.planRows

    def ParameterTable(self, machineID, settings):
        machine = Machine(machineID=machineID)
        parameterRows = []

        parameterNames = extract_list(machine["parameters"])
        parameterSettings= extract_list(settings)

        for i in range(0, len(parameterNames)):
            parameterRows.append(
                DataRow(
                    cells=[
                        DataCell(
                            content=Text(parameterNames[i])
                        ),
                        DataCell(
                            content=Text(parameterSettings[i])
                        ),
                    ]
                )
            )

        return DataTable(
            heading_row_height=0,
            data_row_height=45,
            data_text_style=TextStyle(
                size = 12,
                weight = FontWeight.NORMAL,
                color=colors.BLACK
            ),
            bgcolor=colors.TRANSPARENT,
            vertical_lines=border.BorderSide(1, colors.BLACK12),
            horizontal_lines=border.BorderSide(1, colors.BLACK12),
            sort_column_index=0,
            sort_ascending=True,
            rows=self.planRows,
            columns=self.planColumns,
        )

    def setDate(self, e):
        self.selectedDate = e.control.value
        print(self.selectedDate)
        self.planTable = self.plan_table()
        self.page.clean()
        self.page.add(
            self.plan_table(),
        )
        self.page.update()

    def delete_record(self, e):
        self.trainingPlans.deletePlan(ymdDateString=self.formatDate(self.selectedDate))
        self.confirmDialog.close_dialog(e)
        self.page.snack_bar.content=Text(
            f"Trainingsplan vom {self.selectedDate} gelöscht!",
            color=colors.WHITE,
            weight=FontWeight.BOLD,
            size=14
        )
        self.page.snack_bar.open = True

    def deletePlan(self, e):
        self.confirmDialog.open_confirm_dialog()

    def plan_table(self):
        self.planTable = Column(
            alignment=MainAxisAlignment.START,
            controls=[
                Row(
                    alignment=alignment.center_left,
                    controls=[
                        Text(
                            "Gültig ab",
                            size=16,
                            weight=FontWeight.BOLD,
                            bgcolor=colors.WHITE,
                            color=colors.BLUE,
                        ),
                        Dropdown(
                            value=self.selectedDate,
                            width=190,
                            options=self.dropDownOptions,
                            on_change=self.setDate
                        )
                    ],
                ),
                Divider(
                    color=colors.BLUE,
                    thickness=1,
                ),
                DataTable(
                    bgcolor=colors.WHITE,
                    border_radius=10,
                    vertical_lines=border.BorderSide(1, colors.BLACK12),
                    horizontal_lines=border.BorderSide(1, colors.BLACK12),
                    sort_column_index=0,
                    sort_ascending=True,
                    heading_text_style=TextStyle(
                        size=16,
                        weight=FontWeight.BOLD,
                        color=colors.BLACK,
                    ),
                    heading_row_color=colors.BLACK12,
                    heading_row_height=50,
                    data_row_height=40,
                    data_text_style=TextStyle(
                        size=14,
                        weight=FontWeight.NORMAL,
                        color=colors.BLACK,
                    ),
                    divider_thickness=1,
                    column_spacing=30,
                    columns=self.planColumns,
                    rows=self.plan_rows(),
                ),
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
                            bgcolor=colors.TRANSPARENT,
                            content=OutlinedButton(
                                text="Löschen dieses\n Trainingplans",
                                on_click=self.deletePlan,
                                opacity=1.0,
                            )
                        )
                    ]
                )
            ]
        )

        return self.planTable

    def build(self):
        return self.plan_table()