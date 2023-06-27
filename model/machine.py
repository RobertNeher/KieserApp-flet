import sys
sys.path.append("C:\\Users\\Robert\\Documents\\KieserApp-flet\\src")
import persistence

class Machine:
    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.db = persistence.DBConnection(initialize=False)
        
        machine_rows = self.db.connection.execute(f"""SELECT *
                    FROM {persistence.MACHINE_TABLE}
                    {f"WHERE name = '{machine_id}'" if machine_id is not None else ""}
                    """)
        result = [dict((machine_rows.description[i][0], value)
               for i, value in enumerate(row)) for row in machine_rows.fetchall()]

        if machine_id is None:
            self.machines = (result if len(result) > 0 else None)
        else:
            self.machines = result[0]

#-------------------------- TEST -------------------------#
if __name__ == "__main__":
    m = Machine("D5")
    print(m.get_machine_detail())