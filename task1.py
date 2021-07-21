import unittest
from library_function import sort_name_docnumber, documents, directories, searh_number_shelf, output_document, new_document


class TestTask1(unittest.TestCase):
    def test_sort_name_docnumber_10006(self):
        self.assertEqual("Аристарх Павлов", sort_name_docnumber(documents))

    def test_searh_number_shelf_10006(self):
        self.assertEqual('2', searh_number_shelf(directories))

   # def test_output_document(self):              # Тест функции вывода работает корректно в отсутсвии теста на добавления записи
       # self.assertMultiLineEqual('insurance  "10006"  "Аристарх Павлов"', output_document(documents))

    def test_new_document(self):
        documents1 = [
            {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
            {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
            {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
            {'type': 'passport', 'number': '2347 879201', 'name': 'Иван Иванов'}
]
        directories1 = {
            '1': ['2207 876234', '11-2'],
            '2': ['10006'],
            '3': ['2347 879201']}
        self.assertEqual((documents1, directories1), new_document())















