import http.server
import socketserver
import json

PORT = 8000

# Simple handler to serve static files and respond with JSON data
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':  # Endpoint to return JSON data
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Example data to pass to the frontend
            data = {
                "name": "John Doe",
                "age": 25,
                "city": "New York"
            }

            # Send JSON data to the frontend
            self.wfile.write(json.dumps(data).encode())
        
        elif self.path == '/':
            # Serve the HTML file
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open("templates/index.html", "rb") as file:
                self.wfile.write(file.read())

        else:
            self.send_response(404)
            self.end_headers()

# Start the server
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()