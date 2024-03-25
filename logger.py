from date_create import *

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'

def add_contact():
    contact = create_contact()
    with open('phonebooke.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)

def show_info():
    with open('phonebooke.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        #print(file.read().rstrip())
        for contact in enumerate(contacts_list,1):
            print(*contact)

def search_contact():
    print('Выберите вариант поиска:\n'
              '1. По фамилии\n'
              '2. По имени\n'
              '3. По отчеству\n'
              '4. По номеру телефона\n'
              '5. По адресу\n')
    
    while var_seach not in ('1','2','3','4','5'):
        print('Некорректные данные')
        var_seach = input()
    
    index_var = int(var_seach) - 1

    seach = input('Введите данные для поиска: ')
    with open('phonebooke.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()
        if seach in contact_lst[index_var]:
            print(contact_str)