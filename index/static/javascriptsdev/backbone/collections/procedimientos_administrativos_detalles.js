var Backbone = require('backbone');
var ProcedimientoAdministrativoDetalle = require('../models/procedimiento_administrativo_detalle');


class ProcedimientoAdministrativoDetalleCollection extends Backbone.Collection
{
	initialize()
	{
		this.model = ProcedimientoAdministrativoDetalle; 
		this.url = "/api/procedimientos_administrativos_detalles";
		this.fetch();
	}
	
}

module.exports = ProcedimientoAdministrativoDetalleCollection;
