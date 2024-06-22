import os

def print_environment_variables():
    for key, value in os.environ.items():
        print(f"{key}: {value}")

def print_python_environment_variables():
    python_env_vars = [
        'PYTHONPATH',
        'PYTHONHOME',
        'PYTHONSTARTUP',
        'PYTHONCASEOK',
        'PYTHONIOENCODING',
        'PYTHONFAULTHANDLER',
        'PYTHONHASHSEED',
        'PYTHONMALLOC',
        'PYTHONPYCACHEPREFIX',
        'PYTHONASYNCIODEBUG',
        'PYTHONDEBUG',
        'PYTHONINSPECT',
        'PYTHONOPTIMIZE',
        'PYTHONWARNINGS',
        'PYTHONNOUSERSITE',
        'PYTHONUNBUFFERED',
        'PYTHONVERBOSE'
    ]

    for var in python_env_vars:
        value = os.getenv(var)
        if value is not None:
            print(f"{var}: {value}")

# Chiamata alla funzione per stampare tutte le variabili d'ambiente
print_environment_variables()

# Chiamata alla funzione per stampare le variabili d'ambiente specifiche di Python
print_python_environment_variables()
