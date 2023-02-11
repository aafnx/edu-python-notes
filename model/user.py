# аутентификация и регистрация должны быть в модели-user!
def authentication(author, password):
    # author = view.get_data('Введите ваше имя >> ')
    # password = view.get_data('Введите пароь >> ')
    return {author: password}
