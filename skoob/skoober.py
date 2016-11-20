import requests

BASE_URL = "https://www.skoob.com.br"

def get_books(user_id):
    api = "{}/{}/{}".format(BASE_URL, "v1/bookcase/books", user_id)
    print("Request to {}".format(api))

    user = requests.get(api)
    total = user.json().get("paging").get("total")
    total_api = "{}/shelf_id:0/page:1/limit:{}".format(api, total)

    json = requests.get(total_api).json()
    livros = [livro.get("edicao").get("titulo") for livro in json.get("response")]
    return livros 


def main(user_id):
    print(get_books(user_id))

if __name__ == "__main__":
    import sys
    argumentos = sys.argv
    
    main(argumentos[1])
