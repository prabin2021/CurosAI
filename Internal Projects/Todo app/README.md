# Flask Todo Application

A simple and elegant Todo application built with Flask and SQLAlchemy.

## Features

- Add new todos with title and optional description
- Mark todos as complete/incomplete
- Delete todos
- Responsive design
- SQLite database for data persistence

## Installation

1. Make sure you have Python 3.7+ installed on your system.

2. Clone this repository or download the files.

3. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Make sure your virtual environment is activated.

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

- To add a new todo, fill in the title (required) and description (optional) fields and click "Add Todo"
- To mark a todo as complete/incomplete, click the "Complete" button
- To delete a todo, click the "Delete" button

## Project Structure

```
todo-app/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css      # CSS styles
└── templates/
    └── index.html     # Main template
``` 