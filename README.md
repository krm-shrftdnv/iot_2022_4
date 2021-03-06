# Проект и ДЗ по курсу "Интернет вещей". Команда 4
___
- ### Состав команды:
    - Гариева Аделя 11-802
    - Шайдуллин Айдар 11-802
    - Абдуллин Марат 11-803
    - Шарафутдинов Карим 11-804
    - Мусин Искандер 11-804
- ### Содержание репозитория
    - hw2 - код решения задания №2 (RGB LED)
    - hw3 - код решения задания №3 (Датчик + MQTT)
    - hw4 - код решения задания №4 (GRPC)
    - project - код реализации систем для зачётного проекта
- ### Описание проекта
    - Идея: уведомление пользователя о высоком содержании CO2 и органических соединений в помещении
    - Демонстрация работы проекта по ссылке: [видео](https://drive.google.com/file/d/1dreb0PzjSodUjmBNBcVLCWIr5J82cC9O/view?usp=sharing)
    - Hardware:
      - Модуль качества воздуха CJMCU-8128 с датчиком CCS811 для получения значений содержания углекислого газа и tVOC 
      - Светодиод для уведомления пользователя о достижении критических значений CO2 и tVOC
    - Компоненты:
      - `hardware_service` - сервис на Raspberry Pi для работы с железом (Реализация: Python, Flask)
      - `backend_service` - посредник, между `hardware_service` и `backend` (Реализация: Python)
      - `backend` - веб-сервер. Анализирует показания с датчика и управляет сбором показаний и выводом алертов посредством команд (Реализация: Java, Spring). `API`: [Swagger](https://app.swaggerhub.com/apis-docs/krm-shrftdnv/itis_team_4/0.0.1)
      - `frontend` - веб-страница для вывода графического представления показаний датчика и алертов (Реализация: JavaScript)
    - Информация о значениях и запуске команд передаётся в формате JSON.
    - Графическое представление взаимосвязи компонентов:
     ![Архитектура](https://github.com/krm-shrftdnv/iot_2022_4/blob/1fba4c4fa7a2f307c3ba825c190f62c846069d8a/project/diagram/project_archdrawio.png?raw=true)
    - MQTT:
      - Используется брокер broker.hivemq.com
      - Для передачи показаний датчик на бэкенд используется топик `itis_team_4/indications`
      - Для передачи команд с бэкенда на Raspberry Pi используется топик `itis_team_4/control`
      - Возможные команды:
        - `alert` - включение светодиода
        - `alert_off` - отключение светодиода
        - `get` - запрос показаний с бэкенда
        - `start` - начать стриминг показаний датчика на бэкенд с интервалом 2 секунды
        - `stop` - остановка стриминга показний на бэкенд
    - Frontend:
      - Реализовано графическое представление значений содержания CO2
      - Реализовано графическое представление значений содержания tVOC
      - Реализовано отображение алертов о первышений допустимых значений
      - Реализована кнопка `start` - запуск стриминга показаний
      - Реализована кнопка `stop` - остановка стриминга показаний
      - Реализована форма для задания критических значений
        