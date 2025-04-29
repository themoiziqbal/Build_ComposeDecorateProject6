# The Super Function

class Person:
    def __init__(self,name : str):
        self.name = name

class Teacher(Person):
    def __init__(self,name : str, subject: str):
        super().__init__(name)
        self.subject = subject

def main():
    # Science teacher
    teacher = Teacher("Moiz Iqbal","English")
    print(f"Teacher: {teacher.name}\nSubject: {teacher.subject}")

if __name__ == '__main__':
    main()
