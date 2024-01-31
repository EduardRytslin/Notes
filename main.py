import json
import os
from datetime import datetime

from note_controller import NoteController


def main():
    controller = NoteController()

    while True:
        print("\n===== Меню =====\nВыберите нужную команду")
        print("1. Просмотреть уже созданные заметки")
        print("2. Создать заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            controller.display_notes()
        elif choice == '2':
            controller.add_note()
        elif choice == '3':
            controller.edit_note()
        elif choice == '4':
            controller.delete_note()
        elif choice == '5':
            print("Закрытие программы...")
            break
        else:
            print("Вы выбрали неправильный путь, попробуйте ещё раз")


if __name__ == "__main__":
    main()