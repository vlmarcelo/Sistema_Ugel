var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");

var Administrado = require('../models/administrado');


class AdministradoCollection extends Backbone.Collection
{
	initialize()
	{
		this.model = Administrado; 
		this.url = "/api/administrados";
		this.fetch();
	}
}

module.exports = AdministradoCollection;
