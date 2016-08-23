var Backbone = require("backbone");
var $ 		 = require("jquery");
var _        = require("underscore");

class SearchSelectItemView extends Backbone.View 
{
	tagName() { return "li"; }
	className() { return "OrderList-Item";}

    initialize() 
    {
    	this.template = _.template($("#search-select-item-link-template").html());
    	this.listenTo(this.model, "change", this.render, this);
 	}
 	events() 
	{
        return {
            "click .OrderList-Item-Link": "active_item",
        };
    }
   	active_item(events)
    {
    	events.preventDefault();
        $(".OrderList-Item").removeClass("active"); 
        this.$el.addClass("active"); 
        $("#select-value-show").text(this.$el.children("a").text());
        $("#search-container").slideToggle();
        this.render();
    }
	render()
	{
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
}

module.exports = SearchSelectItemView;