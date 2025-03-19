from permanent_employee import PermanentEmployee
from contract_employee import ContractEmployee
from intern import Intern

if __name__ == "__main__":
    emp1 = PermanentEmployee("Harsh", "101", "IT", 60000, 5000)
    emp2 = ContractEmployee("Ram", "102", "HR", 50, 160)
    emp3 = Intern("Shiv", "103", "Finance", 1500)

    for emp in [emp1, emp2, emp3]:
        emp.display_details()
