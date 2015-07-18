import scrapy
from scrapy.http import FormRequest, Request
from loginform import fill_login_form
import re


class SkoobSpider(scrapy.Spider):
    name = "skoob"
    start_urls = ['http://skoob.com.br/login/']

    user = "teste@gmail.com"
    password = "senha"

    def parse(self, response):
        args, url, method = fill_login_form(
            response.url, response.body, self.user, self.password)

        return FormRequest(
            url,
            method=method,
            formdata=args,
            callback=self.after_login)

    def after_login(self, response):
        user_id = re.search("[0-9]{1,}", response.url).group(0)
        shelf_url = "http://www.skoob.com.br/estante/livros/todos/" + user_id
        return Request(shelf_url, self.get_all_books)

    def get_all_books(self, response):
        print("########")
        print(response.css('div.livro-capa').extract())
        print("########")
