# -*- coding: utf-8 -*-
from odoo import http


class Book(http.Controller):
    @http.route('/book/book/', auth='public')
    def index(self, **kw):
        return "Book Information"

    @http.route('/book/book/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('book.listing', {
            'root': '/book/book',
            'objects': http.request.env['book.book'].search([]),
        })

    @http.route('/book/book/objects/<model("book.book"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('book.object', {
            'object': obj
        })
