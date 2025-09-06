FILENAME = "notebook.txt"

def add_note():
    note = input(" Введи нову замітку: ")
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(note + "\n")
    print("Замітку збережено!")

def show_notes():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            notes = f.readlines()
        if notes:
            print("\n Твої замітки:")
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note.strip()}")
            return notes
        else:
            print("Заміток поки немає.")
            return []
    except FileNotFoundError:
        print("Файл ще не створений. Додай хоча б одну замітку.")
        return []

def delete_note():
    notes = show_notes()
    if not notes:
        return
    try:
        num = int(input("\n Введи номер замітки для видалення: "))
        if 1 <= num <= len(notes):
            deleted = notes.pop(num - 1)
            with open(FILENAME, "w", encoding="utf-8") as f:
                f.writelines(notes)
            print(f" Замітку видалено: {deleted.strip()}")
        else:
            print(" Такого номера немає.")
    except ValueError:
        print(" треба ввести число!")

def main():
    while True:
        print("\n--- Блокнот ---")
        print("1. Додати замітку")
        print("2. Показати замітки")
        print("3. Видалити замітку")
        print("4. Вийти")
        
        choice = input(" Обери дію: ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print(" вихід з блокнота...")
            break
        else:
            print(" Невірний вибір!")


main() 
