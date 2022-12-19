# An iterator class that takes a path to an ebook and iterates over the text
# in the ebook.  The ebook has to be in the epub format.

import os
import zipfile
import tempfile
from bs4 import BeautifulSoup

def iterate_over_epub(file_path: str):
    # Create a temporary directory to extract the epub to
    temp_dir = tempfile.mkdtemp()
    # Extract the epub to the temporary directory
    with zipfile.ZipFile(file_path, 'r') as epub:
        epub.extractall(temp_dir)
        for subdir, dirs, files in os.walk(temp_dir):
            for file in files:
                filepath = os.path.join(subdir, file)
                if filepath.endswith(".xhtml"):
                    print(filepath)
                    with open(filepath, "r", encoding="utf-8") as f:
                        soup = BeautifulSoup(f.read(), "lxml")
                        for text_object in soup.find_all(text=True):
                            text: str = text_object.text
                            if len(text) > 0:
                                yield text