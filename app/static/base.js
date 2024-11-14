$(document).ready(function() {
    var lastScrollTop = 0;
    $(window).scroll(function(event) {
        var st = $(this).scrollTop();
        if (st > lastScrollTop) {
            // Scroll Down
            $('header').slideUp();
        } else {
            // Scroll Up
            $('header').slideDown();
        }
        lastScrollTop = st;
    });
});
