from tkinter import *
from socket import *
import tkinter.messagebox
from PIL import Image, ImageTk
import threading, sys, traceback, os
from time import time, sleep


from RtpPacket import RtpPacket


CACHE_DIR = "Cache_dir"
CACHE_FILE_NAME = "cache-"
CACHE_FILE_EXT = ".jpg"

class Client:
	INIT = 0
	READY = 1
	PLAYING = 2
	state = INIT

	SETUP = 0
	PLAY = 1
	PAUSE = 2
	TEARDOWN = 3

	LABEL = ["Init", "Ready", "Playing"]

	# Initiation..
	def __init__(self, master, serveraddr, serverport, rtpport, filename):

		self.geometry = master.geometry("575x500")
		self.master = master
		self.master.protocol("WM_DELETE_WINDOW", self.handler)
		self.createWidgets()
		self.serverAddr = serveraddr
		print(type(serveraddr))

		self.serverPort = int(serverport)
		self.rtpPort = int(rtpport)
		self.fileName = filename
		self.rtspSeq = 0
		self.sessionId = 0
		self.requestSent = -1
		self.teardownAcked = 0
		self.connectToServer()
		self.frameNbr = 0


		self.VideoStream_handler = {}

		self.setupMovie()




	# THIS GUI IS JUST FOR REFERENCE ONLY, STUDENTS HAVE TO CREATE THEIR OWN GUI
	def createWidgets(self):
		"""Build GUI."""

		# Create Setup button
		# self.setup = Button(self.master, width=20, padx=3, pady=3)
		# self.setup["text"] = "Setup"
		# self.setup["command"] = self.setupMovie
		# self.setup.grid(row=1, column=0, padx=2, pady=2)

		# Create Play button
		self.start = Button(self.master, width=25, padx=3, pady=3)
		self.start["text"] = "Play"
		self.start["command"] = self.playMovie
		self.start.grid(row=1, column=0, padx=2, pady=2)

		# Create Pause button
		self.pause = Button(self.master, width=25, padx=3, pady=3)
		self.pause["text"] = "Pause"
		self.pause["command"] = self.pauseMovie
		self.pause.grid(row=1, column=1, padx=2, pady=2)

		# Create Teardown button
		self.teardown = Button(self.master, width=25, padx=3, pady=3)
		self.teardown["text"] = "Teardown"
		self.teardown["command"] =  self.exitClient
		self.teardown.grid(row=1, column=2, padx=2, pady=2)



		# Create a label to display the movie

		background_image = ImageTk.PhotoImage(Image.open('background_image.jpg'))

		self.label = Label(self.master, height=500, width = 625,image = background_image)
		self.label.image = background_image
		self.label.place(x = 0, y = 40)

		screen_image = ImageTk.PhotoImage(Image.open('screen.jpg'))

		self.screen = Label(self.master, height = 250, width = 313, image = screen_image, anchor = CENTER)
		self.screen.image = screen_image
		self.screen.place(x = 70, y = 140)


		text = Label(self.master, text = "Text")

		text.place(x = 465, y = 90)


	def setupMovie(self):
		"""Setup button handler."""
	#TODO
		if self.state == self.INIT:

			self.sendRtspRequest(0)

			reply_msg = self.recvRtspReply()

			self.parseRtspReply(reply_msg)

			self.openRtpPort()

			self.state = self.READY

		else:
			print("Program has been set up, current state is: ",self.LABEL[self.state])



	def exitClient(self):
		"""Teardown button handler."""
	#TODO

		if self.state == self.PLAYING or self.state == self.READY:

			if self.state == self.PLAYING:

				self.sendRtspRequest(3)

				self.recvRtspReply()

			self.master.destroy()

			image_full_path = os.path.join(CACHE_DIR,str(self.sessionId)+CACHE_FILE_EXT)

			if os.path.isfile(image_full_path):

				os.remove(image_full_path)

				sys.exit(0)

		else:
			print("Program has been set up, current state is: ",self.LABEL[self.state])



	def pauseMovie(self):
		"""Pause button handler."""
	#TODO

		if self.state == self.PLAYING:

			self.sendRtspRequest(2)

			packet = self.recvRtspReply()

			self.state = self.READY

		else:

			print("Program has been set up, current state is: ",self.LABEL[self.state])



	def playMovie(self):
		"""Play button handler."""
	#TODO
		if self.state == self.READY:

			self.sendRtspRequest(1)

			self.VideoStream_handler['event'] = threading.Event()

			self.VideoStream_handler['worker'] = threading.Thread(target = self.listenRtp).start()

			packet = self.recvRtspReply()

			self.state = self.PLAYING

		else:

			print("Program has been set up, current state is: ",self.LABEL[self.state])



	def listenRtp(self):
		"""Listen for RTP packets."""
		#TODO

		self.Data_frame_parser = RtpPacket()

		while True:

			try:

				data, addr = self.RTPSocket.recvfrom(100480)

				self.Data_frame_parser.decode(data)

				self.RTPSocket.settimeout(0.5)

				if self.Data_frame_parser.seqNum() > self.frameNbr:

					self.frameNbr = self.Data_frame_parser.seqNum()

					image_full_path = self.writeFrame(self.Data_frame_parser.getPayload())

					self.updateMovie(image_full_path)

			except:

				if self.VideoStream_handler['event'].isSet():

					break

				elif self.frameNbr == 0:

					print("No packet arrived")

				else:

					print(self.frameNbr)

					print("Received no more packet")

				break




	def writeFrame(self, data):
		"""Write the received frame to a temp image file. Return the image file."""
	#TODO

		image_full_path = os.path.join(CACHE_DIR,str(self.sessionId)+CACHE_FILE_EXT)

		file = open(image_full_path,'wb')

		file.write(data)

		file.close()

		return image_full_path




	def updateMovie(self, imageFile):
		"""Update the image file as video frame in the GUI."""
	#TODO
		try:
			photo = ImageTk.PhotoImage(Image.open(imageFile))
		except:
			print("photo error")

		self.screen.configure(image = photo, height = 250, width = 313)

		self.screen.image = photo


	def connectToServer(self):
		"""Connect to the Server. Start a new RTSP/TCP session."""
	#TODO
		try:
			self.clientSocket = socket(AF_INET,SOCK_STREAM)
			self.clientSocket.bind(('',self.rtpPort))
			self.clientSocket.connect((self.serverAddr,self.serverPort))
		except:
			tkinter.messagebox.showerror("showerror","Fail to connect")
			return

		print("Connection established")




	def sendRtspRequest(self, requestCode):
		"""Send RTSP request to the server."""
		#-------------
		# TO COMPLETE
		#-------------

		self.rtspSeq += 1

		request = ""

		if requestCode == self.SETUP:
			request = "SETUP "+self.fileName+" RTSP/1.0\n"
			request += "CSeq: "+str(self.rtspSeq)+"\n"
			request += "Transport: RTP/UDP; client_port= "+str(self.rtpPort)


		elif requestCode == self.READY:
			request = "PLAY "+self.fileName+" RTSP/1.0\n"
			request += "CSeq: "+str(self.rtspSeq)+"\n"
			request += "Session: "+str(self.sessionId)


		elif requestCode == self.PAUSE:
			request = "PAUSE "+self.fileName + " RTSP/1.0\n"
			request += "CSeq: "+str(self.rtspSeq)+"\n"
			request += "Session: "+str(self.sessionId)


		else:
			request = "TEARDOWN "+self.fileName + " RTSP/1.0\n"
			request += "CSeq: "+str(self.rtspSeq)+"\n"
			request += "Session: "+str(self.sessionId)



		self.clientSocket.sendall(str.encode(request))

	def recvRtspReply(self):
		"""Receive RTSP reply from the server."""
		#TODO
		reply = self.clientSocket.recv(4*1024).decode()

		print(reply)

		return reply




	def parseRtspReply(self, data):
		"""Parse the RTSP reply from the server."""
		#TODO
		if self.state == self.INIT:
			reply = data.split('\n')
			line3 = reply[2]
			self.sessionId = int(line3.split(' ')[1])
			print("Session id: ",self.sessionId)




	def openRtpPort(self):
		"""Open RTP socket binded to a specified port."""
		#-------------
		# TO COMPLETE
		#-------------
		# Create a new datagram socket to receive RTP packets from the server
		# self.rtpSocket = ...

		# Set the timeout value of the socket to 0.5sec
		# ...
		self.RTPSocket = socket(AF_INET,SOCK_DGRAM)

		self.RTPSocket.bind(('',self.rtpPort))

		self.RTPSocket.settimeout(0.5)






	def handler(self):
		"""Handler on explicitly closing the GUI window."""
		#TODO

		if self.state == self.INIT:

			self.master.destroy()

			sys.exit(0)

		else:

			self.exitClient()
