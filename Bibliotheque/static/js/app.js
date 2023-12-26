var browserWindow = $(window);

if ($.fn.scrollUp) {
    browserWindow.scrollUp({
        scrollSpeed: 1500,
        scrollText: '<i class="fa fa-angle-up"></i>'
    });
}