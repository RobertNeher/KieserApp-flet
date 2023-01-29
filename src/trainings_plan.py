import json
from datetime import datetime
from flet import (
    Container,
    ControlEvent,
    FontWeight,
    Page,
    SnackBar,
    Tab,
    Tabs,
    Text,
    UserControl,
    colors,
)
from model.machine import Machine
from model.plan import Plan
from model.result import Result
from src.machine_tab_content import MachineTabContent

class TrainingsPlan(UserControl):
    def __init__(self, page: Page, customerID: int):
        super().__init__()
        self.machinesDetail = Machine()
        self.plan = Plan()
        self.results = Result(customerID=customerID)
        self.page = page
        self.customerID = customerID
        self.machinePark=self.machinesDetail.all()
        self.trainingsPlan = self.plan.lookUp(customerID=customerID)
        self.machines = self.trainingsPlan["machines"]

    def saveResults(self, e:ControlEvent):
        results = []
        for machineTab in self.machineTabs:
            results.append({
                "machineID": machineTab.content.content.machineID,
                "duration":  machineTab.content.content.duration,
                "doneToday":  machineTab.content.content.result,
                "goalNext":  machineTab.content.content.goal
            })

        resultJson = {
            "trainingDate": datetime.today().strftime("%Y-%m-%d"),
            "results": results
        }
        self.results.saveResults(resultJson)

    def build(self):
        i = 0
        self.machineTabs = []

        for machine in self.machines:
            self.machineTabs.append(Tab(
                tab_content=Container(
                        height=40,
                        bgcolor=colors.BLACK,
                        content=Text(machine["machineID"],
                            size=24,
                            weight=FontWeight.BOLD,
                            color=colors.WHITE
                        ),

                ),
                content=Container(
                    padding=10,
                    bgcolor=colors.BLACK,
                    content=MachineTabContent(
                        machineID=machine["machineID"],
                        parameters=self.machinesDetail.parameters(machineID=machine["machineID"]),
                        parameterValues=machine["parameterValues"],
                        comments=machine["comments"],
                        movement=machine["movement"],
                        lastResults=self.results.byMachine(machineID=machine["machineID"]),
                        saveResults=self.saveResults,
                        lastTab=(i == len(self.machines) - 1)
                    ),
                )
            ))
            i += 1

        return Container(
            height=900,
            padding=0,
            content=Tabs(
                selected_index=0,
                tabs=self.machineTabs,
            ),
        )


#-------------------------- TEST -------------------------#
if __name__ == "__main__":
    plan = Plan()
    my_plan = plan.lookUp(customerID=19711)
    _machines = plan.machines(customerID=19711)
    # machines = my_plan["machines"]
    # for m in _machines:
    #     print(m["machineID"])

    # paramValues = p.machineParameterValues(customerID=19711, machineID="D 5")
    # print(paramValues)
