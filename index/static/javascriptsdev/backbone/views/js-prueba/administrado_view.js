var Backbone = require("backbone");
var $ 		 = require("jquery");
var _        = require("underscore");

var Administrado = require('../models/administrado');
var AdministradoCollection = require('../collections/administrados');
var ErrorListView = require("../views/error_list_view");


class AdministradoView extends Backbone.View 
{
	initialize()
	{
		this.template = _.template($("#form-submit-administrado").html());
		this.render();
        this.administrados = new AdministradoCollection();
	}

	events()
	{
		return {
		    "click #submit-add-administrado": "submit_add",
            "change #id_tipo_persona"       : "seleccionar_tipo_persona",
		};
	}

	render () 
	{
        this.$el.html(this.template());
		return this;
    }

    seleccionar_tipo_persona(events)
    {
        alert("tipo");
        events.preventDefault();
        var tipo_persona = $("#id_tipo_persona").$el.val().toUpperCase();

        if(tipo_persona === "NATURAL")
        {
            $("#box-entidad").hide();
            $("#box-apellido-paterno").show();
            $("#box-apellido-materno").show();
            $("#box-genero").show();
        }
        else {
            $("#label-nombre").text("Representante");
            $("#box-entidad").show();
            $("#box-apellido-paterno").hide();
            $("#box-apellido-materno").hide();
            $("#box-genero").hide();
        }
    }
    submit_add(events)
    {
    	alert("save");
    	events.preventDefault();
    	var administrado = new Administrado();


    	administrado.tipo_persona = $("#id_tipo_persona").val().toUpperCase();

    	if(administrado.tipo_persona === "1" )
    	{
    		administrado.entidad 		  = "1";
    		administrado.apellido_paterno = $("#id_apellido_paterno").val().toUpperCase();
    		administrado.apellido_materno = $("#id_apellido_materno").val().toUpperCase();
    		administrado.genero 		  = $("#id_genero").val();
    	}
    	else
    	{
    		administrado.entidad 	      = $("#id_entidad").val();
    		administrado.apellido_paterno = "---------";
    		administrado.apellido_materno = "---------";
    		administrado.genero 		  = "1";
    	} 
    	administrado.nombre 						 = $("#id_nombre").val().toUpperCase();
    	administrado.documento_identificacion 		 = $("#id_documento_identificacion").val();
    	administrado.numero_documento_identificacion = $("#id_numero_documento_identificacion").val();
    	administrado.fecha_nacimiento 		  		 = "01/01/1900";
    	administrado.estado_civil 			       	 = "1";
    	administrado.grupo_sanguineo 		       	 = "1";
    	administrado.numero_hijo 			       	 =  0 ;
    	administrado.distrito 			       		 = "1";
    	administrado.zona 			       			 = "1";
    	administrado.via 			       			 = "1";
    	administrado.nombre_direccion      			 = "---------";
    	

        administrado.usuario_creado                  = "1"
        administrado.ultimo_usuario_editor           = "1"
        administrado.nombre_host                = "---------";
        administrado.direccion_ip                = "192.168.1.100";
    	console.log(administrado);
        administrado.save(null, {
            success: function(response) {
                console.log('Successfully SAVED blog with _id: ' + response.toJSON()._id);
            },
            error: function() {
                console.log('Failed to save blog!');
            }
        });

/*
    	administrado.save({}, 
    							{
            					    success: function() { alert('Successfuly add administrado.'); },
            					    error:  function(model, response) 
		            					    {
						                        var errors = JSON.parse(response.responseText);
						                        _.each(errors, function(errorlist, field) 
						                        {
						                            $('input[name="'+field+'"]')
						                            .before(
						                                new ErrorListView({errors: errorlist}).render().el);
						                        });
						                    }
        						}); */
    	return false;
    }
}

module.exports = AdministradoView;