import HomeWork2Mod12 as hw
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = {}

    def setUp(self):
        self.Us = hw.Runner("Усэйн", 10)
        self.Andr = hw.Runner("Андрей", 9)
        self.Nik = hw.Runner("Ник", 3)


    @classmethod
    def tearDownClass(cls):
        for key, value in all_results.items():
            print(value)


    def test_run_an(self):
        andr_nik = hw.Tournament(90, self.Andr, self.Nik)
        results = andr_nik.start()

        zabeg = ""
        for key, value in results.items():
            zabeg += str(key) + ": " + str(value) + " "
        all_results["1"] = zabeg

        self.assertTrue(results[2] == "Ник", "Неверное имя последнего бегуна в забеге 1")


    def test_run_un(self):
       us_nik = hw.Tournament(90, self.Us, self.Nik)
       results = us_nik.start()

       zabeg = ""
       for key, value in results.items():
           zabeg += str(key) + ": " + str(value) + " "
       all_results["2"] = zabeg

       self.assertTrue(results[2] == "Ник", "Неверное имя последнего бегуна в забеге 2")


    def test_run_uan(self):
        us_andr_nik = hw.Tournament(90, self.Us, self.Andr, self.Nik)
        results = us_andr_nik.start()

        zabeg = ""
        for key, value in results.items():
            zabeg += str(key) + ": " + str(value) + " "
        all_results["3"] = zabeg

        self.assertTrue(results[3] == "Ник", "Неверное имя последнего бегуна в забеге 3")


if __name__ == "__main__":
    unittest.main()