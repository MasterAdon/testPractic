import requests

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def sort_name_docnumber(doc):
    ''' function for sorting a directory
     number document ->>> name user '''
    num_in = "10006"  # переменная задана в интересах тестирования
    # num_in = (input('Введите номер документа: '))
    need_name = str()
    for key in doc:
        if key["number"] == num_in:
            need_name += (key["name"])

    if need_name != str():
        print(need_name)
    else:
        print('Документ с таким номером отсутсвует в каталоге')

    return need_name


# sort_name_docnumber(documents)

def searh_number_shelf(direct):
    ''' function for search shelf
    number document ->>> number shelf '''
    num_in = "10006"  # переменная задана в интересах тестирования
    # num_in = (input('Введите номер документа: '))
    num_shelf = str()
    for shelf, document in direct.items():  # видит все списки и полки, в том числе пустой список
        if num_in in document:
            num_shelf += shelf
    if num_shelf != str():
        print(f'Документ находится на полке № {num_shelf}')
    else:
        print('Документ с таким номером отсутсвует в каталоге')

    return num_shelf


# searh_number_shelf(directories)


def output_document(doc):
    ''' function for document outpust '''
    for dic in doc:
        doc_format = f'{dic["type"]}  "{dic["number"]}"  "{dic["name"]}"'
        print(f'{dic["type"]}  "{dic["number"]}"  "{dic["name"]}"')

    return doc_format


# output_document(documents)


def new_document():
    ''' function for new document '''
    number_new = "2347 879201"     # переменная задана в интересах тестирования
    type_new = "passport"          # переменная задана в интересах тестирования
    name_new = "Иван Иванов"       # переменная задана в интересах тестирования
    # number_new = input('Введите номер документа: ')
    # type_new = input('Введите тип документа: ')
    # name_new = input('Введите имя обладателя документа: ')
    new_dict = {"type": type_new, "number": number_new, "name": name_new}
    documents.append(new_dict)
    num_shelf = '3'               # переменная задана в интересах тестирования
    # num_shelf = (input('Введите номер полки для размещения документа: '))
    if num_shelf in directories.keys():
        directories[num_shelf].append(number_new)
        print('Документ добавлен')
    else:
        print('Полка с таким номером не используеться')

    return  documents, directories


# new_document()
# output_document(documents)
def main():
    while True:
        user_imp = (input("Введите команду действия (p,s,l,a,end): "))
        if user_imp == 'p':
            sort_name_docnumber(documents)
        elif user_imp == 's':
            searh_number_shelf(directories)
        elif user_imp == 'l':
            output_document(documents)
        elif user_imp == 'a':
            new_document()
        elif user_imp == 'end':
            print("Работа с программой завершена")
            break
        else:
            print('Неправильная команда')


#main()

def create_yadiskfolder():
    """ Метод для создания папки на Яндекс диске """
    #folder_name = str(input('Введите имя создаваемой папки на диске: '))
    folder_name = "test"
    url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
    get_headers = {'Content-Type ': 'application/json',
                   'Authorization': 'OAuth {}'.format("AQAAAABUIDncAADLW4JVo84R103XiYuL8INwv-Y")}
    params = {'path': folder_name}
    requests.put(url, headers=get_headers, params=params)
    respose = requests.get(url, headers=get_headers, params=params)
    print(respose)

    return respose


#create_yadiskfolder()