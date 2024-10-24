from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

# Кнопка для завершения ввода текста
done_button = KeyboardButton(text="Закончить ввод текста")

# Кнопка для сильного сжатия текста (сжатие до одного-двух предложений)
strong_compression_button = InlineKeyboardButton(
    text="Сильное сжатие (одно-два предложения)",  # Текст на кнопке
    callback_data="strong_compression_button_pressed"  # Данные для callback'а
)

# Кнопка для слабого сжатия текста (сжатие до краткого абзаца)
weak_compression_button = InlineKeyboardButton(
    text="Слабое сжатие (краткий абзац)",  # Текст на кнопке
    callback_data="weak_compression_button_pressed"  # Данные для callback'а
)

# Инлайн-клавиатура с кнопками для выбора типа сжатия текста
text_compression_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [strong_compression_button],  # Кнопка сильного сжатия в отдельной строке
        [weak_compression_button]  # Кнопка слабого сжатия в отдельной строке
    ]
)

# Клавиатура с кнопкой для завершения ввода текста
done_keyboard = ReplyKeyboardMarkup(
    keyboard=[[done_button]],  # Кнопка для завершения ввода
    resize_keyboard=True  # Изменяем размер клавиатуры под экран устройства
)
