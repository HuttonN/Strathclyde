from air_quality import Species, Site
import unittest


class TestSpecies(unittest.TestCase):
    def test_repr(self):
        species = Species("ABC", 3)
        new_species = eval(str(species))
        self.assertEqual(new_species.code, species.code)
        self.assertEqual(new_species.air_quality_index,
                         species.air_quality_index)

    def test_load_from_json(self):
        json_data = {
            "code": "ABC",
            "airQualityIndex": 3
        }
        species = Species()
        species.load_from_json(json_data)
        self.assertEqual(species.code, json_data["code"])
        self.assertEqual(species.air_quality_index,
                         json_data["airQualityIndex"])


class TestSite(unittest.TestCase):
    def test_repr(self):
        species = Species("ABC", 3)
        site = Site("Glasgow", 55.8617, -4.2583, [species])
        new_site = eval(str(site))
        self.assertEqual(new_site.latitude, site.latitude)
        self.assertEqual(new_site.longitude, site.longitude)
        self.assertEqual(len(new_site.species), len(site.species))
        self.assertEqual(new_site.species[0].code, new_site.species[0].code)
        self.assertEqual(new_site.species[0].air_quality_index,
                         site.species[0].air_quality_index)

    def test_load_from_json(self):
        json_data = {
                "name": "Glasgow",
                "latitude": 55.8617,
                "longitude": -4.2583,
                "species": [
                    {
                        "code": "ABC",
                        "airQualityIndex": 3
                    }
                ]
        }
        site = Site()
        site.load_from_json(json_data)
        self.assertEqual(site.latitude, json_data["latitude"])
        self.assertEqual(site.longitude, json_data["longitude"])
        self.assertEqual(len(site.species), len(json_data["species"]))
        self.assertEqual(site.species[0].code, json_data["species"][0]["code"])
        self.assertEqual(site.species[0].air_quality_index,
                         json_data["species"][0]["airQualityIndex"])

    def test_average_air_quality_index(self):
        json_data = {
                "name": "Glasgow",
                "latitude": 55.8617,
                "longitude": -4.2583,
                "species": [
                    {
                        "code": "ABC",
                        "airQualityIndex": 3
                    },
                    {
                        "code": "DEF",
                        "airQualityIndex": 1
                    }
                ]
        }
        site = Site()
        site.load_from_json(json_data)
        self.assertEqual(site.average_air_quality_index(), 2)


if __name__ == "__main__":
    unittest.main()
