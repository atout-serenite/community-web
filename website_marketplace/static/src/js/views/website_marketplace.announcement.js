var valeur = openerp.Class.extend({

    init: function() {
    	// Début Modification Type : offer or want
	    $('span[name=choixtype]').on('click',function(){
            var valeur = $(this).text();
            $("#" + valeur).prop("checked",true);
            $('span[class=checked]').attr("class",'');
            $(this).attr('class','checked');
        })
        // Début modification checkbox Quantité
        if($('input[name=unlimited]').attr('checked') == 'checked' && $('#quantity').val() != '') {
            $("#quantity").val('');
            $("#quantity").prop('disabled', true);
        }
        $("input[name=unlimited]").on('click', function(e){
            if($('input[name=unlimited]').attr('checked') == 'checked') {
                // si checked 
                $("#quantity").val('');
                $("#quantity").prop('disabled', true);
            } else {
                $("#quantity").prop('disabled', false);
            }
        })
        $("#quantity").on('change',function(e){
            $('input[name=unlimited]').attr('checked', false);
        })

        $('.derouler').mouseover(function(){
        	var donnee = $('.box_4').css('display');
            
            // on remet tout à 0
            if(donnee != 'block') {
	            setTimeout(function() {
	                    $('.box_4').hide().fadeIn();
	            }, 250 );
	       	}
        })
    }
});


openerp.website.theme.views['website_marketplace.edit_announcement'] = valeur;
openerp.website.theme.views['website_marketplace.new_announcement'] = valeur;