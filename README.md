Book Wishlist
=============================

This application is an python Flask RESTful API.
It was built using python 3.9.2

The application only represents the wishlist secton of the api.
It is assumed the user(create, get, update, delete) and book(create, get, update, delete) sections exist elsewhere.

The assumed existence of these other routes are why wishlist is included in all the routes here.

Since this is just a coding exercise I have done everything to shrink the work needed.

I am only keeping track of a book id and a user id.  It is assumed that if you wanted more information on both you would use the book and user api.

You can only add a book to your wishlist once.  If it is already there it will not be added again, but the add will return a success.

If you delete a book that is not on the list, the return will be a success since the book is not on the list.

I do have a check in place to confirm a user and book do exist before they are added to the list.  In order to "play" with the application, two users and books are preloaded.

In the tests I have mocked the variables I am holding the data in, where normally I would have mocked the database connection.



Getting started
---------------

- Clone this example.

- From the server directory

        #Set up a python virtual environment (may need pip install virtualenv)
        python -m venv venv
        
        #Use the environment
        Linux:  source venv/bin/activate
        Powershell: .\venv\Scripts\activate

        #Install requirements
        pip install -r requirements.txt

        #run the flask app
        Linux: FLASK_APP=flask_app FLASK_ENV=development flask run
        Powershell:
        $Env:FLASK_APP="flask_app"
        $Env:FLASK_ENV="development"
        flask run

        #When you are done with the virtual environment deactivate it
        deactivate

To run tests
---------------

- tests use unittest and mock  

        pip install mock

- From the server directory

        python -m unittest tests/test_flask.py