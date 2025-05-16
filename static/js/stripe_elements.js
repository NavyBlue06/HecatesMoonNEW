console.log("Stripe elements loaded");

// Initialize Stripe
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

// Create a card element
const card = elements.create('card');
card.mount('#card-element');

// Handle real-time validation errors
card.on('change', function(event) {
    const errorDiv = document.getElementById('card-errors');
    if (event.error) {
        errorDiv.textContent = event.error.message;
    } else {
        errorDiv.textContent = '';
    }
});
