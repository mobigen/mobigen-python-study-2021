import sys
import unittest


class TestGenerator(unittest.TestCase):
    TEST_SCRIPT = "generator_skeleton"
    max_duration = 1

    @classmethod
    def setUpClass(cls) -> None:
        cls.module = __import__(cls.TEST_SCRIPT)
        print(cls.TEST_SCRIPT)

    def test_get_values(self):
        print(self.TEST_SCRIPT)
        (group, cnt), duration = self.module.get_values()
        self.assertEqual(
            group,
            {
                0: 100000,
                1: 100000,
                2: 100000,
                3: 100000,
                4: 100000,
                5: 100000,
                6: 100000,
                7: 100000,
                8: 100000,
                9: 100000}
        )
        self.assertEqual(cnt, 1000000)
        if duration > self.max_duration:
            self.fail(f"duration is grater than {self.max_duration}: [{duration}]")
        else:
            pass

    def test_get_values_generator(self):
        print(self.TEST_SCRIPT)
        (group, cnt), duration = self.module.get_values_generator()
        self.assertEqual(
            group,
            {
                0: 100000,
                1: 100000,
                2: 100000,
                3: 100000,
                4: 100000,
                5: 100000,
                6: 100000,
                7: 100000,
                8: 100000,
                9: 100000}
        )
        self.assertEqual(cnt, 1000000)
        if duration > self.max_duration / 2:
            self.fail(f"duration is grater than {self.max_duration / 2}: [{duration}]")
        else:
            pass


if __name__ == '__main__':
    if len(sys.argv) > 1:
        TestGenerator.TEST_SCRIPT = "generator_" + sys.argv.pop().strip()
    unittest.main()
