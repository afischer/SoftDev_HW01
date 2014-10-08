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

})();
