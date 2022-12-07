import requests
from bs4 import BeautifulSoup
import nltk

# URL of the BBC website
url = "https://bbc.com/"

# Fetch the HTML content of the webpage
response = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract the text of the articles on the page
article_text = ""
for article in soup.find_all("article"):
    article_text += article.text
    print(article_text)

# Tokenize the text into words
tokens = nltk.word_tokenize(article_text)

# Simplify the text using rules or other techniques
simplified_text = ""
for token in tokens:
    # Apply simplification rules here, such as shortening sentences or reducing complexity
    simplified_text += token + " "

# Print the simplified text
print(simplified_text)
