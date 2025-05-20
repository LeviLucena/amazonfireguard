import unittest
from app.services.firms import fetch_firms_csv

class FirmsServiceTest(unittest.TestCase):
    def test_fetch_firms_data(self):
        url = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_Global_7d.csv"
        df = fetch_firms_csv(url)
        self.assertFalse(df.empty)

if __name__ == "__main__":
    unittest.main()
