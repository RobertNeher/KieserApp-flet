
import json
import os
from pathlib import Path

PLANS_DATASET = "plans.json"
DATASET_FOLDER = "assets/datasets"

class Plan:
    def __init__(self):
        self.plansDataset = open(Path(os.curdir, DATASET_FOLDER, PLANS_DATASET), "rt", encoding="UTF-8")
        self.plans = json.load(self.plansDataset)

    def lookUp(self, customerID):
        for plan in self.plans["Plans"]:
            if (plan["customerID"] == customerID):
                return plan

        return None

    def machines(self, customerID):
        customerMachines =  self.lookUp(customerID=customerID)
        if customerMachines != None:
            return customerMachines["machines"]

        return


    def machineParameterValues(self, customerID, machineID):
        customerMachines =  self.machines(customerID=customerID)
        if customerMachines != None:
            for machine in customerMachines:
                if (machine["machineID"] == machineID):
                    return machine["parameterValues"]

        return None

#-------------------------- TEST -------------------------#
if __name__ == "__main__":
    p = Plan()
    paramValues = p.machineParameterValues(customerID=19711, machineID="D 5")
    print(paramValues)