import random
import string

import allure


def random_non_exist_token(length=8):
    chars = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(chars) for _ in range(length))
    return random_string


class BaseMethods:
    BASE_URL = 'http://167.172.172.115:52355'
    response = None
    json = None

    def headers(self, token=None):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        if token:
            headers['Authorization'] = token
        return headers

    @allure.step("Проверка, что статус код 200")
    def check_status_code_is_200(self):
        assert self.response.status_code == 200

    @allure.step("Проверка, что статус код не 200")
    def check_status_code_is_not_200(self):
        assert self.response.status_code != 200

    @allure.step("Проверка, что статус код 400")
    def check_status_code_is_400(self):
        assert self.response.status_code == 400

    @allure.step("Проверка, что статус код 401")
    def check_status_code_is_401(self):
        assert self.response.status_code == 401

    @allure.step("Проверка, что статус код 403")
    def check_status_code_is_403(self):
        assert self.response.status_code == 403

    @allure.step("Проверка, что статус код 404")
    def check_status_code_is_404(self):
        assert self.response.status_code == 404
