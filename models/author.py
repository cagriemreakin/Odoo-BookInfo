from odoo import models, fields,api

class Author(models.Model):
    _name='about.author'
    _inherits = {'res.partner' : 'partner_id'}
    _columns={'is_book_author':fields.Boolean('Is Book Author',default=False)
}
    partner_id = fields.Many2one('res.partner', string="Author")
    is_book_author= fields.Boolean('Is Book Author',required=True,default=False)

