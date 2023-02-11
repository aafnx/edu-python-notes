def create(note):
    return {'id': 0, 'date': '', 'note': note}


def formatted_output(note):
    return f'id: {note["id"]} | date: {note["date"]}\n{note["note"]}\n---'
