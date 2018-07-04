import unittest

from converter import convert_ip, FormatError


class TestIpConverter(unittest.TestCase):
    def test_correctness(self):
        assert 2896692481 == convert_ip('172.168.5.1\0')
        assert 16843009 == convert_ip('1.1.1.1\0')
        assert 0 == convert_ip('0.0.0.0\0')
        assert 4294967295 == convert_ip('255.255.255.255\0')

    def test_format(self):
        assert 2896692481 == convert_ip('172 .168.5.1\0')
        assert 2896692481 == convert_ip('172. 168.5.1\0')
        assert 2896692481 == convert_ip('172. 168 .5.1\0')
        assert 2896692481 == convert_ip('172 . 168 . 5 . 1\0')
        try:
            convert_ip('172.1 68.5.1\0')
            assert False
        except FormatError:
            pass

        try:
            convert_ip('1 72.1 68.5.1\0')
            assert False
        except FormatError:
            pass

        try:
            convert_ip('172.168.5.1 \0')
            assert False
        except FormatError:
            pass

        try:
            convert_ip(' 172.168.5.1\0')
            assert False
        except FormatError:
            pass

        try:
            convert_ip('172.168.5.1')
            assert False
        except FormatError:
            pass


if __name__ == '__main__':
    unittest.main()
