$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active col-md-0 offset-md-0');
        $('#content').toggleClass('col-md-12');
        $(this).toggleClass('active');
    });

    $('.icon').each(function () {
        $(this).on('click', function () {
            let currentTag = $(this);
            if (currentTag.hasClass('current'))
                return;

            $('.current').removeClass('current');
            currentTag.addClass('current');

        })
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
            cards.toggleClass('flex-row');
            cards.toggleClass('flex-wrap');
            cards.toggleClass('col-sm-4');
        });
    });

    $('.like').each(function () {
       $(this).on('click', function () {
           let currentTag = $(this);
           let childTag = currentTag.find('small');

           if (currentTag.hasClass('active'))
               childTag.text(childTag.text() - 1);
           else
               childTag.text( Number(childTag.text()) + 1);

           currentTag.toggleClass('active');
       })
    });

});