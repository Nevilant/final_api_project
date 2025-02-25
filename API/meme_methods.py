import allure
import requests

from API.base_methods import BaseMethods


class MemeMethods(BaseMethods):

    @allure.step("Получить все мемы")
    def get_all_memes(self, token):
        self.response = requests.get(
            url=f'{self.BASE_URL}/meme',
            headers=super().headers(token)
        )
        return self.response

    @allure.step("Получить мем по id")
    def get_meme_by_id(self, token, id_meme):
        self.response = requests.get(
            url=f'{self.BASE_URL}/meme/{id_meme}',
            headers=super().headers(token)
        )
        return self.response

    @allure.step("Добавить мем")
    def post_meme(self, token, payload):
        self.response = requests.post(
            url=f'{self.BASE_URL}/meme',
            headers=super().headers(token),
            json=payload
        )
        return self.response

    @allure.step("Изменить существующий мем")
    def edit_meme(self, token, id_meme, payload):
        self.response = requests.put(
            url=f'{self.BASE_URL}/meme/{id_meme}',
            headers=super().headers(token),
            json=payload
        )
        return self.response

    @allure.step("Удалить мем")
    def delete_meme(self, token, id_meme):
        self.response = requests.delete(
            url=f'{self.BASE_URL}/meme/{id_meme}',
            headers=super().headers(token)
        )
        return self.response
