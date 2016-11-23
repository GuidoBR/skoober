import requests
import json
import csv

BASE_URL = "https://www.skoob.com.br"

def get_books(user_id):
    api = "{}/{}/{}".format(BASE_URL, "v1/bookcase/books", user_id)
    print("Request to {}".format(api))

    user = requests.get(api)
    total = user.json().get("paging").get("total")
    total_api = "{}/shelf_id:0/page:1/limit:{}".format(api, total)

    books_json = requests.get(total_api).json().get("response")
    return books_json

def books_title(books_json):
    return [book.get("edicao").get("titulo")
            for book in books_json]


def save_json(data, filename="skoob.json"):
    with open(filename, 'w') as output:
        json.dump(data, output)


def save_csv(data, filename="skoob.csv"):
    header = ["Title", "Author", "ISBN", "My Rating", "Average Rating", 
            "Publisher", "Binding", "Year Published", "Original Publication Year",
            "Date Read", "Date Added", "Bookshelves", "My Review"]

    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for book in data:
            writer.writerow(book)



def export_to_goodreads(data):
    books = []
    for book in data:
        b = book['edicao']
        goodread_book = [b['titulo'], b['autor'], b['isbn'], 0, 0, b['editora'], '', b['ano'], '', '', '', '', '']
        books.append(goodread_book)

    return books


def main(user_id):
    json_books = (get_books(user_id))
    csv_books = export_to_goodreads(json_books)
    save_csv(csv_books)

if __name__ == "__main__":
    import sys
    argumentos = sys.argv
    
    main(argumentos[1])
