/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    and here:
    https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/a75791ce63bfce9a05f614d7712199c893063ed9/checkout/static/checkout/js/stripe_elements.js
    
    CSS from here: 
    https://stripe.com/docs/stripe-js

   
*/

// Get public key from DOM and remove the quotes
let stripe_public_key = $("#id_stripe_public_key").text().slice(1, -1);
// Get client secret from DOM and remove the quotes
let client_secret = $("#id_client_secret").text().slice(1, -1);
// Set up Stripe
let stripe = Stripe(stripe_public_key);
// Create an instance of Elements
let elements = stripe.elements();

let style = {
  base: {
    color: "#000",
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4",
    },
  },
  // Colours used to match bootstrap 5 danger class
  invalid: {
    color: "#dc3545",
    iconColor: "#dc3545",
  },
};
// Create card element and apply above styles
let card = elements.create("card", { style: style });
// Add an instance of the card element into the `card-element` <div>
card.mount("#card-element");
