$('.dropdown-toggle').dropdown();
$('body').on('touchstart.dropdown', '.dropdown-menu', function (e) { e.stopPropagation(); });
