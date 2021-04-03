from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import time
import board
import adafruit_dht

hostName = ""
serverPort = 8080

dhtDevice = adafruit_dht.DHT22(board.D4)

dhtTemp = 0.0
dhtHum = 0.0

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Sensors</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Temperature %s &deg;C</p>" % dhtTemp, "utf-8"))
        self.wfile.write(bytes("<p>Humidity %s %%</p>" % dhtHum, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

def start_server():
        webServer = HTTPServer((hostName, serverPort), MyServer)
        webServer.serve_forever()

if __name__ == "__main__":
        daemon = threading.Thread(name='daemon_server', target=start_server)
        daemon.setDaemon(True)
        daemon.start()

        while True:
                try:
                        dhtTemp = dhtDevice.temperature
                        dhtHum = dhtDevice.humidity
                        print("Temperature: {:.1f} Humidity: {}".format(dhtTemp, dhtHum))

                except RuntimeError as error:
                        print(error.args[0])
                        continue
                except Exception as error:
                        dhtDevice.exit()
                        raise error

                time.sleep(2)
