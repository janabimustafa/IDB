import unittest
from urllib.request import urlopen
import json
from models import *

UNIVERSAL_PROPERTIES = {"id", "type", "name"}

class TestRLDBAPI(unittest.TestCase):

	# For these tests, we will only test that deserializing the result returns
	# object(s) of the appropriate type. The exact data that is returned may
	# change, and is irrelevant to the functionality of the API. If the API
	# returns SOMETHING, and it is of the right type, we can say the API works
	# properly.

	def testGetAllPaints(self):
		result = urlopen(r"http://127.0.0.1:5000/api/paints/").read().decode()
		object_list = deserialize_list(result)
		self.assertTrue(len(object_list) > 1)
		for obj in object_list:
			self.assertTrue(isinstance(obj, Paint))

	def testGetPaintFinishByName(self):
		result = urlopen(r"http://127.0.0.1:5000/api/paints/Circuit%20Board").read().decode()
		obj = deserialize(result)
		self.assertTrue(isinstance(obj, Paint))

	def testGetPaintFinishByID(self):
		result = urlopen(r"http://127.0.0.1:5000/api/paints/10000").read().decode()
		obj = deserialize(result)
		self.assertTrue(isinstance(obj, Paint))

	def testGetAllBodies(self):
		result = urlopen(r"http://127.0.0.1:5000/api/bodies/").read().decode()
		obj_list = deserialize_list(result)
		self.assertTrue(len(obj_list) > 1)
		for obj in obj_list:
			self.assertTrue(isinstance(obj, Body))

	def testGetBodyByName(self):
		result = urlopen(r"http://127.0.0.1:5000/api/bodies/Backfire").read().decode()
		obj = deserialize(result)
		self.assertTrue(isinstance(obj, Body))

	def testGetBodyById(self):
		result = urlopen(r"http://127.0.0.1:5000/api/bodies/70560080").read().decode()
		obj = deserialize(result)
		self.assertTrue(isinstance(obj, Body))

	def testGetAllDecals(self):
		result = urlopen(r"http://127.0.0.1:5000/api/decals/").read().decode()
		obj_list = deserialize_list(result)
		self.assertTrue(len(obj_list) > 1)
		for obj in obj_list:
			self.assertTrue(isinstance(obj, Decal))

	def testGetDecalByName(self):
		result = urlopen(r"http://127.0.0.1:5000/api/decals/Spatter").read().decode()
		obj = deserialize(result)
		self.assertTrue(isinstance(obj, Decal))

	def testGetDecalByID(self):
		result = urlopen(r"http://127.0.0.1:5000/api/decals/74418619").read().decode()
		obj = deserialize(result)
		self.assertTrue(isinstance(obj, Decal))

	def testGetAllCrates(self):
		result = urlopen(r"http://127.0.0.1:5000/api/crates/").read().decode()
		obj_list = deserialize_list(result)
		self.assertTrue(len(obj_list) > 1)
		for obj in obj_list:
			self.assertTrue(isinstance(obj, Crate))

	def testGetCrateByName(self):
		result = urlopen(r"http://127.0.0.1:5000/api/crates/Turbo%20Crate").read().decode()
		obj = deserialize(result)
		self.assertTrue(isinstance(obj, Crate))

	def testGetCrateByID(self):
		result = urlopen(r"http://127.0.0.1:5000/api/crates/6991").read().decode()
		obj = deserialize(result)
		self.assertTrue(isinstance(obj, Crate))

	def testGetAllDLC(self):
		result = urlopen(r"http://127.0.0.1:5000/api/dlcs/").read().decode()
		obj_list = deserialize_list(result)
		self.assertTrue(len(obj_list) > 1)
		for obj in obj_list:
			self.assertTrue(isinstance(obj, DLC))

	def testGetDLCByName(self):
		result = urlopen(r"http://127.0.0.1:5000/api/dlcs/Supersonic%20Fury").read().decode()
		obj = deserialize(result)
		self.assertTrue(isinstance(obj, DLC))

	def testGetDLCByID(self):
		result = urlopen(r"http://127.0.0.1:5000/api/dlcs/44776510").read().decode()
		obj = deserialize(result)
		self.assertTrue(isinstance(obj, DLC))


	def testGetObjectByID(self):
		result = urlopen(r"http://127.0.0.1:5000/api/id/6991").read().decode()
		obj = deserialize(result)
		self.assertTrue(isinstance(obj, RLObject))
		self.assertTrue(isinstance(obj, Crate))

	def testGetAllPlayers(self):
		result = urlopen(r"http://127.0.0.1:5000/api/players/").read().decode()
		obj_list = deserialize_list(result)
		self.assertTrue(len(obj_list) > 1)
		for obj in obj_list:
			self.assertTrue(isinstance(obj, Player))

	def testGetPlayerByName(self):
		result = urlopen(r"http://127.0.0.1:5000/api/players/Kaydop").read().decode()
		obj = deserialize(result)
		self.assertTrue(isinstance(obj, Player))

	def testGetPlayerByID(self):
		result = urlopen(r"http://127.0.0.1:5000/api/players/201346119").read().decode()
		obj = deserialize(result)
		self.assertTrue(isinstance(obj, Player))

if __name__ == "__main__":
    unittest.main()
