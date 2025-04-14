import random

import allure
import pytest


DATA = [
    (
        {
            'text': f'{random.randint(1, 100)}',
            'url': 'https://www.google.com/',
            'tags': ['python'],
            'info': {
                'author': '<NAME>',
                'author_email': '<EMAIL>',
            }
        },
        "Blocker"
    ),
    (
        {
            'text': f'Memes from Mexes',
            'url': 'https://www.google.com/',
            'tags': ['book', 'video'],
            'info': {
                'author': '<NAME>',
                'author_email': '<EMAIL>',
            }
        },
        "Blocker"
    ),
    (
        {
            'text': f'!"№;%:?*()_+-=',
            'url': 'https://www.google.com/',
            'tags': ['book', 'video'],
            'info': {
                'author': '<NAME>',
                'author_email': '<EMAIL>',
            }
        },
        "Normal"
    ),
    (
        {
            'text': f'{random.randint(1, 100)}',
            'url': 'www.google.com/',
            'tags': ['python'],
            'info': {
                'author': '<NAME>',
                'author_email': '<EMAIL>',
            }
        },
        "Critical"
    ),
    (
        {
            'text': f'{random.randint(1, 100)}',
            'url': 'https://www.google.com/',
            'tags': [],
            'info': {
                'author': '<NAME>',
                'author_email': '<EMAIL>',
            }
        },
        "Normal"
    ),
    (
        {
            'text': f'{random.randint(1, 100)}',
            'url': 'https://www.google.com/',
            'tags': ['python'],
            'info': {
                'author': '<NAME>',
                'author_email': '<EMAIL>',
            }
        },
        "Blocker"
    ),
    (
        {
            'text': f'{random.randint(1, 100)}',
            'url': 'https://www.google.com/',
            'tags': ['python'],
            'info': {
                'author': '<NAME>'
            }
        },
        "Blocker"
    ),
    (
        {
            'text': f'{random.randint(1, 100)}',
            'url': 'https://www.google.com/',
            'tags': ['python'],
            'info': {}
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


@allure.title("Удаление мема")
def test_delete_meme(get_token, wrapper_meme):
    payload = {
        "text": "for delete",
        "url": "https://example.com/meme.jpg",
        "tags": ["test", "python", "delete"],
        "info": {"author": "auto-test"}
    }
    wrapper_meme.post_meme(get_token, payload)
    wrapper_meme.check_status_code_is_200()

    meme_id = wrapper_meme.response.json()["id"]

    wrapper_meme.delete_meme(get_token, meme_id)
    wrapper_meme.check_status_code_is_200()

    wrapper_meme.get_meme_by_id(get_token, meme_id)
    wrapper_meme.check_status_code_is_404()
