import sys
sys.path.append("C:\\Users\\Robert\\Documents\\KieserApp-flet\\src")
import persistence

class Customer:
    def __init__(self, customer_id):
        db = persistence.DBConnection(initialize=False)
        customers = db.connection.execute(f"""SELECT name FROM {persistence.CUSTOMER_TABLE}
                                            WHERE customer_id = {customer_id}""")

        result = customers.fetchone()
        self.full_name = result[0] if result else None

#-------------------------- TEST -------------------------#
if __name__ == "__main__":
    c = Customer(19711)
    print(c.full_name)
