import pandas as pd
data = pd.read_csv(r"C:\Users\Ivan\PycharmProjects\scrapy_my\tutorial\file.csv")
print(int(data.get('description').count()/max(data.count())*100),'% - description')
print((data['region']) , "all description")
count_fr = 0
count_it = 0
count_us = 0
count_nl = 0
count_be = 0
count_nl_nl = 0
count_es = 0
count_de = 0
for i in data['region']:
    if i == 'fr_fr':
        count_fr += 1
    elif i == 'it_it':
        count_it += 1
    elif i == 'en_us':
        count_us += 1
    elif i == 'nl_be':
        count_nl += 1
    elif i == 'fr_be':
        count_be += 1
    elif i == 'nl_nl':
        count_nl_nl += 1
    elif i == 'es_es':
        count_es += 1
    elif i == 'de_de':
        count_de += 1
item = {'es_es':count_es,'fr_fr':count_fr, 'it_it':count_it, 'en_us':count_us, 'nl_be':count_nl, 'nl_nl':count_nl_nl, 'de_de':count_de, 'fr_be':count_be}
print(item)