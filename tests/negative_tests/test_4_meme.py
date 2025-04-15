import random

import allure
import pytest

from API.base_methods import random_non_exist_token


DATA = [
    (
        {
            'url': 'https://www.google.com/',
            'tags': ['python'],
            'info': {
                'author': '<NAME>',
                'author_email': '<EMAIL>',
            }
        }
    ),
    (
        {
            'text': f'Test-{random.randint(1, 100)}',
            'tags': ['python'],
            'info': {
                'author': '<NAME>',
                'author_email': '<EMAIL>',
            }
        }
    )
]


@allure.step("Получение всех мемов с несуществующим токеном")
@allure.severity("Blocker")
def test_get_all_memes_with_incorrect_token(wrapper_meme):
    wrapper_meme.get_all_memes(random_non_exist_token())
    wrapper_meme.check_status_code_is_not_200()


@allure.step("Получение мема с несуществующим id")
@allure.severity("Blocker")
def test_get_meme_by_incorrect_id(wrapper_meme, get_token, get_list_of_memes_id):
    wrapper_meme.get_meme_by_id(get_token, get_list_of_memes_id[-1] + 1)
    wrapper_meme.check_status_code_is_404()


@allure.step("Постим мем с некорректными телом запроса")
@pytest.mark.parametrize("data", DATA)
@allure.severity("Blocker")
def test_post_meme_with_incorrect_body(wrapper_meme, get_token, data):
    wrapper_meme.post_meme(get_token, payload=data)
    print(wrapper_meme.response.status_code)
    wrapper_meme.check_status_code_is_400()


@allure.title("Удаление чужого мема")
@allure.severity("Blocker")
def test_delete_meme(get_token, wrapper_meme, get_list_of_memes_id):
    wrapper_meme.delete_meme(get_token, get_list_of_memes_id[0])
    wrapper_meme.check_status_code_is_403()
