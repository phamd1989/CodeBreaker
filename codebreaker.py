import sys

def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except ValueError:
        return default
 
class CodeBreak:
  def play(self, params):
    if len(params) == 0 :
      params = sys.argv
    l = len(params)
    if(l == 2 and params[1].startswith("--debug=")):
      code=params[1][len("--debug="):]
      try:
	self.code = int(code)
      except ValueError:
        self.code = None

      print 'Code :: ', self.code

#c = CodeBreak()
#c.play(sys.argv)


import unittest
class TestCodeBreak(unittest.TestCase):
  def setUp(self):
    self.c = CodeBreak()
  def testCodeGood(self):
    self.c.play(["programname", "--debug=2342"])
    self.assertEqual(self.c.code, 2342)
  def testCodeBad(self):
    self.c.play(["programname", "--debug=2342a"])
    self.assertEqual(self.c.code, None)


if __name__ == "__main__":
  unittest.main()


