var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");

var TipoPersona = require('../models/tipo_persona');


class TipoPersonaCollection extends Backbone.Collection
{
	initialize()
	{
		this.model = TipoPersona; 
		this.url = "/api/tipos_personas";
		this.fetch();
	}
}

module.exports = TipoPersonaCollection;
