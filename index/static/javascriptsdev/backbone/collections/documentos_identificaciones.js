var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");

var DocumentoIdentificacion = require('../models/documento_identificacion');


class DocumentoIdentificacionCollection extends Backbone.Collection
{
	initialize()
	{
		this.model = DocumentoIdentificacion; 
		this.url = "/api/documentos_identificaciones";
		this.fetch();
	}
}

module.exports = DocumentoIdentificacionCollection;
