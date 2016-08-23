var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");

var Entidad = require('../models/entidad');


class EntidadCollection extends Backbone.Collection
{
	initialize()
	{
		this.model = Entidad; 
		this.url = "/api/entidades/";
		this.fetch({reset:true});
	}
}

module.exports = EntidadCollection;
