# -*- coding: utf-8 -*-
import re

from odoo import api, fields, models


class Language(models.Model):

    _name = 'about.language'
    _order = 'name asc'
    _sql_constraints = [(
        'name_uniq',
        'unique (name)',
        'Language already exists!')
    ]

    # Model Field
    name = fields.Char('Language', required=True)

    # Relation with Book Model
    language_id = fields.Many2one(
        'about.book',
        select=True,
        string="Book Language"
    )
    # Checking the name is alphabetical

    @api.constrains('name')
    def is_valid_name(self):
        if not re.match("^[A-Za-z]*$", self.name):
            raise models.ValidationError('Language must be alphabetic !')

    # First letter capitalization when onchange
    @api.onchange('name')
    def caps_name(self):
        if self.name:
            self.name = str(self.name).title()
