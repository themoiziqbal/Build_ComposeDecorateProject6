# Aggregation
# Just like composition, it allows one object, composite, to have another object as its
# member, component.
# Unlike composition, the component exists independently of the composite. In
# composition, the creation of the composite triggers the creation of the
# component.


class Employee:
    def __init__(self,name : str):
        self.name = name
        pass

class Department:
    def __init__(self):
        self.employees : list = []
        pass

    def add_employee(self,employee : Employee):
        self.employees.append(employee)

    def display_employees(self):
        print("Employees:")
        index = 1
        for employee in self.employees:
            print(f"\t{index}. {employee.name}")
            index += 1

def main():
    # Create a department
    department = Department()

    # Create employees
    employee_1 = Employee("Tish")
    employee_2 = Employee("Hish")
    employee_3 = Employee("Bish")

    # Add them to department
    department.add_employee(employee_1)
    department.add_employee(employee_2)
    department.add_employee(employee_3)

    # Display the employees!
    department.display_employees()

if __name__ == '__main__':
    main()