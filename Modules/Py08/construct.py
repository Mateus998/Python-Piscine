import sys
import os
import site

def is_virtual() -> bool:
    if sys.prefix != sys.base_prefix:
        return True
    return False

def matrix_status() -> str:
    if is_virtual():
        return 'Welcome to the construct'
    return 'You\'re still plugged in'

def python_info() -> None:
    print(f'Current Python: {sys.executable}')
    if is_virtual():
        print(f'Virtual Environment: {os.path.basename(sys.prefix)}')
        print(f'Environment Path: {sys.prefix}\n')
        print('SUCCESS: You\'re in an isolated environment!')
        print('Safe to install packages without affectingthe global system.\n')
    else:
        print(f'Virtual Environment: None detected\n')
        print('WARNING: You\'re in the global environment!')
        print('The machines can see everything you install.\n')

def instructions() -> None:
    if not is_virtual():
        print('To enter the construct, run:\n\
python -m venv matrix_env\n\
source matrix_env/bin/activate # On Unix\n\
matrix_env\\Scripts\\activate # On Windows\n\n\
Then run this program again.\n')

    print(f'Package installation path:\n{site.getsitepackages()[0]}')

def main():
    print(f'MATRIX STATUS: {matrix_status()}\n')
    python_info()
    instructions()

if __name__ == "__main__":
    main()