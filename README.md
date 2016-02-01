# tellmeevents - Eventbrite API in Django
A basic exploration of the Eventbrite API built using Django. Users are presented with categories, as given by Eventbrite's API, and can choose up to 3. They are then presented with events from that category.

It is designed to be a very basic implementation with little to no styling done.

## Getting Started 
### Installation
- Clone the repository to your machine
- Navigate to this folder
- Install virtualenv using ``pip install virtualenv`` (if it's not already installed)
- Create a virtualenv in your folder using ``virtualenv env``
- Add ``export EVENTBRITE_API_KEY=YOUR_API_KEY`` to ``env/bin/actiate``
- Run ``source env/bin/activate``
- Install the dependencies using ``env/bin/pip install -r requirements.txt``
- Start Django using ``env/bin/pip manage.py runserver``
- Navigate to http://127.0.0.1:8000
- You're done!

## Tests
Unit tests have been written with 96% code coverage. These mock the eventbrite API responses and are designed to be as isolated as possible.
- Use ``env/bin/python manage.py test events.tests``
- To see test coverage run ``coverage run --source='.' manage.py test events`` then ``coverage report``

## Structure
The ``data.py`` file interacts directly with the Eventbrite API. This was designed to abstract the Eventbrite API from the views.

``views.py`` contains basic logic about which templates are displayed.

### Pagination
The Eventbrite API is paginated, which was relatively hard to abstract.

### Models/caching
Eventbrite's terms and conditions state that data cannot be stored. The option of using models to temporarily store data was explored, however this was generally just overkill and not necessary. Also, as the events returned by the API are paginated, it became quite tricky to implement pagination of results along with models. If you create 50 'Event' models with the first API call, and rely on database data only, then you can't have a paginate feature, as there may be disparity between the database and the API.