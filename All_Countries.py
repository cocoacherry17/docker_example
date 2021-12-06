import pandas as pd
df=pd.read_csv('All_Countries.csv')

while True:
    Country=input("")
    if Country in df.Country.values:
        print(Country+ " means " +df.loc[df['Country'] == Country, 'English translation of name/etymology'].iloc[0])
        print('Type in another country')
    elif Country == 'Exit':
        break
    else:
        print("Sorry that country is not in the dataset, try again") 