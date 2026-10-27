# Import Flask so the program can create a web application.
>> from flask import Flask
>> 
>> # Create the Flask application and name it using this file's context.
>> app = Flask(__name__)
>> 
>> # Connect the website's home address to the function below it.
>> @app.route("/")
>> # Define the function that handles requests to the home page.
>> def home():
>>     # Send the welcome message back to the browser.
>>     return "Welcome to Viral Protection"
# Connect the website's about address to the function below it
>> @app.route("/about")
>> # Define the function that handles requests to the about page.
>> def about():
>>      # Send the about message back to the browser.
>>      return "Viral Protection is a safe friendly neighborhood software protection service in Coral Gables."
