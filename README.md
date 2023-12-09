
# python
python, http://www.legacycode.info

# SPLITUP

Python script that will parse through a Python source file, extract each top-level function, and save them into separate files. The script will then create a `main.py` file that imports all of these functions.

Here's a simple Python script that performs the described task. Please note that this script assumes that your functions are not nested within classes or other functions and that your source file is not doing anything unusual with source code encoding or manipulation.


1. This script will not necessarily capture and handle all complex refactoring cases, especially those involving class methods, nested functions, and decorators.
2. All functions will get the same set of imports from the original file, which might not be necessary and could lead to unused import warnings.
3. The use of the `ast` since parsing the file as text may not be robust enough to handle complex cases of code structuring or syntax.
4. The `main.py` simply imports all functions, but does not replicate any imperative code that existed in the original file; additional logic might be required for a complete refactor.

## How to start

```bash
python3 splitup.py main functions
```
## Dependency

parse each function file we created to find out which functions it calls, and then add the necessary imports at the top of the function files. This updated script assumes that we're working with the output of the previous refactoring operation, with all function files located in a directory.

This code example performs the following:

1. Parses each function file to collect function calls.
2. Determines if the function calls refer to functions within our set of refactored files.
3. Adds import statements to the top of each file for the functions it depends on from within the folder.

1. This script assumes that the refactored functions do not call functions outside of the refactored set.
2. It does not handle calls made with alternative syntax (e.g., using `getattr()`), calls made through variables, method calls, or function calls within nested functions or classes.
3. The script checks for function filenames which correspond to function calls (i.e., it assumes that there is a 1-to-1 mapping between calls and files, without considering scope or context).
4. Each refactored file should contain only one top-level function for the import statements to work correctly without causing circular imports.


## How to start

```bash
python3 splitup.py main functions
```
