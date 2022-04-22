from typing import Any
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from sympy import true

def app():
    @st.cache
    def get_data():
        return pd.read_csv('http://data.insideairbnb.com/united-states/ny/new-york-city/2021-11-02/visualisations/listings.csv')

    df = get_data()

    #st.header("Dataframe")
    st.subheader("Listing")

    #checkbox
    show_df = st.checkbox('Show Dataframe')
    if show_df:
        st.write(df)

    st.header('Q1')
    st.map(df[(df['price']>=800)][['latitude','longitude']].dropna(how='any'))
    st.write(df.query('price>=800').sort_values('price',ascending=False).head())

    st.header('Q2')
    defaultcols= ['name','host_name', 'neighbourhood', 'room_type', 'price']
    cols= st.multiselect('Columns', df.columns.tolist(), default=defaultcols)
    st.dataframe(df[cols].head(10))

    st.header('Q3')
    st.write('matplotlib')
    df_room= df.groupby(['room_type'])['price'].mean()
    plt.figure(figsize=(12,6))
    plt.bar(df_room.index, df_room)
    plt.xlabel('room_type')
    plt.ylabel('avg_price')
    plt.xticks(rotation=90)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    st.header('Q4')
    st.table(df_room.reset_index().round(2).sort_values('price', ascending=True)\
        .assign(avg_price=lambda x: x.pop('price').apply(lambda y: '%.2f' % y)))
    #visualisasi dengan plotly
    fig= px.bar(x=df_room, y=df_room.index, color= df_room.index, orientation='h',
        labels= {'y': 'room_type', 'x': 'Avg Price'}, 
        title='Avg Price by room_type')
    st.plotly_chart(fig)

    #selectbox
    st.header('Q5')
    room_type = st.selectbox('room_type',df['room_type'].unique())
    fig = px.scatter(df.query('room_type==@room_type'),x='price',
    y='number_of_reviews',color='room_type',size='price')
    st.plotly_chart(fig)

    #radio button
    st.header('Q6')
    room_type_radio = st.radio('room_type',df.room_type.unique())
    st.write(f'avg price of {room_type_radio}: {df.query("room_type==@room_type_radio")["price"].mean():.2f}')

    #slider
    values=st.slider('Price Range', float(df.price.min()),float(df.price.clip(upper=1000.).max()),(50.,300.)) #kalau mau jadi sidebar st.sidebar.slider
    f=px.histogram(df.query(f'price.between{values}'),x='price',nbins=15,title='Price Distribution')
    f.update_xaxes(title='Price')
    f.update_yaxes(title='Count')
    st.plotly_chart(f)

    st.button("Rerun")