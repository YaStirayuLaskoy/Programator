# Programator
Планировщик смен. Тестовое от BIA Technologies.

## ТЗ:
Написать бекэнд сервис для планировщика смен.<br>
Во все дни месяца должны быть сотрудники с 8:00 до 22:00<br>
Программа сама заполняет график исходя из исходных данных.<br>
Записать видео с выполнением программы. Прислать ссылку на ютуб или git

### Дано:

Число дней в месяце меняется: 28, 30, 31 день<br>
Есть 10 сотрудников: worker1, worker2, …., worker10<br>
Максимальное число часов в месяц на 1 сотрудника = 144 часа<br>
Длительность стандартной смены = 12 часов<br>
Время начала смены в 8:00 и в 10:00, завершение смены в 20:00 и 22:00 соответственно<br>
В понедельник нужен +1 сотрудник к средней нагрузке<br>
В воскресенье  -1 сотрудник к средней нагрузке

Чтобы понять, где будет использоваться:<br> [https://www.figma.com/file/Tba6UR1T3hiNtRNngitlit/BIA-Tech.-React.Тестовое?type=design&node-id=1345-21512&mode=design](https://www.figma.com/file/Tba6UR1T3hiNtRNngitlit/BIA-Tech.-React.%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5?type=design&node-id=1345-21512&mode=design)


## Описание возможностей:

API для планировщика смен.

- Есть возможность создать работников
  
  <img src="https://github.com/YaStirayuLaskoy/Programator/assets/122834885/fd100f6b-115c-4bf1-819d-4b5bb1269ea0" alt="Screenshot" width="50%" height="50%">

- Работникиков можно отмечать (Работал/Отдыхал/Уволился/.../)
- Работники могут отмечать начало и конец смены

  <img src="https://github.com/YaStirayuLaskoy/Programator/assets/122834885/705e8258-8908-41af-8997-67d61f021fd7" alt="Screenshot" width="50%" height="50%">

- Рабочая Админка

  <img src="https://github.com/YaStirayuLaskoy/Programator/assets/122834885/a7c1951c-85af-48b9-87c9-f3fe1a8b3ed1" alt="Screenshot" width="50%" height="50%">


## Как запустить:

#### Клонировать репозиторий

```
git clone git@github.com:YaStirayuLaskoy/Programator.git
```

#### Перейти во внутреннюю директорию. Cоздать и активировать виртуальное окружение:
```
cd programator
```
```
python -m venv venv
```
```
source venv/Scripts/activate
```
#### Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
```
python -m pip install --upgrade pip
```
#### Перейти в директорию с manage.py. Провести миграции:
```
cd backend/programator_backend/
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
#### Запустить проект:
```
python manage.py runserver
```

## Админка:

login: admin</br>
password: admin

## Эндпоинты:
Админка
```
http://127.0.0.1:8000/admin
```

API
```
http://127.0.0.1:8000/api
```

Работяги
```
http://127.0.0.1:8000/api/workers/
```

Смены
```
http://127.0.0.1:8000/api/shifts/
```

Дни
```
http://127.0.0.1:8000/api/days/
```

Тип активности
```
http://127.0.0.1:8000/api/events/
```


## Планы по развитию:

Интересный проект, очень похож на учебные. Обязательно доведу до ума.

ChekPoints:

- Разобраться со связями моделей. Некоторые поля напрашиваются на M2M
- Некоторые поля можно сделать автоматическими (например, вторая дата у смены, она всегда +12 часов)
- Пересобрать апишки (Можно попробовать работяг и их тип активности вложить в дату. Мб, нужна промежуточная моделька ~~Смотри foodgram~~)
- Настроить доступ (Например, чтобы работяги не могли удалять записи друг друга.)
