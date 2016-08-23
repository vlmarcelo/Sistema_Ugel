var $         = require("jquery");
var _         = require("underscore");
var Backbone  = require("backbone");
require("backbone-model-file-upload");
var Entidad   = require("../models/entidad");
var ErrorListView = require("../views/error_list_view");

Backbone.$ = $;

class EntidadFormCreateView extends Backbone.View 
{
	initialize()
	{
		this.template = _.template($("#form_entidad_create_template").html());
		this.render();
        this.listenTo(this.model, 'change', this.render);
	}

    render() 
	{
        this.$el.html(this.template());
		return this;
    }
	events()
	{
		return { 
				"click #submit_entidad" : "submit_add",
			   };
	}
	submit_add(events)
	{
		
	    if(events){ events.preventDefault(); }
		this.model =  new Entidad();
		var fileObject = $('#id_logotipo')[0].files[0];

		var id_clase_entidad = $("#id_clase_entidad").val();
	    this.model.set({clase_entidad:"/api/clases_entidades/" + id_clase_entidad + "/"});

    	var id_tipo_entidad = $("#id_tipo_entidad").val();
        this.model.set({tipo_entidad:"/api/tipos_entidades/" + id_tipo_entidad + "/"});

	    this.model.set({nombre:$("#id_nombre").val()});
	    this.model.set({siglas:$("#id_siglas").val()});

	    var id_documento_identificacion = $("#id_documento_identificacion").val();
	    this.model.set({documento_identificacion        :"/api/documentos_identificaciones/" + id_documento_identificacion + "/"});
	    this.model.set({numero_documento_identificacion : $("#id_numero_documento_identificacion").val()}); 
	    this.model.set({mision : $("#id_mision").val()}); 
	    this.model.set({vision : $("#id_vision").val()}); 
	    this.model.set({fecha_creacion : "1900-01-01"}); 
	    this.model.set({observacion    : $("#id_observacion").val()}); 
	    this.model.set({descripcion    : $("#id_descripcion").val()}); 
	    this.model.set({logotipo:fileObject});

	    this.model.save(null, {
            wait: true,
		    success: function (model, response) {
		        console.log("success");
		    },
		    error: function(model, response) {
		    	is_error = true;
                var errors = JSON.parse(response.responseText);
                console.log(errors);    
                _.each(errors, function(errorlist, field) {
                	var e = new ErrorListView({errors: errorlist})
                    $('input[name="'+field+'"]').after(e.render().el);
                });
            }
		});

		this.popup_value_return(this.model);
		return false;
	}

  	popup_value_return(entidad)
  	{
	   window.opener.document.getElementById('id_entidad').value=entidad.get("nombre"); 
	   window.close(); 

  	}
}


module.exports = EntidadFormCreateView;