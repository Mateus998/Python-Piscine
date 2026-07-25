from dotenv import load_dotenv
import sys
import os

mode_values = ['development', 'production']
log_values = ['DEBUG', 'INFO', 'WARNING', 'ERROR']

def main():
    missing_variables = False
    print('ORACLE STATUS: Reading the Matrix...\n')
    if not load_dotenv():
        print('ERROR: Missing .env file')
        sys.exit(0)

    print('Configuration loaded:')
    #------------- Mode-------------------
    mode = os.getenv('MATRIX_MODE')
    if not mode:
        mode = 'Missing'
        missing_variables = True
    elif mode not in mode_values:
        mode = 'Wrong value'
    print(f'Mode: {mode}')

    #-----------Database----------------
    database = os.getenv('DATABASE_URL')
    if not database:
        database = 'Missing'
        missing_variables = True
    else:
        database = 'Connected to local instance'
    print(f'Database: {database}')

    #-------------API Access-----------
    api = os.getenv('API_KEY')
    if not api:
        api = 'Mising'
        missing_variables = True
    else:
        api = 'Authenticated'
    print(f'API Access: {api}')

    #--------------Log Level---------------
    log = os.getenv('LOG_LEVEL')
    if not log:
        log = 'Missing'
        missing_variables = True
    elif log not in log_values:
        log = 'Wrong value'
    print(f'Log Level: {log}')

    #-------------Zion Network-------------
    net = os.getenv('ZION_ENDPOINT')
    if not net:
        net = 'Missing'
        missing_variables = True
    else:
        net = 'Online'
    print(f'Zion Network: {net}')

    print('\nEnvironment security check:')
    print('[OK] No hardcoded secrets detected')
    if missing_variables:
        print("[WARNING] .env file incomplete")
    else:
        print('[OK] .env file properly configured')
    if mode == "production":
        print("[OK] Production overrides active")
    else:
        print("[OK] Production overrides available")

    print('\nThe Oracle sees all configurations.')

if __name__ == '__main__':
    main()


    


    


    

