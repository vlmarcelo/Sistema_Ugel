var Backbone 	  = require("backbone");
var $ 		 	  = require("jquery");
var _        	  = require("underscore");
var OrderListMenuView       = require("../views/order_list_menu_view");


class SearchBoxListView extends Backbone.View 
{
	tagName() { return "div"; }

	className() { return "SearchSelectContainer"; }

	collection() { return this.collection; }
	
	initialize(ol)
	{
        console.log(ol);
		this.template = _.template($("#search-box-list-template").html());
        this.render();
	}
	

	events() 
	{
        return {
            "keyup"						: "buscar",
        };
    }
   
    buscar(events)
    {
        event.preventDefault();
        //Obtener el valor del InputText;
    	var value_search = $(this).$el.children($(".SearchSelect")).val().toLowerCase();

    	var values = this.collection.filter(function(model) {
    		var value_model = model.get("apellido_paterno").substring(0, value_search.length).toLowerCase();
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

module.exports = SearchBoxListView;