/* Jquery kod */
$(document).ready(function() {
    $("#toggleNav").click(function() {
      $("#navigation").toggleClass("hidden");
      if ($("#navigation").hasClass("hidden")) {
        $(this).text("Visa meny");
      } else {
        $(this).text("Göm meny");
      }
    });
  });
  
  