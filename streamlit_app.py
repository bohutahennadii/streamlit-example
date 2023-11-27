import requests
from bs4 import BeautifulSoup
import csv
import streamlit as st

url = st.text_input('Enter url')
response = requests.get(url)

# Перевірте статус відповіді; 200 означає, що все гаразд
  if response.status_code != 200:
    st.text(f'Failed to retrieve the page with status code: {response.status_code}')
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
# Ім'я CSV-файлу
csv_filename = 'bbc_headlines.csv'

# Змінна для збереження вмісту файлу
english_text = ''

# Відкриваємо CSV-файл для читання
with open(csv_filename, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Ітеруємося через рядки CSV-файлу та додаємо їх до змінної text
    for row in reader:
        english_text += ', '.join(row) + '\n'

# Виводимо вміст
st.text(headlines)
