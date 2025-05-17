console.log("Stripe elements loaded");

// Initialize Stripe
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

// Create a card element
const card = elements.create('card', {
    style: {
        base: {
            color: '#000',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    }
});
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

// Handle form submission
const form = document.getElementById('payment-form');
form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    
    card.update({ 'disabled': true });
    document.querySelector('button[type="submit"]').disabled = true;

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: form.full_name.value.trim(),
                phone: form.phone_number.value.trim(),
                email: form.email.value.trim(),
                address: {
                    line1: form.street_address1.value.trim(),
                    line2: form.street_address2.value.trim(),
                    city: form.town_or_city.value.trim(),
                    country: form.country.value,
                    state: form.county.value.trim(),
                    postal_code: form.postcode.value.trim(),
                }
            }
        }
    }).then(function(result) {
        if (result.error) {
            const errorDiv = document.getElementById('card-errors');
            errorDiv.textContent = result.error.message;
            card.update({ 'disabled': false });
            document.querySelector('button[type="submit"]').disabled = false;
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
