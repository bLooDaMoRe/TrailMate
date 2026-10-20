# TrailMate

TrailMate is a Django web application for discovering and managing hiking trails and locations in Bulgaria.

## About the Project

TrailMate provides a simple interface for exploring hiking trails, viewing detailed trail information, managing hiking locations, and organizing trails by category and features.

The application was developed as an individual Django project.

## Features

- Browse hiking trails and view their details.
- Create, edit, and delete hiking trails.
- Browse hiking locations and view associated trails.
- Create, edit, and delete locations.
- Organize trails by location and category.
- Associate features with hiking trails.
- Create and browse trail features.
- Save and view favorite trails.
- Responsive navigation and custom CSS styling.
- Custom page for handling not-found URLs.

## Technologies

- Python
- Django
- SQLite
- HTML5
- CSS3
- Git
- GitHub

## Project Structure

- `config/` — Django project configuration and URL routing.
- `trails/` — Trail and location models, forms, views, and templates.
- `catalog/` — Trail feature management.
- `favorites/` — Favorite trail functionality.
- `templates/` — Shared and custom templates.
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

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install Django:

   ```bash
   pip install django
   ```

4. Apply database migrations:

   ```bash
   python3 manage.py migrate
   ```

5. Start the development server:

   ```bash
   python3 manage.py runserver
   ```

6. Open the application in your browser:

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
