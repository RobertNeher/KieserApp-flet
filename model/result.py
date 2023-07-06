import os
from datetime import datetime
import src.persistence

class Result:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.timeStamp = datetime.today().strftime("%Y-%m-%d")

        self.db = src.persistence.DBConnection(initialize=False)


    def all(self):
        result_rows = self.db.connection.execute(f"""SELECT *
                    FROM {src.persistence.RESULT_TABLE}
                    WHERE customer_id = {self.customer_id}
                    """)

        result = [dict((result_rows.description[i][0], value)
               for i, value in enumerate(row)) for row in result_rows.fetchall()]

        return (result if len(result) > 0 else None)

    def trainingdates(self, latest: bool):
        result_rows = self.db.connection.execute(f"""SELECT DISTINCT training_date
                    FROM {src.persistence.RESULT_TABLE}
                    WHERE customer_id = {self.customer_id}
                    ORDER BY training_date DESC
                    """)

        result = [dict((result_rows.description[i][0], value[0:10])
               for i, value in enumerate(row)) for row in result_rows.fetchall()]

        if len(result) > 0:
            return (result[0] if latest else result)
        else:
            return None

    def byDate(self, trainingDate):
        result_rows = self.db.connection.execute(f"""SELECT
                    machine_id,
                    duration,
                    weight_done,
                    weight_planned
                    FROM {src.persistence.RESULT_TABLE}
                    WHERE customer_id = {self.customer_id}
                    AND training_date LIKE "{trainingDate[0:10]}%"
                    ORDER BY machine_id
                    """)

        result = [dict((result_rows.description[i][0], value)
               for i, value in enumerate(row)) for row in result_rows.fetchall()]

        if len(result) > 0:
            return result
        else:
            return None

    def latest(self, machine_id):
        latest_training = self.trainingdates(latest=True)["training_date"]

        if machine_id is None:
            result_rows = self.db.connection.execute(f"""SELECT *
                        FROM {src.persistence.RESULT_TABLE}
                        WHERE customer_id = {self.customer_id} AND training_date = '{latest_training}'
                        ORDER BY machine_id
                        """)
        else:
            result_rows = self.db.connection.execute(f"""SELECT *
                        FROM {src.persistence.RESULT_TABLE}
                        WHERE customer_id = {self.customer_id}
                        AND training_date LIKE '{latest_training}%'
                        AND machine_id = '{machine_id}'
                        """)

        result = [dict((result_rows.description[i][0], value)
               for i, value in enumerate(row)) for row in result_rows.fetchall()]

        if len(result) > 0:
            return result if machine_id is None else result[0]
        else:
            return None

    def deleteResults(self, ymdDateString):
        print(ymdDateString)
        # self.db.connection.execute(f"""
        #         DELETE FROM {src.persistence.RESULT_TABLE}
        #          {f"WHERE training_date LIKE '{ymdDateString}%'" if ymdDateString != "Alle" else ""}
        # """)
        # self.db.connection.commit()


    def saveResults(self, machineID, duration, weightDone, weightPlanned):
        self.db.connection.execute(f"""
                INSERT OR REPLACE INTO {src.persistence.RESULT_TABLE}
                (
                    customer_id,
                    training_date,
                    machine_id,
                    duration,
                    weight_done,
                    weight_planned
                )
                VALUES(
                    {self.customer_id},
                    '{self.timeStamp}',
                    '{machineID}',
                    {duration},
                    {weightDone},
                    {weightPlanned}
                )
        """)
        self.db.connection.commit()


#-------------------------- TEST -------------------------#
if __name__ == "__main__":
    r = Result(customer_id=19711)
    print(r.latest(machine_id="F1.1"))

