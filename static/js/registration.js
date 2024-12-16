function registration_validateForm() {
    // Get the form fields
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const contactNumber = document.getElementById('contact_number').value.trim();

    // Get the error message containers
    const nameError = document.getElementById('name_error');
    const emailError = document.getElementById('email_error');
    const contactError = document.getElementById('contact_error');
    const registration_successfully = document.getElementById('registration_successfully');

    // Clear previous error messages
    nameError.textContent = '';
    emailError.textContent = '';
    contactError.textContent = '';
    registration_successfully.textContent = '';


    // Validation flags
    let isValid = true;

    // Validate Name
    if (name === '') {
        nameError.textContent = "Name is required.";
        isValid = false;
    }

    // Validate Email
    if (email === '') {
        emailError.textContent = "Email is required.";
        isValid = false;
    } else if (!/\S+@\S+\.\S+/.test(email)) {
        emailError.textContent = "Please enter a valid email address.";
        isValid = false;
    }

    // Validate Contact Number
    if (contactNumber === '') {
        contactError.textContent = "Contact number is required.";
        isValid = false;
    } else if (isNaN(contactNumber) || contactNumber.length < 10) {
        contactError.textContent = "Please enter a valid contact number with at least 10 digits.";
        isValid = false;
    }

    // If all fields are valid, submit the form
    if (isValid) {
        registration_successfully.textContent="Registration successful"
        document.getElementById('registration_form').submit();
    }
}