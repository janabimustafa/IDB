from unittest import main, TestCase
from urllib.request import urlopen
import json
import db_definitions

UNIVERSAL_PROPERTIES = {"id", "type", "name"}

class TestRLDBAPI(TestCase):


	def testGetAllPaints(self):
		result = urlopen("http://dev.rldb.me/api/paints/").read().decode()
		obj = db_definitions.deserialize(result)

	def testGetPaintFinishByName(self):
		result = urlopen("http://dev.rldb.me/api/paints/Circuit%20Board").read().decode()
		self.assertEqual(result, "[]")
		self.assertEqual(None, "Results returned as expected, given we have no data")

	def testGetPaintFinishByID(self):
		result = urlopen("http://dev.rldb.me/api/paints/0").read().decode()
		self.assertEqual(result, "[]")
		self.assertEqual(None, "Results returned as expected, given we have no data")

	def testGetAllBodies(self):
		result = urlopen("http://dev.rldb.me/api/paints/0").read().decode()
		bodyNames = [""]


if __name__ == "__main__":
    main()
