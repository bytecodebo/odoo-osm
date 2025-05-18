odoo.define("byc_web_widget_fullscreen.FullScreenWidget", function (require) {
    "use strict";
    var Widget = require('web.Widget');
    var widget_registry = require("web.widget_registry");
      var ajax = require("web.ajax");

    var FullScreenWidget = Widget.extend({
            template: 'FullScreenControl',
            className: 'oe_fullscreen_control',
            xmlDependencies: ['/byc_web_widget_fullscreen/static/src/xml/fullscreen_widget.xml'],
           /* jsLibs: [
                '/byc_web_widget_fullscreen/static/lib/fullscreen-widget/fullscreen-widget.js',
            ],*/
            events: {
                'click': '_onClickButton',
            },
             init: function (parent, options) {
                 this._super(...arguments);
                 this.options = options;
                 if(!options || options === undefined){
                     this.options = {}
                 }
                this.parent = parent;
                //this.widgets_control = {};
                //this.isFullScreen = false;
                this.$targetElement = $(this.options.targetElement || document);
                 this.uniqueId = this.options.uniqueId || new Date().getTime().toString();
                 this.controlId = this.options.controlId || new Date().getTime().toString();
                 this.isFullscreen = false;
                //this.parentElement = this.parent.name;
                 this.$documents = $([window.top, ...Array.from(window.top.frames).filter(frame => {
                    try {
                        const document = frame.document;
                        return !!document;
                    } catch (error) {
                        // We cannot access the document (cross origin).
                        return false;
                    }
                })].map(w => w.document));
            },
           /* willStart: function () {
                return this._super.apply(this, arguments);
                //return ajax.loadLibs(this);
            },*/

            start: function () {
                /*const proms = [this._super(...arguments)];
                //var self = this;
                //return this._super.apply(this, arguments);
                    proms.push(this.appendTo(this.targetElement.$el));
                    return Promise.all(proms);*/
                return this._super.apply(this, arguments);
                },
        
            destroy: function () {
                this._super.apply(this, arguments);
                this.$documents.off(`.${this.uniqueId}`);
            },
            _renderWidget: async function(){
               await  this.appendTo(this.$targetElement);
            },
           /* _clear() {
                var self = this;
                self.$listButtons.forEach($btn => {
                    $btn.clearInterval();
                    $btn.destroy();
                })
                self.$listButtons = [];
            },*/
            _onClickButton: async function (event) {
                 if (this.options.stopClickPropagation) {
                        event.stopPropagation();
                    }
                var parentName = event.currentTarget.id;
                var options = {
                    'type': event.currentTarget.type,
                    'id': parentName
                };
                var element = $(this.$targetElement)[0];
               await screenFull.toggle(element, options);
                this.isFullscreen = screenFull.isFullscreen;            
               this.renderElement();               
            }
        });

    widget_registry.add(
        "full_screen_control",
        FullScreenWidget
    );

    return FullScreenWidget;

});
