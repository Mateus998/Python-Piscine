import importlib
import sys
from types import ModuleType

save_file = 'matrix_analysis.png'

def install_dependencies(missing_lib: bool):
    if missing_lib:
        print('Installing with pip')
        print('pip install -r requirements.txt')
        print('python3 loading.py\n')
        print('Installing with Poetry')
        print('poetry install')
        print('poetry run python loading.py\n')
        sys.exit(0)

def check_dependencies() -> dict[str, ModuleType]:
    loaded_modules: dict[str, ModuleType] = {}
    print('Checking dependencies:')
    libs = ['pandas', 'numpy', 'matplotlib', 'requests']
    missing_lib = False
    for name in libs:
        try:
            module = importlib.import_module(name)
            loaded_modules[name] = module
            version = getattr(module, '__version__', 'unknown')
            print(f'[OK] {name} ({version})')
        except ModuleNotFoundError:
            print(f'ERROR {name} not instaled')
            missing_lib = True
    print()
    install_dependencies(missing_lib)
    return loaded_modules

def loading_program(modules: dict[str, ModuleType]):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as mpl

    col1 = np.random.randint(0, 100, size=20)
    col2 = np.random.randint(0, 100, size=20)

    df = pd.DataFrame({
        "value1": col1,
        "value2": col2
    })

    print(df.describe())

    figure, axis = mpl.subplots()
    axis.scatter(df['value1'], df['value2'])
    axis.set_title('Matrix Values')
    axis.set_xlabel('value 1')
    axis.set_ylabel('value 2')

    figure.savefig(save_file)
    mpl.close(figure)

def main():
    print('LOADING STATUS: Loading programs...\n')
    modules: dict[str, ModuleType] = check_dependencies()
    loading_program(modules)
    print('\nAnalysis complete!')
    print(f'Results saved to: {save_file}')

if __name__ == '__main__':
    main()