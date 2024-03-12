## WebLogger

This repository provides a simple web-based logger using Flask and Flask-SocketIO. It allows you to tail a live log file and shows a real-time feed of its contents in a web browser.

### Usage

1. Clone the repository:
```
git clone https://github.com/IdrisFallout/WebLogger.git
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Run the main script:
```
python main.py
```
4. Open your web browser and navigate to `http://localhost:5000` to view the log in real-time.

### Implementation

The WebLogger is implemented using the following components:

- **Flask**: A web framework for creating web applications in Python.
- **Flask-SocketIO**: A Socket.IO extension for Flask that enables real-time communication between the client and server.
- **Subprocess**: A Python module that allows for the execution of external commands and the capture of their output.

The `main.py` script continuously prompts the user for commands to execute. Each command is appended to a `output.txt` file using the `execute_command()` function.

The `app.py` script uses Flask-SocketIO to handle WebSocket connections and emit log data to connected clients. The `tail()` event handler in `app.py` reads the `output.txt` file and sends new lines to the client in real-time.