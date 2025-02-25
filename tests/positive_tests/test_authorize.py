import pytest
import allure


DATA = [
    (
        {
            "name": "SOME words"
        },
        "Blocker"
    ),
    (
        {
            "name": "Русский"
        },
        "normal"
    ),
    (
        {
            "name": "123"
        },
        "normal"
    ),
    (
        {
            "name": "!@#$%^&*()_+'/"
        },
        "minor"
    ),
]


@allure.title("Авторизация c корректными данными")
@pytest.mark.parametrize("data, severity", DATA)
def test_1_authorize(wrapper_authorize, data, severity):
    allure.dynamic.severity(severity)
    wrapper_authorize.authorize(payload=data)
    wrapper_authorize.check_status_code_is_200()


@allure.title("Жив ли токен?")
@allure.severity(allure.severity_level.BLOCKER)
def test_2_authorize(get_token, wrapper_authorize):
    wrapper_authorize.is_token_live(get_token)
    wrapper_authorize.check_status_code_is_200()
