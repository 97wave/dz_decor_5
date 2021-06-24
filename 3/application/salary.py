from application.logger import logger
from datetime import datetime

@logger('log.txt')
def calculate_salary():
    print('salary', '\n', 'Текущая дата и время: ', datetime.today())
