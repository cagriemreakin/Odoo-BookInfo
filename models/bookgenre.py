# -*- coding: utf-8 -*-
import re

from odoo import api, fields, models


class BookGenre(models.Model):

    _name = 'about.genre'
    _order = 'name asc'

    _sql_constraints = [(
        'name_uniq',
        'unique (name)',
        'Genre already exists!')
    ]

    # Model Field
    name = fields.Char('Genre', required=True)

    # Relation with Book Model
    book_id = fields.Many2one(
        'about.book',
        select=True,
        string="Book Genre"
    )
    
    # Constraints and Onchange
    # Checking the name is alphabetical
    @api.constrains('name')
    def is_valid_name(self):
        if not re.match("^[A-Za-z\s&-,]*$", self.name):
            raise models.ValidationError('Genre should be alphabetic !')

    # First letter capitalization 
    @api.onchange('name')
    def caps_name(self):
        if self.name:
            self.name = str(self.name).title()
