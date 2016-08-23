var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");


var Pais	 = require("../models/pais");
var ErrorListView = require("../views/error_list_view");


class PaisNewView extends Backbone.View 
{
	initialize()
	{
		this.template = _.template($("#form-submit-pais").html()); //mi template donde esta el formulario
		this.render();
	}
	events()
	{
		return {"click #submit-pais": "submit_add",	};
	}
    submit_add(events)
    {
    	events.preventDefault();
    	this.model = new Pais();

    	this.model.set({
    					"nombre": $("#id_nombre").val(), 
    					"codigo_postal": $("#id_codigo_postal").val(),});

        this.model.save(null, {
		    success: function (model, response) {
		        console.log("success");
		    },
		    error: function(model, response) {
                var errors = JSON.parse(response.responseText);

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
    render () 
	{
        this.$el.html(this.template());
		return this;
    }
}

module.exports = PaisNewView;