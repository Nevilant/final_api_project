import pytest
import allure

from conftest import wrapper_authorize


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


@allure.title("Авторизация")
@pytest.mark.parametrize("data, severity", DATA)
def test_1_authorize(wrapper_authorize, data, severity):
    allure.dynamic.severity(severity)
    wrapper_authorize.authorize(payload=data)
    wrapper_authorize.check_status_code_is_200()
