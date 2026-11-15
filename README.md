# Todo List

A Django web application for managing daily tasks and organizing them with tags.

## Requirements

- Python 3.12+

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Shkabaduba/TODO_LIST.git
   cd TODO_LIST
   ```

2. Create and activate a virtual environment:
   - Windows (cmd):
     ```bat
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - macOS / Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` in your browser.

## Running Tests

```bash
python manage.py test
```

## Features

- **Home page (`/`)**: displays the todo list ordered from not done to done and from newest to oldest, showing task content, creation datetime, optional deadline, completion status, and tags.
- **Quick status toggle**: `Complete` / `Undo` button switches task completion status and redirects back to the home page.
- **Task management**: create, update, and delete tasks.
- **Tag list page (`/tags/`)**: displays all tags in a table with links to create, update, and delete tags.
- **Navigation sidebar**: available on all pages with links to Home and Tags.
