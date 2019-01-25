import pandas as pd
opendata = pd.read_csv('D://project_mineral/news_1_edit.csv', encoding='cp949')

dflist = list(opendata.columns)

new_data = pd.DataFrame()
new_data = opendata[['newsID (S)','createdAt (S)','nation (S)','paragraphs (L)']]
new_data.columns = ['NewsID','Date','Nation','Context']

data = new_data['Context'].values
print(str(data[0]))

pd.Series(data).to_json(orient='values')
data.tostring()
print(data[0])
print(len(str_data)) #752
