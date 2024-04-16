def get_cats_info(file_name):
    """
    Reads the contents of a provided txt file and returns them as a dictionary.
    
    Each line contains a cat's id, name and age separated by a comma.

    Args:
    path (str): The path to the CSV file.

    Returns:
    list: A list of dictionaries containing the cat's id, name and age.

    Raises:
    FileNotFoundError: If the file is not found.
    UnicodeDecodeError: If the file encoding is not UTF-8.
    """
    encoding = 'utf-8'
    cats_info = []
    try:
        with open(file = file_name, mode = 'r', encoding = encoding) as file_handle:
            for line in file_handle:
                if line.strip():  # skips any empty lines
                    cat_id, name, age = line.strip().split(',')
                    cats_info.append({
                        'id': cat_id,
                        'name': name,
                        'age': age
                    })
            return cats_info
    except UnicodeDecodeError:
        raise UnicodeDecodeError(f"File encoding is not '{encoding}' and it couldn't be decoded.")
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_name}' not found")

cats_info = get_cats_info("cats.txt")
print(cats_info)