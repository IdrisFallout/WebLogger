# WebLogger

## Overview

WebLogger is a simple web application that allows users to execute commands in their terminal and view the output in real-time through a web interface. It uses Flask, Flask-SocketIO, and subprocess to handle client connections, execute commands, and stream the output back to the client.

## Features

- Execute commands in the terminal
- View the output of the commands in real-time
- Tail a file for continuous updates

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/IdrisFallout/WebLogger.git
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the app:
   ```
   python app.py
   ```

2. Open a web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Enter a command in the text box and click the "Execute" button.

## Configuration

The following configuration options are available in the `app.py` file:

- `SECRET_KEY`: The secret key used for Flask session management.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

WebLogger is released under the MIT license. See the [LICENSE](LICENSE) file for more information.