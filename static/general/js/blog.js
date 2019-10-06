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
            $.ajax( getPage() );
        });
    });

    $('.tag').each(function () {
        $(this).on('click', function () {
            $(this).toggleClass('active');
        })
    });

    $.ajax( getPage() );
});

function getPage(){
    let page = $('.current').find('.icon-text').html();

    let url = window.location.href.split('/');
    let baseUrl = url.shift() + '//' + url.shift() + url.shift();
    let username = url.shift().replace('.', '');

    return {
        type: "GET",
        url: '/change_page',
        data: {
            username: username,
            page: page,
        },
        success: function (data) {
            $('main').html(data);
            window.history.pushState("", "", baseUrl + "/." + username + "/" + page )
        }
    }
}

function deletePost(item) {
    let currentPost = $(item);
    let postId = currentPost.find('.post').html();

    $.ajax({
        type: 'GET',
        url: '/delete_post',
        data: {
            postId: postId,
        },
        success: function (data) {
            $.ajax( getPage() );
        }
    })
}



