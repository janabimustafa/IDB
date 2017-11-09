import unittest
import requests
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
        result = requests.get(r"http://127.0.0.1:5000/api/paints/").text
        object_list = deserialize_list(result)
        self.assertTrue(len(object_list) > 1)
        for obj in object_list:
            self.assertTrue(isinstance(obj, Paint))

    def testGetPaintFinishByName(self):
        result = requests.get(r"http://127.0.0.1:5000/api/paints/Circuit%20Board").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Paint))

    def testGetPaintFinishByID(self):
        result = requests.get(r"http://127.0.0.1:5000/api/paints/10000").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Paint))

    def testGetAllBodies(self):
        result = requests.get(r"http://127.0.0.1:5000/api/bodies/").text
        object_list = deserialize_list(result)
        self.assertTrue(len(object_list) > 1)
        for obj in object_list:
            self.assertTrue(isinstance(obj, Body))

    def testGetBodyByName(self):
        result = requests.get(r"http://127.0.0.1:5000/api/bodies/Backfire").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Body))

    def testGetBodyById(self):
        result = requests.get(r"http://127.0.0.1:5000/api/bodies/70560080").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Body))

    def testGetAllDecals(self):
        result = requests.get(r"http://127.0.0.1:5000/api/decals/").text
        object_list = deserialize_list(result)
        self.assertTrue(len(object_list) > 1)
        for obj in object_list:
            self.assertTrue(isinstance(obj, Decal))

    def testGetDecalByName(self):
        result = requests.get(r"http://127.0.0.1:5000/api/decals/Spatter").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Decal))

    def testGetDecalByID(self):
        result = requests.get(r"http://127.0.0.1:5000/api/decals/74418619").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Decal))

    def testGetAllCrates(self):
        result = requests.get(r"http://127.0.0.1:5000/api/crates/").text
        object_list = deserialize_list(result)
        self.assertTrue(len(object_list) > 1)
        for obj in object_list:
            self.assertTrue(isinstance(obj, Crate))

    def testGetCrateByName(self):
        result = requests.get(r"http://127.0.0.1:5000/api/crates/Turbo%20Crate").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Crate))

    def testGetCrateByID(self):
        result = requests.get(r"http://127.0.0.1:5000/api/crates/6991").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Crate))

    def testGetAllDLC(self):
        result = requests.get(r"http://127.0.0.1:5000/api/dlcs/").text
        object_list = deserialize_list(result)
        self.assertTrue(len(object_list) > 1)
        for obj in object_list:
            self.assertTrue(isinstance(obj, DLC))

    def testGetDLCByName(self):
        result = requests.get(r"http://127.0.0.1:5000/api/dlcs/Supersonic%20Fury").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, DLC))

    def testGetDLCByID(self):
        result = requests.get(r"http://127.0.0.1:5000/api/dlcs/44776510").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, DLC))


    def testGetObjectByID(self):
        result = requests.get(r"http://127.0.0.1:5000/api/id/6991").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, RLObject))
        self.assertTrue(isinstance(obj, Crate))

    def testGetAllPlayers(self):
        result = requests.get(r"http://127.0.0.1:5000/api/players/").text
        object_list = deserialize_list(result)
        self.assertTrue(len(object_list) > 1)
        for obj in object_list:
            self.assertTrue(isinstance(obj, Player))

    def testGetPlayerByName(self):
        result = requests.get(r"http://127.0.0.1:5000/api/players/Kaydop").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Player))

    def testGetPlayerByID(self):
        result = requests.get(r"http://127.0.0.1:5000/api/players/143045192").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Player))

    def testGetBodiesCrates(self):
        result = requests.get(r"http://127.0.0.1:5000/api/bodies/42545540").text
        obj = deserialize(result)
        self.assertTrue(len(obj.crates) > 0)
    def testGetBodiesDlcs(self):
        result = requests.get(r"http://127.0.0.1:5000/api/bodies/Scarab").text
        obj = deserialize(result)
        self.assertTrue(len(obj.dlcs) > 0)
    def testGetAllBoosts(self):
        result = requests.get(r"http://127.0.0.1:5000/api/boosts").text
        object_list = deserialize_list(result)
        self.assertTrue(len(object_list) > 1)
        for obj in object_list:
            self.assertTrue(isinstance(obj, Boost))

    def testGetBoostByName(self):
        result = requests.get(r"http://127.0.0.1:5000/api/boosts/Datastream").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Boost))

    def testGetBoostByID(self):
        result = requests.get(r"http://127.0.0.1:5000/api/boosts/89065759").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Boost))

    def testGetAllWheels(self):
        result = requests.get(r"http://127.0.0.1:5000/api/wheels").text
        object_list = deserialize_list(result)
        self.assertTrue(len(object_list) > 1)
        for obj in object_list:
            self.assertTrue(isinstance(obj, Wheel))

    def testGetWheelByName(self):
        result = requests.get(r"http://127.0.0.1:5000/api/wheels/Veloce").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Wheel))

    def testGetWheelByID(self):
        result = requests.get(r"http://127.0.0.1:5000/api/wheels/3509034").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Wheel))

    def testGetAllToppers(self):
        result = requests.get(r"http://127.0.0.1:5000/api/toppers").text
        object_list = deserialize_list(result)
        self.assertTrue(len(object_list) > 1)
        for obj in object_list:
            self.assertTrue(isinstance(obj, Topper))

    def testGetTopperByName(self):
        result = requests.get(r"http://127.0.0.1:5000/api/toppers/Beret").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Topper))

    def testGetTopperByID(self):
        result = requests.get(r"http://127.0.0.1:5000/api/toppers/47806438").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Topper))

    def testGetAllExplosions(self):
        result = requests.get(r"http://127.0.0.1:5000/api/explosions").text
        object_list = deserialize_list(result)
        self.assertTrue(len(object_list) > 1)
        for obj in object_list:
            self.assertTrue(isinstance(obj, Explosion))

    def testGetExplosionByName(self):
        result = requests.get(r"http://127.0.0.1:5000/api/explosions/Classic").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Explosion))

    def testGetExplosionByID(self):
        result = requests.get(r"http://127.0.0.1:5000/api/explosions/58207753").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Explosion))

    def testGetAllTrails(self):
        result = requests.get(r"http://127.0.0.1:5000/api/trails").text
        object_list = deserialize_list(result)
        self.assertTrue(len(object_list) > 1)
        for obj in object_list:
            self.assertTrue(isinstance(obj, Trail))

    def testGetTrailByName(self):
        result = requests.get(r"http://127.0.0.1:5000/api/trails/Batmobile").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Trail))

    def testGetTrailByID(self):
        result = requests.get(r"http://127.0.0.1:5000/api/trails/29653844").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Trail))

    def testGetAllBanners(self):
        result = requests.get(r"http://127.0.0.1:5000/api/banners").text
        object_list = deserialize_list(result)
        self.assertTrue(len(object_list) > 1)
        for obj in object_list:
            self.assertTrue(isinstance(obj, Banner))

    def testGetBannerByName(self):
        result = requests.get(r"http://127.0.0.1:5000/api/banners/Block").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Banner))

    def testGetBannerByID(self):
        result = requests.get(r"http://127.0.0.1:5000/api/banners/34975547").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Banner))

    def testGetAllAntennas(self):
        result = requests.get(r"http://127.0.0.1:5000/api/antennas").text
        object_list = deserialize_list(result)
        self.assertTrue(len(object_list) > 1)
        for obj in object_list:
            self.assertTrue(isinstance(obj, Antenna))

    def testGetAntennaByName(self):
        result = requests.get(r"http://127.0.0.1:5000/api/antennas/Balloon%20dog").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Antenna))

    def testGetAntennaByID(self):
        result = requests.get(r"http://127.0.0.1:5000/api/antennas/74354673").text
        obj = deserialize(result)
        self.assertTrue(isinstance(obj, Antenna))


class TestSerialization(unittest.TestCase):

    def testSerialize(self):
        i = RLObject(name='test', id=0,  image='null')
        out = serialize(i)
        self.assertTrue(out == {'name': 'test', 'id': 0, 'type': None,
            'image': 'null', 'crates': [], 'dlcs': []})

    def testReserialize(self):
        i = Crate(name='test', id=0, description='Test', image='null')
        out = deserialize(serialize_str(i))
        self.assertTrue(getattr(i, attr) == getattr(out, attr) for attr in vars(i) if not attr.startswith('_'))

    def testDeserialize(self):
        out = deserialize('''
        {
            "description": "Test",
            "source": null,
            "rarity": null,
            "release_date": "1970-01-01",
            "image": "null",
            "dlcs": [],
            "id": 0,
            "items": [],
            "retire_date": null,
            "platform": null,
            "name": "test",
            "crates": [],
            "type": "crate"
        }''')
        self.assertTrue(isinstance(out, Crate))

if __name__ == "__main__":
    unittest.main()
