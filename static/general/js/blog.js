$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active col-md-0 offset-md-0');
        $('#content').toggleClass('col-md-12');
        $(this).toggleClass('active');
    });
});