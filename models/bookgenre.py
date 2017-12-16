# -*- coding: utf-8 -*-
from odoo import models, fields,api
import re

class BookGenre(models.Model):
    
    _name='about.genre'
    
    #Model Field
    name = fields.Char('Genre',required=True)
    
    _sql_constraints = [(
        'name_uniq', 
        'unique (name)',
        'Genre already exists!')
    ]
    
    #Relation with Book Model
    genre_id = fields.Many2one(
        'about.book',  
        select=True,
        string="Book Genre"
    )
    

    
    #First letter capitalization when onchange
    @api.onchange('name')
    def caps_name(self):
        if self.name :
            self.name = str(self.name).title()
    
    #Checking the name is alphabetical        
    @api.constrains('name')
    def is_valid_name(self):
            if not re.match("^[A-Za-z\s&-]*$",self.name):
                raise models.ValidationError('Genre should be alphabetic !')
    
