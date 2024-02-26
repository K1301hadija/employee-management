import unittest
from employee import Employee, EmployeeManagementSystem

class TestEmployeeManagementSystem(unittest.TestCase):
    def setUp(self):
        self.emp_sys = EmployeeManagementSystem()
        self.emp_sys.create_employee("John Doe", 30, 1001, "IT")

    def test_create_employee(self):
        self.emp_sys.create_employee("Jane Smith", 25, 1002, "HR")
        self.assertEqual(len(self.emp_sys.employees), 2)

    def test_retrieve_employee_by_id(self):
        emp = self.emp_sys.retrieve_employee_by_id(1001)
        self.assertEqual(emp.name, "John Doe")

    def test_delete_employee(self):
        self.emp_sys.delete_employee(1001)
        self.assertEqual(len(self.emp_sys.employees), 0)

if __name__ == '__main__':
    unittest.main()
