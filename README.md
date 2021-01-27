<p id="top"></p>

# MARSHAL PUNDIT REVIEWS WEBSITE

[View live deployment of site here](http://marshal-pundit-reviews.herokuapp.com/)

![responsive](static/images/responsive.png)

This is a Data Driven website created to provide the much needed information architecture to address organizational needs for storing,
retrieving, updating and processing exponentially growing data sets.

As our appetites to read, acquire and analyze more books intensified, "Marshal Pundit Book Reviews" emerged.


# Table of Contents

- [UX](#ux)
- [Database](#database)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_

<a name="ux"/>

# UX

## UX Design

The color scheme used in this project is a deviation from the basic "Achromatic" use of a white background with black text in web design yet the motifs were simply structured to be aesthetic and user friendly. All sections are arranged in a logical order to provide intuitive user experience.

The following colors were used: blanchedalmond (`#ffebcd`), range of blue-grey (`#263238`, `#37474f`, `#78909c`), grey lighten-5 (`#fafafa`), amber accent-4 (`#ffab00`), green accent-4 (`#00c853`), red lighten-1 (`#ef5350`), moderate red (`#D05F59`), white (`#ffffff`), black (`#000000`) and very dark (`#121315`).

## Target Audience

This application aims to attract readers, voracious readers, who like to share their thoughts on books they have read, and interact with other readers. The website provides user with synopsis about various genres and reviews, and allows interface for their reactions. Users are also able to upvote or downvote reviews. 

The main objective of the website is to provide users with the functionality to read, add, comment and vote for reviews.

## User Stories

Users:
* As a first time user, I would like to create my own account with the option to login and logout so nobody else can access it.
* As a prospective user, I want to be able to navigate throughout the site with ease to find content and access all collection of reviews in an organised format.
* As a user, I would like to be able to add, share and see all of my inputs within the app (i.e. comments, reviews, votes).
* As a user, I would like to search any particular book quickly using e.g. book title or author.
* As a user I would like to be able to like or dislike any review.
* As a user I would like to be able to edit or delete any content added by me.
* As a user I would like to be sure that no other user is able to edit or delete my input. 

Owners:
* As a owner, I want my website to be desirable and accessible to users.
* As a owner, I want to earn money on each book purchased via a link from the site.

## Wireframe
The skeletal framework of this website was designed using [Balsamiq](https://balsamiq.com) as a visual guide to represent the page schematic and screen blueprint.

Links to final version of the wireframe can be found below:
* [Wireframe Final Version](https://seagather.github.io/Marshal-Pundit-Reviews/wireframes/marshal-reviews-wireframe.pdf)

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_

<a name="database"/>

# Database

MongoDB Atlas was used for this project. A leading NoSQL system in document-oriented cloud database.

The functionality was generally structured to action four types of operations, known collectively by the acronym CRUD, standing for Create, Read, Update, and Delete as shown below:

![dmo](static/images/dmo.png)

## Database Design

The database integrates four collections, namely: users, genres, reviews and  upvotes as represented in the database schema below:

![schema](static/images/schema.png)

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_

<a name="features"/>

# Features

## Existing Features

#### Structure

- **Navbar** - mobile collapse button from Materialize framework was used for the navbar which framed the brand logo and links to relevant sections namely:
 Home, Profile, Add Review, Manage Genres, Sign Out. When the nav bar is resized, you will see that the links on the right turn into a hamburger icon, an effect of `class=sidenav-trigger` functionality. 

- **Footer** - A Sticky-footer was utilized for the purpose of this project because it always stays on the bottom of the page regardless of how little content is on the page.
The footer contains the copyright formality.

#### Forms

- **Register form** - This provides interface to new users for sign up.

- **Log In form** - form that enable users to sign into already created account. 

- **Add Review form** - contain fields that enable users to add new review to the website.

- **Edit Review form** - This form retrieves existing review data for revise.

- **Add Genre form** - form that enable users to add new genre to database.

- **Edit Genre form** - Allows for retrieve and revise of existing genre.

#### Home

* The Home Page offers the - **Search bar** - which enables users to search any book by name or author.
It contains collapsibles; accordion elements that expand when clicked on. The collapsible-header framed the caret-down, delete and edit buttons for reviews
while the collapsible-body encapsulates the set of data stored about a particular instance of an entity.

* When users get at the button of a long page, they often need to get back to the top.
There is a Back to Top button integration with JavaScript to allow users to quickly navigate to the top of the page.

#### Profile

* The Profile section features exclusively for a user session. All collections per user are stored in their respective profile.

#### Manage Genres

The Manage Genre section comprises of cards displaying content composed of different genres.
It allows user to add, edit and delete existing genres.

#### Security

* To make the user authentication more secure, the Log In form integrates werkzeug security features namely: "generate_password_hash" and "check_password_hash".
Hashing passwords makes it tougher to crack.

## Features Left to Implement

* A Virtual Reality should be added for users. 

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_

<a name="technologies-used"/>




