var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");


class ExpedienteCollection extends Backbone.Collection
{
	initialize()
	{
		this.model = Expediente; 
		this.url = "/api/expedientes";
		this.fetch();
	}
}

module.exports = ExpedienteCollection;
