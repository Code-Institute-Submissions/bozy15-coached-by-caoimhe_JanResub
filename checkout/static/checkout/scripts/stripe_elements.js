/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    and here:
    https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/a75791ce63bfce9a05f614d7712199c893063ed9/checkout/static/checkout/js/stripe_elements.js
    
    CSS from here: 
    https://stripe.com/docs/stripe-js

   
*/

// Get public key from DOM and remove the quotes
let stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
// Get client secret from DOM and remove the quotes
let clientSecret = $("#id_client_secret").text().slice(1, -1);
// Set up Stripe
let stripe = Stripe(stripePublicKey);
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

// Handle realtime validation errors on the card element
card.on("change", (event) => {
  let errorDiv = $("#card-errors");
  if (event.error) {
    // Display error on your form
    let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = "";
  }
});

// Handle form submit
form = $("#payment-form");

form.submit((ev) => {
  ev.preventDefault(); // Prevent the form from submitting on its own
  card.update({ disabled: true }); // Disable the card element, prevent double submission
  $("#submit-button").attr("disabled", true); // Disable the submit button
  $("#payment-form").fadeToggle(100); // Fade out the form
  $("#loading-overlay").fadeToggle(100); // Fade in the loading overlay

  // Get the checkbox value
  let saveInfo = Boolean($("#id-save-info").attr("checked"));
  // From using {% csrf_token %} in the form
  let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  // Create a new object with the data to send
  let postData = {
    csrfmiddlewaretoken: csrfToken,
    client_secret: clientSecret,
    save_info: saveInfo,
  };
  // The url to send the data to
  let url = "/checkout/cache_checkout_data/";

  // Send the data to the server
  $.post(url, postData)
    .done(function () {
      stripe
        .confirmCardPayment(clientSecret, {
          payment_method: {
            card: card,
            billing_details: {
              // Send the billing details to Stripe
              name: $.trim(form.full_name.value),
              phone: $.trim(form.phone_number.value),
              email: $.trim(form.email.value),
              address: {
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                state: $.trim(form.county.value),
              },
            },
          },
          shipping: {
            // Not needed for now, future proofing
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            address: {
              line1: $.trim(form.street_address1.value),
              line2: $.trim(form.street_address2.value),
              city: $.trim(form.town_or_city.value),
              country: $.trim(form.country.value),
              postal_code: $.trim(form.postcode.value),
              state: $.trim(form.county.value),
            },
          },
        })
        .then((result) => {
          if (result.error) {
            let errorDiv = $("#card-errors");
            // Display error on form
            let html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $("#payment-form").fadeToggle(100); // Fade in the form
            $("#loading-overlay").fadeToggle(100); // Fade out the loading overlay
            card.update({ disabled: false }); // Re-enable the card element
            $("#submit-button").attr("disabled", false); // Re-enable the submit button
          } else {
            // if the payment was successful submit the form
            if (result.paymentIntent.status === "succeeded") {
              form.submit();
            }
          }
        });
    })
    .fail(function () {
      // just reload the page, the error will be in django messages
      location.reload();
    });
});
