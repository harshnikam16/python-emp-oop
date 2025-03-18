# Main file
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id, department):
        self._name = name  
        self._employee_id = employee_id
        self._department = department

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print("--- Employee Details ---")
        print(f"Employee ID: {self._employee_id}")
        print(f"Name: {self._name}")
        print(f"Department: {self._department}")

class PermanentEmployee(Employee):
    def __init__(self, name, employee_id, department, salary, bonus):
        super().__init__(name, employee_id, department)
        self._salary = salary
        self._bonus = bonus

    def calculate_salary(self):
        return self._salary + self._bonus

    def display_details(self):
        super().display_details()
        print(f"Basic Salary: ${self._salary:.2f}")
        print(f"Bonus: ${self._bonus:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

class ContractEmployee(Employee):
    def __init__(self, name, employee_id, department, hourly_rate, hours_worked):
        super().__init__(name, employee_id, department)
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked

    def calculate_salary(self):
        return self._hourly_rate * self._hours_worked

    def display_details(self):
        super().display_details()
        print(f"Hourly Rate: ${self._hourly_rate:.2f}")
        print(f"Hours Worked: {self._hours_worked}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

class Intern(Employee):
    def __init__(self, name, employee_id, department, stipend):
        super().__init__(name, employee_id, department)
        self._stipend = stipend

    def calculate_salary(self):
        return self._stipend

    def display_details(self):
        super().display_details()
        print(f"Stipend: ${self._stipend:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

if __name__ == "__main__":
    emp1 = PermanentEmployee("Harsh", "101", "IT", 60000, 5000)
    emp2 = ContractEmployee("Ram", "102", "HR", 50, 160)
    emp3 = Intern("Shiv", "103", "Finance", 1500)

    for emp in [emp1, emp2, emp3]:
        emp.display_details()
