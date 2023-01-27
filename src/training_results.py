from datetime import datetime
from flet import (
    DataCell,
    DataColumn,
    DataRow,
    DataTable,
    InputBorder,
    DataTable,
    Text,
    TextField,
    colors,
)


def trainingResults(lastResults, durationEdit, resultEdit, goalEdit):
        def copyValue(e):
            if (goalField.value == None) or (goalField.value == ""):
                goalField.value = e.control.value
                goalField.update()

        durationField=TextField(
            color=colors.WHITE,
            border=InputBorder.UNDERLINE,
            border_color=colors.WHITE,
            focused_color=colors.WHITE,
            # # TODO: Activate, when label color = border_color. Bug in Flet (0.3.2)
            # # label="Dauer",
            # # TODO: Deactivate, when label color = border_color. Bug in Flet (0.3.2)
            # prefix=Text(
            #     "Dauer:",
            #     color=colors.WHITE,
            #     size=14
            # ),
            # value="120",
            # suffix=Text(
            #     "sec.",
            #     color=colors.WHITE,
            #     size=14
            # ),
            on_change=durationEdit,
            width=150,
            value=lastResults["duration"]
        )
        resultField=TextField(
            color=colors.WHITE,
            border=InputBorder.UNDERLINE,
            border_color=colors.WHITE,
            focused_color=colors.WHITE,
            # # TODO: Activate, when label color = border_color. Bug in Flet (0.3.2)
            # # label="Dauer",
            # # TODO: Deactivate, when label color = border_color. Bug in Flet (0.3.2)
            # prefix=Text(
            #     "Dauer:",
            #     color=colors.WHITE,
            #     size=14
            # ),
            # value="120",
            # suffix=Text(
            #     "sec.",
            #     color=colors.WHITE,
            #     size=14
            # ),
            on_change=resultEdit,
            on_blur=copyValue,
            width=150,
            value=lastResults["doneToday"]
        )

        goalField=TextField(
            color=colors.WHITE,
            border=InputBorder.UNDERLINE,
            border_color=colors.WHITE,
            focused_color=colors.WHITE,
            # # TODO: Activate, when label color = border_color. Bug in Flet (0.3.2)
            # # label="Ziel",
            # # TODO: Deactivate, when label color = border_color. Bug in Flet (0.3.2)
            # prefix=Text(
            #     "Ziel:",
            #     color=colors.WHITE,
            #     size=14
            # ),
            # value="",
            # suffix=Text(
            #     "lbs.",
            #     color=colors.WHITE,
            #     size=14
            # ),
            on_change=goalEdit,
            width=150,
            value=lastResults["goalNext"]
        )

        resultsColumns = [
            DataColumn(
                label=Text(
                    "1",
                    height=0,
                )
            ),
            DataColumn(
                label=Text(
                    "2",
                    height=0,
                    width=150,
                )
            ),
            DataColumn(
                label=Text(
                    "3",
                    height=0
                )
            ),
        ]
        resultsRows = [
            DataRow(
                cells=[
                    DataCell(
                        content=Text(
                            "Dauer:",
                            size=14,
                            color=colors.WHITE
                        ),
                    ),
                    DataCell(
                        content=durationField
                    ),
                    DataCell(
                        content=Text(
                            "sec.",
                            size=14,
                            color=colors.WHITE
                        ),
                    ),
                ]
            ),
            DataRow(
                cells=[
                    DataCell(
                        content=Text(
                            "Ergebnis:",
                            size=14,
                            color=colors.WHITE
                        ),
                    ),
                    DataCell(
                        content=resultField
                    ),
                    DataCell(
                        content=Text(
                            "lbs.",
                            size=14,
                            color=colors.WHITE
                        ),
                    ),
                ]
            ),
            DataRow(
                cells=[
                    DataCell(
                        content=Text(
                            "Ziel:",
                            size=14,
                            color=colors.WHITE
                        ),
                    ),
                    DataCell(
                        content=goalField
                    ),
                    DataCell(
                        content=Text(
                            "lbs.",
                            size=14,
                            color=colors.WHITE
                        ),
                    ),
                ]
            ),

        ]
        return DataTable(
                bgcolor=colors.BLACK,
                columns=resultsColumns,
                heading_row_height=0,
                rows=resultsRows,
                column_spacing=10,
                divider_thickness=0,
                data_row_color=colors.BLUE_GREY,
                show_bottom_border=False,
            )

