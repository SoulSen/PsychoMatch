let patient = document.getElementById("button_patient")

let button = document.getElementById("button_psychologist");

patient.onclick = function() {
    location.href = "patient";
}

button.onclick = function() {
    location.href = "psychologist";
}

window.onscroll = function() {
    myFunction()
};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function myFunction() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky")
    } else {
        navbar.classList.remove("sticky");
    }
}