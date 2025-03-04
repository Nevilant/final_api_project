from random import choice

import pytest

from API.authorize_methods import AuthorizeMethod
from API.meme_methods import MemeMethods


@pytest.fixture()
def wrapper_authorize():
    return AuthorizeMethod()


@pytest.fixture()
def get_token(wrapper_authorize):
    payload = {
        'name': 'pre_condition'
    }
    json_data = wrapper_authorize.authorize(payload)
    return json_data.json()['token']


@pytest.fixture()
def wrapper_meme():
    return MemeMethods()


@pytest.fixture()
def get_random_id_meme(wrapper_meme, get_token):
    json_data = wrapper_meme.get_all_memes(get_token)
    response_json = json_data.json()
    memes_list = response_json['data']
    all_ids = [meme['id'] for meme in memes_list]
    id_meme = choice(all_ids)
    return id_meme
