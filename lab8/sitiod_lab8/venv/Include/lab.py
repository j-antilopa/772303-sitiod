import http.server as server
import socketserver
import pymongo

PORT = 1548


class HTTPHandler(server.SimpleHTTPRequestHandler):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['sitiod']
    table = db["logs"]

    def log_message(self, format, *args):
        log = {"client": self.client_address[0],
               "date": self.log_date_time_string(),
               "request": format % args}
        self.table.insert_one(log)
        print(id)


Handler = HTTPHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.serve_forever()
