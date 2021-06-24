from application.logger import logger
from datetime import datetime

@logger('log.txt')
def get_employees():
    print('employees list', '\n', 'Текущая дата и время:', datetime.today())