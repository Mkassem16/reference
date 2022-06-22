from this import d
from typing import Dict
import pandas as pd

people = {
    'first_name': ['Mohamed', 'Alicia'],
    'last_name': ['Kassem', 'Maillet']
}

df = pd.DataFrame(people)
df.columns
#select
df['first_name']
df.first_name
df[['first_name', 'last_name']]
#filter
df.loc[1]
df.loc[0:1, 'first_name']
df.iloc[1]
df.iloc[0:2]
df.iloc[[0,1], [0,1]]

df = pd.read_csv('data.csv')
schema_df = pd.read_csv('schema.csv')

df.shape
sorted(df.columns)
df['Age']
df.loc[0:30, ['Age']]
df.iloc[0:30, [1,3,5]]
df.Age.value_counts()
df.loc[0:10, 'MainBranch': 'Ethnicity'].columns




#indexing
people = {
    'first_name': ['Mohamed', 'Alicia'],
    'last_name': ['Kassem', 'Maillet']
}

df = pd.DataFrame(people)
df.set_index('first_name', inplace=True)
df.loc['Alicia']
df.iloc[0]
df = pd.read_csv('data.csv', index_col='ResponseId')
df2 = pd.read_csv('schema.csv', index_col='qname').sort_index()
df2.loc['Employment', 'question']


##filtering
df = pd.read_csv('data.csv')
df[df['Age']=='25-34 years old']['SurveyEase']
df.loc[df['Age']=='25-34 years old', 'SurveyEase']
mask = (df['Age']=='25-34 years old') | (df['Age']=='18-24 years old')
df.loc[~mask, ['MainBranch', 'Country']]
countries = ['United States of America', 'Israel', 'Norway']
mask = df['Country'].isin(countries)
df.loc[mask, 'Country'].value_counts()
mask = df['LanguageHaveWorkedWith'].str.contains('python|Python', na=False, regex=True)
df.loc[mask, 'SurveyEase']

#columns
df.columns =[column.upper() for column in df.columns]
df.columns = df.columns.str.replace('WITH', 'W/')
df.rename(columns={'UK_COUNTRY': 'UK_COUNTRY1'}, inplace=True)
df['NewColumn'] =df['Age'] +" born in "+df['Country']
df.drop(columns={'Age', 'Country'}, inplace=True)
df['MentalHealth'].str.split(expand=False)
#rows
df.loc[2, 'TRANS'] = 'Yes'
df['UK_COUNTRY1'] = df['UK_COUNTRY1'].str.upper()
df['UK_COUNTRY_len'] = df['UK_COUNTRY1'].str.len()
df['UK_COUNTRY_count'] = df['UK_COUNTRY1'].str.count('ENG')

def update_str(string):
    return str(string).upper()

df['Trans2'] = df.apply(lambda row: row['Trans'] if row['Trans'] in ['Yes', 'No'] else 'Other', axis=1)

df['Trans3'] = df.apply(lambda row: row['Trans'] if row['Trans']=='Yes' else 'No Other' if row['Trans'] == 'No' else 'Other' , axis=1)

df['Trans3'] = df.apply(lambda row: str(row['Trans']).lower(), axis=1)

df['Trans3'] = df.apply(lambda row: update_str(row['Trans']), axis=1)

df['Trans4'] = df['Trans3'].map({'NO': 'False', 'YES': 'True'}, na_action='ignore')

df['Trans4'] = df['Trans3'].replace({'PREFER NOT TO SAY|prefer not to say':'Others', 'NO': 'False', 'YES': 'True'}, regex=True)

df2 = df.iloc[700:800]
df3 = df.iloc[900:950]
df4 = df2.append(df3, ignore_index=True)
df.sort_values(by=['NewColumn', 'MainBranch'], ascending=[False, True], inplace=True)

df['ResponseId'].nlargest(10)
df.nlargest(10, 'ResponseId')
df.nsmallest(10, 'ResponseId')

# grouping
df['Age'].value_counts(normalize=True)
df['Country'].value_counts(normalize=True)*100
country_group = df.groupby('Country')
country_group.get_group('India')
mask = df['Country'] == 'Egypt'
filtered = df.loc[mask, 'Trans']
filtered.value_counts()

column_name = 'Trans'
variable_name = 'Egypt'

def get_distribution(groupby=None, distribution_of=None, group=None, df=None) -> pd.DataFrame :
    """
    This function returns a sorted dataframe of distributions depending on the input
    arguments. 
    group argument is optional. if given results will be filtered accordingly. 
    """
    country_group = df.groupby(groupby)
    if group is not None:
        df = country_group[distribution_of].value_counts(normalize=True).sort_values(ascending=False)[group]*100
    else:
        df = country_group[distribution_of].value_counts(normalize=True).sort_values(ascending=False)*100
    return df



get_distribution(groupby='Country', distribution_of='Age', group='Canada', df=df)
get_distribution(groupby='Country', distribution_of='Trans', df=df)


country_group = df.groupby('Country')
country_group['CompTotal'].median().sort_values(ascending=False)['Germany']
country_group['CompTotal'].agg(['median', 'mean', 'max']).sort_values('mean', ascending=False).loc['Germany']

mask = df['Country'] == 'Egypt'
result = df.loc[mask]['LanguageHaveWorkedWith'].str.contains('python|Python', regex=True).value_counts(ascending=False, normalize=True)*100
result[True]


def get_langugage_usage(df: pd.DataFrame = None,
 country: str = None, pattern: str = None, regex: bool = True) -> int:
    country_group = df.groupby('Country')
    count = country_group['LanguageHaveWorkedWith'].apply(lambda x: x.str.contains(pattern, regex=regex))
    return count.drop_na()

get_langugage_usage(df, pattern="java|Java", regex=True)

count = country_group['LanguageHaveWorkedWith'].apply(lambda x: x.str.contains("java|Java", regex=True)).count()

country_group = df.groupby(['Country', 'LanguageHaveWorkedWith']).sum().pivot(columns=['Country', 'LanguageHaveWorkedWith'])

country_group['CompTotal'].sum()
