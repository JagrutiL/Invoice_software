function validate_upload_invoice_form(event) {
    // Prevent the form from submitting by default
    event.preventDefault();

    // Get form fields
    const invoiceName = document.getElementById("invoice_name").value.trim();
    const invoiceNo = document.getElementById("invoice_no").value.trim();
    const invoiceAmount = document.getElementById("invoice_amount").value.trim();
    const paymentMethod = document.getElementById("paymentMethod").value;
    const invoiceFile = document.getElementById("invoicename").files.length;

    // Check if all fields are empty
    if (!invoiceName || !invoiceNo || !invoiceAmount || !paymentMethod || !invoiceFile) {
        // Display error message
        const uplaod_invoice_errorMessage = document.getElementById("uplaod_invoice_errorMessage");
        uplaod_invoice_errorMessage.style.display = "block";
        uplaod_invoice_errorMessage.textContent = "Please fill all fields.";
        return false; // Prevents the form from submitting
    }

    // If all fields are filled, allow form submission
    uplaod_invoice_errorMessage.style.display = "none";
    return true; // Allows the form to submit
}