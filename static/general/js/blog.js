$(document).ready(function () {
    let baseUrl = window.location.href;

    window.addEventListener("popstate", function(e) {
        window.location.href = location.href;
    });

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
            let pageRedirect = $(this).find('.icon-text').text();
            $.ajax(getPage(pageRedirect, baseUrl));
        });
    });

    $('.tag').each(function () {
        $(this).on('click', function () {
            $(this).toggleClass('active');
        })
    });

    $.ajax(getPage("videos", baseUrl));
});

function getPage(page, baseUrl){
    return {
        type: "GET",
        url: '/change_page',
        data: {
            'username': window.location.href.match(/\/\.([a-zA-Z0-9]+)\/?/)[1],
            'page': page,
        },
        success: function (data) {
            $('main').html(data);
            window.history.pushState("", "", baseUrl + "/" + page )
        }
    }
}