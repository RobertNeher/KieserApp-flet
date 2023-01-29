from datetime import datetime
from flet import (
    Column,
    Container,
    DataCell,
    DataColumn,
    DataRow,
    DataTable,
    Divider,
    FontWeight,
    IconButton,
    MainAxisAlignment,
    Row,
    DataTable,
    Text,
    TextStyle,
    UserControl,
    alignment,
    colors,
    icons,
)
from model.machine import Machine
from src.training_results import trainingResults

class MachineTabContent(UserControl):
    def resultEdit(self,e):
        self.result = e.control.value

        if self.goal == "":
            self.goal = e.control.value

    def goalEdit(self,e):
        self.goal = e.control.value

    def durationEdit(self, e):
        self.duration = e.control.value

    def __init__(self, machineID, parameters, parameterValues, comments, movement, lastResults, saveResults, lastTab):
        super().__init__()
        self.today = datetime.today().strftime("%d.%m.%Y")
        self.goal = 0 if (len(lastResults) == 0) else lastResults["goalNext"]
        self.duration = 120 if (len(lastResults) == 0) else lastResults["duration"]
        self.result = 0 if (len(lastResults) == 0) else lastResults["doneToday"]
        self.machines = Machine()
        self.machineID = machineID
        self.machineDetails = self.machines.lookUp(machineID=machineID)
        self.parameters = parameters
        self.parameterValues = parameterValues
        self.comments = comments
        self.movement = movement
        self.lastResults = lastResults
        self.saveResults = saveResults
        self.lastTab = lastTab

        self.paramsHeader = [
            DataColumn(Text("Parameter")),
            DataColumn(Text("Einstellung"))
        ]

        self.paramRows = []

        for i in range(0, len(self.parameters)):
            self.paramRows.append(
                DataRow(
                    cells=[
                        DataCell(Text(self.parameters[i])),
                        DataCell(Text(self.parameterValues[i])),
                    ]
                )
            )

        self.paramTable = DataTable(
            columns=self.paramsHeader,
            rows=self.paramRows,
            column_spacing=2,
            data_text_style=TextStyle(
                color=colors.WHITE,
                weight=FontWeight.NORMAL,
            ),
            divider_thickness=1,
            heading_text_style=TextStyle(
                color=colors.WHITE,
                weight=FontWeight.BOLD,
            ),
            show_bottom_border=False,
        )

    # TODO: Workaround, because FloatingActionButton is not visible (0.3.2), i.e. it won't show up on top
    def SaveButton(self, showTab: bool):
        if showTab:
            return Container(
                 alignment=alignment.bottom_right,
                 content=IconButton(
                        icon=icons.SAVE,
                        icon_color=colors.WHITE,
                        icon_size=40,
                        bgcolor=colors.BLUE,
                        on_click=self.saveResults,
                        autofocus=True,
                    )
            )
        else:
                return Container()

    def build(self):
        return Column(
            # MainAxisAlignment.SPACE_AROUND,
            controls=[
                Container(
                    alignment=alignment.top_center,
                    content=Text(
                        self.machineDetails["title"],
                        color=colors.WHITE,
                        size=20,
                        weight=FontWeight.BOLD,
                    )
                ),
                Text(
                    self.machineDetails["description"],
                    color=colors.WHITE,
                    size=14,
                    weight=FontWeight.NORMAL,
                ),
                Divider(thickness=2, height=5,color=colors.BLUE),
                Row(
                    # MainAxisAlignment.START,
                    controls=[
                        Column(
                            alignment=MainAxisAlignment.START,
                            controls=[
                                Text(
                                    "Körperbereiche",
                                    color=colors.WHITE,
                                    size=18,
                                    weight=FontWeight.BOLD
                                ),
                                Text(
                                    "<Bild>",
                                    # self.machineDetails["affectedBodyParts"],
                                    color=colors.WHITE,
                                    size=14,
                                    weight=FontWeight.NORMAL
                                ),
                                Text(
                                    "Einzustellende Parameter",
                                    color=colors.WHITE,
                                    size=18,
                                    weight=FontWeight.BOLD
                                ),
                                self.paramTable,
                                # Divider(thickness=2, height=5,color=colors.BLUE),
                                # Text(
                                #     "<a href=\"%s\">Tutorial Video</a>" % self.machineDetails["tutorialVideoURL"],
                                #     color=colors.WHITE,
                                #     size=14,
                                #     weight=FontWeight.NORMAL
                                # ),
                                Container(
                                    height=70,
                                )
                            ]
                        ),
                        # TODO: Replacement for non working VerticalDivider control (0.3.2)
                        Container(
                            height = 350,
                            width = 2,
                            bgcolor=colors.BLUE
                        ),
                        # VerticalDivider(thickness=2, width=20, color=colors.BLUE),
                        Column(
                            alignment=MainAxisAlignment.END,
                            controls=[
                                Text(
                                    "Bewegung",
                                    color=colors.WHITE,
                                    size=18,
                                    weight=FontWeight.BOLD
                                ),
                                Text(
                                    self.movement,
                                    color=colors.WHITE,
                                    size=14,
                                    weight=FontWeight.NORMAL,
                                    width=175,
                                ),
                                Text(
                                    "Hinweise",
                                    color=colors.WHITE,
                                    size=18,
                                    weight=FontWeight.BOLD
                                ),
                                Text(
                                    self.comments,
                                    color=colors.WHITE,
                                    size=14,
                                    weight=FontWeight.NORMAL,
                                    width=200
                                ),

                                # TODO: Column alignment does not work in current version (0.3.2), fix it with later version of Flet
                                Container(
                                    height=250,
                                )
                            ]
                        ),
                    ]
                ),
                Divider(thickness=2, height=5,color=colors.BLUE),
                Column(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Text(
                            "Deine Trainingsdaten für heute (%s)" % self.today,
                            color=colors.WHITE,
                            size=18,
                            weight=FontWeight.BOLD
                        ),
                        Container(height=10),
                        trainingResults(lastResults=self.lastResults, durationEdit=self.durationEdit, resultEdit=self.resultEdit, goalEdit=self.goalEdit),
                        Container(height=10),
                        self.SaveButton(self.lastTab)
                    ]
                )
            ]
        )
