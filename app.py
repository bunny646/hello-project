from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            body = b"Hello from Python in Docker!\n"
            self.send_response(200)
        else:
            body = b"Not found\n"
            self.send_response(404)

        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer(("0.0.0.0", port), HelloHandler)
    print(f"Serving on port {port}", flush=True)
    server.serve_forever()
