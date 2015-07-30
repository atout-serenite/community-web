openerp.website.theme.views['website_marketplace.new_announcement'] = openerp.Class.extend({

    init: function() {


        $("input[name=default_value]").keyup(function(e){
            var valeur = $("input[name=default_value]").val();
            valeur = valeur.replace(",",'.');
            $("input.number").val(valeur);
        });

        $('#category_id').on('change', function(e){
            e.preventDefault();
            
            var self = $(this);

            openerp.jsonRpc('/marketplace/announcement_detail/tags/' + self.val() + '/get', 'call', {})
                .then(function (data) {
                    var tag_select = $('#tag_ids');
                    tag_select.html('');
                    for (var id in data.tag_dict) {
                        tag_select.append('<option value="' + id + '">' + data.tag_dict[id] + '</option>');
                    }
                    $(tag_select).selectpicker('refresh');
                });
        });

    }
});
