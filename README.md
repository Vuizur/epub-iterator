# Epub Iterator

A simple library iterating over a the text of an epub ebook.

### Usage

```python
from epub_iterator import iterate_over_epub


EBOOK_PATH = r"Hra o trůny.epub"

for text in iterate_over_epub(EBOOK_PATH):
    print(text) # This will print each paragraph of the ebook. 

```