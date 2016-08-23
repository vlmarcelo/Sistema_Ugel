var Backbone = require("backbone");
var $ 		 = require("jquery");
var _        = require("underscore");


class OptionTipoPersonaView extends Backbone.View 
{
	tagName() { return "option"; }
	className() {return "Select-Option";}
    initialize() 
    {
    	this.template = _.template($("#select-tipo-persona-template").html());
    	this.listenTo(this.model, "change", this.render, this);
 	}
 	events() 
	{
        
    }

	render()
	{
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
}

module.exports = OptionTipoPersonaView;