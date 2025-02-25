import random

import allure
import pytest


DATA = [
    (
        {
            'text': f'{random.randint(1, 100)}',
            'url': 'https://www.google.com/',
            'tags': ['python', 'javascript'],
            'info': {
                'author': '<NAME>',
                'author_email': '<EMAIL>',
            }
        },
        "Blocker"
    ),
]


@allure.title("Получение всех мемов")
def test_get_all_meme(get_token, wrapper_meme):
    wrapper_meme.get_all_memes(get_token)
    wrapper_meme.check_status_code_is_200()


@allure.title("Получение случайного мема")
def test_get_meme_by_id(get_token, wrapper_meme, get_random_id_meme):
    wrapper_meme.get_meme_by_id(get_token, get_random_id_meme)
    wrapper_meme.check_status_code_is_200()


@allure.title("Загрузка мема")
@pytest.mark.parametrize("data, severity", DATA)
def test_post_meme(get_token, wrapper_meme, data, severity):
    allure.dynamic.severity(severity)
    wrapper_meme.post_meme(get_token, payload=data)
    wrapper_meme.check_status_code_is_200()

