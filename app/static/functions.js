$(document).ready(function(){
    $('.cardBack').hide();
    if ($('.memorizePanel').length != 0) {

        $('.flipCard').click(function(){
            if ($('.cardFront').is(":visible") == true) {
                $('.cardFront').hide();
                $('.cardBack').show();
            } else {
                $('.cardFront').show();
                $('.cardBack').hide();
            }
        });
    }
});

