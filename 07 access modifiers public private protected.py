# Access modifiers: Public, private, and protected

class Employee:
    def __init__(self,name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn


def main():
    employee = Employee("Moiz",100000,2103)
    print(f"Name: {employee.name}")
    try:
        print(f"Salary: {employee._salary}")
    except:
        print(f"Sorry, cannot display {employee.name}'s salary")

    try:
        print(f"Social security number: {employee.__ssn}")
    except:
        print(f"Sorry, cannot display {employee.name}'s social security number")
        print(f"Wait, we can! {employee._Employee__ssn}")

if __name__ == '__main__':
    main()
