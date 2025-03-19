from employee import Employee

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
