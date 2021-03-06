# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Book(models.Model):

    _name = 'about.book'
    _description = 'Book Information'
    _order = 'publication_date desc'

    _sql_constraints = [(
        'isbn_uniq',
        'unique (isbn)',
        'ISBN already exists!')
    ]

    # Model Fields
    isbn = fields.Char(
        'ISBN',
        required=True
    )

    name = fields.Char(
        'Title',
        required=True
    )

    publication_date = fields.Date(
        'Publication Date'
    )

    """ Relations with Other Models"""

    # Relation with Author Model
    author_ids = fields.Many2many(
        'about.author',
        select=True,
        required=True,
        string='Authors',
        domain=[('is_book_author', '=', True)]
    )

    # Relation with Publisher Model
    publisher_ids = fields.Many2many(
        'about.publisher',
        select=True,
        string='Publishers',
        domain=[('is_book_publisher', '=', True)]
    )

    # Relation with Genre Model
    genre_id = fields.One2many(
        'about.genre',
        'book_id',
        select=True,
        required=True,
        string="Genres"
    )

    # Relation with Language Model
    language_id = fields.One2many(
        'about.language',
        'book_id',
        select=True,
        required=True,
        string="Language"
    )
    
    # Constraints and onchange
    @api.constrains('publication_date')
    def _check_publication_date(self):
        for r in self:
            if (r.publication_date > fields.Date.today()):
                raise models.ValidationError(
                    'Publication date must be in the past !')
            if (r.publication_date == False):
                raise models.ValidationError('Date must not be empty!')

    @api.constrains('author_ids')
    def has_author(self):
        for r in self:
            if r.author_ids == False:
                raise models.ValidationError(
                    'Book must have at least 1 author!')
    # First letter capitalization 
    @api.onchange('name')
    def caps_name(self):
        if self.name:
            self.name = str(self.name).title()
