from odoo import models, fields,osv

class Author(models.Model):
    _inherit= 'res.partner'
    _name="res.partner"
    book_id = fields.Many2many('about.book',string='Books')
    #res_partner_id = fields.Many2one('res.partner', string="ResPartner")
    is_book_author= fields.Boolean('Is Book Author',required=True,default=False)

