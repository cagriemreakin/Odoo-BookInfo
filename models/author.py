# -*- coding: utf-8 -*-
from odoo import api, fields, models,exceptions

class Author(models.Model):

    _name = 'about.author'
    _inherits = {'res.partner': 'partner_id'}
    _order = 'name asc'

    # Field
    is_book_author = fields.Boolean(
        'Is Book Author',
        required=True,
        default=False
    )

    # Relation with res.partner
    partner_id = fields.Many2one(
        'res.partner',
        string="Author"
    )

    @api.multi
    def unlink(self):
        book = self.env['about.book']
        book_ids = book.search([('author_ids', 'in', self.ids)]) 
        if book_ids:
            raise exceptions.Warning("You are trying to delete an Author who is still referenced!")
        return super(Author, self).unlink()
