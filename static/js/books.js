/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */

var prevScrollpos = window.pageYOffset;

window.onscroll = function() {

  var currentScrollPos = window.pageYOffset;

  if (prevScrollpos > currentScrollPos) {

    document.getElementById("navbar").style.top = "0";

  } else {

    document.getElementById("navbar").style.top = "-100px";

  }
  // log.console("ssss")

  prevScrollpos = currentScrollPos;

}


/* Open */

function openNav() {

  document.getElementById("myNav").style.display = "block";
  console.log("why");
}


/* Close */

function closeNav() {

  document.getElementById("myNav").style.display = "none";

}