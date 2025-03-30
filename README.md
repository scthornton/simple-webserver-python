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

# Combine options
python simple_server.py --port 3000 --directory ./website
```

### Help

```bash
python simple_server.py --help
```

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serves files from the specified directory |
| `/api/test` | GET | Returns a JSON response with query parameters and request info |
| `/api/test` | POST | Accepts and echoes back POST data as JSON |
| `/echo` | GET | Returns detailed information about the incoming request |

## Examples

### Serving Static Files

1. Create an `index.html` file in your directory
2. Run the server
3. Open `http://localhost:8000` in your browser

### Testing GET Requests

Try accessing:
```
http://localhost:8000/api/test?name=John&role=developer
```

You'll receive a JSON response like:
```json
{
  "message": "API test successful",
  "query_parameters": {
    "name": ["John"],
    "role": ["developer"]
  },
  "method": "GET",
  "headers": {
    "User-Agent": "Mozilla/5.0...",
    ...
  }
}
```

### Testing POST Requests

Using curl:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"John","age":30}' http://localhost:8000/api/test
```

Response:
```json
{
  "message": "POST request received",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json",
    ...
  },
  "body": {
    "name": "John",
    "age": 30
  }
}
```

## How It Works

The server builds on Python's built-in `http.server` module, extending it with:

1. Custom request handling for API endpoints
2. JSON response formatting
3. Support for query parameters and POST data
4. Command-line configuration options

## Use Cases

- Local web development testing
- Mocking APIs during frontend development
- Learning HTTP concepts and web server functionality
- Simple file sharing on a local network
- Testing webhooks locally

## Requirements

- Python 3.6 or higher
- No external dependencies required

## License

MIT

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

