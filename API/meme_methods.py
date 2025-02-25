import allure
import requests

from API.base_methods import BaseMethods


class MemeMethods(BaseMethods):

    @allure.step("Получение всех мемов")
    def get_all_memes(self, token):
        self.response = requests.get(
            url=f'{self.BASE_URL}/meme',
            headers=super().headers(token)
        )
        return self.response

    @allure.step("Получение мема по id")
    def get_meme_by_id(self, token, id_meme):
        self.response = requests.get(
            url=f'{self.BASE_URL}/meme/{id_meme}',
            headers=super().headers(token)
        )
        return self.response

    @allure.step("Добавление мема")
    def post_meme(self, token, payload):
        self.response = requests.post(
            url=f'{self.BASE_URL}/meme',
            headers=super().headers(token),
            json=payload
        )
        return self.response
