var Backbone   = require("backbone");
var $          = require("jquery");

var PaisNewView = require("../views/pais_new_view");
var AdministradoFormCreateView = require("../views/administrado_form_create_view");
var EntidadFormCreateView = require("../views/entidad_form_create_view");

class Router extends Backbone.Router 
{
    initialize () {
        this._bindRoutes();
    }

    routes () 
    { 
        return {
            "administrado/nuevo/"          : "nuevo_administrado",
            "entidad/nuevo/"               : "nuevo_entidad",
            //"pais/nuevo/"                  : "nuevo_pais",
        };
    }
        

    nuevo_pais () {
        var pais_form_view = new PaisNewView({el:$("#form-create-pais")});
    }

    nuevo_administrado () {
        var administrado_form_create_view = new AdministradoFormCreateView({el:$("#form_administrado_create")});
    }

    nuevo_entidad () {
        var entidad_form_create_view = new EntidadFormCreateView({el:$("#form_entidad_create")});
    }

}

module.exports = Router;