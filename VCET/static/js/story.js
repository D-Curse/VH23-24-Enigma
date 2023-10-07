var slideIndex = 0;
var slides = document.getElementsByClassName("mySlides");

function showSlides() {
    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {
        return;
    }
    slides[slideIndex - 1].style.display = "block";
}

showSlides();

function replaySlides(audioElement) {
    if (audioElement) {
        audioElement.play();
    }
}


function nextSlide() {
    showSlides();
}



