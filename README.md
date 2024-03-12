# WebLogger

This Flask + SocketIO application allows you to track the real-time output of a command line process.

## Features

- Web interface to view the output of the process
- Real-time updates via SocketIO
- Ability to enter commands and execute them on the command line

## Setup

1. Install the required Python packages:
```
pip install -r requirements.txt
```

2. Run the main Python script:
```
python main.py
```

3. Open `http://localhost:5000/` in a web browser.

## Usage

Enter commands in the input field and click the "Execute" button. The output of the command will be displayed in real time on the web page.

## Code Overview

### app.py

- Defines the Flask application and SocketIO instance.
- Includes event handlers for `connect`, `disconnect`, and `tail`.

### main.py

- Executes user-entered commands using `subprocess` and writes the output to a file.
- Continues running until the user types "exit" or "quit".

### output.txt

- Contains the output of the executed commands.

### requirements.txt

- Specifies the required Python packages for the application.