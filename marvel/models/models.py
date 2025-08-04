# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.osv import expression

class QueueItem(models.Model):
    _name = 'marvel.queue.item'
    _description = 'Queue Item'

    flow_name = fields.Char(required=True)
    create_date = fields.Datetime(required=True, default=fields.Datetime.now)
    closed_date = fields.Datetime()
    created_by = fields.Many2one('res.users', string='Created By')
    is_clossed = fields.Boolean(default=False, required=True)
    is_deleted = fields.Boolean(default=False, required=True)
    priority = fields.Integer(default=3, required=True)
    fields_data = fields.Json(string='Fields')
    
    statuses_ids = fields.One2many('marvel.queue.status', 'token_id', string='Statuses')


class QueueStatus(models.Model):
    _name = 'marvel.queue.status'
    _description = 'Queue Status'

    status = fields.Char(default='initial', required=True)
    token_id = fields.Many2one('marvel.queue.item', string="Queue Item")
    owner = fields.Many2one('res.users', string='Owner')
    previous_owner = fields.Many2one('res.users', string='Previous Owner')
    start_time = fields.Datetime(required=True, default=fields.Datetime.now)
    end_time = fields.Datetime()
    is_current = fields.Boolean(default=True, required=True)
    prossesing_stage = fields.Char(default='initial')
    notes = fields.Text()
    is_deleted = fields.Boolean(default=False, required=True)
    escalated = fields.Boolean(default=False, required=True)
    reopen_count = fields.Integer(default=0, required=True)


class BlockedAttributeValue(models.Model):
    _name = 'marvel.blocked.attribute.value'
    _description = 'Blocked Attribute Value'

    parameter = fields.Char(required=True)
    value = fields.Char(required=True)
    created_by = fields.Many2one('res.users', string='Created By')
    created_at = fields.Datetime(required=True, default=fields.Datetime.now)
    
