import zipfile
import os
#распаковка архива в отдельную папку
with zipfile.ZipFile("info.zip", 'r') as zip_ref:
    zip_ref.extractall(os.path.dirname(os.path.abspath(__file__))+"\\extracted")
#превразаем данные из файла в массив
data_to_parse = []
with open("extracted/bm_rates.dat") as f:
    for line in f:
        data_to_parse.append(line)
#переводим данные в формат:
#[0] - id обменника
#[1] - id отдаваемой валюты
#[2] - курс отдаваемой валюты
#[3] - id получаемой валюты
#[4] - курс получаемой валюты
#[5] - резерв
#[6] - отзывы
parsed_data = []
for i in range(0, len(data_to_parse)):
    data_to_parse[i] = data_to_parse[i].split(";")
    parsed_data.append([data_to_parse[i][2],
                        data_to_parse[i][0],
                        data_to_parse[i][3],
                        data_to_parse[i][1],
                        data_to_parse[i][4],
                        data_to_parse[i][5],
                        data_to_parse[i][6]])
#добавляем название обменника
#[0] - id обменника
#[1] - название обменника
#[2] - id отдаваемой валюты
#[3] - курс отдаваемой валюты
#[4] - id получаемой валюты
#[5] - курс получаемой валюты
#[6] - резерв
#[7] - отзывы
with open("extracted/bm_exch.dat") as f:
    for line in f:
        for i in range(0,len(parsed_data)):
            tmp = line
            tmp = tmp.split(';')
            if parsed_data[i][0] == tmp[0]:
                parsed_data[i].insert(1,tmp[1])
#переводим в формат
#[0] - id обменника
#[1] - название обменника
#[2] - id отдаваемой валюты
#[3] - название отдаваемой валюты
#[4] - курс отдаваемой валюты
#[5] - id получаемой валюты
#[6] - название отдаваемой валюты
#[7] - курс получаемой валюты
#[8] - резерв
#[9] - отзывы
with open("extracted/bm_cy.dat") as f:
    for line in f:
        tmp = line
        tmp = tmp.split(";")
        for i in range(0, len(parsed_data)):
            if parsed_data[i][2] == tmp[0]:
                parsed_data[i].insert(3, tmp[2])
with open("extracted/bm_cy.dat") as f:
    for line in f:
        tmp = line
        tmp = tmp.split(";")
        for i in range(0, len(parsed_data)):
            if parsed_data[i][5] == tmp[0]:
                parsed_data[i].insert(6, tmp[2])
#кэшируем результат
with open(os.path.expanduser('~\\Documents\\parsed.txt'), 'w') as f:
    f.write(str(parsed_data))