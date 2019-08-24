$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active col-md-0 offset-md-0');
        $('#content').toggleClass('col-md-11');
        $(this).toggleClass('active');
    });

    $('.icon').each(function () {
        $(this).on('click', function () {
            let currentTag = $(this);
            if (currentTag.hasClass('current'))
                return;

            $('.current').removeClass('current');
            currentTag.addClass('current');
            $.ajax({
                type: "GET",
                url: '/change_page',
                data: {
                    'page': $(this).find('.icon-text').text(),
                },
                success: function (data) {
                    $('main').html(data);
                }
            });

        });
    });

    $('.tag').each(function () {
        $(this).on('click', function () {
            $(this).toggleClass('active');
        })
    });

    $('.view').each(function () {
        $(this).on('click', function(){
            $('.view').removeClass('active');
            $(this).addClass('active');

            let cards = $('.card');
            if (cards.hasClass('video')){
                cards.toggleClass('flex-row');
                cards.toggleClass('flex-wrap');
            }

            cards.toggleClass('col-sm-4');
        });
    });

});

