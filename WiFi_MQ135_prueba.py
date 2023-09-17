import RPi.GPIO as GPIO
import http.server

host_name = '192.168.0.12'  # IP Address of Raspberry Pi
host_port = 8000


class MyServer(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(b'<html>')
        self.wfile.write(b'<body>')
        self.wfile.write(b'<h1>Welcome to my Raspberry Pi</h1>')
        self.wfile.write(b'</body>')
        self.wfile.write(b'</html>')


# # # # # Main # # # # #

if __name__ == '__main__':
    http_server = http.server.HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()