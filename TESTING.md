# Coached by Caoimhe Testing

This is the documentation for the testing file. If you would like to the view the README.md click **[here!](README.md)**

## Table of Contents

1. [Validation](#validation)
2. [Security](#security)
3. [Responsiveness](#responsiveness)
4. [Functionality](#functionality)
5. [User Stories](#user-stories)
6. [Resolved Bugs](#resolved-bugs)
7. [Unresolved Bugs](#unresolved-bugs)

## Validation

### HTML Validation

All tests are run through [HTML Validation Service](https://validator.w3.org/). and came out with no errors.

### CSS Validation

All tests are run through [CSS Validation Service](https://jigsaw.w3.org/css-validator/). and came out with 5 warnings which after closer inspection are nothing to worry about.

### JavaScript Validation

All tests are run through [JS Validation Service](https://beautifytools.com/javascript-validator.php/). and came out with no errors only warnings that `$` was no defined.

### Python Validation

All tests are run through [Python Validation Service](https://extendsclass.com/python-tester.html).

**PLEASE NOTE:** Warnings and errors were given on most pages due to template logic being used. Certain files failed PEP\* due to base code set by Django.

## Security

All pages were tested with a basic account without any special permissions to make sure that no special features were available.
Attempt to access a page that requires special permissions will result in a 403 error or a redirect to the login page.

## Responsiveness

The responsiveness of the website was tested by using google chrome and Firefox on a Windows 11 machine. Safari on iPad and iPhone, google chrome and opera on a Xiaomi Mi 10. I found no limitations on the responsiveness of the website.

## Functionality

### The Navigation Bar

- The nav bar is fixed to the top of the screen and is always visible.
- The nav bar is responsive and will change to a mobile version when the screen is too small.
- All links in the nav bar are connected to the correct pages.
- The two drop down menus are responsive and are always visible.
- The search bar is responsive and functional.
- All links change color when hovered over.

### The Footer

- The footer is fixed to the bottom of all content.
- Links in the footer are connected to the correct pages.
- Login and register links are only visible when not logged in.
- the footer is fully responsive and will change to a mobile version when the screen is too small.

### The Home Page

- The background animate color changes infinitely.
- The CTA button leads the user to the all workouts page.
- The text on the home page is responsive and changes to a mobile version when the screen is too small.

### Workouts Page

- All the correct images are connected to the correct workouts.
- The workouts all display the correct information.
- The workouts are responsive and change to a mobile version when the screen is too small.
- When searched in the search bar the correct workouts are displayed.
- When the image or the "Details" button is clicked the correct workout is displayed.
- All hover effects are correct.

### Workout Details Page

- Image is connected to the correct workout.
- All the correct information is displayed.
- The workout details page is responsive and changes to a mobile version when the screen is too small.
- The "Back" button leads the user to the workouts page.
- The "Add to Cart" button leads the user to the cart page.
- Reviews show reviews from users for that specific workout.
- The user can only leave a review if they are logged in.
- The user can leave all the fields blank but must leave at least 1 star
- If there are no reviews there is text saying there are no reviews.

### About Page

- The about page is responsive and changes to a mobile version when the screen is too small.
- All information is correct and the buttons are connected to the correct pages.

### Contact Page

- The contact page is responsive and changes to a mobile version when the screen is too small.
- The embedded map is responsive and changes to a mobile version when the screen is too small.
- The map is connected to the correct location and has the API key hidden.
- All information is correct and the buttons are connected to the correct pages.
- The user can submit a form that will send an email to the correct email address.

### Cart Page

- Workout details are connected to the correct workout and displayed.
- Total adds correctly if more than on product is added.
- The cart page is responsive and changes to a mobile version when the screen is too small.
- The "Checkout" button leads the user to the checkout page.
- The "Back" button leads the user to the workouts.
- The "Remove" button removes the product from the cart.
- When no products are in the cart there is a text saying there are no products in the cart and a button that directs to workouts.

### Checkout Page

- The checkout page is responsive and changes to a mobile version when the screen is too small.
- The order summary is correct and displays the correct information.
- Checkout form is correctly displayed to the user and auto fills the correct information if it was saved to the database.
- Default stripe card is used for payments and have no issues.
- Payment won't be processed if the form is not filled out correctly, errors will be displayed.
- Payment won't be processed if the card details are incorrect, errors will be displayed.
- The back button leads the user to the cart page.
- The "Checkout" button leads the user to the checkout success page.

### Checkout Success Page

- The checkout success page is responsive and changes to a mobile version when the screen is too small.
- The correct information is displayed.
- If the user is not logged in the user will see a button that will redirect to the workouts page.
- If the user is logged in the user will see a button that will redirect to the profile page.

### Sign Up / Login Page

- The sign up / login page is responsive and changes to a mobile version when the screen is too small.
- The correct form is displayed for each page.
- The sign up form allows the user to sign up using their email and password.
- The login form allows the user to login using their email and password.
- The user can only sign up if the email is not already in use.
- On the login in page there is a checkbox that allows the users details to be saved to the database.

### Profile Page

- The profile page is responsive and changes to a mobile version when the screen is too small.
- The correct information is displayed.
- The user can only edit their information if they are logged in.
- Updated information is saved to the database and displayed the next time the user goes to the checkout page.

#### Add/Edit Workouts

- The add/edit workouts page is responsive and changes to a mobile version when the screen is too small.
- The correct form is displayed for each page.
- Removing an image will remove the image from the workout.
- Adding an image will add the image to the workout.
- Cancel button will lead the user to the workouts page.
- Save button will save the workout to the database.

#### Error Pages

- I could only find a way to test the 404 page but the structure is the same as the other pages and they're all in the right directory.
- The error page is responsive and changes to a mobile version when the screen is too small.
- The Home button leads the user to the home page.

## User Stories

### First User Stories

"To easily understand the site and its features."
"To see clearly what the site has to offer."

- Coached by Caoimhe logo
- CTA action, one click away from the workouts page
- About link in the navbar will lead to the about page

"To be able to buy workout plans and be coached online and/or in person by a qualified personal trainer."

- Workouts page with many options to choose from
- Contact form to get in touch with the Trainer

"Create an account and sign in to access the site."

- Sign up form to create an account
- Register links located int he navbar and the footer.
- Register button in the sign in page will lead to the sign up page

"Know about the personal trainer and their qualifications."

- About page with personal trainer information
- Contact page with personal trainer details to contact for further information

"To easily find the contact information of the personal trainer."

- Contact link located in the navbar and the footer, will lead to the contact page
- Contact page with personal trainer details to contact for further information

### Recurring User Stories

"To log in and sign up for coaching"

- Login form to log in
- Register links located in the navbar and the footer.
- Workouts page with many options to choose from
- Secure payment through stripe to buy workout plans

"To login in and check my profile."

- Login form to log in
- Profile link located in the account dropdown that's only visible when logged in

"To have all my personal data stored."

- Billing information will be stored in the database along with the users full name and email

"To have previous purchases stored."

- Previous purchases can be seen in the users profile, must have an account to do this.

"To have a secure way to pay for my workout plans."

- Stripe payment form to securely pay for workout plans

"To receive a confirmation email when I buy a workout plan."

- Email will be sent to the user when they buy a workout plan with the order date, order number and the total cost

"To subscribe to the site and so I can receive an email with information in the future."

- Email subscription form to subscribe to the site is located in the footer. The email is store in the database for future use.

### Admin/site owner User Stories

"To be able to add new workout plans."

- Add workout page with all the correct functioning inputs needed to add a workout, only accessible by superusers

"To be able to edit existing workout plans."

- Edit workout page with all the correct functioning inputs needed to edit a workout, only accessible by superusers

"To be able to delete existing workout plans."

- Delete workout button used to delete a workout, only accessible by superusers

## Resolved Bugs

### UnboundLocalError: local variable 'category' referenced before assignment

#### Fixed

- In the all_workouts view I declared "category" as a variable and then used the variable "categories". This caused an error and was easily fixed by changing the variable name to "categories".

### Payments would not be processed

#### Fixed

- There was an issue with my jQuery code where the payment form was not being submitted and the loading spinner would spin forever. I looked through the boutique ado and found a solution to this issue but changing the some of the code back to JS.

### Toast success message cart preview, not working as intended

#### Fixed

- The contents of the cart preview were overflowing the container and the CSS was not being applied correctly. This lead me to believe that perhaps one or more HTML closing tags were missing. Looking through the code I found that the closing tags were missing in the `.toast-body` container and the `.card-notifaction-wrapper` closing tag was inside the for loop when it should been just outside.

## Unresolved Bugs

### Bootstrap 5 toasts not working

#### Current status

- Issues with the bootstrap 5 toasts not working while tryin to initialize them with jQuery. I noticed an error in the console saying `(...).toast()` is not a function. I tried to initialize the toasts with vanilla JavaScript which removed the error but the toasts still didn't show when called. Due to time constraints on this project I decided to link bootstrap 4 popper and JavaScript to the project to allow the toasts to work.
