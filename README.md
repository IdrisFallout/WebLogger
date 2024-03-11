# WebLogger

Developed by IdrisFallout

## Overview

WebLogger is a simple web application that allows you to view the output of terminal commands in real-time through a web browser.

## Setup

1. Install Python 3 and the required packages:

   ```
   pip install -r requirements.txt
   ```

2. Run the application:

   ```
   python app.py
   ```

## Usage

1. Open a web browser and navigate to `localhost:5000`.
2. In the terminal, enter the command you want to execute.

The output of the command will be displayed in the web browser in real-time.

## Tail Functionality

WebLogger also supports tail functionality, allowing you to continuously monitor the output of a command.

1. Connect to the web socket by clicking the "Connect" button in the web browser.
2. Enter the command you want to tail in the "Tail" input field.

The web browser will continuously receive and display the output of the command.

## Command Execution

Command execution is handled by `main.py`. It uses `subprocess` to execute the command and save the output to a file called `output.txt`. The output file is then monitored by the web application to display the output in real-time.

## Socket.IO

WebLogger uses Socket.IO for real-time communication between the web browser and the server. The following events are supported:

- `connect`: Emitted when a client connects to the web socket.
- `disconnect`: Emitted when a client disconnects from the web socket.
- `tail`: Emitted to send the tail output to the client.