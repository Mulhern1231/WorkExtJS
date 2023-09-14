
# WorkExtJS
Тестовое задание по ExtJS

# Информация по заданию: 
### Задание 1.
Разработать web-приложение с использованием связки Django+ExtJS проверки имени пользователя. При построение странички использовать внутренние компоненты фреймворка ExtJS. 
В системе авторизации есть ограничение: логин должен начинаться с латинской буквы, состоять из латинских букв, цифр, точки и минуса, но заканчиваться только латинской буквой или цифрой; минимальная длина логина — один символ, максимальная — 20. Написать функцию, проверяющую соответствие входной строки этому правилу (использовать регулярные выражения). Придумать несколько способов. Сравнить их (просто описать какой подход лучше). 
Вход: строка с именем пользователя
Выход: true - логин прошел проверку, false - не прошел.
С точки зрения представления результатов.
Это должно быть веб-приложение на Django в качестве сервер-сайда и ExtJS страница в качестве клиент-сайда.

На странице допускается минимальное количество элементов:
1) поле ввода логина
2) кнопка "Проверить"

### Задание 2.
Разработать web-приложение с использованием связки Django+ExtJS. При построение странички использовать внутренние компоненты фреймворка ExtJS.
Необходимо разработать клиент-серверное приложение. Интерфейс представляет собой таблицу, наполненную любыми тестовыми данными (5 столбцов, 10000 строк), хранящимися на сервере в БД (SqlLite). 
Общение между сервером и клиентом должно быть реализовано на основе AJAX – запросов.
В таблице должна быть возможность добавлять новые строки, удалять и редактировать существующие.  
Все изменения должны сохраняться в базе данных и доступны при следующем подключении.


# Сравнение функций:
Функция №1

    def is_valid_username_v1(username: str) -> bool:
	    pattern = r"^[a-zA-Z][a-zA-Z0-9.-]{0,18}[a-zA-Z0-9]$"
	    return  bool(re.match(pattern, username))

Функция №2
   
    def is_valid_username_v2(username: str) -> bool:
	    if not 1 <= len(username) <= 20:  
		    return  False
	    if not re.match(r"^[a-zA-Z]", username):
		    return  False
	    if not re.match(r"[a-zA-Z0-9]$", username):
		    return  False
	    if re.search(r"[^a-zA-Z0-9.-]", username):
		    return  False
	    return True

Эффективность: Первый способ, использующий одно регулярное выражение, может быть более эффективным, так как он выполняет всего одно сопоставление с регулярным выражением.

Читаемость: Второй способ может быть более читаемым, особенно если у вас много правил. Он также позволяет легко добавлять или удалять правила.

Обратная связь: Второй способ может быть полезным, если вы хотите предоставить пользователю конкретную обратную связь о том, какое правило нарушено.

# Директория:
Задание №1 - /
Задание №2 - /table

### Перед использование установить нужные библиотеки
Установка необходимых библиотек:
```sh
pip install -r requirements.txt
```
