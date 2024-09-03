Краулер для инстаграмма

## Описание
Python приложение, которое извлекает данные пользователей по их никнейму и сохранает в базу данных

## Функционал
- Извлечение данных пользователя 
- Сохранение данных в базу данных

## Установка
** Клонирование репозитория **
```bash
https://github.com/eSTaGe-spec/instaCrawler.git
cd instaCrawler
```

** Создание вирутального окружения **
```bash
python -m venv venv
.\venv\Scripts\activate # Windows
source venv/bin/activate # Linux/Mac
```

** Установка зависимостей **
```bash
pip install -r requirements.txt
```

** Настройка переменных окружения **
```bash
USERNAME='inst_username'
PASSWORD='inst_password'
```

## Использование
1) Создайте файл usernames.txt, куда нужно вставить логины пользователей у которых хотите извлечь данные
2) Запустите основной файл
```bash
python main.py
```
