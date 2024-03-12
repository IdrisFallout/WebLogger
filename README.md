## WebLogger

A simple web application that allows you to monitor the output of a command in real-time.

### Features

- Execute commands from the web interface
- Real-time updates of the command output
- Stores the command output in a file for later review

### Installation

1. Create a virtual environment:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the application:

   ```
   python main.py
   ```

4. Open a web browser and go to `http://localhost:5000`.

### Usage

1. Enter the command you want to execute in the input field and click "Run".
2. The output of the command will be displayed in the textarea below.
3. The output is also saved to a file called `output.txt`.

### Troubleshooting

If you encounter any problems, please open an issue on the GitHub repository.