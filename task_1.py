def total_salary(path: str) -> tuple:
    """
    Calculates the total and average salaries from a provided txt file.
    
    Each line of the file should contain an employee's name and salary, separated by a comma.

    Args:
    path (str): The path to the CSV file.

    Returns:
    tuple: Total salary (float) and average salary (float).

    Raises:
    FileNotFoundError: If the file is not found.
    UnicodeDecodeError: If the file encoding is not UTF-8.
    """
    encoding = 'utf-8'
    total = 0
    count = 0
    try:
        with open(file = path, mode = 'r', encoding = encoding) as file_handle:
            for line in file_handle:
                if line.strip():  # skips any empty lines
                    name, salary = line.strip().split(',')
                    total += float(salary)
                    count += 1
            if count == 0:
                return 0.0, 0.0
            average = total / count
            return total, average
    except UnicodeDecodeError:
        raise UnicodeDecodeError(f"File encoding is not '{encoding}' and it couldn't be decoded.")
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{path}' not found")

try:
    total, average = total_salary("salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except Exception as e:
    print(e)
