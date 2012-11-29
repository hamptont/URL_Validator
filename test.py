import unittest
from url import URL

class RadixTestCase(unittest.TestCase):
  def test_validator(self):
    url = URL('www.google.com')
    self.assertFalse(url.isValid())
    url = URL('google.com')
    self.assertFalse(url.isValid())
    url = URL('https://www.google.com/googleplus/whousesthis')
    self.assertTrue(url.isValid())
    url = URL('https://www.google.com/googleplus/whousesthis?true=false&not=really')
    self.assertTrue(url.isValid())
    url = URL('https://www.google.com/')
    self.assertTrue(url.isValid())

  def test_canonicalizer(self):
    url = URL('www.google.com').getNormalized()
    self.assertEqual(url, 'http://www.google.com/')
    url = URL('google.com').getNormalized()
    self.assertEqual(url, 'http://google.com/')
    url = URL('https://www.google.com/googleplus/whousesthis').getNormalized()
    self.assertEqual(url, 'https://www.google.com/googleplus/whousesthis')
    url = URL('https://www.google.com/googleplus/whousesthis?true=false&not=really').getNormalized()
    self.assertEqual(url, 'https://www.google.com/googleplus/whousesthis?true=false&not=really')

  def test_lt(self):
    url1 = URL('www.google.com');
    url2 = URL('www.google.com/hello/world');
    self.assertTrue(url1.__lt__(url2))

    url1 = URL('www.google.com');
    url2 = URL('www.google.com/?hello=world');
    self.assertTrue(url1.__lt__(url2))

    url1 = URL('www.google.com/a');
    url2 = URL('www.google.com/b/oh');
    self.assertTrue(url1.__lt__(url2))

    url1 = URL('www.foogle.com/what');
    url2 = URL('www.google.com/');
    self.assertTrue(url1.__lt__(url2))


  def test_gt(self):
    url1 = URL('www.google.com');
    url2 = URL('www.google.com/hello/world');
    self.assertTrue(url2.__gt__(url1))

    url1 = URL('www.google.com');
    url2 = URL('www.google.com/?hello=world');
    self.assertTrue(url2.__gt__(url1))

    url1 = URL('www.google.com/a');
    url2 = URL('www.google.com/b/oh');
    self.assertTrue(url2.__gt__(url1))

    url1 = URL('www.foogle.com/what');
    url2 = URL('www.google.com/');
    self.assertTrue(url2.__gt__(url1))

  def test_eq(self):
    url1 = URL('www.google.com');
    url2 = URL('www.google.com/');
    self.assertTrue(url2.__eq__(url1))
        
    url1 = URL('google.com');
    url2 = URL('www.google.com/');
    self.assertFalse(url2.__eq__(url1))

    url1 = URL('www.google.com/hello');
    url2 = URL('www.google.com/');
    self.assertFalse(url2.__eq__(url1))

    url1 = URL('https://www.google.com/');
    url2 = URL('http://www.google.com/');
    self.assertFalse(url2.__eq__(url1))

    url1 = URL('google.com');
    url2 = URL('google.com');
    self.assertTrue(url2.__eq__(url1))

if __name__ == '__main__':
  unittest.main()
