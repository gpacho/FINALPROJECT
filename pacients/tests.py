from django.test import TestCase
from pacients.models import Pacient
import random
import string

# Create your tests here.

KEY_LEN = 5

class PacientTestCase(TestCase):

    pacient_names = list()
    pacient_surnames = list()
    pacient_dni = list()

    def setUp(self):
        for _ in range(5):
            char_list = [
                random.choice((string.ascii_letters + string.digits))
                for _ in range(KEY_LEN)
            ]
            
            char_list_surname = [
                random.choice((string.ascii_letters + string.digits))
                for _ in range(KEY_LEN)
            ]

            int_list_dni = [
                random.choice((string.digits))
                for _ in range(KEY_LEN)
            ]

            mock_name = ''.join(char_list)
            mock_surname = ''.join(char_list_surname)
            mock_dni = ''.join(int_list_dni)
            Pacient.objects.create(name=mock_name, surname=mock_surname, dni=mock_dni)
            self.pacient_names.append(mock_name)
            self.pacient_surnames.append(mock_surname)
            self.pacient_dni.append(mock_dni)


    def test_random_names(self):
        print('\n****Pacientes de Prueba****\n')
        for name in self.pacient_names:
            pacient = Pacient.objects.get(name=name)
            self.assertEqual(pacient.name, name)

        for surname in self.pacient_surnames:
            pacient = Pacient.objects.get(surname=surname)
            self.assertEqual(pacient.surname, surname)

        for dni in self.pacient_dni:
            pacient = Pacient.objects.get(dni=dni)
            self.assertEqual(pacient.dni, int(dni))

            print(f'****Name: {pacient.name}****')
            print(f'****Surname: {pacient.surname}****')
            print(f'****DNI: {pacient.dni}****\n')
