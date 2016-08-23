var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");

var Pais = require('../models/pais');


class PaisCollection extends Backbone.Collection
{
	initialize()
	{
		this.model = Pais; 
		this.url = "/api/paises/";
		this.fetch();
	}
}

module.exports = PaisCollection;
