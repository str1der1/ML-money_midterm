<<<<<<< HEAD
# Thanks to Max Halfords BoilerPlate code for Flask.  Modified for a Mid Term in Sirajs online Course 

![License](http://img.shields.io/:license-mit-blue.svg)

A fork of [Max Halford's](https://github.com/MaxHalford) [flask-boilerplate](https://github.com/MaxHalford/flask-boilerplate). 

Please take a look at MAx's page for full details.   

This fork has modified the BoilerPlate code and allowed pulling of Tweets from Twitter.    Performinign Sentiment Analysis on it using TextBlob. Producing the output in a table format.

The code also allows account management.  Sign Up,  Sign in
THe code also allows Payment options to identify as a Premium member vs a free member
The code links in with Stripe to allow payments to be processed
The code identifies if the customer is premium and offers additional fields like Tweet count override 

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
