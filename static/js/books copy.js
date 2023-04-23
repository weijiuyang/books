/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */

var prevScrollpos = window.pageYOffset;
var name;

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

}




/* Close */

function closeNav() {

  document.getElementById("myNav").style.display = "none";

}

/* Set the width of the side navigation to 250px */
function openSideNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function closeSideNav() {
  document.getElementById("mySidenav").style.width = "0";
}






/* Open */
var curelementId = null;

function playAudio(name) {
  if (document.getElementById(curelementId)) {
    document.getElementById(curelementId).pause();
  }
  audio = document.getElementById(name);
  aduiotext = document.getElementById('text_'+name);
  // print(typeWriter)
  console.log(audio)
  console.log(aduiotext)
  console.log(aduiotext.text)

  console.log(name)

  // text = typeWriter.id;
  duration = audio.duration
  var textlength = aduiotext.text.length
  // typeWriter.innerHTML = '';
  let i = 0;
  charInterval = duration / textlength
  console.log(textlength)
  console.log(duration)


  // aduiotext.classList.add("masked-text-animation");
  // var currentLength = 0;

  // function animateMask() {
  //   currentLength++;
  //   var textLength = aduiotext.textContent.length;

  //   var percentage = currentLength / textLength * 100;
  //   console.log(currentLength,percentage)

  //   var maskImage = "linear-gradient(to right, transparent, black " + percentage + "%)";
  //   console.log(maskImage)

  //   aduiotext.style.webkitMaskImage = maskImage;
  //   aduiotext.style.maskImage = maskImage;
    
  //   if (currentLength < textLength) {
  //     console.log(currentLength,charInterval)
  //     setTimeout(animateMask, charInterval);
  //   } else {
  //     aduiotext.classList.remove("masked-text-animation");
  //   }
  // }
  
  // aduiotext.textContent = aduiotext.textContent.trim(); // 去除首尾空格
  // aduiotext.classList.add("masked-text-animation"); // 添加动画类
  // aduiotext.style.animationDuration = duration +'s';
  // aduiotext.style.animationDuration = `${animationDuration}s`;
  aduiotext.style.animation = ``;

  aduiotext.offsetHeight; 
  // aduiotext.classList.add("breathe"); // 添加动画类

  aduiotext.style.animation = `breathe 1s ease-in-out `;
  console.log(aduiotext.style.animation)
  // aduiotext.style.animationDuration = "100s";
  aduiotext.style.animationIterationCount = Math.round(duration)
  console.log('ttt')

  console.log(aduiotext.style.animationIterationCount)

  console.log(aduiotext.style.animationDuration)
  console.log('ttt')

  // console.log('ttt')

  // animateMask(); // 开始动画
  // console.log('ss')

  
  // aduiotext.innerHTML = aduiotext.textContent.replace(/./g, `<a>$&</a>`);

  // const spans = aduiotext.querySelectorAll('a');
  // console.log(spans)
  // spans.forEach((span, index) => {
  //   span.style.animationDelay = `${index * 100}ms`; // 这里可以调整动画的速度
  // });
  // const timer = setInterval(() => {
  //   if (i < textlength) {
  //     aduiotext.text.style = "h3";
  //     i++;
  //   } else {
  //     clearInterval(timer);
  //   }
  // }, charInterval);
  curelementId = name;
  console.log(curelementId)
  document.getElementById(name).play();
  aduiotext.classList.remove("breathe");

}



