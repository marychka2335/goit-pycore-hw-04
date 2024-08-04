import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True) 
def display_directory_structure(directory_path, indent=0):
   

    path = Path(directory_path)

    if not path.exists():
        print(Fore.RED + f"Помилка: Шлях '{directory_path}' не існує.")
        return
    if not path.is_dir():
        print(Fore.RED + f"Помилка: '{directory_path}' не є директорією.")
        return

    print(" " * indent + Fore.BLUE + Style.BRIGHT + f"📁 {path.name}/")

    for item in path.iterdir():
        if item.is_dir():
            display_directory_structure(str(item), indent + 2) # Передаємо шлях як рядок
        elif item.is_file():
            print(" " * (indent + 2) + Fore.GREEN + f"📄 {item.name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Помилка: Потрібно вказати шлях до директорії.")
        print(f"Використання: python {sys.argv[0]} /шлях/до/директорії")
        sys.exit(1)

    directory_path = sys.argv[1]
    display_directory_structure(directory_path)
