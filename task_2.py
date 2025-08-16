# Завдання 2
def get_cats_info(path):
    try:
        with open(path, encoding="utf-8") as file:
            cats = []
            for line in file:
                lines = line.strip().split(",")
                if len(lines) == 3:
                    cats.append({
                        "id": lines[0],
                        "name": lines[1],
                        "age": lines[2]
                    })
        return cats
    except FileNotFoundError:
        return "Файл не знайдено"

print(get_cats_info("text.txt"))
