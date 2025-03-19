from employee import Employee

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
