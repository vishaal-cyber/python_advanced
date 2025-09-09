import xml.etree.ElementTree as ET
import xml.dom.minidom

# Parsing XML Data
def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for book in root.findall('book'):
        title = book.find('title').text
        author = book.find('author').text
        year = book.find('year').text
        price = book.find('price').text

        genres = [genre.text          for genre in book.find('genres').findall('genre')]

        # genres = []
        # for genre in book.find('genres').findall('genre'):
        #     genres.append(genre.text)


        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Year: {year}")
        print(f"Price: {price}")
        print(f"Genres: {', '.join(genres)}\n")

# Adding New Book
def add_new_book(file_path, new_book_data):
    tree = ET.parse(file_path)
    root = tree.getroot()

    new_book = ET.Element('book')
    ET.SubElement(new_book, 'title').text = new_book_data['title']
    ET.SubElement(new_book, 'author').text = new_book_data['author']
    ET.SubElement(new_book, 'year').text = str(new_book_data['year'])
    ET.SubElement(new_book, 'price').text = str(new_book_data['price'])
    
    genres = ET.SubElement(new_book, 'genres')
    ET.SubElement(genres, 'genre').text = new_book_data['genre']

    root.append(new_book)

    # Convert the updated tree to a string
    xml_str = ET.tostring(root, encoding='unicode')
    print(xml_str)

    # Pretty-print the XML string
    xml_pretty_str = xml.dom.minidom.parseString(xml_str).toprettyxml(indent="    ")

    # Remove extra newlines
    xml_pretty_str = "\n".join([line for line in xml_pretty_str.split('\n') if line.strip()])
    print(xml_pretty_str)

    # Write the pretty-printed XML string to the file
    with open('updated_data.xml', 'w', encoding='utf-8') as f:
        f.write(xml_pretty_str)

if __name__ == "__main__":
    # Path to the XML file
    xml_file_path = '025B_data.xml'
    
    # Parsing the XML file and printing the contents
    parse_xml(xml_file_path)
    
    # New book data to be added
    new_book = {
        'title': 'Python Programming',
        'author': 'Guido van Rossum',
        'year': 2022,
        'price': 39.99,
        'genre': 'Programming'
    }
    
    # Adding the new book and writing to a new file
    add_new_book(xml_file_path, new_book)
