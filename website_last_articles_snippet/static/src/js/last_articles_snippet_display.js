(function(){
  'use strict';

  var website = openerp.website;
  var choixmethode = '2';



  website.add_template_file('/website_last_articles_snippet/static/src/xml/lasts_articles_blocks.front.xml');

  website.snippet.animationRegistry.js_get_posts = website.snippet.Animation.extend({
    selector : ".last_articles_snippets",
    getMainObject: function () {
        var repr = $('html').data('main-object');
        var m = repr.match(/(.+)\((\d+),(.*)\)/);
        if (!m) {
            return null;
        } else {
            return {
                model: m[1],
                id: m[2]|0
            };
        }
    },

    start: function(){
      this.clean();
      this.build();
    },
    stop: function(){
      this.clean();
    },
    clean:function(){
      this.$target.empty();
    },
    build: function() {
      var mainObject = this.getMainObject();

      var self = this;

      var domain = [['page','=','True'],['active','=','True']]

      if (mainObject[1] == 'ir.ui.view')
      {
        domain.push(['id','<',mainObject[2]]);
      }

      openerp.jsonRpc('/web/dataset/call_kw', 'call', {
                model: 'ir.ui.view',
                method: 'search_read',
                args: [],
                kwargs: {
                    fields: ['slug', 'website_meta_image', 'website_meta_title', 'website_meta_description'],
                    domain: domain,
                    order: 'create_date desc',
                    limit: 3
                }
            }).then( function(data) {
                self.$el.append(openerp.qweb.render("website_last_articles_snippet.liste_articles", {"posts": data}));
            });
    }

  })

})();