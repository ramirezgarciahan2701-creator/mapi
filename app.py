import streamlit as st
import folium
from streamlit_folium import st_folium
import requests

st.title("App de Geolocalización Satelital")
st.write("Esta aplicación utiliza servicios web para mostrar coordenadas.")

# 🌐 Obtener ubicación desde API
res = requests.get("https://ipinfo.io/json")
data = res.json()

loc = data["loc"].split(",")
lat = float(loc[0])
lon = float(loc[1])

# 🗺️ Crear mapa con ubicación real
m = folium.Map(location=[lat, lon], zoom_start=12)

# 📍 Marcador
folium.Marker(
    [lat, lon],
    popup="Ubicación detectada",
    icon=folium.Icon(color="blue")
).add_to(m)

# Renderizar
st_folium(m, width=725)
