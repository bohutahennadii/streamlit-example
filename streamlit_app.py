import streamlit as st
import requests
from bs4 import BeautifulSoup
st.text('XIY')
url = st.text_input('Enter url')
st.text(url)
def fetch_bbc_news():
    response = requests.get(url)

    # Перевірте статус відповіді; 200 означає, що все гаразд
    if response.status_code != 200:
        print(f'Failed to retrieve the page with status code: {response.status_code}')
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Збір заголовків новин
    headlines = []
    for article in soup.find_all('h6'):
        headline_text = article.text.strip()
        if headline_text:  # Перевірка на наявність тексту
            headlines.append(headline_text)
    # Збереження заголовків новин у файл CSV
    with open('bbc_headlines.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Headline'])  # Заголовок стовпця
        for headline in headlines:
            writer.writerow([headline])
fetch_bbc_news()
st.text(healines)
