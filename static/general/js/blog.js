$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active col-md-0 offset-md-0');
        $('#content').toggleClass('col-md-12');
        $(this).toggleClass('active');
    });

    $('.icon').each(function () {
        $(this).on('click', function () {
            if ($(this).hasClass('current'))
                return;

            $('.current').each(function () {
                $(this).removeClass('current');
                $(this).find('path').attr('fill', 'white');
            })

            $(this).addClass('current');
            $(this).find('path').attr('fill', '#6dbad6');
        })
    });

    $('.tag').each(function () {
        $(this).on('click', function () {
            $(this).toggleClass('active');
        })
    });
});