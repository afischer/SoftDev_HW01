$(function() {

    var quotes = $(".quotes");
    var quoteIndex = -1;

    function showNextQuote() {
        ++quoteIndex;
        quotes.eq(quoteIndex % quotes.length)
            .fadeIn(700)
            .delay(600)
            .fadeOut(700, showNextQuote);
    }

    showNextQuote();

});

$(document).keydown(function(e) {
    if(e.keyCode == 13)
        $(".centered").animate({
            top: '10%'
        }, 600);
});
