import sys
from time import time
HEADER_SIZE = 12

class RtpPacket:
	header = bytearray(HEADER_SIZE)

	def __init__(self):
		pass

	def encode(self, version, padding, extension, cc, seqnum, marker, pt, ssrc, payload):
		"""Encode the RTP packet with header fields and payload."""
		timestamp = int(time())
		header = bytearray(HEADER_SIZE)
		#--------------
		# TO COMPLETE
		#--------------
		# Fill the header bytearray with RTP header fields

		#set version
		header[0] |= version<<(7 - 1)

		#set padding
		header[0] |= padding<<(7 - 2)

		#set extension
		header[0] |= extension<<(7 - 3)

		#set cc
		header[0] |= cc

		#set M
		header[1] |= marker<<(7 - 0)

		#set pt
		header[1] |= pt

		#set sequence number msb
		header[2] |= (seqnum >> 8) & 0xFF

		#set sequence number lsb
		header[3] |= seqnum & 0xFF

		#set timestamp and sscr
		for i in range(4,8):
			header[i] |= (timestamp >> (32 - (i - 3)*8))&0xFF
			header[i + 4] = (ssrc >> (32 - (i - 3)*8))&0xFF

		#assign header
		self.header = header

		# assign payload
		self.payload = payload

		# header[0] = ...
		# ...

		# Get the payload from the argument
		# self.payload = ...

	def decode(self, byteStream):
		"""Decode the RTP packet."""
		self.header = bytearray(byteStream[:HEADER_SIZE])
		self.payload = byteStream[HEADER_SIZE:]

	def version(self):
		"""Return RTP version."""
		return int(self.header[0] >> 6)

	def seqNum(self):
		"""Return sequence (frame) number."""
		seqNum = self.header[2] << 8 | self.header[3]
		return int(seqNum)

	def timestamp(self):
		"""Return timestamp."""
		timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
		return int(timestamp)

	def payloadType(self):
		"""Return payload type."""
		pt = self.header[1] & 127
		return int(pt)

	def getPayload(self):
		"""Return payload."""
		return self.payload

	def getPacket(self):
		"""Return RTP packet."""

		#print("packet: ", self.header + self.payload)

		return self.header + self.payload
