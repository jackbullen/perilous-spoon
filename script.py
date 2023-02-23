import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

# Open the EPUB file
book = epub.read_epub('kann.epub')

# Iterate through each chapter and extract the text
text = ''
for item in book.get_items():
    # Check if the item is a chapter
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        # Extract the text from the chapter
        soup = BeautifulSoup(item.get_content(), 'html.parser')
        chapter_text = soup.get_text().replace('*', '\n\n')
        text += chapter_text

# Save the text to a pgn file
with open('kann.pgn', 'w', encoding='utf-8') as f:
    f.write(text)
