from employee import Employee

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
