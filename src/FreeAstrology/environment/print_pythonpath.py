import os

def print_pythonpath():
    pythonpath = os.getenv('PYTHONPATH')
    if pythonpath:
        print(f'PYTHONPATH: {pythonpath}')
    else:
        print('PYTHONPATH is not set')

# Call the function to print the PYTHONPATH
print_pythonpath()
