# SummarizerBot Project Documentation

## 1. main.py
**Описание**: Основной файл проекта, который управляет работой бота.
- Обрабатывает входные сообщения от пользователей.
- Подключает вспомогательные модули, такие как обработчики команд и ИИ-инструменты.
- Содержит основные состояния FSM (Finite State Machine) для управления процессом взаимодействия с пользователем.

## 2. compression_states.py
**Описание**: Этот файл описывает состояния Finite State Machine (FSM), которые управляют процессом сжатия текста.
- **waiting_for_text**: Ожидание ввода текста пользователем.
- **waiting_for_compression_type**: Ожидание выбора типа сжатия текста.

## 3. lexicon.py
**Описание**: Содержит лексикон и текстовые шаблоны для сообщений бота.
- Содержит строки для приветственного сообщения, сообщений о состоянии и результатов сжатия текста.

## 4. keyboard_utils.py
**Описание**: Утилита для создания клавиатур в боте.
- Кнопки выбора типа сжатия текста: 'Сильное сжатие' и 'Слабое сжатие'.
- Клавиатура для завершения ввода текста.

## 5. user_handlers.py
**Описание**: Содержит обработчики пользовательских команд и состояний.
- Обрабатывает команду `/start` и инициирует взаимодействие с пользователем.
- Обрабатывает ввод текста и выбор метода сжатия текста.
- Взаимодействует с FSM для управления процессом взаимодействия.

## 6. config.py
**Описание**: Содержит функции для загрузки конфигурации бота.
- Использует файл `.env` для хранения токена API Telegram.
- Загружает и возвращает объект конфигурации.

## 7. text_summary_tool.py
**Описание**: Основной модуль для сжатия текста.
- Использует токенизацию текста и TF-IDF для создания краткого содержания.
- Реализует два метода сжатия: 'weak' для абзаца и 'strong' для одного-двух предложений.


# Краткая инструкция по запуску скрипта

1. Клонировать репозиторий при помощи:
 ```bash
  git clone https://github.com/snthnk/SummarizerBot.git
 ```
2. Установить необходимые библиотеки из файла:
```bash
  pip install -r requirements.txt
```
3. Запустить скрипт ```main.py```
4. Перейти в Telegram.
5. Открыть бота [@Summarizer1734_bot](https://t.me/Summarizer1734_bot).
6. Нажать кнопку "Запустить" для начала работы с ботом.

# Краткая инструкция по пользованию ботом

1. Нажать кнопку "Запустить" для начала работы.
2. Отправить текст одним или несколькими сообщениями. Когда ввод текста закончен, нажать кнопку "Закончить ввод текста".
3. Выбрать тип сжатия, нажав на одну из инлайн-кнопок.
4. После получения сжатого текста, если хотите продолжить работу с ботом, вернитесь к шагу 2.

# Инструкция для MacOS

1. Добавьте следующий код в файл `text_summary_tool.py`:

   ```python
   import ssl

   try:
       _create_unverified_https_context = ssl._create_unverified_context
   except AttributeError:
       pass
   else:
       ssl._create_default_https_context = _create_unverified_https_context
   ```
  
2. Замените строку:
    
   ```python
    ntlk.download("punkt")
   ```

   на:

   ```python
    ntlk.download("punkt_tab")
   ```
