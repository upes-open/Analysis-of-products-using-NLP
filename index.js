
// Search Products button
document.querySelector(".lefttop-btn").addEventListener("click", function() {
    document.querySelector(".searchinput").focus();
});



// scrolling navbar becomes opaque
const navbar = document.querySelector('.nav');
window.onscroll = () => {
    if (window.scrollY > 90) {
        navbar.classList.add('nav-active');
    } else {
        navbar.classList.remove('nav-active');
    }
};



// middle page results cards carousel

var swiper = new Swiper(".slide-content", {
    slidesPerView: 3,
    spaceBetween: 30,
    slidesPerGroup: 3,
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });



// clicking search button goes to results
document.querySelector(".searchicon").addEventListener("click", function() {
    document.querySelector("#midd").scrollIntoView(false);
});

document.querySelector(".searchinput").addEventListener("keypress", function(event) {
    if (event.key === "Enter"){
        document.querySelector(".searchinput").blur();
        document.querySelector("#midd").scrollIntoView(false);
    }
});
