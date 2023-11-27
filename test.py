import requests
from bs4 import BeautifulSoup
import csv
import streamlit as st
st.text('Hyi')
def fetch_bbc_news():
    url = 'https://www.bbc.com/news/world-60525350'
    response = requests.get(url)

    # Перевірте статус відповіді; 200 означає, що все гаразд
    if response.status_code != 200:
        print(f'Failed to retrieve the page with status code: {response.status_code}')
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Збір заголовків новин
    headlines = []
    for article in soup.find_all('h3'):
        headline_text = article.text.strip()
        if headline_text:  # Перевірка на наявність тексту
            headlines.append(headline_text)

    # Збереження заголовків новин у файл CSV
    with open('bbc_headlines.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Headline'])  # Заголовок стовпця
        for headline in headlines:
            writer.writerow([headline])

# Виклик функції
fetch_bbc_news()
