import pytest

from endpoints.get_is_token_live_method import IsTokenLiveMethod
from endpoints.post_authorize_method import AuthorizeMethod


@pytest.fixture()
def wrapper_authorize():
    return AuthorizeMethod()


@pytest.fixture()
def wrapper_is_token_live():
    return IsTokenLiveMethod()


@pytest.fixture(scope='session')
def get_authorization_token(wrapper_authorize):
    token = wrapper_authorize.json()["token"]
    return token
