function getXhr(){
  var xhr = null; 
  if(window.XMLHttpRequest) // Firefox et autres
     xhr = new XMLHttpRequest(); 
  else if(window.ActiveXObject){ // Internet Explorer 
     try {
            xhr = new ActiveXObject("Msxml2.XMLHTTP");
            } catch (e) {
                xhr = new ActiveXObject("Microsoft.XMLHTTP");
            }
  }
  else { // XMLHttpRequest non supporté par le navigateur 
     alert("Votre navigateur ne supporte pas les objets XMLHTTPRequest..."); 
     xhr = false; 
  } 
  return xhr;
}
 

// (function(){
//   'use strict';
  
//   var website = openerp.website;

//   website.snippet.animationRegistry.js_get_posts = website.snippet.Animation.extend({
//     selector : ".last_articles_snippets",
//     start: function(){
//       this.clean();
//       this.build();
//     },
//     stop: function(){
//       this.clean();
//     },

//     clean:function(){
//       this.$target.empty();
//     },

//     build: function(){
//       var self     = this,
//           limit    = self.$target.data("posts_limit"),
//           template = self.$target.data("template"),
//           loading  = self.$target.data("loading");

//       // if no data, then use defaults values
//       if(!limit)limit = 3; // Limit default
//       if(!template) template = 'snippet_last_articles.liste_article';
      
//       // create the domain
//       alert(1)
//       // call posts
//       openerp.jsonRpc('/snippet_latest_posts/render', 'call',{
//         'template': template,
//         'limit': limit,
//       }).then(function(posts) {
//          // just print the posts
//          alert(posts)
//          $(posts).appendTo(self.$target);
        
//       })
//       .fail(function(e) {
//         // debug in js console
//         return;
//       });
//     }

//   })

// })();

// // function getXhr(){
// //     var xhr = null; 
// //     if(window.XMLHttpRequest) // Firefox et autres
// //        xhr = new XMLHttpRequest(); 
// //     else if(window.ActiveXObject){ // Internet Explorer 
// //        try {
// //                   xhr = new ActiveXObject("Msxml2.XMLHTTP");
// //               } catch (e) {
// //                   xhr = new ActiveXObject("Microsoft.XMLHTTP");
// //               }
// //     }
// //     else { // XMLHttpRequest non supporté par le navigateur 
// //        alert("Votre navigateur ne supporte pas les objets XMLHTTPRequest..."); 
// //        xhr = false; 
// //     } 
// //     return xhr
// //   }
// //   function go(){
// //     var xhr = getXhr()
// //     // On défini ce qu'on va faire quand on aura la réponse
// //     xhr.onreadystatechange = function(){
// //       // On ne fait quelque chose que si on a tout reçu et que le serveur est ok
// //       if(xhr.readyState == 4 && xhr.status == 200){
// //         $('.last_articles_snippets').html(xhr.responseText);
// //       }
// //     }
// //     xhr.open("POST","/snippet_latest_posts/render",true);
// //     xhr.send(null);
// //   }
