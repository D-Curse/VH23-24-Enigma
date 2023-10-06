var slideIndex = 0;
var slides = document.getElementsByClassName("mySlides");

function showSlides() {
    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {
        // Redirect to another URL when all images are displayed
        window.location.href = "/home/";
        return;
    }
    slides[slideIndex - 1].style.display = "block";
    //setTimeout(showSlides, 2000); // Change image every 2 seconds (adjust as needed)
}

// Initial call to start the slideshow
showSlides();

function translateSlides() {
    // Add code to translate slides here if needed
}

function nextSlide() {
    showSlides();
}



