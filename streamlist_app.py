
import streamlit
import pandas as pd


streamlit.title("My parents New Healthy Diner")

streamlit.header('Beakfast Favorites')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

asw_S3_dabw = "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/"
filename = "fruit_macros.txt"

filepathname = asw_S3_dabw + filename

my_fruit_list = pd.read_csv(filepathname)

streamlit.dataframe(my_fruit_list)
