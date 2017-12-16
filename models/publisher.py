# -*- coding: utf-8 -*-
from odoo import fields, models


class Publisher(models.Model):

    _name = 'about.publisher'
    _inherits = {'res.partner': 'partner_id'}
    _order = 'name asc'

    # Model Fields
    is_book_publisher = fields.Boolean(
        'Is Book Publisher',
        required=True,
        default=False
    )

    # Relation with res.partner
    partner_id = fields.Many2one(
        'res.partner',
        string="Publisher"
    )
