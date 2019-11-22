# -*- coding: utf-8 -*-
import csv

class Contact:

    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name,phone,email)
        self._contacts.append(contact)
        self._save()
        print('name: {}, phone: {}, email: {} added'.format(name, phone, email))

    
    def show_all(self):
        for contact in self._contacts:
            self.print_all(contact)


    def print_all(self, contact):
        print('name: {}, phone: {}, email: {}'.format(contact._name, contact._phone, contact._email))

    def delete_contact(self, name):
        for index,contact in enumerate(self._contacts):
            if(contact._name.lower()==name.lower()):
                del self._contacts[index]
                break

    def _save(self):
        with open('contacts.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))
            for contact in self._contacts:
                writer.writerow((contact._name, contact._phone, contact._email))

def run():

    contact_book = ContactBook()

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]Ã±adir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el tel del contacto: '))
            email = str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            print('actualizar contacto')

        elif command == 'b':
            print('buscar contacto')

        elif command == 'e':
            print('eliminar contacto')
            contact_book.delete_contact(name)

        elif command == 'l':
            print('listar contactos')
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')



print('B I E N V E N I D O  A  L A  A G E N D A')
run()