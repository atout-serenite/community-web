openerp.website.theme.views['website_marketplace.edit_announcement'] = openerp.Class.extend({

    init: function() {
        
	    $('.remove-attachment').on('click',function(e){
	        e.preventDefault();

	        var self = $(this);

	        openerp.jsonRpc($(this).attr('href')+'/delete', 'call', {})
	            .then(function (data) {
	                self.parent().remove();
	            });
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
