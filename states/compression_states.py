from aiogram.fsm.state import State, StatesGroup

# Класс состояний для работы со сжатием текста


class CompressionState(StatesGroup):
    waiting_for_text = State()  # Ожидание ввода текста для сжатия
    waiting_for_compression_type = State()  # Ожидание ввода типа сжатия
