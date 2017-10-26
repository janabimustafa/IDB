from unittest import main, TestCase
from urllib.request import urlopen
import json
from db_definitions import *

UNIVERSAL_PROPERTIES = {"id", "type", "name"}

class TestRLDBAPI(TestCase):

	# For these tests, we will only test that deserializing the result returns
	# object(s) of the appropriate type. The exact data that is returned may
	# change, and is irrelevant to the functionality of the API. If the API
	# returns SOMETHING, and it is of the right type, we can say the API works
	# properly.

	def testGetAllPaints(self):
		result = urlopen("http://dev.rldb.me/api/paints/").read().decode()
		object_list = deserialize_list(result)
		self.assertTrue(len(obj) > 1)
		for obj in object_list:
			self.assertTrue(isinstance(obj, Paint))

	def testGetPaintFinishByName(self):
		result = urlopen("http://dev.rldb.me/api/paints/Circuit%20Board").read().decode()
		obj = desserialize(result)
		self.assertEqual(isinstance(obj, Paint))

	def testGetPaintFinishByID(self):
		result = urlopen("http://dev.rldb.me/api/paints/0").read().decode()
		obj = desserialize(result)
		self.assertEqual(isinstance(obj, Paint))

	def testGetAllBodies(self):
		result = urlopen("http://dev.rldb.me/api/bodies").read().decode()
		obj_list = deserialize_list(result)
		self.assertTrue(len(obj) > 1)
		for obj in object_list:
			self.assertTrue(isinstance(obj, Body))

	def testGetBodyByName(self):
		result = urlopen("http://dev.rldb.me/api/bodies/Backfire").read().decode()
		obj = desserialize(result)
		self.assertEqual(isinstance(obj, Body))

	def testGetBodyById(self):
		result = urlopen("http://dev.rldb.me/api/bodies/7071").read().decode()
		obj = desserialize(result)
		self.assertEqual(isinstance(obj, Body))

	def testGetAllDecals(self):
		result = urlopen("http://dev.rldb.me/api/decals").read().decode()
		obj_list = deserialize_list(result)
		self.assertTrue(len(obj) > 1)
		for obj in object_list:
			self.assertTrue(isinstance(obj, Decal))

	def testGetDecalByName(self):
		result = urlopen("http://dev.rldb.me/api/decals/Funny%20Book").read().decode()
		obj = desserialize(result)
		self.assertEqual(isinstance(obj, Decal))

	def testGetDecalByID(self):
		result = urlopen("http://dev.rldb.me/api/decals/0").read().decode()
		obj = desserialize(result)
		self.assertEqual(isinstance(obj, Decal))

	def testGetAllCrates(self):
		result = urlopen("http://dev.rldb.me/api/crates").read().decode()
		obj_list = deserialize_list(result)
		self.assertTrue(len(obj) > 1)
		for obj in object_list:
			self.assertTrue(isinstance(obj, Crate))

	def testGetCrateByName(self):
		result = urlopen("http://dev.rldb.me/api/Crate/Turbo%20Crate").read().decode()
		obj = desserialize(result)
		self.assertEqual(isinstance(obj, Crate))

	def testGetCrateByID(self):
		result = urlopen("http://dev.rldb.me/api/Crate/6991").read().decode()
		obj = desserialize(result)
		self.assertEqual(isinstance(obj, Crate))

	def testGetAllDLC(self):
		result = urlopen("http://dev.rldb.me/api/dlcs").read().decode()
		obj_list = deserialize_list(result)
		self.assertTrue(len(obj) > 1)
		for obj in object_list:
			self.assertTrue(isinstance(obj, DLC))

	def testGetDLCByName(self):
		result = urlopen(r"http://dev.rldb.me/api/dlcs/Supersonic%20Fury").read().decode()
		obj = desserialize(result)
		self.assertEqual(isinstance(obj, DLC))

	def testGetDLCByID(self):
		result = urlopen(r"http://dev.rldb.me/api/dlcs/0").read().decode()
		obj = desserialize(result)
		self.assertEqual(isinstance(obj, DLC))

	def testGetObjectByID(self):
		result = urlopen("http://dev.rldb.me/api/id/6991").read().decode()
		obj = desserialize(result)
		self.assertEqual(isinstance(obj, RLObject))
		self.assertEqual(isinstance(obj, Crate))

	def testGetAllPlayers(self):
		result = urlopen("http://dev.rldb.me/api/players").read().decode()
		obj_list = deserialize_list(result)
		self.assertTrue(len(obj) > 1)
		for obj in object_list:
			self.assertTrue(isinstance(obj, Player))

	def testGetPlayerByID(self):
		result = urlopen(r"http://dev.rldb.me/api/players/76561198067659330").read().decode()
		obj = desserialize(result)
		self.assertEqual(isinstance(obj, Player))

if __name__ == "__main__":
    main()
