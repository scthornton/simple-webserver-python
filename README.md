# simple-webserver-python
 
Let me explain how I built this simple web server script and how it works:
What the Script Does
This Python script creates a customizable web server that:

Serves static files from a directory (HTML, CSS, JavaScript, etc.)
Provides API testing endpoints that return JSON responses
Handles both GET and POST requests
Can be configured for different ports and directories

How to Use It

Save the script as simple_server.py
Run it from the command line:
Copypython simple_server.py

Access it in your browser at http://localhost:8000

You can also:

Change the port: python simple_server.py --port 8080
Serve files from a specific directory: python simple_server.py --directory /path/to/your/files

Key Features and Testing

Static file serving: Put HTML/CSS/JS files in the same directory and access them by name
API test endpoint: Try http://localhost:8000/api/test?name=value&another=parameter
Echo endpoint: Visit http://localhost:8000/echo to see details about your request
POST handling: Use tools like Postman or curl to send POST requests to /api/test

Code Breakdown
Let me walk through how I built this script:

Imported necessary modules:

http.server: Python's built-in HTTP server library
socketserver: Handles the network connections
os: For directory operations
argparse: For command-line arguments
json: For working with JSON data
urllib.parse: For parsing URLs and query parameters


Created a custom request handler class:

Extends SimpleHTTPRequestHandler to inherit file-serving capabilities
Overrides do_GET to handle GET requests
Overrides do_POST to handle POST requests
Adds special endpoints for API testing


Added the main server function:

Sets up the TCP server with our handler
Configures the port and directory
Starts the server with error handling


Implemented command-line parsing:

Uses argparse to handle command-line options
Provides help text for users



Learning Points

Object-Oriented Programming: The script uses class inheritance to extend built-in functionality
HTTP Protocol: You can see how HTTP requests and responses are structured
JSON APIs: The script demonstrates creating simple JSON responses
Command-line Interfaces: Shows how to make a configurable script
Error Handling: Includes try/except blocks for graceful error handling
