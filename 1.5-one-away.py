import unittest

class OneAwayTest(unittest.TestCase):

  def test_oneaway_missing_letter1(self):
    actual = one_away("pale", "ple")
    self.assertTrue(actual)

  def test_oneaway_missing_letter2(self):
    actual = one_away("p", "")
    self.assertTrue(actual)

  def test_oneaway_same_letters(self):
    actual = one_away("justin", "justin")
    self.assertTrue(actual)

  def test_oneaway_missing_letter3(self):
    actual = one_away("jstin", "jsti")
    self.assertTrue(actual)

  def test_oneaway_changed_letter1(self):
    actual = one_away("pale", "bake")
    self.assertFalse(actual)

  def test_oneaway_changed_letters1(self):
    actual = one_away("pale", "bale")
    self.assertTrue(actual)

def one_away(string1, string2):

  diff_count = 0
  i = 0
  j = 0

  # for now, we break out separate case for if the string lengths are 
  # different or not

  if len(string1) == len(string2):

    while (i < len(string1)) and (diff_count <= 1):
      if string1[i] != string2[i]:
        diff_count += 1
      i += 1

  else:
  
    if len(string1) < len(string2):
      string_short = string1
      string_long = string2
    else:
      string_long = string1
      string_short = string2

    while(i < len(string_long)) and (diff_count <= 1):
      if j >= len(string_short):
        diff_count += 1
      else:
        if string_long[i] != string_short[j]:
          diff_count += 1
        else:
          j += 1
      i += 1

  if diff_count > 1:
    return False
  else:
    return True

if __name__ == '__main__':
  unittest.main()
