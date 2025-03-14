import pandas as pd
#import openpyxl as pl
import plotly.express as px
import streamlit as st

df = pd.read_excel(r'C:\Users\julio.rubem\Desktop\PyCharm 2024.3.4\Amostras_Recebidas2.xlsx')

escolha = st.multiselect('Filtro:', df['Data'],)
escolha2 = st.multiselect('Filtro:', df['Contratante'],)
df2 = df[(df['Data'].isin(escolha)) | (df['Contratante'].isin(escolha2))]

if  df2.empty:
    fig = px.histogram(df,
                       y='Contratante',
                       text_auto=True,
                       color_discrete_sequence=['#09124F'],
                       template='simple_white',
                       )
    fig.update_yaxes(categoryorder='total ascending')
    st.plotly_chart(fig)


else:
    fig = px.histogram(df2,
                   y = 'Contratante',
                   text_auto=True,
                   color_discrete_sequence=['#09124F'],
                   template = 'simple_white',
                  )
    fig.update_yaxes(categoryorder = 'total ascending')
    st.plotly_chart(fig)




