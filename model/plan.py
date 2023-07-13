import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import persistence

class Plan:
    def __init__(self, customerID):
        db = persistence.DBConnection(initialize=False)

        plan_rows = db.connection.execute(f"""SELECT valid_from, machine_id, machine_parameters, machine_movement, machine_comments
                    FROM {persistence.PLAN_TABLE} WHERE customer_id="{customerID}"
                    AND valid_from = (SELECT MAX(valid_from) FROM {persistence.PLAN_TABLE})
                    """)
        result = [dict((plan_rows.description[i][0], value)
               for i, value in enumerate(row)) for row in plan_rows.fetchall()]

        self.plan = (result if len(result) > 0 else None)

        self.machines = []
        for machine in self.plan:
            self.machines.append(machine["machine_id"])

    def machine_parameter_values(self, machine_id):
        customer_machines =  self.machines
        if customer_machines is not None:
            for machine in self.plan:
                if machine["machineID"] == machine_id:
                    return machine["parameterValues"]

        return None

#-------------------------- TEST -------------------------#
if __name__ == "__main__":
    p = Plan(customerID=19711)
    print(p.plan)
    print(p.machines)
