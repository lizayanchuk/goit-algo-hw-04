# Завдання 1
def total_salary(path):
    try:
        with open(path, encoding="utf-8") as file:
            salaries = []
            for line in file:
                if line:
                    salaries.append(int(line.strip().split(",")[1]))

        return (sum(salaries), int(sum(salaries) / len(salaries))) if salaries else (0, 0)
    except FileNotFoundError:
        return (0, 0)


print(total_salary("text.txt"))
