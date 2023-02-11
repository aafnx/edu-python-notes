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
                show_notes(db.read())
            case 'find':
                key_word = get_key_word_find_note().lower()
                found_notes = db.find(key_word)
                if len(found_notes) == 0:
                    view.show('Заметка не найдена')
                else:
                    show_notes(found_notes)
            case 'delete':
                notes = db.read()
                show_notes(notes)
                view.show('Чтобы удалить заметку')
                id_note = get_id_note()
                notes = change(notes, id_note, 'del')
                if len(notes) > 0:
                    db.overwrite(notes)
                else:
                    view.show(f'Заметка с id: {id_note} не найдена')
            case 'change':
                notes = db.read()
                show_notes(notes)
                view.show('Чтобы изменить заметку')
                id_note = get_id_note()
                notes = change(notes, id_note)
                if len(notes) > 0:
                    db.overwrite(notes)
                else:
                    view.show(f'Заметка с id: {id_note} не найдена')

def change(src_notes, id_note, mode='change'):
    for row in src_notes:
        if id_note == row['id']:
            if mode == 'del':
                src_notes.remove(row)
                return src_notes
            view.show(row['note'])
            row['note'] = get_note()
            return src_notes

def show_notes(notes):
    for row in notes:
        view.show(note.formatted_output(row))

def get_command():
    return view.get_data('Введите команду (new, change, find, showall, delete, exit) >> ')


def get_username():
    return view.get_data('Введите имя пользователя >> ')


def get_user_password():
    return view.get_data('Введите пароль >> ')


def get_note():
    return view.get_data('Введите текст заметки:\n')


def get_key_word_find_note():
    return view.get_data('Введите слово или дату для поиска заметки >> ')


def get_id_note():
    return view.get_data('Введите id >> ')
