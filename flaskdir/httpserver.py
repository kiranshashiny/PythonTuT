#!/usr/bin/python3

import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "127.0.0.1"
hostPort = 8081 

class MyServer(BaseHTTPRequestHandler):

	#	GET is for clients geting the predi
	def do_GET(self):
		self.send_response(200)
		self.send_header ( "HTTP-Version" , "HTTP/1.1" )
		self.end_headers( )
		print ("IN the do_GET function")
		self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))


	#	POST is for submitting data.
	def do_POST(self):

		print( "incomming http: ", self.path )

		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		post_data = self.rfile.read(content_length) # <--- Gets the data itself
		self.send_response(200)

		client.close()

		#import pdb; pdb.set_trace()


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))


