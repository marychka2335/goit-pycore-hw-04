from pathlib import Path

def get_cats_info(path):
   
    cats_info = []

    if not path.exists():
        print(f"Файл {path} не знайдено")
    if not path.suffix == ".txt":
        print(f"Файл {path} не є текстовим файлом (.txt)")

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                parts = line.strip().split(',')

                if len(parts) == 3:
                    cat_id, name, age_str = parts
                    try:
                        age = int(age_str)
                    except ValueError:
                        raise ValueError(f"Невірний формат віку кота у рядку: {line.strip()}")
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_info.append(cat_info)
                else:
                    print(f"Некоректний формат рядка: {line.strip()}")

    return cats_info

if __name__ == "__main__":
    file_path = Path(__file__).parent / "file2.txt"
    cats_info = get_cats_info(file_path)
    print(cats_info)


