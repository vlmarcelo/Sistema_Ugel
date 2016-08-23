var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");


class ErrorListView extends Backbone.View 
{
    tagName() { return "ul"; }
    className() {return "errorlist";}
    initialize(options) 
    {
        this.options = options;
        
        _.defaults(this.options, {
            errors: [],
        }); 
    }

    render(events)
    {
        this.$el.empty();
        _.each(this.options.errors, function(error) {
            this.$el.append($('<li></li>').text(error));
        }, this);
        return this;   
    }
}

module.exports = ErrorListView;