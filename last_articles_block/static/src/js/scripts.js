(function(){
  'use strict';

  var website = openerp.website;
  var choixmethode = '2';

  

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

      var xhr = new XMLHttpRequest();
      // On défini ce qu'on va faire quand on aura la réponse
      xhr.onreadystatechange = function(){
        // On ne fait quelque chose que si on a tout reçu et que le serveur est ok
        if(xhr.readyState == 4 && xhr.status == 200){
          $('.last_articles_snippets').html(xhr.responseText);
        }
      }
      var repr = $('html').data('main-object');
      var m = repr.match(/(.+)\((\d+),(.*)\)/);
      
      

      xhr.open("POST","/snippet_latest_posts/render/"+ m[1] + "/" + m[2],true);
      
      if (!m) {
          xhr.send(null);
      } else {
          xhr.send('?page='+ m[2] + '&base=' + m[1]);
      }
    }

  })

})();