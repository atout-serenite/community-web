openerp.website.theme.views['website_marketplace.mp_search'] = openerp.Class.extend({
    init: function() {
        actionliste($("#choixmarketplace").val());
        remiseazero();
        var action = "mouse"; // Mouse pour action au défilement, Click Pour action au click
        this.action(action);
        $('span[name=old]').on('click',function(){ 
            valuechoixaffichage('old'); 
            actionliste('old'); 
        })
        $('span[name=liste]').on('click',function(){ 
            valuechoixaffichage('liste'); 
            actionliste('liste'); 
        })
        $('span[name=bigpicture]').on('click',function(){
            valuechoixaffichage('bigpicture');
            actionliste('bigpicture');
        })
        $('span[name=grid]').on('click',function(){
            valuechoixaffichage('grid');
            actionliste('grid');
        })
    }, 
    action: function(action) {
        if (action == "mouse") {
           $( window ).scroll(function() {
                if($(window).scrollTop() == $(document).height() - $(window).height()) {
                   remiseazero();
               }
            });
        } else {
            $(".page").on('click',function() {
                remiseazero();
                return false; 
            })
        }
    }
})

function actionliste (choix) {
    if(choix == 'old') {
        $('.liste_colonne').css("display",'');
        $('.ligne').css("display",'none');
    } else if(choix == 'bigpicture') {
         $('.liste_colonne').css("display",'none');
         $('.ligne').css("display",'');
         // $('.modOffers').attr('class','col-md-3 modOffers');
         // $('.modWants').attr('class','col-md-3 modWants');    
    } else if(choix == 'grid') {
        $('.liste_colonne').css("display",'none');
        $('.ligne').css("display",'');
        $('.modOffers').attr('class','col-md-6 modOffers');
        $('.modWants').attr('class','col-md-6 modWants');
    } else if(choix == 'liste') {
        $('.liste_colonne').css("display",'none');
        $('.ligne').css("display",'');
        $('.modWants').attr('class','col-md-6 modWants');
    }
    $("#choixmarketplace").val(choix);
}
function ListeForm (){
    var form = document.forms.searchform;
    data = {};
    for (i=0 ; i<= form.length-1 ; i++){
        if(form[i].value != '') {
            data[form[i].name] = form[i].value;
            //alert("Le champ " + form[i].name + "  == > " + form[i].value];
        }
    }
    return data
}
function valuechoixaffichage (resultat) {
    openerp.jsonRpc('/marketplace/session_affichage/' + resultat, 'call', {})
    .then(function (data) {
        $('.page').css("display",'');
        $('#npage').val('0');
        $('.liste_colonne').html('');
        $('.mp_four_liste').html('');
        remiseazero();
    });
}
function remiseazero() {
    npage = $('#npage').val();
    if (npage == '0') npage = 1;
    suivante = parseInt(npage) + 1;
    datas = ListeForm();
    datas['page'] = npage;
    choixmarketplace = $("#choixmarketplace").val();
    datas['choix'] = choixmarketplace;
    urls = "/marketplace/search-function"
    if (parseInt(npage) > parseInt($('#page_count').val())) {
        if(choixmarketplace == 'old') {
            $('.liste_colonne').html($('.liste_colonne').html());
        } else {
            $('.mp_four_liste').html($('.mp_four_liste').html());
        }
        return false;
    }
    $.ajax({
        url: urls,
        method: 'GET',
        data: datas,
        success: function( data ) {
            if(choixmarketplace == 'old') {
                $('.liste_colonne').html($('.liste_colonne').html() + data);
            } else {
                $('.mp_four_liste').html($('.mp_four_liste').html() + data);
            }
            
            $('#npage').val(suivante);
            if(npage == $("#page_count").val()) {
                $('.page').css("display",'none');
            }
            actionliste(choixmarketplace);
        },
        error: function() {
        }
    });
}

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





