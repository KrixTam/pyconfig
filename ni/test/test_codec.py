import unittest
import os
from ni.config import EasyCodec

cwd = os.path.abspath(os.path.dirname(__file__))
test_filename = os.path.join(cwd, 'key.dat')


class TestCodec(unittest.TestCase):

    def test_default(self):
        codec = EasyCodec()
        message = '测试一下这个能否正确加解密'
        self.assertEqual(message, codec.decode(codec.encode(message)))
        ec = EasyCodec(test_filename)
        e_message = b'gAAAAABgvOaW4FxnYy9Y7nlZZ31EunzokoqNvxh5Xbk5gI8KeWe3Jk7NOlZ99V7FuqI2ZZbObDs2PJE1eV6Pt4S-vLs5u3K5WZFB14BbBNA9xQRexEzHz8vSc0usJa0yQcpk3dfOgZGh'
        self.assertEqual(message, ec.decode(e_message))


if __name__ == '__main__':
    unittest.main()
