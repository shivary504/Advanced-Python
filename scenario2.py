class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Category:", self.category())
        print()


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_all(self):
        for emp in self.employees:
            emp.display()

company = Company()

n = int(input("Enter number of employees: "))

for i in range(n):
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    salary = int(input("Salary: "))
    company.add_employee(Employee(emp_id, name, salary))

print("\nEmployee Details")
company.display_all()
