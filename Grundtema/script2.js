const myButton = document.getElementById("myButton");

myButton.addEventListener("click", function () {
  const screenWidth = screen.width;
  const screenHeight = screen.height;
  const newWindowWidth = 300;
  const newWindowHeight = 200;

  const leftPosition = (screenWidth - newWindowWidth) / 2;
  const topPosition = (screenHeight - newWindowHeight) / 2;

  const newWindow = window.open(
    "",
    "",
    `width=${newWindowWidth},height=${newWindowHeight},top=${topPosition},left=${leftPosition}`
  );

  // Create elements for the new window's content
  newWindow.document.write(
    "<p>Hejsan! Jag vill bara tacka för att ni besökt min sida, det är väldigt snällt och jag blir fruktansvärt glad för detta! ;) Klicka på knappen ok för att stänga den rutan.</p>"
  );
  const closeButton = newWindow.document.createElement("button");
  closeButton.textContent = "OK";
  newWindow.document.body.appendChild(closeButton);

  // Add the close functionality
  closeButton.addEventListener("click", function () {
    newWindow.close();
  });
});
