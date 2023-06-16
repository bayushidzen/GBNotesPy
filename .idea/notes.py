import datetime
import os
import csv
import json
os.system('clear')

def show_notes_csv():
    notes = open('notesdb.csv','r')
    notesdb = csv.DictReader(notes, delimiter=";")
    count = 0
    for row in notesdb:
        if count == 0:
            print(f' {" | ".join(row)}')
        print(f' {row["id"]} | {row["Caption"]} | {row["Note"]} | {row["Timestamp"]}')
        count += 1
    print(f'Всего в файле {count + 1} строк.')
    notes.close()

def search_notes_csv():
    notes = open('notesdb.csv','r')
    notesdb = csv.DictReader(notes, delimiter=";")
    note_id = input("Введите ID для поиска: ")
    count = 0
    for row in notesdb:
        if count == 0:
            print(f' {" | ".join(row)}')
        if row["id"] == note_id:
            print(f' {row["id"]} | {row["Caption"]} | {row["Note"]} | {row["Timestamp"]}')
        count += 1
    notes.close()
def create_note():
    notes = open('notesdb.csv','a+')
    id = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    title = input('Введите заголовок заметки: ')
    body = input('Введите содержимое заметки: ')
    timestamp = datetime.datetime.now().strftime('%H:%M:%S-%Y.%m.%d')
    names = ["id","title",'body','timestamp']
    file_writer = csv.DictWriter(notes, delimiter = ";",lineterminator="\r", fieldnames=names)
    file_writer.writerow({'id':id,'title':title,'body':body,'timestamp':timestamp})
    notes.close()

def edit_note():
    notes = open('notesdb.csv','a+')
    title = input('Введите заголовок заметки: ')
    body = input('Введите содержимое заметки: ')
    names = ["id", "title",'body']
    file_writer = csv.DictWriter(notes, delimiter = ";",lineterminator="\r", fieldnames=names)
    file_writer.writerow({'id':id,'title':title,'body':body})
    notes.close()

def delete_note():
    note_id = input("Введите ID для удаления: ")
    count = 0

    notes = open('notesdb.csv','r+')
    notes_lines = notes.readlines()
    notesdb = csv.DictReader(notes, delimiter=";")
    for row in notesdb:
        print(f'Count {count}')
        if count == 0:
            print(f' {" | ".join(row)}')
        if row["id"] == note_id:
            print(f' {row["id"]} | {row["Caption"]} | {row["Note"]} | {row["Timestamp"]}')
            notes_lines.pop(count)
    notes_lines2 = ''.join(notes_lines)
    print(notes_lines2)
    with open('notesdb.csv', 'w', encoding="utf-8") as notes:
        notes.write(f'{notes_lines2}')
        print ('Контакт удалён')

def intro_text():
    print('Меню: ')
    print('1) Создать заметку 2) Показать все заметки')
    print('3) Редактировать заметку  4) Удалить заметку')
    print('5) Найти заметку ')

def restart_text():
    print('1) Да 2) Нет')

def restart(command):
    match command:
        case 1:
            os.system('clear')
            intro_text()
            menu(int(input('Выберите необходимое действие: ')))
        case _:
            print('Спасибо что выбрали нашу записную книжку')

def menu(command):
    match command:
        case 1:
            create_note()
            os.system('clear')
            restart_text()
            restart(int(input('Хотите продолжить работу? \n')))
        case 2:
            show_notes_csv()
            os.system('clear')
            restart_text()
            restart(int(input('Хотите продолжить работу? \n')))
        case 3:
            edit_note()
            os.system('clear')
            restart_text()
            restart(int(input('Хотите продолжить работу? \n')))
        case 4:
            delete_note()
            os.system('clear')
            restart_text()
            restart(int(input('Хотите продолжить работу? \n')))
        case 5:
            search_notes_csv()
            os.system('clear')
            restart_text()
            restart(int(input('Хотите продолжить работу? \n')))
        case _:
            os.system('clear')
            print('Пожалуйста выберите вариант из меню')
            intro_text()
            menu(int(input('Выберите необходимое действие: ')))
            
            
            
notes_list = ()
intro_text()

menu(int(input('Выберите необходимое действие: ')))            