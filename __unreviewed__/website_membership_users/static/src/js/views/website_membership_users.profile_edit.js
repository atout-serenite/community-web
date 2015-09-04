openerp.website.theme.views['website_membership_users.profile_edit'] = openerp.Class.extend({

    init: function() {
        /*
         * Make sure the user can only select one product of each categorie, 
         * but has the option of de-selecting
         */
        $('.container.memberships button').on('click',function(e){
            checkedState = $(this).hasClass('active');
            $(this).parents('.container.memberships').find('button').each(function () {
                if ($(this).hasClass('active'))
                {      
                    $(this).removeClass('active');
                }
            });
            if (!checkedState)
            {
                $(this).addClass('active'); 
            }
            else
            {
                $(this).removeClass('active'); 
            }
        });

        /*
         * Collect selected product data to send to server
         */
        $('form button[type=submit]').on('click', function(e){
            var hidden = $('<input type="hidden" name="products"/>');

            var ids = Array();

            $('.container.memberships button.active').each(function()
                {
                    var id=$(this).attr('data-id'); 
                    if (ids.indexOf(id) == -1)
                    {
                        ids.push(id)
                    };
                });

            hidden.attr('value', ids.join());

            $('form button[type=submit]').parent().append(hidden);
        });

    }
});
