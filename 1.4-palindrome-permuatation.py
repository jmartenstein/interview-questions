import unittest

class PalindromePermutationTest(unittest.TestCase):

  def test_is_palindrome_permuatation1(self):
    actual = is_palindrome_permutation("race car")
    self.assertTrue(actual)

  def test_is_palindrome_permuation2(self):
    actual = is_palindrome_permutation("justin")
    self.assertFalse(actual)

  def test_is_palindrome_permutation3(self):
    actual = is_palindrome_permutation("")
    self.assertTrue(actual)

  def test_is_palindrome_permutation4(self):
    actual = is_palindrome_permutation("Tact Coa")
    self.assertTrue(actual)

def is_palindrome_permutation(palindrome):
  palindrome_set = set()
  for letter in palindrome:
    if letter == ' ':
      continue
    else:
      letter = letter.lower()
    if letter not in palindrome_set:
      palindrome_set.add(letter)
    else:
      palindrome_set.remove(letter)

  if len(palindrome_set) <= 1:
    return True
  else:
    return False

if __name__ == '__main__':
  unittest.main()
