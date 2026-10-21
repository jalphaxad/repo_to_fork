#!/usr/bin/env python3
import re
import unittest
def rearrange(name):
	pattern=r'^(\w+) (\w+)$'
	return re.sub(pattern,r'\2 \1',name.strip())

class testrearrange(unittest.TestCase):
	def test_return(self):
		self.assertEqual(rearrange('joseph makori'),'makori joseph')
unittest.main()
