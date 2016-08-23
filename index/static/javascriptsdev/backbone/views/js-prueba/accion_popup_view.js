var Backbone = require("backbone");
var $ 		 = require("jquery");
var _        = require("underscore");


class AccionPopupView extends Backbone.View 
{
	tagName() { return "div"; }
	className() { return "SelectValue";}

    initialize() 
    {
    	this.template = _.template($("#accion-popup-template").html());
        this.render();
 	}
 	events() 
	{
        return {
            "click #accion-popup-add": "open_create_object",
            "click #accion-popup-edit": "edit_create_object",
        };
    }
    
    open_create_object(events)
    {
        events.preventDefault();
        window.open(
                    $("#accion-popup-add").attr("href"), 
                    $("#accion-popup-add").attr("target"), 
                   "width=600,height=600");
        return false;
    }
    edit_create_object(events)
    {
        events.preventDefault();
        window.open(
                    $("#accion-popup-edit").attr("href"), 
                    $("#accion-popup-edit").attr("target"), 
                   "width=600,height=600");
        return false;
    }
	render()
	{
		this.$el.html(this.template());
		return this;
	}
}

module.exports = AccionPopupView;