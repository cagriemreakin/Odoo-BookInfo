# -*- coding: utf-8 -*-
from odoo import models, fields

class Publisher(models.Model):
    
    _name='about.publisher'
    
    _inherits = {'res.partner' : 'partner_id'}
    
    partner_id = fields.Many2one('res.partner', string="Publisher")
    
    is_book_publisher= fields.Boolean('Is Book Publisher',required=True,default=False)
