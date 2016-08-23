var Backbone 	  			  = require("backbone");
var $ 		 	  			  = require("jquery");
var OrderListItemView		  = require("../views/order_list_item_view");


class OrderListMenuView extends Backbone.View 
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
    	var order_list_item_view = new OrderListItemView({model: model});
    	this.$el.append(order_list_item_view.render().el);
    }

	render()
	{
		//Crear Cache 
		var cache = document.createDocumentFragment();
		//Iterar objetos y pasando a la vista
		this.collection.each(function(model){
			var order_list_item_view = new OrderListItemView({model: model});
			cache.appendChild(order_list_item_view.render().el);

		});

		this.$el.append(cache);
	}
}

module.exports = OrderListMenuView;