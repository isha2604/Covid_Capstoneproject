import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import urllib 
import requests
df_covid = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vS8SzaERcKJOD_EzrtCDK1dX1zkoMochlA9iHoHg_RSw3V8bkpfk1mpw4pfL5RdtSOyx_oScsUtyXyk/pub?gid=43720681&single=true&output=csv')
df_covid.head(15)
df_covid.drop(['Date', 'Cases_AIAN','Cases_NHPI', 'Cases_Multiracial',
       'Cases_Other', 'Cases_Unknown', 'Cases_Ethnicity_Hispanic',
       'Cases_Ethnicity_NonHispanic', 'Cases_Ethnicity_Unknown' , 'Deaths_AIAN', 'Deaths_NHPI', 'Deaths_Multiracial',
       'Deaths_Other', 'Deaths_Unknown', 'Deaths_Ethnicity_Hispanic',
       'Deaths_Ethnicity_NonHispanic', 'Deaths_Ethnicity_Unknown', 'Hosp_AIAN', 'Hosp_NHPI', 'Hosp_Multiracial',
       'Hosp_Other', 'Hosp_Unknown', 'Hosp_Ethnicity_Hispanic',
       'Hosp_Ethnicity_NonHispanic', 'Hosp_Ethnicity_Unknown','Tests_AIAN', 'Tests_NHPI', 'Tests_Multiracial',
       'Tests_Other', 'Tests_Unknown', 'Tests_Ethnicity_Hispanic',
       'Tests_Ethnicity_NonHispanic', 'Tests_Ethnicity_Unknown'], axis = 1, inplace = True)
df_covid.head(15)
df_covid.columns.values
df_covid.index.values
df_covid.set_index ('State', inplace = True)
df_covid.head(15)
print(df_covid.iloc[0]) #for row 0 = AK
df_covid.sort_values(by = ['Cases_Total', 'Deaths_Total', 'Hosp_Total', 'Tests_Total'], ascending = False, axis = 0, inplace = True)
df_covid.head(15)
