**WebLogger**

This repository contains a Flask-based web application that allows you to execute commands on your local machine and tail the output in real-time.

**Requirements**

* Python 3.8 or higher
* Flask
* Flask-SocketIO

**Installation**

1. Clone this repository:
```
git clone https://github.com/IdrisFallout/WebLogger.git
```

2. Install the required Python packages:
```
pip install -r requirements.txt
```

**Usage**

1. Start the web application:
```
python app.py
```

2. Open your browser and navigate to the following URL:
```
http://localhost:5000
```

3. In the text input field, type in the command you want to execute. For example, you can type `ping google.com`.

4. Click the "Execute" button.

5. The output of the command will be displayed in real-time in the text area below.

**WebSockets**

The application uses WebSockets to stream the output of the command to the client in real-time.

**Security**

The application uses the `SECRET_KEY` configuration option to protect the WebSocket connection. You should configure a strong `SECRET_KEY` before deploying the application to a production environment.

**Limitations**

The application only supports executing commands on the local machine. It does not support executing commands over SSH or other remote connections.