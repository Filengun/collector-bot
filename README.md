# collector-bot
### Достали люди которые не возвращают деньги? Этот тг-бот поможет напоминать людям об их долге. бери и пользуйся :)

### Установка:
#### *Действия для юзеров Windows**

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Filengun/collector-bot.git
```
```
cd collector-bot
```
Cоздать и активировать виртуальное окружение:
```
python -m venv env
```
```
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
### Настройка:
- Необходимо создать файл .env и записать туда необходимые данные (TOKEN, APIID) с помощью которых бот будет определять откуда отправлять сообщения.
- В файле data.xlsx необходимо внести данные о должниках. CLIENT - Это id которому будет отправлять сообщение, CASH - сумма долга, DATE - дата выдачи средств. В данный момент эти данные необходимо записывать полностью.
- После этого вводим в консоль python main.py и вауля, через мгновение сообщения начинают отправляться.
