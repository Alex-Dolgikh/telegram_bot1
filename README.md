# Телеграм-бот для транскрипции имен с кириллицы на латиницу

В переменных окружения надо проставить API токен бота.

`TOKEN` — API токен бота

Использование с Docker показано ниже. Предварительно заполните ENV переменную, указанную выше, в Dockerfile.

```
docker build .
docker run -d -p 80:80 (ID вашего контейнера)
```

