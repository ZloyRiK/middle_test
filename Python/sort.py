import storage as s


def sorting():
    notes = s.load()
    sorted_notes = sorted(notes.items(), key=lambda x: x[1]["Дата создания"], reverse=True)

    return sorted_notes


# for note_id, note in sorting():
#     print(f"{note_id}: {note['Заголовок']} {note['Текст заметки']} ({note['Дата создания']})")
