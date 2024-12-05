import json


class Species:
    """
    A class to hold measurements of different gas
    species and the associated air quality.
    """

    def __init__(self, code="", air_quality_index=0):
        self.code = str(code)
        self.air_quality_index = int(air_quality_index)

    def __repr__(self):
        s = "Species("
        s += f"code=\"{self.code}\","
        s += f"air_quality_index={self.air_quality_index})"
        return s

    """
    A function to fill the data members from
    input JSON.
    """
    def load_from_json(self, json_data):
        self.code = json_data["code"]
        self.air_quality_index = json_data["airQualityIndex"]


class Site:
    """
    A class to hold site information and associated measurements.
    """

    def __init__(self,
                 name="",
                 latitude=0.,
                 longitude=0.,
                 species=[]):
        self.name = str(name)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.species = species.copy()

    def __repr__(self):
        s = "Site("
        s += f"name=\"{self.name}\","
        s += f"latitude={self.latitude},"
        s += f"longitude={self.longitude},"
        s += f"species={self.species})"
        return s

    def load_from_json(self, json_data):
        """
        A function to fill the data members from
        input JSON.
        """
        self.name = json_data["name"]
        self.latitude = json_data["latitude"]
        self.longitude = json_data["longitude"]
        del self.species[:]
        for json_species in json_data["species"]:
            species = Species()
            species.load_from_json(json_species)
            self.species.append(species)

    def average_air_quality_index(self):
        """
        A function to return the average air quality index
        for a site.
        """
        n = len(self.species)
        average = 0.
        for i in range(n):
            average += float(self.species[i].air_quality_index)/n
        return average


class LocalAuthority:
    """
    A class to hold measurements that are associated
    with a local authority.
    """
    def __init__(self, name="", sites=[]):
        self.name = str(name)
        self.sites = sites.copy()

    def __repr__(self):
        s = "LocalAuthority("
        s += f"name=\"{self.name}\","
        s += f"sites={self.sites})"
        return s

    def load_from_json(self, json_data):
        """
        A function to fill the data members from
        input JSON.
        """
        self.name = json_data["name"]
        del self.sites[:]
        for json_site in json_data["sites"]:
            site = Site()
            site.load_from_json(json_site)
            self.sites.append(site)


def read_json(file_name):
    """
    A function to read a JSON file into memory.
    """
    input_file = open(file_name, "r", encoding="utf-8")
    json_data = json.load(input_file)
    input_file.close()
    return json_data


"""
A test program to load the JSON file and calculate the
average air quality index per site.
"""
if __name__ == "__main__":
    # Load the data values into memory.
    json_data = read_json("air_quality.json")

    # Create data objects and populate them with data
    # from the JSON file.
    local_authorities = []
    for json_record in json_data:
        local_authority = LocalAuthority()
        local_authority.load_from_json(json_record)
        local_authorities.append(local_authority)

    # Print the average air quality index for each site.
    for local_authority in local_authorities:
        for site in local_authority.sites:
            s = f"Site name: {site.name}"
            s += ", average air_quality_index:"
            s += f"{site.average_air_quality_index()}"
            print(s)
