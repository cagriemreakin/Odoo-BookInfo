# -*- coding: utf-8 -*-
from odoo import models, fields,api
import re

class Language(models.Model):
    
    _name='about.language'
    name = fields.Char('Language',required=True)
    language_id = fields.Many2one('about.book',  select=True,string="Book Language")
    _sql_constraints = [('name_uniq', 'unique (name)','Genre already exists!')]
    
    @api.constrains('name')
    def is_valid_name(self):
            if not re.match("^[A-Za-z]*$",self.name):
                raise models.ValidationError('Language must be alphabetic !')
    
