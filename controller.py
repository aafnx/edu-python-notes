import view
from model import note
from model import db


def init():
    while True:
        command = get_command().lower()
        match command:
            case 'exit':
                return
            case 'new':
                user_note = get_note()
                data = note.create(user_note)
                db.save(data)
            case 'showall':
                notes = db.read()
                for row in notes:
                    view.show(note.format(row))
                

# в заметке будем хранить автора, дату создания, дату изменения
# было бы хорошо что смотреть свои заметки может только автор, и у каждого автора есть пароль
# сделать валидацию пароля чтобы было не мнее 5 знаков и не менее 1ой буквы
# остальные не видят и не знают о заметке другого

# данные о пользователях и пароле записывать в одну базу
# для каждого пользователя создавать отдельную базу

# если пользователь не зарегистрирован, то сообщиь об этом и показать
# сообщение о регистрации после ввода данных

# немогут быть 2 пользователя с одним именем в базе, регистр не должен быть важен при проверке имени

# можно попробовать хранить все в csv файлах
def get_command():
    return view.get_data('Введите команду (new, change, find, showall, delete, exit) >> ')

def get_username():
    return view.get_data('Введите имя пользователя >> ')

def get_user_password():
    return view.get_data('Введите пароль >> ')

def get_note():
    return view.get_data('Введите текст заметки:\n')
