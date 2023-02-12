from odoo import models, fields, api, _
from odoo.exceptions import UserError

class material_models(models.Model):
	_name = "test.material_models"

	code = fields.Char(string="Material Code", required=True)
	name = fields.Text(string="Material Name", required=True)
	mat_type = fields.Selection([('fabric','Fabric'),('jeans','Jeans'),('cotton','Cotton')], string="Material Type", required=True)
	buy_price = fields.Float(string="Material Buy Price", required=True) 
	supplier = fields.Many2one(string="Material Supplier", required=True, comodel_name="res.partner")

	@api.onchange('buy_price')
	def change_value(self):
		if self.buy_price > 100 :
			return {'warning':{'title':'Error!','message':'Material Buy Price harus dibawah 100 !'}}