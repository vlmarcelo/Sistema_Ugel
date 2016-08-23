var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");


class Administrado extends Backbone.Model
{
	urlRoot() { return "/api/administrados/"; }

	url() 
	{
	  var base = this.urlRoot();
	  if (this.isNew()) return base;
	  return base + (base.charAt(base.length - 1) == "/" ? '' : "/") + encodeURIComponent(this.get("id")) + "/";
	}

}

module.exports = Administrado;

 
