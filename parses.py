import pandas as pd
data = pd.read_csv(r"C:\Users\Ivan\PycharmProjects\scrapy_my\tutorial\file.csv")
print(max(data.count()))
print(int(data.get('description').count()/max(data.count())*100),'% - description')
print(data.get('description').count() , "all description")