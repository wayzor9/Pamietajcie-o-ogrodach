from trefle_api.schemas import FinalSchema


def test_load(fake_plant_data):

    loaded = FinalSchema().load(fake_plant_data)
    assert loaded["data"]["main_species"]["growth"]["bloom_months"] == "june"
