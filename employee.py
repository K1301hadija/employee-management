class Employee:
    def __init__(self, name, age, employee_id, department):
        self.name = name
        self.age = age
        self.employee_id = employee_id
        self.department = department

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def create_employee(self, name, age, employee_id, department):
        emp = Employee(name, age, employee_id, department)
        self.employees.append(emp)

    def retrieve_employee_by_id(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        return None

    def delete_employee(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                self.employees.remove(emp)
                return True
        return False
