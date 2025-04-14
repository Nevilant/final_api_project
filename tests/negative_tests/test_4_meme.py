import allure


@allure.title("Удаление чужого мема")
def test_delete_meme(get_token, wrapper_meme, get_random_id_meme):
    wrapper_meme.delete_meme(get_token, get_random_id_meme)
    wrapper_meme.check_status_code_is_403()
