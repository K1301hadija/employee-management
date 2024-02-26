import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_employee_initialization(self):
        emp = Employee("John Doe", 30, 1001, "IT")
        self.assertEqual(emp.name, "John Doe")
        self.assertEqual(emp.age, 30)
        self.assertEqual(emp.employee_id, 1001)
        self.assertEqual(emp.department, "IT")

if __name__ == '__main__':
    unittest.main()
