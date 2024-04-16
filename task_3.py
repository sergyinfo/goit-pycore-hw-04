import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)  # Автоматичне скидання стилів після кожного виведення

def print_directory_structure(path, indent=0):
    """
    Recursively prints the directory structure starting from the provided path.

    Args:
    path (Path): The path to the directory.
    indent (int): The number of spaces to indent the output.
    
    """
    try:
        if path.is_dir():
            print(Fore.BLUE + '  ' * indent + f'{path.name}/')
            directories = []
            files = []
            for item in sorted(path.iterdir()):
                if item.is_dir():
                    directories.append(item)
                else:
                    files.append(item)
            for directory in directories:
                print_directory_structure(directory, indent + 1)
            for file in files:
                print(Fore.GREEN + '  ' * indent + file.name)
    except PermissionError:
        print(Fore.RED + '  ' * indent + f'Access not allowed: {path.name}/')
    except Exception as e:
        print(Fore.RED + '  ' * indent + f'Error while accessing {path.name}/: {e}')



def main():
    """
    The main function that is executed when the script is run.
    """
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python directory_structure.py patg/to/directory")
        return

    directory_path = Path(sys.argv[1])
    if not directory_path.exists() or not directory_path.is_dir():
        print(Fore.RED + f"Error: A path '{directory_path}' " +
               "doesn't not exist or is not a directory.")
        return

    print_directory_structure(directory_path)

if __name__ == '__main__':
    main()
