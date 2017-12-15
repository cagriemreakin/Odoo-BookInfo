# -*- coding: utf-8 -*-
from odoo import models, fields,api

class Author(models.Model):
    _name='about.author'
    _inherits = {'res.partner' : 'partner_id'}
    partner_id = fields.Many2one('res.partner', string="Author")
    is_book_author= fields.Boolean('Is Book Author',required=True,default=False)

    @api.multi
    def unlink(self):
        """when delete author we should delete his books"""
        books = self.env['about.book'].search([('author_ids', 'in', self.ids)])
        if books:
            books.unlink()

        return super(Author, self).unlink()