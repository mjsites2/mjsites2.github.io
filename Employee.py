class Employee:
    def __init__(self, first_name, last_name, employee_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__employee_id = employee_id
        self.__hours_worked = 0

    # Setters and Getters
    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked

    def get_hours_worked(self):
        return self.__hours_worked

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def calculate_weekly_salary(self):
        regular_rate = 20
        overtime_rate = 35
        if self.__hours_worked <= 40:
            return self.__hours_worked * regular_rate
        else:
            regular_pay = 40 * regular_rate
            overtime_pay = (self.__hours_worked - 40) * overtime_rate
            return regular_pay + overtime_pay

    def __str__(self):
        return f"Employee ID: {self.__employee_id}\nName: {self.__first_name} {self.__last_name}\nHours Worked: {self.__hours_worked}\nWeekly Salary: ${self.calculate_weekly_salary():.2f}"


def main():
    # Create two Employee objects
    employee1 = Employee("Matt", "Polk", "E001")
    employee2 = Employee("Jane", "Smith", "E002")

    # Set hours worked for each employee
    employee1.set_hours_worked(45)
    employee2.set_hours_worked(35)

    # Print employee information
    print("Employee 1 Information:")
    print(employee1)
    print("\nEmployee 2 Information:")
    print(employee2)


if __name__ == "__main__":
    main()
