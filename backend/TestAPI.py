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
		result = urlopen("http://dev.rldb.me/api/bodies/0").read().decode()
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

if __name__ == "__main__":
    main()
