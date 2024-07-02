Here's a comprehensive README.md for your project:

---

# i18n in Flask

This project implements internationalization (i18n) in a Flask application. The app supports multiple languages and localizes timestamps based on user settings, URL parameters, and request headers.

## Learning Objectives
- Parametrize Flask templates to display different languages
- Infer the correct locale based on URL parameters, user settings, or request headers
- Localize timestamps

## Requirements
- All files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All files should end with a new line
- A README.md file at the root of the folder is mandatory
- Code should follow the pycodestyle style (version 2.5)
- First line of all files should be exactly `#!/usr/bin/env python3`
- All `*.py` files should be executable
- All modules should have documentation
- All classes should have documentation
- All functions and methods should have documentation
- Documentation should be a real sentence explaining the purpose of the module, class, or method
- All functions and coroutines must be type-annotated

## Tasks

### 0. Basic Flask App
- Set up a basic Flask app in `0-app.py`.
- Create a single `/` route.
- Create an `index.html` template that outputs "Welcome to Holberton" as the page title and "Hello world" as the header.

### 1. Basic Babel Setup
- Install Flask-Babel (`pip3 install flask_babel==2.0.0`).
- Instantiate the Babel object and store it in a variable named `babel`.
- Create a `Config` class with a `LANGUAGES` attribute set to `["en", "fr"]`.
- Set Babel’s default locale to "en" and timezone to "UTC".
- Use this class as the config for your Flask app.

### 2. Get Locale from Request
- Create a `get_locale` function with the `babel.localeselector` decorator.
- Use `request.accept_languages` to determine the best match with supported languages.

### 3. Parametrize Templates
- Use the `_` or `gettext` function to parametrize your templates.
- Create a `babel.cfg` file for extracting translatable strings.
- Initialize translations and edit `messages.po` files to provide translations.
- Compile your dictionaries and ensure the correct messages show up.

### 4. Force Locale with URL Parameter
- Implement logic to detect a `locale` argument in the request and use it if valid.
- Test different translations by visiting URLs with the `locale` parameter.

### 5. Mock Logging In
- Mock a user database and login system by passing a `login_as` URL parameter.
- Define `get_user` and `before_request` functions to manage user state.
- Display a welcome message if a user is logged in.

### 6. Use User Locale
- Modify `get_locale` to prioritize locale from URL parameters, user settings, request header, and then default locale.

### 7. Infer Appropriate Time Zone
- Define a `get_timezone` function with the `babel.timezoneselector` decorator.
- Prioritize time zone from URL parameters, user settings, and then default to UTC.
- Validate the time zone before returning it.

### 8. Display the Current Time (Advanced)
- Display the current time on the home page based on the inferred time zone.
- Use provided translations to format the time appropriately in English and French.

## How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/alx-backend.git
   cd alx-backend/0x02-i18n
   ```

2. Set up a virtual environment and activate it:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```sh
   export FLASK_APP=0-app.py
   flask run
   ```

5. Access the app in your browser at `http://127.0.0.1:5000`.

## Author
[Johnny](https://github.com/johnamet.git)

