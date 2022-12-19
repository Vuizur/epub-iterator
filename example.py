from epub_iterator import iterate_over_epub


PATH = r"C:/Users/hanne/Downloads/Martin, George Raymond Richard - 1-1 - Hra o trůny.epub"

for i, text in enumerate(iterate_over_epub(PATH)):
    print(text)

    if i > 100:
        break