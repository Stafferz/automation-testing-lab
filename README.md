# Лабораторная работа 5

Пять UI-тестов для учебного магазина SauceDemo. Проверяются форма входа, успешный вход, каталог, корзина и ошибка при неверном пароле.

В Python 3.12 установите зависимости и запустите тесты:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m playwright install chromium
.\.venv\Scripts\python.exe -m pytest -v
```

Для запуска нужен доступ к www.saucedemo.com. Workflow находится в `.github/workflows/tests.yml` и запускается при push, pull request или вручную из вкладки Actions. Для эксперимента с падением измените ожидаемый адрес в `test_successful_login` на `/incorrect.html`, затем восстановите `/inventory.html`.
