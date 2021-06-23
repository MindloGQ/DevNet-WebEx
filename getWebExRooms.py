import requests
import json
from WebExBearerToken import WebExBearerToken

url = 'https://webexapis.com/v1/rooms'
hdr = {'Authorization': "Bearer "+ WebExBearerToken, 'content-type' : 'application/json'}


roomData = '{"title": "MindloGQPythonRoom"}'


def create_room():
	"""
		creates a new WebEx room
	"""
	resp = requests.post(url, headers=hdr, data=roomData)
	print("post new room response status:", resp)
	get_rooms()

def get_rooms():
	"""
		function for retrieving a list of WebEx rooms
	"""
	resp = requests.get(url, headers=hdr)
	print("get rooms response status:", resp)
	rooms_list = resp.json()

	print_rooms_info(rooms_list)


#Functions to Print Nice tables
def print_rooms_info(rooms_list):
	"""Print list of organizations
	"""
	print("{0:45}{1:30}".format("Room Name", "Room Type"))
	for room in rooms_list['items']:
		print("{0:45}{1:30}".format(room['title'], room['type']))


if __name__ == "__main__":
	create_room()