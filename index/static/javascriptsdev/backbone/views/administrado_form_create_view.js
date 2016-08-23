var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");


var Administrado  = require("../models/administrado");
var ErrorListView = require("../views/error_list_view");
var DocumentoIdentificacionCollection = require("../collections/documentos_identificaciones");


class AdministradoFormCreateView extends Backbone.View 
{
    defaults() {
      return {
        documentos_identificaciones:  '',
      };
    }

	initialize()
	{
		this.template = _.template($("#form_administrado_create_template").html());
		this.render();
        this.select_persona_natural();
        this.documentos_identificaciones = new DocumentoIdentificacionCollection();
        this.listenTo(this.model, 'change', this.render);
	}


	events()
	{
		return { 
				"click #submit_administrado": "submit_add",
				"change #id_tipo_persona" 	: "select_tipo_persona", 
                "change #id_documento_identificacion"   : "select_documento_identificacion", 	
                "click #accion_popup_search_entidad" : "popup_search_entidad",
                "click #accion_popup_add_entidad"    : "popup_add_entidad",
                "click #accion_popup_edit-entidad"   : "popup_edit_entidad"
			   };
	}

    render() 
	{
        this.$el.html(this.template());
		return this;
    }
	//Eventos
    submit_add(events)
    {
    	events.preventDefault();
    	this.model = new Administrado();

        var tipo_persona = $("#id_tipo_persona option:selected").text().toUpperCase();
        if(tipo_persona === "NATURAL")
        {
            this.model.set({entidad           : "/api/entidades/1/"});
        }
        else
        {
            var id_entidad = $("#id_entidad").val();
            this.model.set({entidad           : "/api/entidades/" + id_entidad + "/"});
            this.model.set({email_corporativo : $("#id_email_corporativo").val()});
        }

        var id_tipo_persona = $("#id_tipo_persona").val();
        this.model.set({tipos_personas                  :"/api/tipos_personas/" + id_tipo_persona + "/"});

        this.model.set({apellido_paterno                : $("#id_apellido_paterno").val()});
        this.model.set({apellido_materno                : $("#id_apellido_materno").val()});
        this.model.set({nombre                          : $("#id_nombre").val()});

        var id_documento_identificacion = $("#id_documento_identificacion").val();
        this.model.set({documento_identificacion        :"/api/documentos_identificaciones/" + id_documento_identificacion + "/"});

        this.model.set({numero_documento_identificacion : $("#id_numero_documento_identificacion").val()}); 
        this.model.set({genero                          : $("#id_genero:checked").val()}); 
        this.model.set({telefono_personal               : $("#id_telefono_personal").val()});
        this.model.set({celular_personal                : $("#id_celular_personal").val()}); 
        this.model.set({email_personal                  : $("#id_email_personal").val()});
        this.model.set({descripcion_admistrado          : $("#id_descripcion_admistrado").val()});
        this.model.set({observacion_admistrado          : $("#id_observacion_admistrado").val()});
        this.model.save(null, {
            wait: true,
		    success: function (model, response) {
		        console.log("success");
		    },
		    error: function(model, response) {
                var errors = JSON.parse(response.responseText);
                console.log(errors);    
                _.each(errors, function(errorlist, field) {
                	var e = new ErrorListView({errors: errorlist})
                    $('input[name="'+field+'"]').after(e.render().el);
                });
            }
		});

		events.currentTarget.checkValidity();

		//Backbone.navigate('pais/' + this.model.id, {trigger: true});
        return false;
    }

    select_tipo_persona()
    {
    	var tipo_persona = $("#id_tipo_persona option:selected").text().toUpperCase();
        if(tipo_persona === "NATURAL")
        {
            this.select_persona_natural();
        }
        else 
        {
            this.select_persona_juridica();
        }
       
    }

    select_persona_natural()
    {
        $("#box_entidad").hide();
        $("#box_email_corporativo").hide();
    }
    select_persona_juridica()
    {
    	$("#box_entidad").show();
        $("#box_email_corporativo").show();
    }

    select_documento_identificacion()
    {

        if (typeof(this.documentos_identificaciones) === "undefined") {
            this.documentos_identificaciones = new DocumentoIdentificacionCollection();
        }
         
        var id_documento_identificacion = $("#id_documento_identificacion").val();
        var documento_identificacion = this.documentos_identificaciones.get(id_documento_identificacion);
        $("#id_numero_documento_identificacion").attr({
            "size":documento_identificacion.get("numero_digito"),
        });
    }

    popup_search_entidad()
    {
        window.open($("#accion_popup_search_entidad").attr("href"), $("#accion_popup_search_entidad").target, 'width=600,height=600');
        return false;
    }
    popup_add_entidad()
    {
        window.open($("#accion_popup_add_entidad").attr("href"), $("#accion_popup_add_entidad").target, 'width=600,height=600');
        return false;
    }
    popup_edit_entidad()
    {
        window.open($("#accion_popup_edit_entidad").attr("href"), $("#accion_popup_edit_entidad").target, 'width=300,height=400');
        return false;
    }
}

module.exports = AdministradoFormCreateView;