from django.shortcuts import render
from django.http import JsonResponse

import re

def is_valid_username_v1(username: str) -> bool:
    pattern = r"^[a-zA-Z][a-zA-Z0-9.-]{0,18}[a-zA-Z0-9]$"
    return bool(re.match(pattern, username))

def is_valid_username_v2(username: str) -> bool:
    # Проверка на минимальную и максимальную длину
    if not 1 <= len(username) <= 20:
        return False
    # Проверка на начало с латинской буквы
    if not re.match(r"^[a-zA-Z]", username):
        return False
    # Проверка на закрытие латинской буквой или цифрой
    if not re.match(r"[a-zA-Z0-9]$", username):
        return False
    # Проверка на допустимые символы
    if re.search(r"[^a-zA-Z0-9.-]", username):
        return False
    return True


"""
Эффективность: Первый способ, использующий одно регулярное выражение, может быть более эффективным, так как он выполняет всего одно сопоставление с регулярным выражением.
Читаемость: Второй способ может быть более читаемым, особенно если у вас много правил. Он также позволяет легко добавлять или удалять правила.
Обратная связь: Второй способ может быть полезным, если вы хотите предоставить пользователю конкретную обратную связь о том, какое правило нарушено.
"""


def check_username(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        result = is_valid_username_v1(username)  # используйте функцию, которую мы написали ранее

        if result:
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False})

    return render(request, 'user_check/index.html')
