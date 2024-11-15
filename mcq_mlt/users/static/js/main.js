const body = document.body;
let lastScroll = 0;

// window.addEventListener("scroll", () => {
// 	const currentScroll = window.pageYOffset;
// 	if (currentScroll <= 0) {
// 		body.classList.remove("scroll-up");
// 		return;
// 	}

// 	if (currentScroll > lastScroll && !body.classList.contains("scroll-down")) {
// 		body.classList.remove("scroll-up");
// 		body.classList.add("scroll-down");
// 	} else if (
// 		currentScroll < lastScroll &&
// 		body.classList.contains("scroll-down")
// 	) {
// 		body.classList.remove("scroll-down");
// 		body.classList.add("scroll-up");
// 	}
// 	lastScroll = currentScroll;
// });

$("#search-icon").click(function() {
	$(".nav").toggleClass("search");
	$(".nav").toggleClass("no-search");
	$(".search-input").toggleClass("search-active");
  });
  
  $('.menu-toggle').click(function(){
	  console.log('deam');
	 $(".nav").toggleClass("mobile-nav");
	 $(this).toggleClass("is-active");
  });
  