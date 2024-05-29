$(document).ready(function() {
    function checkSize() {
      if ($(window).width() <= 1300) {
        $("body").css("background-color", "#f0f0f0"); // Change background color
        $("#resolution").text($(window).width() + "x" + $(window).height()); // Show resolution
        $("#resolution").show(); // Show the resolution element
      } else {
        $("body").css("background-color", "#1c7cb5"); // Reset background color
        $("#resolution").hide(); // Hide the resolution element
      }
    }
  
    checkSize();
    $(window).resize(checkSize);
  });
  