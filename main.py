from pyrogram import Client
import time, datetime
import os

from dotenv import load_dotenv


load_dotenv()


api_id = os.getenv('APIID')
api_hash = os.getenv('TOKEN')
app = Client('my_account', api_id, api_hash)
cash = os.getenv('CASH')


def plural_days():
    # Делаем правильное окончание слова
    day = ['день', 'дня', 'дней']
    n = days()
    if n % 10 == 1 and n % 100 != 11:
        p = 0
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        p = 1
    else:
        p = 2
    return day[p]

def days():
    # Высчитываем день
    date = datetime.datetime(day=24, month=9, year=2022)
    time_has_passed = datetime.datetime.now() - date
    return time_has_passed.days

def Send_Mess():
    # Отправляем сообщение
    app.send_message('poteryalas11', f'Привет, я бот! Мой создатель всего-лишь хотел напомнить что ты ему должен {cash}. Уже прошло {days()} {plural_days()}. Ахуеть можно')
 
def main():
    app.start()
    while True:
        try:
            Send_Mess()
        finally:
            time.sleep(43000)

if __name__ == '__main__':
    main()
