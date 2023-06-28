from flet import (
    Container,
    FontWeight,
    Page,
    Tab,
    Tabs,
    Text,
    UserControl,
    alignment,
    colors,
)
from model.preferences import Preferences
from model.machine import Machine
from model.plan import Plan
from model.result import Result
from src.machine_tab_content import MachineTabContent
from src.helper import extract_list

class TrainingsPlan(UserControl):
    def __init__(self, page, customer_id):
        super().__init__()
        self.customer_id = customer_id
        self.machineTabs = []
        self.plan = Plan(customer_id=customer_id)
        self.results = Result(customer_id=customer_id)
        self.page = page
        self.prefs = Preferences()
        self.tabs = []

    def saveResults(self, e):
        for machineTab in self.machineTabs:
            print(machineTab.weightPlannedEdit)

    def triggerAutoForward(self, e):
        if self.prefs.auto_forward:
            self.tabs.selected_index += 1 if self.tabs.selected_index < len(self.plan.plan) - 1 else 0
            self.tabs.update()

    def build(self):
        i = 0

        for machine in self.plan.plan:
            machineDetail = Machine(machine_id=machine["machine_id"])

            parameters = extract_list(machineDetail.machines["parameters"])
            values = extract_list(machine["machine_parameters"])

            self.machineTabs.append(Tab(
                tab_content=Container(
                        alignment=alignment.center,
                        height=40,
                        # width=45,
                        bgcolor=colors.BLUE,
                        content=Text(machine["machine_id"],
                            size=24,
                            weight=FontWeight.BOLD,
                            color=colors.WHITE
                        ),
                ),
                content=Container(
                    padding=10,
                    bgcolor=colors.BLACK,
                    content=MachineTabContent(
                        customerID = self.customer_id,
                        machineID=machine["machine_id"],
                        parameters=parameters,
                        parameterValues=values,
                        comments=machine["machine_comments"],
                        movement=machine["machine_movement"],
                        lastResults=self.results.latest(machine_id=machine["machine_id"]),
                        lastTab=(i == (len(self.plan.plan) - 1)),
                        autoForward=self.triggerAutoForward)
                    ),
                )
            )
            i += 1

        self.tabs = Tabs(
                selected_index=0,
                tabs=self.machineTabs,
                indicator_color=colors.RED,
                indicator_tab_size=True,
                indicator_border_radius=5,
                indicator_padding=3,
                indicator_border_side=colors.AMBER,
                divider_color=colors.BLACK
            )

        return Container(
            height=900,
            padding=0,
            content=self.tabs
        )


#-------------------------- TEST -------------------------#
# if __name__ == "__main__":
#     plan = TrainingsPlan(page=Page(), customer_id=19711)

#     print(plan.machines)
#     print(plan.plan)