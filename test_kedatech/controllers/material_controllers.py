from odoo import http
from odoo.http import request

class MaterialData(http.Controller):
	@http.route(['/materialdata/'], type='http', auth='public', website=True)
	def material_data(self, **kwargs):
		materials_data = request.env['test.material_models'].sudo().search([])
		values = {
						'records': materials_data
				} 
		return request.render('test_kedatech.tmp_materials_data', values)