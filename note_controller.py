from note_model import NoteModel
from note_view import NoteView


class NoteController:
    def __init__(self):
        self.model = NoteModel()
        self.view = NoteView()

    def display_notes(self):
        self.view.display_notes(self.model.notes)

    def add_note(self):
        note_id = input("Введите ИД заметки: ")
        title = input("Введите заголовок: ")
        body = input("Введите текст: ")
        success, message = self.model.add_note(note_id, title, body)
        if success:
            print(message)
        else:
            print(f"Ошибка: {message}")

    def edit_note(self):
        note_id = input("Введите ИД заметки для редактирования: ")
        new_title = input("Введите новый заголовок (оставьте пустым, чтобы сохранить прежний): ")
        new_body = input("Введите новый текст (оставьте пустым, чтобы сохранить прежний): ")
        success, message = self.model.edit_note(note_id, new_title, new_body)
        if success:
            print(message)
        else:
            print(f"Ошибка: {message}")

    def delete_note(self):
        note_id = input("Введите ИД заметки для её удаления: ")
        success, message = self.model.delete_note(note_id)
        if success:
            print(message)
        else:
            print(f"Ошибка: {message}")