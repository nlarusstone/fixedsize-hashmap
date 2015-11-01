from hashmap import hashmap
import unittest

class HashMapTests(unittest.TestCase):

    def testHashMapConstructor(self):
        h = hashmap(5)
        self.failUnless(h)

    def testSetElementInHashMap(self):
        h = hashmap(5)
        self.assertTrue(h.set("key1", "val1"))

    def testHashMapFull(self):
        h = hashmap(2)
        h.set("key1", "val1")
        h.set("key2", "val2")
        self.assertFalse(h.set("key3", "val3"))

    def testGetElementInHashMap(self):
        h = hashmap(5)
        h.set("key1", "val1")
        self.assertIsNotNone(h.get("key1")) 

    def testGetElementNotInHashMap(self):
        h = hashmap(5)
        self.assertIsNone(h.get("key1"))

    def testValueStoredInHashMap(self):
        h = hashmap(5)
        h.set("key1", "val1")
        self.assertIs(h.get("key1"), "val1")

    def testValueOverwrittenInHashMap(self):
        h = hashmap(5)
        h.set("key1", "val1")
        h.set("key1", "val2")
        self.assertIs(h.get("key1"), "val2")

    def testValueDeletedFromHashMap(self):
        h = hashmap(5)
        h.set("key1", "val1")
        h.delete("key1")
        self.assertIsNone(h.get("key1"))

    def testLoad(self):
        h = hashmap(4)
        h.set("key1", "val1")
        self.assertEqual(h.load(), 0.25)

    def testInvalidSizeException(self):
        try:
            h = hashmap(0)
            self.failUnless(False)
        except ValueError:
            self.failUnless(True)

if __name__ == '__main__':
    unittest.main()
