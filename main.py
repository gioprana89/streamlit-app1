import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

import plotly.graph_objects as go

import plotly.express as px


st.markdown("<h2 style='text-align: center; color: blue;'>VISUALISASI DATA DENGAN PYTHON-STREAMLIT (GRAFIK BATANG)<br><br></h5>", unsafe_allow_html=True)

left_co, cent_co,last_co = st.columns(3)
with cent_co:
 st.image("ugi.jpg", caption='', width = 350)


 st.image("gambar.png", caption='', width = 450)



st.write("<br><br><br><br>", unsafe_allow_html=True)

df = pd.DataFrame(
    {
         "Label": ["A", "B", "C"],
                  "Angka": [12, 8, 5],
                  "Warna": ["red", "pink", "yellow"]
    }
)


config = {
    'Label' : st.column_config.TextColumn('Label'),
    'Angka' : st.column_config.NumberColumn('Angka'),
    'Warna' : st.column_config.TextColumn('Warna')
}


col1, col2 = st.columns([1, 3])


Height_Bar = col1.slider('Height', 0, 1000, 600)

Width_Bar = col1.slider('Width', 0, 1000, 600)

result = st.data_editor(df, column_config = config, num_rows='dynamic')


variabel_label = result['Label']
variabel_label = variabel_label.to_numpy()


variabel_angka = result['Angka']
variabel_angka = variabel_angka.to_numpy()

variabel_warna = result['Warna']
variabel_warna = variabel_warna.to_numpy()

if st.button('Button'):
 fig = go.Figure(
  
   go.Bar(x = variabel_label, y = variabel_angka, marker_color = variabel_warna),
   go.Layout(height = Height_Bar, width = Width_Bar)

  )
 st.plotly_chart(fig, theme=None)

