# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.osv import expression

class Vehicle(models.Model):  
    _name = 'devansh_insurance.vehicle'
    _description = 'Vehicle Details'
    
    make = fields.Char(min=6,max=255, string="Make", required=True)
    model = fields.Char(min=6,max=255, string= "Model", required=True)
    idv = fields.Char(min=6,max=255, string="IDV", required=True)
    invoice_date = fields.Date(string="Invoice Date", required=True)
    chassis_no = fields.Char(min=10, max=255, string="Chassis Number", required=True)
    engine_no = fields.Char(min=10, max=255, string="Engine Number", required=True)
    policy_from = fields.Date(string="Policy From", required=True)
    policy_till = fields.Date(string="Policy Up To", required=True)
    owner_id = fields.Many2one('res.partner', string='Owner', required=True)

    

class ResPartner(models.Model):
    _inherit = 'res.partner'

    pan_number = fields.Char(min=6,max=12, string="Pan Number")
    aadhaar_number = fields.Char(min=12,max=12, string="Adhaar Number")
    vehicle_ids = fields.One2many('devansh_insurance.vehicle', 'owner_id', string='Vehicles')

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []

        if name:
            domain = expression.OR([
                [('name', operator, name)],
                [('phone', operator, name)],
                [('mobile', operator, name)],
            ])
        else:
            domain = []

        return self.search(expression.AND([domain, args]), limit=limit).name_get()
    
