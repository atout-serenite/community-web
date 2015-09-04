(function(){
  'use strict';

  var website = openerp.website;
  var choixmethode = '2';

  website.add_template_file('/website_last_articles_snippet/static/src/xml/lasts_articles_blocks.seo.xml');

  website.seo.Configurator = website.seo.Configurator.extend({
        template: 'website.seo_configuration',
        events: {
            'keyup input[name=seo_page_keywords]': 'confirmKeyword',
            'keyup input[name=seo_page_title]': 'titleChanged',
            'keyup textarea[name=seo_page_description]': 'descriptionChanged',
            'click button[data-action=add]': 'addKeyword',
            'click button[data-action=update]': 'update',
            'click button[data-action=setSEOImage]': 'uploadImage',
            'hidden.bs.modal': 'destroy',
        },

        uploadImage: function (e) {
            var self = this;
            var $modal = self.$el;
            var fileSelect = $modal.find('#fileselect')[0];
            var files = fileSelect.files;
            var mainObject = this.getMainObject();

            // Loop through each of the selected files.
            for (var i = 0; i < files.length; i++) {
                var file = files[i];
                if (!file.type.match('image.*')) {
                  continue;
                }
            }

            var data = {}
            var odooFileReader= new FileReader();
            odooFileReader.onload = function(e) {
                data.website_meta_image = e.target.result.replace(/^data:image\/(png|jpeg);base64,/, "");
                var model = website.session.model(mainObject.model);
                return model.call('write', [[mainObject.id], data, website.get_context()]);
            };       
            odooFileReader.readAsDataURL(file);
            
            
          }
        }

  );


})();