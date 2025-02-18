import allure
import requests

from API.base_endpoints import BaseEndpoints


class AuthorizeMethod(BaseEndpoints):

    @allure.step("Авторизация")
    def authorize(self, payload):
        self.response = requests.post(
            url=f'{self.BASE_URL}/authorize',
            headers=super().headers(),
            json=payload
        )
        return self.response.json()
