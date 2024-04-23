const form = document.getElementById("contact-form");
const errorMessage = document.getElementById("error-message");

form.addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent default form submission

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const message = document.getElementById("message").value;

  // Check if any field is empty
  if (name === "" || email === "" || message === "") {
    errorMessage.textContent = "Please fill in all required fields.";
    return; // Prevent form submission if empty fields exist
  }

  // Simulate submission (replace with actual logic)
  console.log(`Name: ${name}, Email: ${email}, Message: ${message}`);

  // Open a new window with thank you message
  const thankYouWindow = window.open("", "", "width=400,height=200");
  thankYouWindow.document.write(`Tack, ${name} för ditt meddelande!!`);
});
