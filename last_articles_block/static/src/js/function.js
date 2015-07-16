function UploadImage(message) {
  var form = document.getElementById('file-form');
  var fileSelect = document.getElementById('fileselect');
  var files = fileSelect.files;
  var formData = new FormData();

  // Loop through each of the selected files.
  for (var i = 0; i < files.length; i++) {
    var file = files[i];
    // Check the file type.
    if (!file.type.match('image.*')) {
      continue;
    }
    // Add the file to the request.
    //formData.append('photos[]', file, file.name);
  }
  formData.append('image', file, file.name);

  var repr = $('html').data('main-object');
  var m = repr.match(/(.+)\((\d+),(.*)\)/);
  
  var xhr = new XMLHttpRequest();
  xhr.open("POST","/snippet_latest_posts/updimage/"+ m[1] + "/" + m[2],true);
  // On défini ce qu'on va faire quand on aura la réponse
  xhr.onreadystatechange = function(){
    // On ne fait quelque chose que si on a tout reçu et que le serveur est ok
    if(xhr.readyState == 4 && xhr.status == 200){
    }
  }
 
  
  xhr.send(formData);
}

