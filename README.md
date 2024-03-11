# WebLogger

This repository contains a web application that allows you to execute commands on your computer and view the output in real-time.

## Features

* Execute commands on your computer remotely
* View the output of commands in real-time
* Disconnect and reconnect without losing output

## Usage

1. Clone the repository: `git clone https://github.com/IdrisFallout/WebLogger.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Open your browser and go to `http://localhost:5000`
5. Enter a command in the text box and click "Execute"
6. The output of the command will be displayed in the chat window

## Code Overview

The repository contains the following files:

* `app.py`: The main Flask application file
* `main.py`: The script that executes commands and writes the output to a file
* `output.txt`: The file that stores the output of commands
* `requirements.txt`: The file that lists the required packages

The `app.py` file uses Flask and Flask-SocketIO to create a web application. The `/` route renders the index.html template, which contains a chat window and a text box for entering commands.

The `tail` event handler in `app.py` reads the `output.txt` file and emits the new lines to the client.

The `main.py` script uses the `subprocess` module to execute commands and write the output to the `output.txt` file.

The `output.txt` file stores the output of commands.

The `requirements.txt` file lists the required packages for the application.