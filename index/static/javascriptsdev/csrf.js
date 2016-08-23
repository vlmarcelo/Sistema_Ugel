var Backbone = require("backbone");
var $ 		 = require("jquery");
var _        = require("underscore");

Backbone._sync = Backbone.sync;

Backbone.sync = function (method, model, options) {
  if (method === 'post' || method === 'put' || method === 'delete') {
    var csrfToken = $('meta[name="csrf-token"]').attr('content');

    options.beforeSend = function (xhr) {
      xhr.setRequestHeader('X-CSRFToken', csrfToken);
    };
  }

  return Backbone._sync(method, model, options);
};

module.exports = Backbone.sync;


    /*


    var getCookie;

    getCookie = function(name) {
        var cookie, cookieValue, cookies, i;

        cookieValue = null;
        if (document.cookie && document.cookie !== "") {
          cookies = document.cookie.split(";");
          i = 0;
          while (i < cookies.length) {
            cookie = $.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
            }
            i++;
          }
        }
        return cookieValue;
    };
    var oldSync = Backbone.sync;
    Backbone.sync = function(method, model, options) 
    {
        options.beforeSend = function(xhr){
            xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}');
        };

        return oldSync(method, model, options);
    };
    
    var _sync = Backbone.sync;
      Backbone.sync = function(method, model, options){
        options.beforeSend = function(xhr){
          var token = $('meta[name="csrf-token"]').attr('content');
          xhr.setRequestHeader('X-CSRFToken', token);
        };
        return _sync(method, model, options);
    };*/