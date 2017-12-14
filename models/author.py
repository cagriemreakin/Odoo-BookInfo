from odoo import models, fields,api

class Author(models.Model):
    _inherit= 'res.partner'
    _name="about.author"
    is_book_author= fields.Boolean('Is Book Author',default=False)
    res_partner_id = fields.Many2one('res.partner', string="ResPartner")
