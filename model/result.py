
import json
import os
from pathlib import Path
from datetime import datetime
from model.plan import Plan

RESULTS_DATASET = "results.json"
DATASET_FOLDER = "assets/datasets"

class Result:
    def __init__(self, customerID:int):
        self.customerID = customerID
        self.timeStamp = datetime.today().strftime("%Y-%m-%d")
        self.resultsDataset = open(Path(os.curdir, DATASET_FOLDER, RESULTS_DATASET), "r+", encoding="UTF-8")

        try:
            self.results = json.load(self.resultsDataset)
        except:
            self.resultsDataset = open(Path(os.curdir, DATASET_FOLDER, RESULTS_DATASET), "w", encoding="UTF-8")
            self.results = {
                "Results": [
                    {
                        "customerID": self.customerID,
                        "trainings": []
                    }
                ]
            }
            self.resultsDataset.flush()

        for customerResults in self.results["Results"]:
            if customerResults["customerID"] == self.customerID:
                self.customerResults = customerResults

        self.plan = Plan().lookUp(customerID=self.customerID)

    def all(self):
        for result in self.results["Results"]:
            if (result["customerID"] == self.customerID):
                return result["trainings"]

        return None

    def byDate(self, trainingDate:datetime):
        trainingResults = self.all()

        for trainingResult in trainingResults:
            filterDate = datetime.strptime(trainingResult["trainingDate"], "%Y-%m-%d")

            if filterDate == trainingDate:
                return trainingResult

        return None

    def byMachine(self, machineID:str, ** kwargs): #trainingDate:datetime):
        filterDate = kwargs.get('trainingDate', None)

        if filterDate != None:
            trainingResults = self.byDate(trainingDate=filterDate)
        else:
            trainingResults = self.latest()

        if len(trainingResults) > 0:
            for trainingResult in trainingResults["results"]:
                    if trainingResult["machineID"] == machineID:
                        return trainingResult
        # else:
        #     return {
        #         "trainingDate": self.timeStamp,
        #         "results": []
        #     }

        return []

    def latest(self):
        trainingData = self.all()

        if len(trainingData) > 0:
            trainingData.reverse()
            return trainingData[0]
        else:
            return trainingData

    def saveResults(self, resultSet):
        if len(self.plan["machines"]) != len(resultSet["results"]):
            return False

        for customer in self.results["Results"]:
            if customer["customerID"] == 19711:
                customer["trainings"].append(resultSet)
                self.resultsDataset.seek(0)
                self.resultsDataset.truncate(0)
                json.dump(self.results, self.resultsDataset)
                self.resultsDataset.flush()
                return True

#-------------------------- TEST -------------------------#
if __name__ == "__main__":
    resultSet = {
                    "trainingDate": "2023-01-24",
                    "results": [
                        {
                            "machineID": "B 1",
                            "duration": "120",
                            "doneToday": "108",
                            "goalNext": "110"
                        },
                        {
                            "machineID": "B 7",
                            "duration": "120",
                            "doneToday": "108",
                            "goalNext": "110"
                        },
                        {
                            "machineID": "F 2.1",
                            "duration": "120",
                            "doneToday": "86",
                            "goalNext": "88"
                        },
                        {
                            "machineID": "F 3.1",
                            "duration": "120",
                            "doneToday": "86",
                            "goalNext": "88"
                        },
                        {
                            "machineID": "C 1",
                            "duration": "120",
                            "doneToday": "86",
                            "goalNext": "88"
                        },
                        {
                            "machineID": "C 3",
                            "duration": "120",
                            "doneToday": "178",
                            "goalNext": "180"
                        },
                        {
                            "machineID": "C 7",
                            "duration": "120",
                            "doneToday": "92",
                            "goalNext": "94"
                        },
                        {
                            "machineID": "D 5",
                            "duration": "120",
                            "doneToday": "66",
                            "goalNext": "68"
                        },
                        {
                            "machineID": "D 6",
                            "duration": "120",
                            "doneToday": "90",
                            "goalNext": "92"
                        },
                        {
                            "machineID": "H 1",
                            "duration": "120",
                            "doneToday": "60",
                            "goalNext": "62"
                        }
                    ]
                }

    filterDate = datetime.strptime("2022-11-22", "%Y-%m-%d")
    r = Result(customerID=19711)
    # print(r.byDate(training=filterDate))

    print(r.byMachine(machineID='C 1'))