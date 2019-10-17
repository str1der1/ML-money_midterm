<<<<<<< HEAD
# Mid Term WebApp for Sirajs online Course 

Thanks to Max Halfords BoilerPlate code for Flask.  Modified for a 
![License](http://img.shields.io/:license-mit-blue.svg)
A fork of [Max Halford's](https://github.com/MaxHalford) [flask-boilerplate](https://github.com/MaxHalford/flask-boilerplate). 
Please take a look at MAx's page for full details.   

This fork has modified the MAx's code andbuilt on top by :
- allowing a change of the stylings,
- Allowing the pulling of Tweets from Twitter.    
- Performing Sentiment analysis using TextBlob
- Fixed the Payment and Premium user identification 
- Producing Nice table output of sentiment with color coding.

The code also allows account management.  Sign Up,  Sign in
THe code also allows Payment options to identify as a Premium member vs a free member
The code links in with Stripe to allow payments to be processed
The code identifies if the customer is premium and offers additional fields like Tweet count override 


# Screenshots

### Landing page  (NON logged in )

![Alt text](screenshots/LandingPage_nonauthenticated.png?raw=true "Landing Page (Not logged in)")

### Sign up page

![Alt text](screenshots/SignUp.png?raw=true "Landing Page (Sign up new USer)")

### Sign In  

![Alt text](screenshots/SignIn.png?raw=true "Sign in web Page")

### Landign page as a Logged in user

![Alt text](screenshots/LandingPage_Authenticated.png?raw=true "Landing Page (Signed in)")

### Account Upgrade page  (Non Premium user )

![Alt text](screenshots/Accounts_PremiumUpgrade.png?raw=true "Upgrade to Premium account page")

### Main Feature -  Twitter Form  (Non Premium user)

![Alt text](screenshots/FormFeaturePage_NonAuthenticatedUser.png?raw=true "Twitter Form Page (  reduced Features )")

###  Results Page with sentiment Analysis

![Alt text](screenshots/ResultsPage.png?raw=true "Sentiment Analysis Page")

### Upgrade to Premium via Accounts page  (using Stripe)

![Alt text](screenshots/PremiumUpgradePayPage.png?raw=true "Upgrade to Premium via Accounts page ")

### Confirmd Premium Payment (using Stripe)

![Alt text](screenshots/PaymentStripe.png?raw=true "Card Payment entry via Stripe API")

### Main Feature -  Twitter Form  (Premium additonal Features)

![Alt text](screenshots/FormFeaturePage_PremiumUser.png?raw=true "Twitter Form with additional Count Feature")

### Landing page  (Premium)

![Alt text](screenshots/LandingPage_AuthenticatedPremium.png?raw=true "Landing Page for Premium users")


## Setup   (Following Max's instructions)

### Vanilla

- Install the requirements and setup the development environment.

	`make install && make dev`

- Create the database.

	`python manage.py initdb`

- Run the application.

	`python manage.py runserver`

- Navigate to `localhost:5000`.

## Configuration  ( Copied from MAx repo )

The goal is to keep most of the application's configuration in a single file called `config.py`. I added a `config_dev.py` and a `config_prod.py` who inherit from `config_common.py`. The trick is to symlink either of these to `config.py`. This is done in by running `make dev` or `make prod`.

I have included a working Gmail account to confirm user email addresses and reset user passwords, although in production you should't include the file if you push to GitHub because people can see it. The same goes for API keys, you should keep them secret. You can read more about secret configuration files [here](https://exploreflask.com/configuration.html).


## License

The MIT License (MIT). Please see the [license file](LICENSE) for more information.
=======
# ML-money_midterm
Midterm_project_code
>>>>>>> 5ec1c8df5c8eb011f262640b332eda35352ee5e1
