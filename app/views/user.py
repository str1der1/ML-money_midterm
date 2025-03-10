from flask import (Blueprint, render_template, redirect, request, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required, current_user
from itsdangerous import URLSafeTimedSerializer

# All local python files
from app import app, models, db
from app.forms import user as user_forms
from app.toolbox import email
# Add the reference to the tweepy code 
from app.toolbox import tweepycode

# Setup Stripe integration
import stripe
import json
from json import dumps

# AA Updated for Stripe
stripe_keys = {
	'secret_key': app.config['STRIPE_SKT'],
	'publishable_key': app.config['STRIPE_PUB']
}
stripe.api_key = stripe_keys['secret_key']

# Serializer for generating random tokens
ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Create a user blueprint
userbp = Blueprint('userbp', __name__, url_prefix='/user')

# This is used for both a GET and a POST 
@userbp.route('/signup', methods=['GET', 'POST'])
def signup():
    # AA: Set up the DB
    form = user_forms.SignUp()
   
    # AA: IF form has been submitted i.e. POST then add into DB
    if form.validate_on_submit():
        # Create a user who hasn't validated his email address
        user = models.User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            phone=form.phone.data,
            email=form.email.data,
            confirmation=False,
            password=form.password.data,
        )
        # Insert the user in the database
        db.session.add(user)
        db.session.commit()
        # Subject of the confirmation email
        subject = 'Please confirm your email address.'
        # Generate a random token
        token = ts.dumps(user.email, salt='email-confirm-key')
        # Build a confirm link with token
        confirmUrl = url_for('userbp.confirm', token=token, _external=True)
        # Render an HTML template to send by email
        html = render_template('email/confirm.html',
                               confirm_url=confirmUrl)
        # Send the email to user
        email.send(user.email, subject, html)
        # Send back to the home page with a FLASH message 
        flash('Check your emails to confirm your email address.', 'positive')
        # AA:  On POST of information,  go back to Index
        return redirect(url_for('index'))
    
    # For a GET,  call the Signup page
    return render_template('user/signup.html', form=form, title='Sign up')

# This is used for both a GET only - For asking the keyword to search for   
@userbp.route('/stockTalk', methods=['GET', 'POST'])
def stockTalk():
    # AA: Set up the form fields
    form = user_forms.stockTalk()
    # For a GET,  call the Signup page
    return render_template('user/stockTalk.html', form=form, title='Sentiment Analysis Result')

# This is used for both a GET only - For display the results of the sentiment analysis
@userbp.route('/stockTalkResults', methods=['GET', 'POST'])
def stockTalkResults():
    # AA: Use the StockTalkForm from earlier.
    form = user_forms.stockTalk()
    # print(form)
    searchTerm = form.search_keyword.data
    count = form.count.data
    # Call the tweepy API with the search keyword
    results = tweepycode.tweep_run(searchTerm, count)
    # For a GET,  call the Signup page
    return render_template('user/stockTalkResults.html', form=form, results=results, title='Sentiment Analysis Result')

@userbp.route('/confirm/<token>', methods=['GET', 'POST'])
def confirm(token):
    try:
        email = ts.loads(token, salt='email-confirm-key', max_age=86400)
    # The token can either expire or be invalid
    except:
        abort(404)
    # Get the user from the database
    user = models.User.query.filter_by(email=email).first()
    # The user has confirmed his or her email address
    user.confirmation = True
    # Update the database with the user
    db.session.commit()
    # Send to the signin page
    flash(
        'Your email address has been confirmed, you can sign in.', 'positive')
    return redirect(url_for('userbp.signin'))


@userbp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = user_forms.Login()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        # Check the user exists
        if user is not None:
            # Check the password is correct
            if user.check_password(form.password.data):
                login_user(user)
                # Send back to the home page
                flash('Succesfully signed in.', 'positive')
                return redirect(url_for('index'))
            else:
                flash('The password you have entered is wrong.', 'negative')
                return redirect(url_for('userbp.signin'))
        else:
            flash('Unknown email address.', 'negative')
            return redirect(url_for('userbp.signin'))
    return render_template('user/signin.html', form=form, title='Sign in')


@userbp.route('/signout')
def signout():
    logout_user()
    flash('Succesfully signed out.', 'positive')
    return redirect(url_for('index'))


@userbp.route('/account')
@login_required
def account():
    return render_template('user/account.html', title='Account')


@userbp.route('/forgot', methods=['GET', 'POST'])
def forgot():
    form = user_forms.Forgot()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        # Check the user exists
        if user is not None:
            # Subject of the confirmation email
            subject = 'Reset your password.'
            # Generate a random token
            token = ts.dumps(user.email, salt='password-reset-key')
            # Build a reset link with token
            resetUrl = url_for('userbp.reset', token=token, _external=True)
            # Render an HTML template to send by email
            html = render_template('email/reset.html', reset_url=resetUrl)
            # Send the email to user
            email.send(user.email, subject, html)
            # Send back to the home page
            flash('Check your emails to reset your password.', 'positive')
            return redirect(url_for('index'))
        else:
            flash('Unknown email address.', 'negative')
            return redirect(url_for('userbp.forgot'))
    return render_template('user/forgot.html', form=form)


@userbp.route('/reset/<token>', methods=['GET', 'POST'])
def reset(token):
    try:
        email = ts.loads(token, salt='password-reset-key', max_age=86400)
    # The token can either expire or be invalid
    except:
        abort(404)
    form = user_forms.Reset()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=email).first()
        # Check the user exists
        if user is not None:
            user.password = form.password.data
            # Update the database with the user
            db.session.commit()
            # Send to the signin page
            flash('Your password has been reset, you can sign in.', 'positive')
            return redirect(url_for('userbp.signin'))
        else:
            flash('Unknown email address.', 'negative')
            return redirect(url_for('userbp.forgot'))
    return render_template('user/reset.html', form=form, token=token)

@app.route('/user/pay')
@login_required
def pay():
    user = models.User.query.filter_by(email=current_user.email).first()
    # print ("In the PAY Route of the code")
    # print ("User Paid setting is : " )
    print (user.paid)
    if user.paid == None:
    	return render_template('user/buy.html', key=stripe_keys['publishable_key'], email=current_user.email)
    else:
        return "You already paid."

@app.route('/user/charge', methods=['POST'])
@login_required
def charge():
    # Amount in cents
    amount = 500
    customer = stripe.Customer.create(email=current_user.email, source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Service Plan'
    )
    user = models.User.query.filter_by(email=current_user.email).first()
    user.paid = 1
    db.session.commit()
    # do anything else, like execute shell command to enable user's service on your app
    return render_template('user/charge.html', amount=amount)

@app.route('/api/payFail', methods=['POST', 'GET'])
def payFail():
	content = request.json
	stripe_email = content['data']['object']['email']
	user = models.User.query.filter_by(email=stripe_email).first()
	if user is not None: 
		user.paid = 0
		db.session.commit()
		# do anything else, like execute shell command to disable user's service on your app
	return "Response: User with associated email " + str(stripe_email) + " updated on our end (payment failure)."

@app.route('/api/paySuccess', methods=['POST', 'GET'])
def paySuccess():
	content = request.json
	stripe_email = content['data']['object']['email']
	user = models.User.query.filter_by(email=stripe_email).first()
	if user is not None: 
		user.paid = 1
		db.session.commit()
		# do anything else on payment success, maybe send a thank you email or update more db fields?
	return "Response: User with associated email " + str(stripe_email) + " updated on our end (paid)."

