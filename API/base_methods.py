import allure


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

    @allure.step("Проверка, что статус код 401")
    def check_status_code_is_401(self):
        assert self.response.status_code == 401
