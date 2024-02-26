import unittest
from employee import Employee, EmployeeManagementSystem

class TestEmployeeManagementSystemIntegration(unittest.TestCase):
    def setUp(self):
        self.emp_sys = EmployeeManagementSystem()
        self.emp_sys.create_employee("John Doe", 30, 1001, "IT")

    def test_create_retrieve_delete_employee(self):
        self.emp_sys.create_employee("Jane Smith", 25, 1002, "HR")
        emp = self.emp_sys.retrieve_employee_by_id(1002)
        self.assertEqual(emp.department, "HR")
        self.assertTrue(self.emp_sys.delete_employee(1002))

if __name__ == '__main__':
    unittest.main()
