import streamlit
import pandas
import requests

streamlit.title('🧇 My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick Some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruitvice Fruit Advice!')
fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

fruitvice_normalized = pandas.json_normalize(fruitvice_response.json())
streamlit.dataframe(fruitvice_normalized)
