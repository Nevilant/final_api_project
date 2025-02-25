import allure
import requests

from API.base_methods import BaseMethods


class AuthorizeMethod(BaseMethods):

    @allure.step("Авторизоваться")
    def authorize(self, payload):
        self.response = requests.post(
            url=f'{self.BASE_URL}/authorize',
            headers=super().headers(),
            json=payload
        )
        return self.response

    @allure.step("Проверить жив ли токен")
    def is_token_live(self, token):
        self.response = requests.get(
            url=f'{self.BASE_URL}/authorize/{token}',
        )
        return self.response
