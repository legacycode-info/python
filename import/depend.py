import argparse
import ast
import os


def get_function_calls(filepath):
    with open(filepath, 'r') as file:
        source = file.read()
    tree = ast.parse(source)
    calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            calls.append(node.func.id)
    return calls


def create_import_statement(function_name, dependency_name, directory_path):
    return f'from {directory_path}.{dependency_name} import {function_name}\n'


def add_imports_to_file(filepath, imports):
    with open(filepath, 'r') as file:
        content = file.readlines()
    with open(filepath, 'w') as file:
        file.writelines(imports)
        file.writelines(content)


def main(directory_path):
    # Get a list of all the refactored function files
    function_files = [f for f in os.listdir(directory_path) if
                      os.path.isfile(os.path.join(directory_path, f)) and f.endswith('.py')]

    # Declare a dict to hold function calls for each file
    file_function_calls = {}

    # Collect function calls within each file
    for function_file in function_files:
        filepath = os.path.join(directory_path, function_file)
        file_function_calls[function_file] = get_function_calls(filepath)

    # Process each file again to add imports based on the collected calls
    for function_file, calls in file_function_calls.items():
        filepath = os.path.join(directory_path, function_file)

        # Initialize the list of import statements to be added
        import_statements = []

        # Check each call to see if it matches a refactored function file
        for call in calls:
            if f'{call}.py' in function_files and f'{call}.py' != function_file:
                # Add an import statement if a match is found, avoiding self-imports
                import_statements.append(create_import_statement(call, call, directory_path))

        # Filter out any duplicate import statements
        import_statements = list(dict.fromkeys(import_statements))

        # Add the import statements to the top of the file
        if import_statements:
            add_imports_to_file(filepath, import_statements)

    print('Dependencies resolved and imports added to files.')


# Command line interface
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resolve dependencies and add imports to refactored function files.')
    parser.add_argument('directory', help='The directory containing the refactored function files.')

    args = parser.parse_args()
    main(directory_path=args.directory)

#python3 splitup.py functions