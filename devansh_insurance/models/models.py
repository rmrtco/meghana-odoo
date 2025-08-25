# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.osv import expression

class Vehicle(models.Model):  
    _name = 'devansh_insurance.vehicle'
    _description = 'Vehicle Details'
    
    vehicle_registration_number = fields.Char(min=6,max=36, string="Vehicle Reqistration No.", required=True)
    mobile_number=fields.Char(min=6,max=36, string="Mobile Number", required=True)
    policy_expiry_date = fields.Date(string="Policy Expiry Date")
    address = fields.Text(string="Address")
    previous_year_policy_photo = fields.Binary(string="Privious Year Policy Image",attachment=True)
    previous_year_policy_photo_filename = fields.Char(string="Privious Year Policy Image Filename")
    rc_number = fields.Char(min=6,max=36, string="RC Number", required=True)
    rc_photo = fields.Binary(string="RC Image",attachment=True)
    rc_photo_filename = fields.Char(string="RC Image Filename")
    make = fields.Char(min=6,max=255, string="Make", required=True)
    model = fields.Char(min=6,max=255, string= "Model", required=True)
    idv = fields.Char(min=6,max=255, string="IDV")
    invoice_date = fields.Date(string="Invoice Date")
    chassis_no = fields.Char(min=10, max=255, string="Chassis Number", required=True)
    engine_no = fields.Char(min=10, max=255, string="Engine Number", required=True)
    policy_from = fields.Date(string="Policy From")
    policy_till = fields.Date(string="Policy Up To")
    owner_id = fields.Many2one('res.partner', string='Owner')
    inspection_photo_1 = fields.Binary(string="Inspection photo 1",attachment=True)
    inspection_photo_1_filename = fields.Char(string="Inspection photo 1 Filename")
    inspection_photo_2 = fields.Binary(string="Inspection photo 2",attachment=True)
    inspection_photo_2_filename = fields.Char(string="RInspection photo 2 Filename")
    inspection_photo_3 = fields.Binary(string="Inspection photo 3",attachment=True)
    inspection_photo_3_filename = fields.Char(string="Inspection photo 3 Filename")
    inspection_photo_4 = fields.Binary(string="Inspection photo 4",attachment=True)
    inspection_photo_4_filename = fields.Char(string="Inspection photo 4 Filename")
    inspection_photo_5 = fields.Binary(string="Inspection photo 5",attachment=True)
    inspection_photo_5_filename = fields.Char(string="Inspection photo 5 Filename")
    inspection_photo_6 = fields.Binary(string="Inspection photo 6",attachment=True)
    inspection_photo_6_filename = fields.Char(string="Inspection photo 6 Filename")
    inspection_photo_7 = fields.Binary(string="Inspection photo 7",attachment=True)
    inspection_photo_7_filename = fields.Char(string="Inspection photo 7 Filename")
    inspection_photo_8 = fields.Binary(string="Inspection photo 8",attachment=True)
    inspection_photo_8_filename = fields.Char(string="Inspection photo 8 Filename")


    def action_download_image(self):
        field_name = self.env.context.get("field_name")
        if not field_name:
            raise UserError("No field name provided!")

        binary_data = getattr(self, field_name, False)
        if not binary_data:
            raise UserError("No image found in field %s" % field_name)

        # return a binary download action
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s/%s/%s?download=true' % (
                self._name, self.id, field_name
            ),
            'target': 'self',
        }

    

class ResPartner(models.Model):
    _inherit = 'res.partner'

    pan_number = fields.Char(min=6,max=12, string="Pan Number")
    aadhaar_number = fields.Char(min=12,max=12, string="Adhaar Number")
    vehicle_ids = fields.One2many('devansh_insurance.vehicle', 'owner_id', string='Vehicles')
    aadhar_card_image = fields.Binary(string="Aadhar Card Image",attachment=True)
    aadhar_card_image_filename = fields.Char(string="Aadhar Card Image Filename")
    pan_card_image = fields.Binary(string="Pan Card Image",attachment=True)
    pan_card_image_filename = fields.Char(string="Pan Card Image Filename")

    def action_download_image(self):
        return {
            'type': 'ir.actions.act_url',
            'url': f"/web/content/{self._name}/{self.id}/image_1920?download=true",
            'target': 'self',
        }

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
    
