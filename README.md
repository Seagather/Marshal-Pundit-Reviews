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

* The Manage Genre section comprises of cards displaying content composed of different genres.
It allows user to add, edit and delete existing genres.

#### Security

* To make the user authentication more secure, the Log In form integrates werkzeug security features namely: "generate_password_hash" and "check_password_hash".
Hashing passwords makes it tougher to crack.

#### Word Counter

* The reviewers comment input field has a word counter integrated with JavaScript.
The counter display while typing to inform and limit users within the context of maximum length and subject matter.

## Features Left to Implement

* Add social media links to generate traffic.
* Reset password option

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_

<a name="technologies-used"/>

# Technologies Used
**Languages:**
* [HTML5:](https://www.w3schools.com/html/default.asp)
    - HTML5 was used to code the content of the website.
* [CSS:](https://www.w3schools.com/css/default.asp)
    - CSS3 was used to style the content.
* [JavaScript:](https://www.w3schools.com/js/default.asp)
    - JavaScript was used to style the significant interactive functionality.
* [Python:](https://www.w3schools.com/python/default.asp)
    - Python was used for the project back-end functions. Flask and Python is used to build route functions.

**Tools and Libraries:**
* [Materialize:](https://materializecss.com/)
    - Materialize was used to create grid layout and styling various features such as navbar accordion, cards, buttons, forms, and footer to render responsive website.
* [W3C Validator:](https://validator.w3.org/)
    - The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to clear syntax errors.
* [Font-Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
* [Flask:](https://flask.palletsprojects.com/)
    - web application framework used to create functions with Python that are injected into html templates. 
* [jQuery:](https://jquery.com/)
    - jQuery library was used to simplify the JavaScript.
* [Tinypng:](https://tinypng.com)
    - Tinypng was used to compress the file size of PNG and JPG files.
* [GTmetrix:](https://gtmetrix.com)
    - GTmetrix was used to run speed tests on each page.
* [Pingdom:](https://tools.pingdom.com)
    - Pingdom was used to run speed tests on each page.
* [HTML and CSS Beautifier:](http://minifycode.com/html-beautifier/)
    - HTML and CSS was used to format the codes to make it more readable.
* [JSHint](https://jshint.com/) 
    - Used to test/validate JavaScript Code.
* [PEP8 Online Checker:](http://pep8online.com/)
    - P8P was used to verify that python coding conventions were applied to meet requirements.
* [drawio:](https://app.diagrams.net/)
    - Diagram software used to create the database schema and data manipulation operations diagrams.
* [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

**External Hosting:**
* [GitHub:](https://github.com/)
    - The project used the GitHub hosting service to save the project in a repository.
* [MongoDB Atlas:](https://www.mongodb.com/)
    - a document-oriented cloud database used to store manage, query and retrieve data set for the app. 
* [Heroku:](https://www.heroku.com/)
    - Heroku platform was used to deploy, manage, and scale the app. 


_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_

<a name="testing"/>

# Testing

Throughout the development process of this project, Chrome DevTools was used for testing variations and simulation of mobile devices.
To validated my Flask pages, I opened each page and right-click to select the - **View Page Source** - option (on Chrome), then copy the populated code and paste into Markup Validator. 
This was necessary to avoid all errors and warnings related to Jinja templates syntax as they are not recognised by the HTML validator.

![flask-page-test](static/images/flask-page-test.png)

## Speed Test

Website was tested on [GTmetrix](https://gtmetrix.com) and [Pingdom](https://tools.pingdom.com) platforms.

![speed-test](static/images/speed-test.png)

## EmailJS Test

The Database Creation with MongoDB Atlas and Heroku deployment was very easy because I followed the well implemented course in code institute module.

Before we create our Heroku application, we need to setup some files that Heroku needs
to run the app.
First, we need to tell Heroku which applications and dependencies are required to run our app:
"pip3 freeze --local > requirements.txt".
Next, the Procfile is what Heroku looks for to know which file runs the app, and how to
run it, so we'll use the echo command: "echo web: python app.py > Procfile".
Remember that the Procfile has a capital 'P', and no file extension.
We can check that the files were created successfully, and as you can see, the requirements.txt file
lists the dependencies that are needed for Flask.
One of these is called Werkzeug, which we'll learn more about later when setting up User
Authentication on our project.
The Procfile might add a blank line at the bottom, and sometimes this can cause problems
when running our app on Heroku, so just delete that line and save the file.
Let's head over to Heroku.com, and once you're logged in on your dashboard, we can click
to 'Create a New App'.
If you recall from our previous lessons, the Heroku app must be unique, and generally use
a 'dash' or 'minus' instead of spaces, and all lowercase letters.
I'm going to call my app "flask-task-manager-project", which means that's no longer available for
you to use, so try something similar, perhaps try including your name.
Next, select the region closest to you, and since I'm in Ireland, I'll select Europe,
then click 'Create App'.
In order to connect our app, we can do one of a few different options.
As you've learned from the previous project using Heroku, we could use the Heroku CLI
to connect our app using the steps outlined below.
However, to simplify the process, we'll setup Automatic Deployment from our GitHub repository.
Make sure your GitHub profile is displayed, then add your repository name, which I've
named exactly the same as my Heroku app, then click 'Search'.
Once it finds your repo, click to connect to this app.
Before we click to Enable Automatic Deployment, we still have a few more steps to do, otherwise
we'll get unwanted application errors.
Since we've contained our environment variables within a hidden env.py file, Heroku won't
be able to read those variables.
Click on the 'Settings' tab for your app, and then click on 'Reveal Config Vars', where
we can securely tell Heroku which variables are required.
Our env.py file contains a few different variables.
Make sure not to include any "quotes" for the key, or the value.
The first variable is IP, with the value of 0.0.0.0.
Next, the PORT, which is 5000.
For the SECRET_KEY, let's copy that from the env.py file, then paste it into Heroku.
We don't have the MONGO_URI string yet, so we'll leave that blank for now.
Finally, the MONGO_DBNAME is the name of our database, so task_manager.
Let's go back to the 'Deploy' tab, but before we connect it, we need to push our two new
files to the repository.
Back within the terminal, I've typed 'git status' just to confirm that those are the
only pending changes.
Add the requirements file to the staging area: "git add requirements.txt".
Then commit the file: "git commit -m "Add requirements.txt".
Next, add the Procfile: "git add Procfile".
Then commit that file as well: "git commit -m "Add Procfile".
Finally, "git push" in order to send those files to GitHub.
When we head back over to Heroku, we can now safely 'Enable Automatic Deployment', as everything
should be available on our repository.
I've only got the main branch for the project, so click 'Deploy Branch'.
Heroku will now receive the code from GitHub, and start building the app using our required
packages.
That should take a minute to build, and hopefully once it's done, you'll also see "Your app
was successfully deployed."
Click "View" to launch your new app.
Wonderful, the deployed site is now available, and should automatically update whenever we
push changes to the GitHub repository.


## Testing User Stories from User Experience (UX) Section

Users:
* As a prospective user, I want to know about the company and what they offer/particularly appealing benefits.
    - The Hero image and colors will essentially communicate visual aesthetic state of mind to viewers, first time user would assimilate the front page
      with various options of self explanatory navigation bar.
    - There is also a "click here for details" popup link at the bottom of the home section after the "Book Now" button which will inform users about our ethos at a glance.
    - There appears a popover box upon clicking the "Flight+Hotel" Tab button at the Booking section which will inform users about discount. 
    

* As a first time user, I want to be able to easily navigate throughout the site to find content about available flights, hotels, cars for rent and fare information
    - The site has been designed to be intuitive and accessible to user. At the top of the index page there is a clean navigation bar, each link describes at what section they will end up at clearly.
    - At the middle of the Hero image there is a "Book Now" call to action button that will take users directly to booking section.
    - The Booking section tab was well structured pertaining to each subject matter with relevant forms and button in sync for users quest.
    - When users must have completed the relevant inputs and check buttons for a particular tab, upon clicking search button pops up another page to clearly render feedback information.
    Each feedback page has a booking section for user accessibility on the spot.
    
* As a user, I want to get expert advice, plan my trip itineraries, tour packages and suitable cost about my destination.
    - Users can make use of the Contact section which contains contact form with EmailJS Integration for submission.
      The contact form has a validating pop up modal assuring users upon submission of their enquires or request.
    - Users are provided with button options at the bottom card of each eye-catching picture on the service section which takes them directly to contact section for more information as related to services.
    - At the footer "Contact details" there is a clickable Email address and Phone number provided for user accessibility and easy workflow.
    
* As a user, I want make alternative booking arrangements or cancellation if changes arise before or during trip.
    - Users can always channel their relevant request through the Contact section.
    - At the footer of the "Connect With Us", the user can alternatively contact the organisation on social media which highlights the links to them.

Owners:
* As a owner, I want my website to be desirable and accessible to users, I want users to see what sets me apart from the competition.
    - The well detailed composition of the website speaks volume, the colors, the captions, the call to action buttons, pop ups and links
     strategically positioned and escalated to desired sections serves to interact with clients to determine travel needs, budgets and preferences.
    - The pop up modal at the contact form section after users submission of their enquires or request is reassuring.
    - Each page has a clickable Email address and Phone number at the footer "contact details" for accessibility.

* As a owner, I want to know what my contemporaries are doing and ways to improve.
    - The Feedback from users on the Contact section comment and the social media platforms depicted with icons on each footer of the page will generate resources for improvement.

* As a owner, I want end-user feedback in shaping services to fit their needs more accurately
    - The "connect with us" social media icons were clearly displayed at the footer for followers and feedbacks.

* As a owner, I want users to get notifications and publications via newsletter when there are new offers.
    - The newsletter subscription option is provided for users at the footer of the website to cascade vital information and promos which will promote the site.
    - Upon clicking "Subscribe Now" button after submission of email address, user will get a reassuring feedback message.

## Further Testing

* All links were tested. Internal links all work. External links all work and open in new window.
* The Website was tested on Google Chrome, Internet Explorer, Firefox, Microsoft Edge and Safari browsers.
* The website was test run on a variety of devices such as Desktop, Laptop, iPhoneXR, Samsung Note3, Samsung Tab2 & Nokia.
* The site was test run by friends and colleagues for possible user experience issues and bugs.
* All the pages are responsive on all screen sizes.
* All the API calls returned responses as expected.
* The call to action buttons links as expected and the modal form pops up with all the input components validated.
* Each Search button generates feedback data on a new page which has a back to homepage link.
* The Email and Phone number at each footer "contact details" are clickable for users.
* All Codes were validated through the Markup Validator to erase syntax error.

## Bugs

### Fixed

* The fetch data from local storage scripts was merged initially to their respective js files but it was generating the below error on the console: 

## Console error
![console-error](https://seagather.github.io/Marshal-Travel-Agency/assets/images/console-error.png)

This was rectify by linking the script to the bottom of the body element at each page since I can't have a "for loop" run after redirecting to a new page
(accessing dom fail because it is redirecting). 

### Known Bugs

* The "Book Now" button and "Click here for details" link tend to overlap on some mobile devices when held in landscape mode.






