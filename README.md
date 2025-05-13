Шаги по стазданию через uv

uv python pin 3.10.2 - для использования определенной версии в проекте

далее 

uv init инициализируем

uv add dajngo

django-admin startproject core .

uv add djangorestframework

Добавление удаленного репозитория

git remote add origin https://github.com/DmitryKireev69/drf_ecommerce.git

Проверка - git remote -v

git add .

git commit -m 'first'

git push origin HEAD:master

uv sync - синхронизация и скачивание нужных зависимостей

