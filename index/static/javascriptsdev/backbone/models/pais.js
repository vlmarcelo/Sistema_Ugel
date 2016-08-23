var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");


class Pais extends Backbone.Model
{
	urlRoot() { return "/api/paises/"; }

	url()
	{
		var base = this.urlRoot();
	    if (this.isNew()) return base;
	    return base + (base.charAt(base.length - 1) == '/' ? '' : '/') + encodeURIComponent(this.id) + "/";
	}
}

module.exports = Pais;

 


