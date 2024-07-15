import streamlit as st
import streamlit.components.v1 as components

# Read the HTML file
with open("index.html", 'r', encoding='utf-8') as file:
    html_content = file.read()

# Display the HTML content
components.html(html_content, height=600)
