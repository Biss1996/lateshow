Late Show API Manager  

## Description  
The application provides a backend API for managing episodes, guests, and their appearances. It allows users to list and create appearances with validation. The data is seeded from a CSV file.

## Features / User Stories  

**A User Can:**
- View all episodes.
- View a single episode with its guest appearances.
- View all guests.
- Create a new guest appearance with a rating between 1 and 5.

**An Admin Can:**
- Seed the database using a CSV file.
- Perform CRUD operations via Postman or Flask endpoints.
- Delete an episode along with its appearances using cascade rules.



## Setup/Installation Requirements

1. **Download or Clone**  
   Fork and Clone this repo:  
   `git clone https://github.com/Biss1996/lateshow.git`

2. **Install Backend Requirements**  
   Open the project in VS Code → Terminal:
   ```bash
   pipenv install
   pipenv shell
3. **Configure Flask Environment**
In .flaskenv or terminal:

``bash
    export FLASK_APP=app:create_app
    export FLASK_ENV=development
    Run Migrations

``bash

    flask db init         
    flask db migrate -m "Initial"
    flask db upgrade
    Seed the Database
Ensure guests.csv is in the root folder, then:

``bash
    python seed.py

4. **Run the Application**

``bash
python app.py  #to run on port 5555


## Deployment
    This is a backend-only project. You can test the endpoints locally or via Postman using the provided collection.

## Known Bugs
    The application works perfectly well, no known bugs.

## Technologies Used
    Python
    Flask
    SQLAlchemy
    Flask-Migrate
    SQLite (local)
## Support and contact details
    email :: bettkipkoech45@gmail.com

## License
Copyright 2025 BISMARK BETT

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

