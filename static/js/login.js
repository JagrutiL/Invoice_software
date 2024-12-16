document.getElementById("loginForm").addEventListener("submit", function(event) {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var emailError = document.getElementById("email_error");
    var passwordError = document.getElementById("password_error");

    // Clear previous error messages
    emailError.textContent = "";
    passwordError.textContent = "";

    var hasError = false;

    // Email validation
    if (email.trim() === "") {
        emailError.textContent = "Email is required.";
        hasError = true;
    }

    // Password validation
    var passwordPattern = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$/;
    if (password.trim() === "") {
        passwordError.textContent = "Password is required.";
        hasError = true;
    } else if (!passwordPattern.test(password)) {
        passwordError.textContent = "Password must be 8-20 characters long, contain a capital letter, a number, and a special character.";
        hasError = true;
    }

    if (hasError) {
        event.preventDefault(); // Prevent form submission
    }
});

// Toggle password visibility and icon
const togglePassword = document.querySelector('#togglePassword');
const passwordInput = document.querySelector('#password_login');

togglePassword.addEventListener('click', function () {
    // Toggle the type attribute 
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);

    // Toggle the eye icon
    if (type === 'text') {
        togglePassword.src = "../static/img/cut-eye.png"; // Closed eye icon
    } else {
        togglePassword.src = "../static/img/eye.png"; // Open eye icon
    }
});