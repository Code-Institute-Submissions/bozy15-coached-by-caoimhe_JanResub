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

## Security

## Responsiveness

## Functionality

## User Stories

## Resolved Bugs

### UnboundLocalError: local variable 'category' referenced before assignment

#### Fixed

- In the all_workouts view I declared "category" as a variable and then used the variable "categories". This caused an error and was easily fixed by changing the variable name to "categories".

### Payments would not be processed

#### Fixed

- There was an issue with my jQuery code where the payment form was not being submitted and the loading spinner would spin forever. I looked through the boutique ado and found a solution to this issue but changing the some of the code back to JS.

## Unresolved Bugs

### Bootstrap 5 toasts not working

#### Current status

- Issues with the bootstrap 5 toasts not working while tryin to initialize them with jQuery. I noticed an error in the console saying `(...).toast()` is not a function. I tried to initialize the toasts with vanilla JavaScript which removed the error but the toasts still didn't show when called. Due to time constraints on this project I decided to link bootstrap 4 popper and JavaScript to the project to allow the toasts to work.
