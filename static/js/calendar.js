var today = new Date();
var dd = today.getDate();
if (dd < 10) {
  dd = "0" + dd;
}

dd = "day-" + dd;
var elmnt = document.getElementById(dd);
elmnt.scrollIntoView({ block: "end", behavior: "smooth" });
elmnt.className += " highlight";

$("#forBtn").click(function() {
  $("#Calendar").animate({ scrollLeft: "+=40px" }, 800);
});

$("#backBtn").click(function() {
  $("#Calendar").animate({ scrollLeft: "-=40px" }, 800);
});
