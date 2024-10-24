from aiogram import Router, F, Bot
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from lexicon.lexicon import LEXICON
from states.compression_states import CompressionState
from keyboards.keyboard_utils import text_compression_keyboard, done_keyboard
from ai_tools.text_summary_tool import compress_text

# Инициализация роутера
router = Router()


# Обработчик команды /start
@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    """
    Обработчик команды /start.
    Очищает текущее состояние и переводит в состояние ожидания ввода текста.
    """
    await state.clear()  # Очищаем текущее состояние FSM
    await message.answer(text=LEXICON['/start'])  # Отправляем сообщение с приветственным текстом
    await state.set_state(CompressionState.waiting_for_text)  # Устанавливаем новое состояние


# Обработчик получения текста от пользователя
@router.message(StateFilter(CompressionState.waiting_for_text))
async def process_waiting_for_text_command(message: Message, state: FSMContext):
    user_data = await state.get_data()  # Получение текущих данных состояния
    collected_text = user_data.get("collected_text", "")  # Извлечение собранного текста
    already_notified = user_data.get("already_notified", False)

    if message.text == "Закончить ввод текста":
        user_data = await state.get_data()  # Получение текущих данных состояния
        collected_text = user_data.get("collected_text", "")  # Извлечение собранного текста

        await message.answer(
            text=LEXICON["compression_type"],
            reply_markup=text_compression_keyboard  # Инлайн-клавиатура с кнопками выбора сжатия
        )
        
        # Сохранение собранного текста и перевод в состояние ожидания выбора типа сжатия
        await state.update_data(collected_text=collected_text)
        await state.set_state(CompressionState.waiting_for_compression_type)
    # Добавление нового сообщения к собранному тексту
    collected_text += " " + message.text
    # Если уведомление еще не отправлено, отправляем его
    if not already_notified:
        msg_text = "Сообщение добавлено, введите еще текст или нажмите кнопку Закончить ввод текста"
        await message.answer(text=msg_text, reply_markup=done_keyboard)
        await state.update_data(already_notified=True)  # Устанавление флага, что уведомление было отправлено
    await state.update_data(collected_text=collected_text)  # Сохранение обновленного текст


# Обработчик нажатия кнопки "сильное сжатие"
@router.callback_query(F.data == "strong_compression_button_pressed", 
                       StateFilter(CompressionState.waiting_for_compression_type))
async def process_strong_compression_command(callback: CallbackQuery, state: FSMContext, bot: Bot):
    """
    Обрабатывает нажатие на кнопку выбора сильного сжатия.
    Здесь будет добавлена логика сильного сжатия текста.
    Очищает текущее состояние после выбора.
    """
    user_data = await state.get_data()  # Получение сохраненного текста
    collected_text = user_data.get("collected_text", "")
    msg_text = LEXICON["waiting_for_compression"]
    await callback.message.edit_text(text=msg_text, reply_markup=None)  # Отправление сообщения о начале сжатия
    msg_text = compress_text(collected_text, "strong")
    await callback.message.edit_text(text=msg_text)  # Отправление сжатого текста
    msg_text = LEXICON["/start"]
    await bot.send_message(callback.from_user.id, text=msg_text, reply_markup=ReplyKeyboardRemove())

    await state.clear()  # Очищение текущего состояния FSM
    await state.set_state(CompressionState.waiting_for_text)  # Обновление состояния FSM


# Обработчик нажатия кнопки "умеренное сжатие"
@router.callback_query(F.data == "weak_compression_button_pressed", 
                       StateFilter(CompressionState.waiting_for_compression_type))
async def process_weak_compression_command(callback: CallbackQuery, state: FSMContext, bot: Bot):
    """
    Обрабатывает нажатие на кнопку выбора слабого сжатия.
    Очищает текущее состояние после выбора.
    """
    user_data = await state.get_data()  # Получение сохраненного текста
    collected_text = user_data.get("collected_text", "")
    msg_text = LEXICON["waiting_for_compression"]
    await callback.message.edit_text(text=msg_text, reply_markup=None)  # Отправление сообщения о начале сжатия
    msg_text = compress_text(collected_text, "weak")
    await callback.message.edit_text(text=msg_text)  # Отправление сжатого текста
    msg_text = LEXICON["/start"]
    await bot.send_message(callback.from_user.id, text=msg_text, reply_markup=ReplyKeyboardRemove())

    await state.clear()  # Очищение текущее состояние FSM
    await state.set_state(CompressionState.waiting_for_text)  # Обновление состояния FSM
