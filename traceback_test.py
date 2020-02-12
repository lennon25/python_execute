#!/usr/bin/env python3

import traceback
import unittest
import logging
import sys


class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def get_grade(self):
		if self.score >= 80:
			return "A"
		elif self.score >=60:
			return "B"
		else:
			return "C"


class StudentTest(unittest.TestCase):

	def test_80_100(self):
		s1 = Student("BART", 80)
		s2 = Student('Lisa', 100)
		self.assertEqual(s1.get_grade(), 'A')
		self.assertEqual(s2.get_grade(), 'A')

	def test_invalid(self):
		s1 = Student('Bart', -1)
		s2 = Student('Lisa', 101)
		with self.assertRaises(ValueError):
			s1.get_grade()
		with self.assertRaises(ValueError):
			s2.get_grade()


if __name__ == '__main__':
	# logger = logging.getLogger()
	# logger.level = logging.DEBUG
	# stream_handler = logging.StreamHandler(sys.stdout)
	# logger.addHandler(stream_handler)

	# filename="./traceback.log"
	# logging.basicConfig(filename=filename, filemode="w+",
 #                        format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
 #                        datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)
 
 	 try:
	# 	unittest.main()
	# except:
	# 	s = traceback.format_exc()
	# 	logging.error(s)
	
	suite = unittest.TestSuite()
	suite.addTest(StudentTest("test_80_100"))
	suite.addTest(StudentTest("test_invalid"))
	with open(filename, 'w+') as f:
		runner = unittest.TextTestRunner(verbosity=2, stream=f)
		runner.run(suite)
		f.close()
	#