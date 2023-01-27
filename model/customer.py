
import json
import os
from pathlib import Path

CUSTOMER_DATASET = "customers.json"
DATASET_FOLDER = "assets/datasets"

class Customer:
    def __init__(self):
        self.customersDataset = open(Path(os.curdir, DATASET_FOLDER, CUSTOMER_DATASET), "rt", encoding="UTF-8")
        self.customers = json.load(self.customersDataset)

    def lookUp(self, customerID):
        for customer in self.customers["Customers"]:
            if (customer["customerID"] == int(customerID)):
                return customer

        return None
#-------------------------- TEST -------------------------#
if __name__ == "__main__":
    c = Customer()
