import unittest
import pandas as pd
from trax import read_data as rd
from trax import subset as ss
from trax import stats as st
from trax import api


class TestDataRead(unittest.TestCase):

    def test_count(self):
        df = pd.read_csv('../data/tracks.csv', sep=';')
        self.assertEqual(rd.count_tracks(df), 35574)

    def test_audio_f(self):
        self.assertEqual(rd.audio_f_list('../data/tracks.csv', 'Radiohead'), [0.405937106918239, 0.5767025157232705,
                                                                              5.2075471698113205, -9.834383647798742,
                                                                              0.5786163522012578,
                                                                              0.055728301886792446, 0.3136607213836478,
                                                                              0.39302680075471697,
                                                                              0.20198553459119495, 0.2859138364779874,
                                                                              119.98000628930818,
                                                                              3.861635220125786])


class TestDataSubset(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._file = '../data/tracks.csv'

    def test_artist_name(self):
        self.assertEqual(ss.artist_name(self._file, 'Radiohead'), 159)

    def test_title_word(self):
        self.assertEqual(ss.title_word(self._file, 'police|Police'), 11)

    def test_release_year(self):
        self.assertEqual(ss.release_year(self._file, 1990), 4638)

    def test_popular_last(self):
        self.assertEqual(ss.popular_last(self._file, 10), ("Beggin'", 'Måneskin'))

    def test_decade_artists(self):
        self.assertEqual(ss.decade_artists(self._file, 1950), {'Louis Armstrong', 'Frank Sinatra'})


class TestDataStats(unittest.TestCase):

    def test_basic_stats(self):
        self.assertEqual(st.basic_stats('../data/tracks.csv', 'energy', 'Metallica'),
                         (0.0533, 0.998, 0.8462655384615388))


class TestDataApi(unittest.TestCase):

    def test_api_r(self):
        self.assertEqual(print(type(api.api_r(['radiohead', 'david bowie', 'maneskin']))), print('pandas.core.frame'
                                                                                                 '.DataFrame'))


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestDataRead))
suite.addTest(unittest.makeSuite(TestDataSubset))
suite.addTest(unittest.makeSuite(TestDataStats))
suite.addTest(unittest.makeSuite(TestDataApi))
unittest.TextTestRunner(verbosity=2).run(suite)
