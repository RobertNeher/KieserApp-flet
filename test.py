import json
import os
from datetime import datetime
from pathlib import Path

RESULTS_DATASET = "results.json"
DATASET_FOLDER = "assets/datasets"

def main():

    condition = False
    bla = "True" if condition else "False"
    print(bla)
    exit()

    results={
        "Results": [
            {
                "customerID": 19711,
                "trainings": []
            }
        ]
    }
    training = {
        "trainingDate": "2023-01-28",
        "results": [],
    }
    trainingResults = [
        {
            "machineID": 'B 1',
            "doneToday": 110,
            "goalNext": 110,
            "duration": 120,
        },
        {
            "machineID": 'B 5',
            "doneToday": 110,
            "goalNext": 110,
            "duration": 121,
        }
    ]

    customerID = 19711
    timeStamp = datetime.today().strftime("%Y-%m-%d")
    resultsDataset = open(Path(os.curdir, DATASET_FOLDER, RESULTS_DATASET), "r+", encoding="UTF-8")

    try:
        results = json.load(resultsDataset)
    except:
        results = {
            "Results": [
                {
                    "customerID": customerID,
                    "trainings": []
                },
            ]
        }
    for customer in results["Results"]:
        if customer["customerID"] == customerID:
            customer["trainings"].append(training)
            json.dump(results, resultsDataset)
            resultsDataset.flush()
            resultsDataset.close()




    print("Done")



#------------------------ MAIN ------------------------#
if __name__ == "__main__":
    main()