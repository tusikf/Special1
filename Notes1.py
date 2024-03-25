# Должно уметь сохранять данные в файл, уметь читать данные из файла, делать выборку по дате, выводить на
# экран выбранную запись, выводить на экран весь список записок, добавлять записку, редактировать ее и удалять


def input_name_notes():
    return input('Введите имя заметки:')
def input_text_notes():
    return input('Введите текст заметки:')
def input_data():
    return input('Введите дату:')

def create_notes():
    name_notes = input_name_notes()
    text_notes = input_text_notes()
    data = input_data()
    
    return f'{data} {name_notes}\n {text_notes}\n\n'

def add_notes():
    notes = create_notes()
    with open('notes.txt', 'a', encoding='UTF-8') as file:
        file.write(notes)

def show_info():
    with open('notes.txt', 'r', encoding='UTF-8') as file:
        notes_list = file.read().rstrip().split('\n\n')
        print(file.read().rstrip())
        for note in enumerate(notes_list,1):
            print(*note)

def search_notes():
    print('Выберите вариант поиска:\n'
              '1. По дате\n'
              '2. По заголовку заметки\n')
    
    while var_seach not in ('1','2'):
        print('Некорректные данные')
        var_seach = input()
    
    index_var = int(var_seach) - 1

    seach = input('Введите данные для поиска: ')
    with open('notes.txt', 'r', encoding='UTF-8') as file:
        notes_list = file.read().rstrip().split('\n\n')
    for note_str in notes_list:
        notes_lst = note_str.replace('\n', ' ').split()
        if seach in notes_lst[index_var]:
            print(note_str)

def interface():
    with open('notes.txt', 'a'):
        pass
    command = '-1'
    while command != '4':
        print('Возможные варианты взаимодействия:\n'
              '1. Добавить заметку\n'
              '2. Вывести на экран все заметки\n'
              '3. Поиск заметки\n'
              '4. Выход из программы')

        command = input('Введите номер действия: ')

        while command not in ('1', '2', '3', '4'):
            print('Некорректные данные, нужно ввести число комманды')
            command = input('Введите номер действия: ')

        match command:
            case '1':
                add_notes()
            case '2':
                show_info()
            case '3':
                search_notes()
            case '4':
                print('Всего хорошего!')

interface()