var Backbone 	  			  = require("backbone");
var $ 		 	  			  = require("jquery");
var OptionTipoPersonaView	  = require("../views/option_tipo_persona_view");


class SelectTipoPersonaView extends Backbone.View 
{
	tagName() { return "select"; }

	className() { return "Select"; }

	initialize(){
		this.listenTo(this.collection, "sync", this.render);
	}
	
	events() 
	{
        return {
        	"change" : "select_tipo_persona", 
        };
    }
    select_tipo_persona(events)
    {
    	events.preventDefault();
        var tipo_persona = this.$el.val().toLowerCase()
        if(tipo_persona === "natural")
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
  
	render()
	{
		//Crear Cache 
		var cache = document.createDocumentFragment();
		//Iterar objetos y pasando a la vista
		this.collection.each(function(model){
			var option_tipo_persona_view = new OptionTipoPersonaView({model: model});
			cache.appendChild(option_tipo_persona_view.render().el);
		});

		this.$el.append(cache);
	}
}

module.exports = SelectTipoPersonaView;