import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


# Скачивание данных nltk для токенизации предложений и слов
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


# Разбитие текста на предложения
def split_into_sentences(text):
    """Токенизация текста в список предложений."""
    return sent_tokenize(text)


# Разбитие текста на слова
def split_into_words(text):
    """Токенизация текста в список слов."""
    return word_tokenize(text)


# Вычисление матрицы TF-IDF для предложений
def compute_tfidf(sentences):
    """Вычислить матрицу TF-IDF для списка предложений.

    Аргументы:
        sentences (list of str): Список предложений.

    Возвращает:
        scipy.sparse.csr_matrix: Матрица TF-IDF для предложений.
    """
    vectorizer = TfidfVectorizer()
    return vectorizer.fit_transform(sentences)


# Генерация резюме на основе TF-IDF для заданного количества предложений
def get_tfidf_summary(text, num_sentences=2):
    """Сделать резюме текста, выбирая предложения с наивысшими оценками TF-IDF.

    Аргументы:
        text (str): Входной текст для резюме.
        num_sentences (int): Количество предложений, включаемых в резюме.

    Возвращает:
        str: Сжатый текст, содержащий наиболее важные предложения.
    """
    sentences = split_into_sentences(text)
    if len(sentences) <= num_sentences:
        return text  # Вернуть полный текст, если он короче размера резюме.

    tfidf_matrix = compute_tfidf(sentences)
    sentence_scores = np.sum(tfidf_matrix.toarray(), axis=1)

    # Получение индексов верхних `num_sentences` предложений на основе оценок TF-IDF
    ranked_sentence_indices = np.argsort(sentence_scores)[-num_sentences:]

    # Создание резюме, упорядочивая выбранные предложения по их появлению
    summary = [sentences[i] for i in sorted(ranked_sentence_indices)]
    return ' '.join(summary)


# Основная функция для сжатия текста на основе выбранного метода
def compress_text(text, method='weak'):
    """Сжать текст, создавая резюме с использованием указанного метода сжатия.

    Аргументы:
        text (str): Входной текст для сжатия.
        method (str): Метод сжатия ('weak' для абзаца, 'strong' для двух предложений).

    Возвращает:
        str: Сжатое резюме текста.

    Исключения:
        ValueError: Если метод не 'weak' или 'strong'.
    """
    if method == 'weak':
        return get_tfidf_summary(text, num_sentences=5)
    elif method == 'strong':
        return get_tfidf_summary(text, num_sentences=2)
    else:
        raise ValueError("Метод должен быть 'weak' или 'strong'.")
