import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Cartoon API",
    page_icon="🎬"
)

st.title("🎬 Cartoon API Explorer")
st.write("FastAPI + Streamlit Practice Project")

st.divider()

st.subheader("GET APIs")

col1, col2, col3 = st.columns(3)

def get_character(endpoint):
    response = requests.get(f"{API_URL}{endpoint}")

    if response.status_code == 200:
        return response.json()

    return {
        "error": response.text,
        "status_code": response.status_code
    }


with col1:
    if st.button("😎 Shinchan"):
        data = get_character("/apna_product")
        st.json(data)

with col2:
    if st.button("🤖 Doraemon"):
        data = get_character("/doraemon")
        st.json(data)

with col3:
    if st.button("👽 Ben 10"):
        data = get_character("/ben10")
        st.json(data)


st.divider()

if st.button("📋 Get All Characters"):
    data = get_character("/characters")
    st.json(data)


st.divider()

st.subheader("POST API")

name = st.text_input("Character Name")
age = st.number_input("Age", min_value=0, max_value=100, value=5)
show = st.text_input("Show Name")

if st.button("➕ Add Character"):

    payload = {
        "name": name,
        "age": age,
        "show": show
    }

    response = requests.post(
        f"{API_URL}/character",
        json=payload
    )

    st.write("Status Code:", response.status_code)
    st.json(response.json())