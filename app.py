import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Titel der App
st.title('Streamlit App Josepdil')

# Daten laden
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
    data = pd.read_csv(url)
    return data

data = load_data()

# Anzeige der Daten in einer Tabelle
st.subheader('Rohdaten')
st.dataframe(data)

# Interaktive Steuerung
species = st.radio("Wählen Sie die Pinguinart", data['species'].unique())
sex = st.radio("Wählen Sie das Geschlecht", data['sex'].dropna().unique())

# Gefilterte Daten anzeigen
filtered_data = data[(data['species'] == species) & (data['sex'] == sex)]
st.subheader('Gefilterte Daten')
st.dataframe(filtered_data)

# Darstellung als Grafik
st.subheader('Darstellung als Grafik')
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_data, x='bill_length_mm', y='bill_depth_mm', hue='species', ax=ax)
plt.title(f'Bill Length vs Bill Depth für {species} ({sex})')
st.pyplot(fig)
