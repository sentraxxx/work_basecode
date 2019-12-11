import logging
import sys
import time
import datetime
import os

def main():
    # Logging
    if os.path.isdir('./logs'):
        pass
    else:
        os.mkdir('./logs')

    logging.basicConfig(
        filename='./logs/work_basic.log',
        format='[%(asctime)s] %(levelname)s: %(name)s : %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
        )
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.info('info logging')
    logger.debug('debug logging')  # 表示されない

    logger = logging.getLogger('')
    loghandler = logging.FileHandler(filename='./logs/work_basic2.log')
    logger.addHandler(loghandler)
    logger.warning('warning logging')

    # 表示
    print('string: Hello')  # string: Hello

    num = 100
    print(f'f string {num}')  # f string 100

    # 時刻
    datetime_datetime = datetime.datetime(year=1990, month=10, day=10, hour=14)
    # datetime.datetime= 1990-10-10 14:00:00
    print(f'datetime.datetime= {datetime_datetime}')

    datetime_datetime_fromtimestamp = datetime.datetime.fromtimestamp(time.time())
    # datetime_datetime_fromtimestamp= 2019-11-21 13:50:54.700799
    print(f'datetime_datetime_fromtimestamp= {datetime_datetime_fromtimestamp}')

    datetime_date_today = datetime.date.today()
    # datetime_date_today= 2019-11-21
    print(f'datetime_date_today= {datetime_date_today}')

    datetime_date_fromtimestamp = datetime.date.fromtimestamp(time.time())
    # datetime_date_fromtimestamp = 2019-11-21
    print(f'datetime_date_fromtimestamp = {datetime_date_fromtimestamp}')

    time_now = time.time()
    print(f'time_now= {time_now}')  # time_now= 1574310946.913544

if __name__ == "__main__":
    main()
