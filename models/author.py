from odoo import models, fields

class Author(models.Model):
    _name='about.author'
    _inherits = {'res.partner' : 'partner_id'}
    partner_id = fields.Many2one('res.partner', string="Author")
    is_book_author= fields.Boolean('Is Book Author',required=True,default=False)
