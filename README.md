# TrailMate

TrailMate is a Django web application for discovering and managing hiking trails and locations in Bulgaria.

## About the Project

The project provides a simple way to explore hiking routes, discover locations, and view information about different trails.

TrailMate is developed as an individual Django project.

## Features

- Browse hiking trails.
- View detailed information about each trail.
- Add, edit, and delete hiking trails.
- Browse hiking locations.
- View location details and associated trails.
- Add, edit, and delete locations.
- Organize trails by location and category.
- Associate features with hiking trails.
- Responsive layout with custom CSS styling.

## Technologies

- Python
- Django
- SQLite
- HTML
- CSS
- Git
- GitHub

## Project Structure

- `config/` — Django project configuration.
- `trails/` — Hiking trails, locations, forms, views, and templates.
- `catalog/` — Trail features and related data.
- `favorites/` — Application module currently under development.
- `manage.py` — Django management utility.

## Getting Started

### Requirements

- Python 3
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bLooDaMoRe/TrailMate.git
   cd TrailMate
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

3. Activate the virtual environment:

   ```bash
   source .venv/bin/activate
   ```

4. Install Django:

   ```bash
   pip install django
   ```

5. Apply database migrations:

   ```bash
   python3 manage.py migrate
   ```

6. Start the development server:

   ```bash
   python3 manage.py runserver
   ```

7. Open the application in your browser:

   http://127.0.0.1:8000/

## Design Resources and Credits

The following resources were used for button styling ideas and CSS hover effect inspiration:

- [CSS Buttons](https://www.css-buttons.com/)
- [Dimas' Toolbox — CSS Button Hover Effects Generator](https://dimastoolbox.com/css-button-hover-effects-generator)

The button styling and hover effects were adapted to fit the TrailMate project.

## Author

Bobi Uruchov

## Project Status

TrailMate is currently under development.
