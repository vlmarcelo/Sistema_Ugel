var Backbone 	  			  = require("backbone");
var $ 		 	  			  = require("jquery");
var SearchSelectItemView  	  = require("../views/search_select_item_view");


class SearchSelectMenuView extends Backbone.View 
{
	tagName() { return "ol"; }

	className() { return "OrderList"; }

	initialize(){
		this.listenTo(this.collection, "sync", this.render);
	}
	events() 
	{
        return {
           
        };
    }
    filtrar_elemento(coleccionFiltro)
    {
    	this.$el.html("");
    	coleccionFiltro.forEach(this.filtro, this);
    }

    filtro(model)
    {
    	var search_select_item_view = new SearchSelectItemView({model: model});
    	this.$el.append(search_select_item_view.render().el);
    }

	render()
	{
		//Crear Cache 
		var cache = document.createDocumentFragment();
		//Iterar objetos y pasando a la vista
		this.collection.each(function(model){
			var search_select_item_view = new SearchSelectItemView({model: model});
			cache.appendChild(search_select_item_view.render().el);

		});

		this.$el.append(cache);
	}
}

module.exports = SearchSelectMenuView;