# -*- coding: utf-8 -*-
from odoo import models, fields,api

class Book(models.Model):
    _name = 'about.book'
    _description = 'Book Information'
    _order = 'publication_date desc, name'
    isbn = fields.Char('ISBN',required=True)
    name = fields.Char('Title', required=True)
    publication_date = fields.Date('Publication Date')
    author_ids = fields.Many2many('res.partner',string='Authors')
    _sql_constraints = [('isbn_uniq', 'unique (isbn)','ISBN already exists!')]

    @api.constrains('publication_date')
    def _check_publication_date(self):
        for r in self:
            if r.publication_date > fields.Date.today():
                raise models.ValidationError('Publication date must be in the past !')
    
