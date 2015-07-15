openerp.website.theme.views['website_membership_users.profile_edit'] = openerp.Class.extend({

    init: function() {
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

    }
});
