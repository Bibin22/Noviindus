/*
====================================
[ CSS TABLE CONTENT ]
------------------------------------
    
	
	1.0 - Pre Loader
	2.0 - MOBILE MENU
	3.0 - COUNTER
	4.0 - OUR CLIENTS CAROUSEL
	5.0 - TESTIMONIAL 1
	6.0 - TESTIMONIAL 2
	7.0 - ACCORDIAN
	8.0 - FOOTER REVEAL
	9.0 - HEADER FIXED
	10.0 - SELECT 2
	11.0 - SCROLL TO TOP
	12.0 - POST SLIDER
	13.0 - FILE UPLOADER
	14.0 - NAV BAR FIXED
	
-------------------------------------
[ END CSS TABLE CONTENT ]
=====================================
*/
(function($) {
    "use strict";
    
    /*--- MOBILE MENU---*/
    $('#mobile-menu-active').meanmenu({
        meanScreenWidth: "991",
        meanMenuContainer: ".mobile-menu",
    });

    /*--- Counter Up---*/

    $('.counter').counterUp({
        delay: 10,
        time: 2000
    });

    /*--- OUR CLIENTS CAROUSEL---*/

    $(".clients-list").owlCarousel({
        autoPlay: true,
        slideSpeed: 2000,
        pagination: false,
        navigation: false,
        loop: true,
        items: 6,
        itemsDesktop: [1199, 4],
        itemsDesktopSmall: [980, 4],
        itemsTablet: [768, 4],
        itemsTabletSmall: false,
        itemsMobile: [479, 2],
    });

    /*--- TESTIMONIAL 1---*/

    $("#owl-testimonial").owlCarousel({
        navigation: false,
        slideSpeed: 600,
        paginationSpeed: 700,
        autoPlay: 5000,
        navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        pagination: false,
        responsive: true,
        loop: true,
        /*"singleItem:true" is a shortcut for:*/
        items: 2

    });

    /*--- TESTIMONIAL 2---*/

    $(".owl-testimonial-2").owlCarousel({
        autoPlay: true,
        slideSpeed: 2000,
        pagination: false,
        navigation: false,
        loop: true,
        items: 3,
        itemsDesktop: [1199, 3],
        itemsDesktopSmall: [980, 2],
        itemsTablet: [768, 2],
        itemsTabletSmall: false,
        itemsMobile: [479, 1]
    });

    /*--- ACCORDIAN---*/

    $('.panel-heading').on('click', function(e) {
        $('.panel-heading').removeClass('tab-collapsed');
        var collapsCrnt = $(this).find('.collapse-controle').attr('aria-expanded');
        if (collapsCrnt != 'true') {
            $(this).addClass('tab-collapsed');
        }
    });

    /*--- FOOTER REVEAL---*/

    $('.fixed-footer').footerReveal({
        shadow: false,
        zIndex: -101
    });

    /*--- HEADER FIXED---*/
    $(window).on('scroll', function() {

        var scrollTop = $(window).scrollTop();
        if (scrollTop > 300) {
            $("header").addClass("navbar-fixed-top");
            $("body").addClass("padding-top-body");

        } else if (scrollTop < 300) {
            $("header").removeClass("navbar-fixed-top");
            $("body").removeClass("padding-top-body");
        }

    });

    /*--- SELECT 2 INITIALIZATION---*/
    $(".questions-category").select2({
        placeholder: "Select Category",
        allowClear: true,
        maximumSelectionLength: 3,
    });
    $(".select-category ").select2({
        placeholder: "Select Budget",
        allowClear: true,
        maximumSelectionLength: 3,
    });
    $(".select-location ").select2({
        placeholder: "Vehicle Type",
        allowClear: true,
        maximumSelectionLength: 3,
    });
    $(".select-general").select2({
        placeholder: "Choose",
        allowClear: true,
    });
    $(".select_dealer_city").select2({
        placeholder: "Choose Your City",
        allowClear: true,
        maximumSelectionLength: 3,
    });
    $(".select_dealer").select2({
        placeholder: "Choose the Dealer",
        allowClear: true,
    });  
    $(".onroad_price_loc ").select2({
        placeholder: "-----------",
        allowClear: true,
        maximumSelectionLength: 3,
    });
    $(".used_veh_budget ").select2({
        placeholder: "Select Budget",
        allowClear: true,
        maximumSelectionLength: 3,
    });
    $(".used_veh_city ").select2({
        placeholder: "Select City",
        allowClear: true,
        maximumSelectionLength: 3,
    });
    $(".select_brand").select2({
        placeholder: "Select Brand/Model",
        allowClear: true,
        maximumSelectionLength: 3,
    });
    $(".select_variant").select2({
        placeholder: "Select Variant",
        allowClear: true,
        maximumSelectionLength: 3,
    });
    /*--- SCROLL TO TOP---*/
    $(document).ready(function() {

        $(window).scroll(function() {
            if ($(this).scrollTop() > 100) {
                $('.scrollup').fadeIn();
            } else {
                $('.scrollup').fadeOut();
            }
        });
        $('.scrollup').on('click', function() {
            $("html, body").animate({

                scrollTop: 0
            }, 600);
            return false;
        });

    });
  /*---COMPARE PRODUCT---*/
  $(document).ready(function() {
    $('[data-filter="trigger"]').on("change", function() {
        var t = $(this).find("option:selected").val().toLowerCase();
    
        $('[data-filter="target"]').css("display", "none"); 
        $("#" + t).css("display", "table-row-group"); 
        if(t == "all") {
            $('[data-filter="target"]').css("display", "table-row-group")
        }
        $(this).css("display", "block"); 
    });
    }) 

    /*--- POST SLIDER---*/

    $(".featured-slider").owlCarousel({
        navigation: false,
        pagination: false,
        autoPlay: 5000,
        navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        slideSpeed: 600,
        items: 4
    });

})(jQuery);

/*--- NAV BAR FIXED---*/
var didScroll;
var lastScrollTop = 0;
var navbarHeight = $('header').outerHeight();
$(window).on('scroll', function() {

    didScroll = true;
});

setInterval(function() {
    if (didScroll) {
        hasScrolled();
        didScroll = false;
    }
}, 250);

function hasScrolled() {
    var st = $(this).scrollTop();

    if (st <= 80) {
        $('header').removeClass('nav-down').removeClass('nav-up');
    } else {
        if (st > lastScrollTop) {
            $('header').removeClass('nav-down').addClass('nav-up');
        } 		  
		else  {
            $('header').removeClass('nav-up').addClass('nav-down');
        }
    }
    lastScrollTop = st;
}