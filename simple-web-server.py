import http.server
import socketserver
import os
import argparse
import json
from urllib.parse import urlparse, parse_qs

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler that extends SimpleHTTPRequestHandler"""
    
    def do_GET(self):
        """Handle GET requests"""
        # Parse the URL
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)
        
        # Special endpoint for API testing
        if path == '/api/test':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # Create a response with the query parameters and other info
            response = {
                'message': 'API test successful',
                'query_parameters': query_params,
                'method': 'GET',
                'headers': dict(self.headers)
            }
            
            self.wfile.write(json.dumps(response, indent=2).encode())
            return
        
        # Echo endpoint - returns information about the request
        elif path == '/echo':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                'path': self.path,
                'method': 'GET',
                'headers': dict(self.headers),
                'query_parameters': query_params
            }
            
            self.wfile.write(json.dumps(response, indent=2).encode())
            return
            
        # For all other paths, use the default behavior (serve files)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
    def do_POST(self):
        """Handle POST requests"""
        # Get the content length to read the body
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # Parse the URL
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        
        # Handle POST to the API test endpoint
        if path == '/api/test':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # Try to parse the body as JSON
            try:
                body_json = json.loads(post_data)
            except json.JSONDecodeError:
                body_json = None
                
            response = {
                'message': 'POST request received',
                'method': 'POST',
                'headers': dict(self.headers),
                'body': body_json if body_json else post_data
            }
            
            self.wfile.write(json.dumps(response, indent=2).encode())
            return
            
        # Default POST handler
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            'message': 'POST request received',
            'path': self.path,
            'headers': dict(self.headers),
            'body': post_data
        }
        
        self.wfile.write(json.dumps(response, indent=2).encode())

def run_server(port=8000, directory=None):
    """Run the web server on the specified port and directory"""
    handler = CustomHTTPRequestHandler
    
    if directory:
        os.chdir(directory)
        print(f"Serving content from: {directory}")
    
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Server running at http://localhost:{port}")
        print(f"Test API endpoint: http://localhost:{port}/api/test")
        print(f"Echo endpoint: http://localhost:{port}/echo")
        print("Press Ctrl+C to stop the server")
        httpd.serve_forever()

if __name__ == "__main__":
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Simple HTTP server for testing and development")
    parser.add_argument("-p", "--port", type=int, default=8000, help="Port to run the server on (default: 8000)")
    parser.add_argument("-d", "--directory", type=str, help="Directory to serve files from")
    
    args = parser.parse_args()
    
    try:
        run_server(port=args.port, directory=args.directory)
    except KeyboardInterrupt:
        print("\nServer stopped.")
