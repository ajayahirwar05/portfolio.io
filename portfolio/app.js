// Wait for the HTML document to fully load before running scripts
document.addEventListener("DOMContentLoaded", () => {
    // 1. Cache DOM elements to avoid repeated querying
    const contactForm = document.querySelector("#contact-form");
    const nameInput = document.querySelector("#name");
    const emailInput = document.querySelector("#email");
    const messageInput = document.querySelector("#message");

    const nameError = document.querySelector("#name-error");
    const emailError = document.querySelector("#email-error");
    const messageError = document.querySelector("#message-error");
    const formStatus = document.querySelector("#form-status");

    if (!contactForm || !nameInput || !emailInput || !messageInput || !nameError || !emailError || !messageError || !formStatus) {
        return;
    }

    // 2. Attach submit event listener to the contact form
    contactForm.addEventListener("submit", (event) => {
        // Prevent default browser form submission
        event.preventDefault();

        // Clear previous error messages and status styles
        nameError.textContent = "";
        emailError.textContent = "";
        messageError.textContent = "";
        formStatus.textContent = "";
        formStatus.className = "form-status";

        let isValid = true;

        // Validate Name
        if (nameInput.value.trim() === "") {
            nameError.textContent = "Please enter your name.";
            isValid = false;
        }

        // Validate Email
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (emailInput.value.trim() === "") {
            emailError.textContent = "Please enter your email address.";
            isValid = false;
        } else if (!emailPattern.test(emailInput.value.trim())) {
            emailError.textContent = "Please enter a valid email address.";
            isValid = false;
        }

        // Validate Message
        if (messageInput.value.trim() === "") {
            messageError.textContent = "Please enter a message.";
            isValid = false;
        }

        // If validation passes, show success status
        if (isValid) {
            const name = nameInput.value.trim();
            formStatus.textContent = `Thank you, ${name}! Your message has been sent successfully.`;
            formStatus.classList.add("success");

            // Reset input fields
            contactForm.reset();
        }
    });
});
