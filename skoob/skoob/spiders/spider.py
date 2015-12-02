import scrapy
import json
from scrapy.selector import Selector
from selenium import webdriver


class SkoobSpider(scrapy.Spider):

    name = "skoob"
    start_urls = ['http://skoob.com.br/login/']

    def __init__(self, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('No username and password provided')
        if isinstance(kwargs, type({})) and args:
            kwargs = args[0]

        super(SkoobSpider, self).__init__(*args, **kwargs)
        self.user = kwargs.get('user')
        self.password = kwargs.get('password')
        self.browser = webdriver.Firefox()

    def parse(self, response):
        self._login_page(response)
        self._navigate_to_bookcase()
        books = self._get_all_books()
        print('{} Books found'.format(len(books)))
        with open('books.json', 'w') as book_file:
            book_file.write(json.dumps(books))
        print('Books.json generated')

    def _login_page(self, response):
        self.browser.get(response.url)
        login = self.browser.find_element_by_id("UsuarioEmail")
        login.send_keys(self.user)
        password = self.browser.find_element_by_id("UsuarioSenha")
        password.send_keys(self.password)
        password.submit()

    def _navigate_to_bookcase(self):
        self.browser.find_element_by_id("topo-menu-conta").click()
        self.browser.find_element_by_css_selector("#topo-menu-conta-hover > li:nth-child(2) > a:nth-child(1)").click()
        self.browser.find_element_by_css_selector("a.bt_est:nth-child(2)").click()

    def _get_total_books(self):
        return int(self.browser.find_element_by_css_selector(".blistaon > span:nth-child(1)").text)

    def _get_all_books(self):
        total_books = self._get_total_books()
        books = []
        while (len(books) < total_books):
            books.extend(self._extract_books_from_page())
            self.browser.find_element_by_css_selector('#corpo > div:nth-child(2) > div:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(8) > a:nth-child(1)').click()
        return books

    def _extract_books_from_page(self):
        content = self.browser.page_source
        books_from_page = Selector(text=content).css('.estante-livros-vertical')
        books_info = []
        for book in books_from_page:
            books_info.append({
                'title': book.css('.livro-conteudo').css('h3').extract(),
                'content': book.css('.livro-conteudo').css('p').extract()
            })
        return books_info

    def goodreads_header():
        return [
            'Book Id',
            'Title',
            'Author',
            'Author l-f',
            'Additional Authors',
            'ISBN',
            'ISBN13',
            'My Rating',
            'Average Rating',
            'Publisher',
            'Binding',
            'Number of Pages',
            'Year Published',
            'Original Publication Year',
            'Date Read',
            'Date Added',
            'Bookshelves',
            'Bookshelves with positions',
            'Exclusive Shelf',
            'My Review',
            'Spoiler',
            'Private Notes',
            'Read Count',
            'Recommended For',
            'Recommended By',
            'Owned Copies',
            'Original Purchase Date',
            'Original Purchase Location',
            'Condition',
            'Condition Description',
            'BCID'
        ]
