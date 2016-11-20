import requests
import json

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


def main(user_id):
    json_books = (get_books(user_id))
    save_json(json_books)
    books = books_title(json_books)

    print("Total de livros: {} - Livros mais recentes: {}".format(len(books), books[0:5]))

if __name__ == "__main__":
    import sys
    argumentos = sys.argv
    
    main(argumentos[1])
