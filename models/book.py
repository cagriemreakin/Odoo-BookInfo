# -*- coding: utf-8 -*-
from odoo import models, fields,api

class Book(models.Model):
    _name = 'about.book'
    _description = 'Book Information'
    _order = 'publication_date desc, name'
    isbn = fields.Char('ISBN',required=True)
    name = fields.Char('Title', required=True)
    publication_date = fields.Date('Publication Date')
    author_ids = fields.Many2many('about.author', select=True, required=True,string='Authors')
    _sql_constraints = [('isbn_uniq', 'unique (isbn)','ISBN already exists!')]
    book_genre = fields.One2many('about.genre', 'genre_id',select=True,required=True, string="Genres")
    
    
    @api.constrains('publication_date')
    def _check_publication_date(self):
        for r in self:
            if (r.publication_date > fields.Date.today()):
                raise models.ValidationError('Publication date must be in the past !')
            if (r.publication_date == False):
                raise models.ValidationError('Date must not be empty!')
    @api.constrains('author_ids')    
    def has_author(self):
        for r in self:
            if r.author_ids == False:
                raise models.ValidationError('Book must have at least 1 author!')
    
    @api.one
    def unlink(self):
        rule = self.env['about.book']
        if rule.search([('author_ids', '!=', False)]):
            pass
        return super(Book,self).unlink()
