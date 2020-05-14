import http.server as server
import socketserver
import pymongo

# Port which requests will be handled
PORT = 1548


# Creating class for handling request
class HTTPHandler(server.SimpleHTTPRequestHandler):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['sitiod-lab8']
    table = db["request-logs"]

    def log_message(self, info, *args):
        log = {"sender": self.client_address[0],
               "request-date": self.log_date_time_string(),
               "request-info": info % args}
        self.table.insert_one(log)
        print(id)


Handler = HTTPHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.serve_forever()
