import http.server
import socketserver
import subprocess

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/c1':
            result = subprocess.run(['jmeter.sh', '-n', '-t', 'esb-1tps.jmx'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Send a 200 OK response
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(result.stdout)

        elif self.path == '/c2':
            result = subprocess.run(['jmeter.sh', '-n', '-t', 'esb-1000tps.jmx'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(result.stdout)


        elif self.path == '/c3':
            result = subprocess.run(['jmeter.sh', '-n', '-t', 'esb-1000tps-10min.jmx'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(result.stdout)

        else:
            # Handle other paths
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
~
          
