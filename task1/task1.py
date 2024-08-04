from pathlib import Path

def get_salary_data(path):
 
    salaries = []
    if not path.exists():
        raise FileNotFoundError(f"Файл {path} не знайдено")
    if not path.suffix == ".txt":
        raise TypeError(f"Файл {path} не є текстовим файлом (.txt)")
    
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            name, salary_str = line.strip().split(",")
            try:
                salary = int(salary_str)
            except ValueError:
                raise ValueError(f"Невірний формат зарплати у рядку: {line}")
            salaries.append(salary)
    return salaries

def total_salary(path):
    total = 0
    average = 0
    
    try:
        salaries = get_salary_data(path)
        total = sum(salaries)
        average = total / len(salaries) if salaries else 0
    except FileNotFoundError as error:
        print(error)
    except TypeError as error:
        print(error)
    except ValueError as error:
        print(error)
        
    return total, average

if __name__ == "__main__":
    file_path = Path(__file__).parent / "file1.txt"
    total, average = total_salary(file_path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
