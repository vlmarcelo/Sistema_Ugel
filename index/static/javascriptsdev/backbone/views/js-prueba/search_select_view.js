var Backbone 	  = require("backbone");
var $ 		 	  = require("jquery");
var _        	  = require("underscore");

var SearchSelectMenuView    = require("../views/search_select_menu_view");
var SearchSelectItemView    = require("../views/search_select_item_view");

class SearchSelectView extends Backbone.View 
{
	tagName() { return "div"; }

	className() { return "SelectContainer"; }

	collection() { return this.collection; }
	
	initialize()
	{
		this.template = _.template($("#search-select-template").html());
		this.render();
		this.elements_view = new SearchSelectMenuView({collection:this.collection, el:$("#ol_administrado")});
	}
	

	events() 
	{
        return {
            "keyup"						: "buscar",
            "click #select-value"  		: "down_up",
        };
    }
   
    down_up(event)
    {	event.preventDefault();
    	$("#search-container").slideToggle();
    }
   
    buscar(events)
    {
        event.preventDefault();
    	var value_search = $("#buscador_administrado").val().toLowerCase();
    	var values = this.collection.filter(function(model) {
    		var value_model = model.get("apellido_paterno").substring(0, value_search.length).toLowerCase();
            console.log(value_model);
            console.log("------------------------")
    		if(
    			(value_search.length != 0)  &&
    			(value_model.length != 0)   &&
    			(value_search === value_model) && 
    			(value_model.length==value_search.length) 
    		  )
    		{
    			return model;
    		}
    		else if((value_search.length === 0)  && (value_model.length === 0))
    		{
    			return model;
    		}
    	});
       
       this.elements_view.filtrar_elemento(values);
    }

	render()
	{
		this.$el.html(this.template());
		return this;
	}
	
}

module.exports = SearchSelectView;