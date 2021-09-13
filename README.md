![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome SNmcdarby1,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidently make it public then you can create a new one with _Regenerate API Key_.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.


Happy coding


- ### links


- (allauth)[https://django-allauth.readthedocs.io/en/latest/installation.html]

### Conxia 
<!-- I used the codeinstitute Boutique_ado design, It inspired me create this website using 
the same code and embedded it to a slightly different style -->
 Conxia is a nail app booking platform  that  provide professional and friendly nail technician services, by highly qualified nail and beauty therepists.
Mockup image of webpage
Features
In this section, you should go over the different parts of your project, and describe each in a sentence or so. You will need to explain what value each of the features provides for the user, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.
Existing Features
•	Navigation Bar
o	Featured on all three pages, the full responsive navigation bar includes links to the Logo, Home page, Gallery and Sign Up page and is identical in each page to allow for easy navigation.
o	This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button.
Image of navigation bar
•	The landing page image
o	The landing includes a photograph with text overlay to allow the user to see exactly which location this site would be applicable to.
o	This section introduces the user to Conxia Nail Parlor with an eye catching animation to grab their attention
Image of landing page
o	Page name Conxia
o	The page section will allow the user to see the benefits of joining the The Lounge Nail products services  and beauty products.
o	This user will see the value of signing up for the Conxia Nail Parlor . This should encourage the user to consider more booking arrangements for their companies around the world.
Image of page
•	Booking section
o	This section will allow the user to see exactly the total budget that every user is allowed to use, where they allocated hotels and restaurants are and the conference bookings within the designated locations.
o	This section will be updated as these times change to keep the user up to date.
data 
installed pip3 django
installed pip3 django-admin statrproject
installed pip3 django-allauth==0.4.0
installed pip3 freeze > requirement.txt
uploaded pre-written data called fixtures
python3 manage.py startapp home
python3 manage.py startapp products



o Preloaded data base called fixtures
Footer image
•	The Footer
o	The footer section includes links to the relevant social media sites for The Lounge Nail Parlor. The links will open to a new tab to allow easy navigation for the user.
o	The footer is valuable to the user as it encourages them to keep connected via social media
 
•	Gallery
o	The gallery will provide the user with supporting images to see what the meet ups look like.
o	This section is valuable to the user as they will be able to easily identify the types of events the organisation puts together.

gallery
•	The Sign Up Page
o	This page will allow the user to get signed up to  Conxia Nail Parlor to start their running journey with the community. The user will be able specify if they would like to take part in road, trail or both types of running. The user will be asked to submit their full name and email address.
Image 
For some/all of your features, you may choose to reference the specific project files that implement them.
In addition, you may also use this section to discuss plans for additional features to be implemented in the future:
Features Left to Implement
•	Another feature idea
Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.
You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.
If this section grows too long, you may want to split it off into a separate file and link to it from here.
Validator Testing
•	HTML
o	No errors were returned when passing through the official W3C validator
•	CSS
o	No errors were found when passing through the official (Jigsaw) validator
Unfixed Bugs
You 
Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub)
•	The site was deployed to GitHub pages. The steps to deploy are as follows:
o	In the GitHub repository, navigate to the Settings tab
o	From the source section drop-down menu, select the Master Branch
o	Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
The live link can be found here - https://code-institute-org.github.io/boutique_ado/index.html
Credits
Photos
A big thank you to the unsplash photographers for allowing free downloads
Photo by Charles Forerunner on Unsplash
Photo by Ales Nesetril on Unsplash
Photo by John Schnobrich on Unsplash
Photo by Hunters Race on Unsplash
Photo by Sven Mieke on Unsplash
Photo by Pawel Janiak on Unsplash
Photo by Jay Clark on Unsplash
Photo by Marten Bjork on Unsplash
Photo by Nik Lanús on Unsplash
Photo by Li Zhang on Unsplash



In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
You can break the credits section up into Content and Media, depending on what you have included in your project.
Content
•	The text for the Home page 
•	form validation 
•	The icons in the footer were taken from Font Awesome
Media
•	The photos used on the home and sign up page 
•	The images used for the gallery page were 
•	
Other General Informatiom
Below you will find a 

About
Resources
 Readme
Releases
No releases published
Packages
Contributors 3
•	
* pip install django-appointment==1.5