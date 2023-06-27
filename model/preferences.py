import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import persistence

class Preferences:
    def __init__(self):
        self.db = persistence.DBConnection(initialize=False)
        pref_row = self.db.connection.execute(f"""SELECT * FROM {persistence.PREFERENCE_TABLE}""")

        result = pref_row.fetchone()

        self.customer_id = result[0]
        self.duration = int(result[1])
        self.auto_forward = result[2] == 1

    def saveSettings(self):
        self.db.connection.execute(f"""DROP TABLE IF EXISTS {persistence.PREFERENCE_TABLE}""")
        self.db.connection.execute(f"""CREATE TABLE {persistence.PREFERENCE_TABLE}
                                (customer_id REFERENCES {persistence.CUSTOMER_TABLE}(customer_id),
                                duration,
                                auto_forward);
                                """)
        self.db.connection.commit()

        self.db.connection.execute(f"""INSERT INTO {persistence.PREFERENCE_TABLE} (
                                    customer_id,
                                    duration,
                                    auto_forward
                                )
                                VALUES (
                                    {self.customer_id},
                                    {self.duration},
                                    {self.auto_forward}
                                )"""
        )
        self.db.connection.commit()

#-------------------------- TEST -------------------------#
if __name__ == "__main__":
    c = Preferences()
    print(c.auto_forward)
