# Coached by Caoimhe

[Visit the live site here!](https://coach-me.herokuapp.com/)

![Site preview](https://coach-me.herokuapp.com/static/media/coach-me-logo.png)

## Table of Contents

1. [Overview](#overview)
2. [UX](#ux)
   - [Strategy](#strategy)
     - [Target Audience](#target-audience)
     - [Business Goals](#business-goals)
     - [User Stories](#user-stories)
   - [Scope](#scope)
   - [Structure](#structure)
   - [Wireframes](#wireframes)
   - [Surface](#surface)
     - [Typography](#typography)
     - [Colours](#colours)
     - [Images](#images)
3. [Features](#features)
   - [Current Features](#current-features)
   - [Future Features](#future-features)
4. [Tech Used](#tech-used)
   - [Languages](#languages)
   - [Frameworks & Libraries](#frameworks-libraries)
5. [Testing](#testing)
6. [Deployment](#deployment)
   - [Heroku](#heroku)
   - [AWS](#aws)
7. [Credits](#credits)

## Overview

Coached by Caoimhe is a web application that allows users to buy workout plans and be coached online and/or in person by a qualified personal trainer. This site you can find all the different workout plans and their details.

## UX

### Strategy

---

#### Target Audience

The target audience for this site are for people who want to be able to buy workout plans and be coached online and/or in person by a qualified personal trainer. Although this site targets a wide range of people its steered towards women who are looking to get back into shape post-pregnancy or maintain a great physique.

#### Business Goals

- To provide a navigable site that can entice users to sign up for coaching.
- Connect with users via social media and through subscriptions.
- Provide a way for users to buy workout plans and be coached online and/or in person by a qualified personal trainer.

#### User Stories

##### As a first time user, I want

- To easily understand the site and its features.
- To see clearly what the site has to offer.
- To be able to buy workout plans and be coached online and/or in person by a qualified personal trainer.
- Create an account and sign in to access the site.
- Know about the personal trainer and their qualifications.
- To easily find the contact information of the personal trainer.

##### As a recurring user, I want all of the above and

- To log in and sign up for coaching.
- To login in and check my profile.
- To have all my personal data stored.
- To have my workout plans stored.
- To have a secure way to pay for my workout plans.
- to receive a confirmation email when I buy a workout plan.
- To subscribe to the site and receive an email with the workout plan or information.
- To reach read the coaches blog.

##### As the Admin/Site owner, I want

- To be able to add new workout plans.
- To be able to edit existing workout plans.
- To be able to delete existing workout plans.
- To add questionaries to workout plans.
- To update blog posts.

---

### Scope

The following features are must have for this site to function, and are correlated to the user stories above.
Any features that are not included are optional and can be added later. Please check [Features](#features) to see a full list of current and future features.

- Clear and fully responsive design.
- Secure payment method.
- Secure authentication.
- User sign up and login.
- User profile.
- User workout plans.
- Full admin access.
- Error pages. (404, 500, etc.)

---

### Structure

Below is a description of the structure of the site.

#### Home App

**HTML**

index.html

#### Plans App

**HTML**

**Models**

#### Checkout App

**HTML**

**Models**

#### Profiles App

**HTML**

**Models**

#### Contact App

**HTML**

**Models**

#### Blog App

**HTML**

**Models**

#### Subscribe App

**HTML**

**Models**

---

### Wireframes

<details>
<summary>Home</summary>
</details>

<details>
<summary>Workout Plans</summary>
</details>

<details>
<summary>Workout Plans Details</summary>
</details>

<details>
<summary>Checkout</summary>
</details>

<details>
<summary>Checkout Success</summary>
</details>

<details>
<summary>Sign Up</summary>
</details>

<details>
<summary>Sign In</summary>
</details>

<details>
<summary>Profile</summary>
</details>

<details>
<summary>Workout Plan Management</summary>
</details>

<details>
<summary>Contact Us</summary>
</details>

<details>
<summary>Error pages</summary>
</details>

---

### Surface

#### Colours

The colours used primarily in the site are:

![Colours](https://coach-me.herokuapp.com/static/media/colours.png)

#### Typography

I used the following fonts:

#### Images

The imagery used throughout the site is allows the use to quickly identify and understand the site. I chose aesthetic imagery to help persuade the user into signing up for coaching.

---

## Features

### Current Features

### Future Features

## Tech Used

### Languages

- [HTML5](https://html.com/html5/)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

### Frameworks & Libraries

- [Django](https://www.djangoproject.com/) - Used for the main framework for this site.
- [Bootstrap](https://getbootstrap.com/) - Used for the styling of the site.
- [Google Fonts](https://fonts.google.com/) - Used for the typography of the site.
- [Font Awesome](https://fontawesome.com/) - Used for the icons of the site.
- [SQLite3](https://www.sqlite.org/)n - Used for the development database of the site.
- [PostgreSQL](https://www.postgresql.org/) - Used for the Deployed database of the site.
- [Heroku](https://www.heroku.com/) - Used for the deployment of the site.
- [AWS](https://aws.amazon.com/) - Used for hosting images and static files.
- [VS Code](https://code.visualstudio.com/) - IDE used for the development of the site.
- [Git](https://git-scm.com/) - Used for the version control of the site.
- [GitHub](https://github.com/) - Used for storing the project files.
- [Balsamiq](https://www.balsamiq.com/) - Used for the wireframes.

## Testing

Find all the testing documentations [**here!**](TESTING.md)

## Deployment

Below describes the deployment of the site on Heroku and set up process to store static files and images on AWS.

### Heroku

- Go to [Heroku](https://www.heroku.com/)

- Create an account or log in if you already have an account.

- Create a new app and give it a unique name in only lowercase letters and numbers.

- Choose the nearest region to your location and click on "Create App".

- When the app has be created, click on the "Resources" tab to add the postgres database. Type in "Heroku Postgres" and select it
  _*This will create a DATABASE_URL in the Config Vars (which can be found in settings)*_

- Click on the "Deployment" tab.

- Select the option to "GitHub" and search for the project.

- Click on "Connect and enable automatic deployments"

- Move back to your IDE and `pip install dj_database_url` and `psycopg2-binary` to be able to use the postgres database.

- In the `settings.py` file, add the following lines:

```
DATABASES = {
    "default": dj_database_url.parse("database_url")
}
```

- Comment out the existing sqlite3 database.
  **PLEASE NOTE: Before committing and pushing to GitHub make sure to uncomment your sqlite3 to ensure this piece of code isn't committed to GitHub**

- Login to Heroku using the command line by typing `heroku login -i`

- Once logged in you will need migrate the models to the postgres database.

- Run the following command in the terminal:

  - `heroku run python manage.py makemigrations --dry-run` to see what changes will be made to the database.

  - `heroku run python manage.py makemigrations` to actually make the changes to the database.

  - `heroku run python manage.py migrate --plan` to see what will be migrated.

  - `heroku run python manage.py migrate` to actually migrate the database.

- You will now need to create a superuser to access the admin side of the site.

  - `heroku run python manage.py createsuperuser`

- Install the `gunicorn` package by typing `pip install gunicorn`

- Now you can create your requirements.txt file by typing `pip freeze > requirements.txt`

- Create a `Procfile` file by typing `touch Procfile`

## Credits

### Code

- How to add dropdown content in markdown was found [here](https://dev.to/asyraf/how-to-add-dropdown-in-markdown-o78).

- Assistance with creating the contact form was found [**here**](https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend).

- The embedded google map was created here [**here**](https://developers.google.com/maps/documentation/embed/map-generator).

- Layout inspired by Bootstrap jumbotron, found [**here**](https://getbootstrap.com/docs/5.1/examples/jumbotron/).

### Image

- The website used to remove the background of an image was found [**here**](https://www.remove.bg/)

- The image used for the landing page was found [**here**](https://www.freepik.com/free-photo/young-beautiful-woman-bright-sportwear-isolated-gradient-pink-blue-background-neon-light_11689908.htm)

- The image used for a plan with no image was taken from the CI walkthrough project which can be found [**here**](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/4b28dfe82da5e5e24ed830f15ebe4f70deca8886/media/noimage.png)

## Acknowledgements
