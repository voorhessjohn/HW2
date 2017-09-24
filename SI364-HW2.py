
## John Voorhess
## voor@umich.edu
## HW 2 
## SI 364 F17
## Due: September 24, 2017
## 500 points

#####

## [PROBLEM 1]

## Edit the following Flask application code so that if you run the application 
# locally and got to the URL http://localhost:5000/question, you see a form that 
# asks you to enter your favorite number. Once you enter a number and submit it to the form, 
# you should then see a web page that says "Double your favorite number is <number>". For example, 
# if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". 
# Careful about types in your Python code!
## You can assume a user will always enter a number only.

from flask import Flask, request
app = Flask(__name__)
app.debug = True

victorFirstNameList = ['Conquering', 'Best', 'Valiant']
victorLastNameList = ['Hero', 'Wolverine', 'Leader', 'Victor']

@app.route('/')
def hello_to_you():
    return 'Hello!'

@app.route('/question')
def question_form():
    if 'favorite_number' in request.args:
        return sendPage(request.args['favorite_number'])
    else:
        return sendForm()

###################################
#[PROBLEM 2]
###################################

@app.route('/nameform')
def name_form():
    if 'firstName' in request.args:
        return victorName(request.args['firstName'], request.args['lastName'])
    else:
        return nameForm()

def victorName(firstName, lastName):
	# values from 97 to 122 for lowercase aa-zz
	firstNameCharValue = ord(firstName[-1])
	lastNameCharValue = ord(lastName[-1])

	if firstNameCharValue < 105:
		firstVictorName = victorFirstNameList[0]
	elif firstNameCharValue in range(105, 112):
		firstVictorName = victorFirstNameList[1]
	else:
		firstVictorName = victorFirstNameList[2]

	if lastNameCharValue < 102:
		lastVictorName = victorLastNameList[0]
	elif lastNameCharValue in range(102, 110) :
		lastVictorName = victorLastNameList[1]
	elif lastNameCharValue in range(111, 115):
		lastVictorName = victorLastNameList[2]
	else:
		lastVictorName = victorLastNameList[3]

	return '''
	<html>
      <body>
        <h1>Your Wolverine name is {0} {1}</h1>
      </body>
    </html>
    '''.format(firstVictorName, lastVictorName)	
	

def sendForm():
    return '''
    <html>
      <body>
          <form method='get'>
              <label for="mynumber">Enter Your Favorite Number</label>
              <input id="mynumber" type="number" name="favorite_number" />
              <input type="submit">
          </form>
      </body>
    </html>
    '''

def sendPage(favorite_number):
    return '''
    <html>
      <body>
        <h1>Double your favorite number is {0}</h1>
      </body>
    </html>
    '''.format(int(favorite_number) * int(2))

def nameForm():
    return '''
    <html>
      <body>
          <form method='get'>
              <label for="myFirstName">Enter Your First Name</label>
              <input id="myFirstName" type="text" name="firstName" />
              <label for="myLastName">Enter Your Last Name</label>
              <input id="myLastName" type="text" name="lastName" />
              <input type="submit">
          </form>
      </body>
    </html>
    '''


if __name__ == '__main__':
    app.run()


## [PROBLEM 2]

## Come up with your own interactive data exchange that you want to see happen dynamically 
# in the Flask application, and build it into the above code for a Flask application. 
# It should:
# - not be an exact repeat of something you did in class, but it can be similar
# - should include an HTML form (of any kind: text entry, radio button, checkbox... feel free to try out whatever you want)
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form 
# (text entered, radio button selected, etc). So if a user has to enter a number, it should do an operation on that number. 
# If a user has to select a radio button representing a song name, it should do a search for that song in an API.

# You should feel free to be creative and do something fun for you -- 
# And use this opportunity to make sure you understand these steps: if you think going slowly and 
# carefully writing out steps for a simpler data transaction, like Problem 1, 
# will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; 
# you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can 
# assume a user will type a reasonable name; if your form asks for a number, you can assume a user 
# will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)









