// Generated by CoffeeScript 1.6.3
(function(){var e,t=function(e,t){return function(){return e.apply(t,arguments)}};e=function(){function e(e){this.initialize=t(this.initialize,this);this.events=e.events;this.loadScript()}e.prototype.loadScript=function(){this.events.trigger("payment-module","load");return $.getScript("https://js.stripe.com/v2",this.initialize)};e.prototype.initialize=function(){return this.events.trigger("payment-module","init")};return e}();window.dd.Modules.StripePaymentModule=e}).call(this);