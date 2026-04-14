# RemarcableAsssessment

## Requirements

Ensure you have a version of Python and pip installed to run this application. Preferably Python 3. These commands also assume you run the project on a Linux Distribution.

## (Recommended) Install and set up a Virtual Environment to run the application:

    sudo apt install python3-virtualenv
    virtualenv .env

Once you created your virtual environment, you can then activate the environment via this command:

    source .env/bin/activate

If you just created this virtual environment, you may need to install django after you've entered it:

    pip install django

## To run the project, you can use the following command:

    python manage.py runserver

## To run unit tests, run the following command:

    python manage.py test

## Additional Notes
I built out this solution with the intention of using as little additional frameworks/libraries/dependencies as possible, aside from the essential Django Web Framework. 

There were additional things I considered such as prepping the views into API endpoints that can be used by other front-end frameworks but that would go against what I was trying to achieve in my first statement, and installing Django Rest Frameworks and would seem unnecessary since I opted for Django Templates for this particular problem.

Another item I was debating on whether I wanted to use Function Based or Class Based Views for this problem. I opted for Class Based more out of curiosity since I've worked with Function Based Views from previous work experiences and I wanted to try and learn first hand what developing Class Based Views were like.