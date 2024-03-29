(function ($) {
  "use strict";
  jQuery(document).ready(function () {
    $(".nav a").on("click", function (e) {
      var anchor = $(this);
      $("html, body")
        .stop()
        .animate({ scrollTop: $(anchor.attr("href")).offset().top - 50 }, 1500);
      e.preventDefault();
    });
    $(window).scroll(function () {
      if ($(this).scrollTop() > 100) {
        $(".menu-top").addClass("menu-shrink");
      } else {
        $(".menu-top").removeClass("menu-shrink");
      }
    });
    $(document).on("click", ".navbar-collapse.in", function (e) {
      if (
        $(e.target).is("a") &&
        $(e.target).attr("class") != "dropdown-toggle"
      ) {
        $(this).collapse("hide");
      }
    });
    $(".main_menu").slicknav({ prependTo: ".mobile-nav" });
    var $grid = $(".work_content_area").isotope({});
    $(".work_filter").on("click", "li", function () {
      var filterValue = $(this).attr("data-filter");
      $grid.isotope({ filter: filterValue });
    });
    $(".work_filter").on("click", "li", function () {
      $(this).addClass("active").siblings().removeClass("active");
    });
    lightbox.option({ resizeDuration: 200, wrapAround: true });
    $("#counter_area").on("inview", function (
      event,
      visible,
      visiblePartX,
      visiblePartY
    ) {
      if (visible) {
        $(this)
          .find(".counter")
          .each(function () {
            var $this = $(this);
            $({ Counter: 0 }).animate(
              { Counter: $this.text() },
              {
                duration: 5000,
                easing: "swing",
                step: function () {
                  $this.text(Math.ceil(this.Counter));
                },
              }
            );
          });
        $(this).unbind("inview");
      }
    });
    $(".testmonial_slider_area").owlCarousel({
      autoPlay: true,
      slideSpeed: 1000,
      items: 3,
      loop: true,
      nav: true,
      navText: [
        '<i class="ti-arrow-left"></i>',
        '<i class="ti-arrow-right"></i>',
      ],
      margin: 30,
      dots: true,
      responsive: {
        320: { items: 1 },
        767: { items: 2 },
        600: { items: 2 },
        1000: { items: 3 },
      },
    });
  });
  $(window).on("load", function () {
    $(".spinner").fadeOut();
    $(".preloader").delay(350).fadeOut("slow");
  });
  new WOW().init();
})(jQuery);
