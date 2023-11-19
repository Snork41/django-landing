// Slick slider
$('.slider-main').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    centerMode: true,
    asNavFor: '.slider-images'
  });
  $('.slider-images').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    asNavFor: '.slider-main',
    dots: false,
    centerMode: true,
    focusOnSelect: true,
    arrows: true,
    prevArrow:"<img class='a-left control-c prev slick-prev' src='static/img/slick-arrow-prev.png'>",
    nextArrow:"<img class='a-right control-c next slick-next' src='static/img/slick-arrow-next.png'>",
    variableWidth: true,
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          infinite: true
        }
      },
      {
        breakpoint: 800,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          arrows: false
        }
      }
    ]
  });

// Открытие изображения на full
$('#fullImgModal').on('show.bs.modal', function (e) {
  var $trigger = $(e.relatedTarget);
  var fullImageUrl = $trigger.data('bs-full-src');
  $('#carouselFull .carousel-inner').find('.active img').attr('src', fullImageUrl);
});