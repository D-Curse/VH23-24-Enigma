var slideIndex = 0;
var slides = document.getElementsByClassName("mySlides");

function showSlides() {
    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {
        window.location.href = "/home/";
        return;
    }
    slides[slideIndex - 1].style.display = "block";
    audioElements[slideIndex - 1].play();
}

showSlides();

function translateSlides() {
}

function nextSlide() {
    showSlides();
}



