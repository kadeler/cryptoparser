from os import path
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #чтение спарсенных данных с файла(файл скинут в документы т.к. у джанго
    #есть некоторые запреты на счет редактирования файлов в своей директории)
    # [0] - id обменника
    # [1] - название обменника
    # [2] - id отдаваемой валюты
    # [3] - название отдаваемой валюты
    # [4] - курс отдаваемой валюты
    # [5] - id получаемой валюты
    # [6] - название отдаваемой валюты
    # [7] - курс получаемой валюты
    # [8] - резерв
    # [9] - отзывы
    with open('C:\\Users\\admin\\Documents\\parsed.txt') as f:
        tmp = f.read()
        parsed_data = eval(tmp)
        table_data = eval(tmp)
        currencies = []
        for i in range(0,len(table_data)):
            table_data[i].pop(0)
            table_data[i].pop(0)
            table_data[i].pop(0)
            table_data[i].pop(2)
        for i in range(0,len(table_data)):
            table_data[i][1] += " " + table_data[i][0]
            table_data[i][3] += " " + table_data[i][2]
        for i in range(0, len(table_data)):
            table_data[i].pop(0)
            table_data[i].pop(1)
        for i in range(0,len(parsed_data)):
            if parsed_data[i][3] not in currencies:
                currencies.append(parsed_data[i][3])

    return render(request, 'main/index.html', context={'table_data': table_data,
                                                       'parsed_data': parsed_data,
                                                       'currencies': currencies,
                                                       'range1': range(0,100),
                                                       'range2': range(0,4)})