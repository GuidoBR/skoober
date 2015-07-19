import scrapy
from scrapy.http import FormRequest, Request
from loginform import fill_login_form
import re


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

    def parse(self, response):
        args, url, method = fill_login_form(
            response.url, response.body, self.user, self.password)

        return FormRequest(
            url,
            method=method,
            formdata=args,
            callback=self._after_login)

    def _get_user_id(self, user_url):
        """Return the user id
        user_url = "http://www.skoob.com.br/usuario/000000-username"
        return 000000
        """
        return re.search("[0-9]{1,}", user_url).group(0)

    def _after_login(self, response):
        shelf_url = "http://www.skoob.com.br/estante/livros/todos/"
        shelf_user_url = shelf_url + self._get_user_id(response.url)
        return Request(shelf_user_url, self.get_all_books)

    def get_all_books(self, response):
        print("########")
        print(response.css('div.livro-capa').extract())
        print("########")
