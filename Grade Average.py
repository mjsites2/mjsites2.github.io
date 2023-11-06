class GradesFile:
    def __init__(self, filename):
        self.__filename = filename

    def get_filename(self):
        return self.__filename

    def set_filename(self, filename):
        self.__filename = filename

    def calculateAverage(self):
        try:
            with open(self.__filename, 'r') as file:
                grades = []
                for line in file:
                    try:
                        grade = float(line.strip())
                        grades.append(grade)
                    except ValueError:
                        print(f"Skipping invalid line: {line}")

                if not grades:
                    return None 

                average = sum(grades) / len(grades)
                return average

        except FileNotFoundError:
            print(f"File '{self.__filename}' not found.")
            return None


def main():
    try:
        with open('Grades.txt', 'w') as file:
            while True:
                grade_str = input("Enter a grade (or 'q' to quit): ")
                if grade_str == 'q':
                    break
                try:
                    grade = float(grade_str)
                    file.write(f"{grade}\n")
                except ValueError:
                    print("Invalid input. Please enter a valid grade.")

        grades_file = GradesFile('Grades.txt')

     
        average = grades_file.calculateAverage()
        if average is not None:
            print(f"Average grade: {average}")
        else:
            print("No valid grades found in the file or an error occurred.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
