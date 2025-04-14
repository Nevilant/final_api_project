import pytest
import allure

from API.base_methods import random_non_exist_token

DATA = [
    (
        {
            "NAME": "Русский"
        },
        "Blocker"
    ),
    (
        {
            "name": True
        },
        "Blocker"
    )
]

DATA_TOKEN = [
    (
        f"{random_non_exist_token()}",
        "Blocker"
    ),
(
        "",
        "Blocker"
    ),

]


@allure.title("Авторизация c некорректными данными")
@pytest.mark.parametrize("data, severity", DATA)
def test_1_authorize(wrapper_authorize, data, severity):
    allure.dynamic.severity(severity)
    wrapper_authorize.authorize(payload=data)
    wrapper_authorize.check_status_code_is_not_200()


@allure.title("Некорректный токен")
@pytest.mark.parametrize("token, severity", DATA)
def test_2_authorize(get_token, wrapper_authorize, token, severity):
    wrapper_authorize.is_token_live(token)
    wrapper_authorize.check_status_code_is_not_200()
