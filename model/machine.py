import json
import os
from pathlib import Path

CUSTOMER_DATASET = "machines.json"
DATASET_FOLDER = "assets/datasets"

class Machine:
    def __init__(self):
        self.machinesDataset = open(Path(os.curdir, DATASET_FOLDER, CUSTOMER_DATASET), "rt", encoding="UTF-8")
        self.machines = json.load(self.machinesDataset)

    def lookUp(self, machineID):
        for machine in self.all():
            if (machine["name"] == machineID):
                return machine

        return None

    def all(self):
        return self.machines["Machines"]

    def parameters(self, machineID):
        machine = self.lookUp(machineID=machineID)

        if machine != None:
            return  machine["parameters"]


#-------------------------- TEST -------------------------#
if __name__ == "__main__":
    m = Machine()
    print(m.all())
    print(m.lookUp("D 5"))
    print(m.parameters("D 5"))
