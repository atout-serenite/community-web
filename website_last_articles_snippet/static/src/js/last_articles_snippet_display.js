(function(){
  'use strict';

  var website = openerp.website;
  var choixmethode = '2';



  

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
      mainObject = this.getMainObject();

      $.get("/website_last_articles_snippet/render/"+ mainObject[1] + "/" + mainObject[2], 
          function( data ) {
            $('.last_articles_snippets').html(data);
  
          });
    }

  })

})();