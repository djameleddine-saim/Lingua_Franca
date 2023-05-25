# Language Translation Web Application

The Language Translation Web Application is a Flask-based web application that allows users to translate text between different languages. It utilizes the Google Translate API and provides a user-friendly interface for easy translation.
## The project consists of the following components:

1. app.py:This is the main Flask application file. It contains the application configuration, routes, and associated functions. Here's a brief description of the main functions:

- translate(): This function is linked to the root route ("/") and is used to handle both GET and POST requests. It retrieves the form data (text, source language, and target language), performs translation using the Google Translation API, and returns the result to the HTML template.
2. templates: This directory contains the HTML template files used to display the application pages.

- index.html: This is the main template file. It displays the text input form, source language and target language selection options, as well as the translation result. Here's a brief description of the main elements:

  - form: This form allows users to input the text to be translated and select the source and target languages.
  - select: These elements allow users to select the source and target languages using options dynamically generated from the JSON file containing the languages.
  - input type="submit": This submit button triggers the form submission.
  - div: This element displays the translation result.
3. static: This directory contains static files such as the JavaScript file and CSS files used to enhance the user interface. In this project, In this project, it only contains the script.js and styles.css file.

   - js/script.js: This JavaScript file is used to enhance the interactivity of the application. It uses libraries such as Bootstrap and jQuery to manipulate the DOM and add dynamic functionalities. For example, it allows hiding and showing the automatic language selection options based on the selected source language.
   - css/styles.css: These styles use the max-width, overflow, text-overflow, white-space, and word-wrap CSS properties to control text width and overflow behavior.
## Features

- Text Translation: Enter the text to be translated in the input field.
- Language Selection: Choose the source and target languages from dropdown menus.
- Auto-detection: Support for auto-detection of the source language.
- Responsive Design: Optimized for mobile devices.
## Usage

1. Home Page:

- The home page displays a form where users can enter the text to be translated.
- Users can select the source and target languages from the dropdown menus.
- Clicking the "Translate" button will submit the form and trigger the translation process.
## Translation:

- Upon submitting the form, the application will translate the input text using the selected languages.
- The translated text will be displayed on the screen.
- If an invalid language is selected, an error message will be shown.
## Mobile Responsiveness:

- The web application is designed to be responsive, providing an optimal viewing experience on mobile devices.
- The interface will adapt to different screen sizes, ensuring readability and usability on smartphones and tablets.

## Installation

1. Clone the repository:

```bash
 git clone https://github.com/djameleddine-saim/Lingua_Franca.git 
 ```

2. Navigate to the project directory:

```bash
 cd Lingua_Franca 
 ```


3. Install the required dependencies:

```bash
 pip install -r requirements.txt
 ```


4. Start the Flask development server:

```bash
 python app.py
 ```


The web application will be accessible at `http://localhost:5000` in your web browser.

## Screenshots




![Capture d’écran (23)](https://github.com/djameleddine-saim/Lingua_Franca/assets/115147662/330ddcee-f029-4881-b92a-d558394828f1)



