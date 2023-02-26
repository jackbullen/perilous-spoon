import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

# Open the EPUB file
book = epub.read_epub('benko.epub')

# Iterate through each chapter and extract the text
text = ''
for item in book.get_items():
    # Check if the item is a chapter
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        # Extract the text from the chapter
        soup = BeautifulSoup(item.get_content(), 'html.parser')
        chapter_text = soup.get_text()
        text += chapter_text
# print(text)
# Save the text to a pgn file
with open('benko.pgn', 'w', encoding='utf-8') as f:
    f.write(text)
