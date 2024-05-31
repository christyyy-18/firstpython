class Employee:
  def __init__(self, emp_id, name, hours_worked, hourly_rate):
      self.emp_id = emp_id
      self.name = name
      self.hours_worked = hours_worked
      self.hourly_rate = hourly_rate

  def calculate_salary(self):
      if self.hours_worked <= 40:
          return self.hours_worked * self.hourly_rate
      else:
          overtime_hours = self.hours_worked - 40
          return (40 * self.hourly_rate) + (overtime_hours * 1.5 * self.hourly_rate)

  def generate_pay_stub(self):
      salary = self.calculate_salary()
      pay_stub = f"Employee ID: {self.emp_id}\nName: {self.name}\nHours Worked: {self.hours_worked}\nHourly Rate: ${self.hourly_rate}\nSalary: ${salary}"
      return pay_stub

# Sample employee data
emp1 = Employee(1, "Alice", 45, 20)
emp2 = Employee(2, "Bob", 35, 25)

# Generate pay stubs
print(emp1.generate_pay_stub())
print(emp2.generate_pay_stub())