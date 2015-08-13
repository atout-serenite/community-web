(function(){
  'use strict';

  var website = openerp.website;
  var choixmethode = '2';



  website.add_template_file('/website_last_articles_snippet/static/src/xml/lasts_articles_blocks.front.xml');

  website.snippet.animationRegistry.js_get_posts = website.snippet.Animation.extend({
    selector : ".last_articles_snippets",

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

      var self = this;

      openerp.jsonRpc('/web/dataset/call_kw', 'call', {
                model: 'blog.post',
                method: 'search_read',
                args: [],
                kwargs: {
                    fields: ['slug', 'subtitle', 'background_image' , 'name'],
                    domain: [],
                    order: 'create_date desc',
                    limit: 3
                }
            }).then( function(data) {
                self.$el.append(openerp.qweb.render("website_last_articles_snippet.liste_articles", {"posts": data}));
            });
    }

  })

})();