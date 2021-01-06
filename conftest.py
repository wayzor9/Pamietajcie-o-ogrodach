import pytest
from PIL import Image
from plantID.utils import PlantIdClient


@pytest.fixture
def image_file(tmp_path):
    image_path = str(tmp_path / "temp.jpg")
    im = Image.new("RGB", (496, 496), 0xFF3333)
    im.save(image_path, format="JPEG", optimize=True)
    return image_path

@pytest.fixture
def plant_client():
    return PlantIdClient()

@pytest.fixture(autouse=True)
def no_requestes(monkeypatch):
    monkeypatch.delattr('requests.sessions.Session.request')

@pytest.fixture
def backend_response():
    return { 'countable': True,
    'custom_id': None,
    'fail_cause': None,
    'feedback': None,
    'finished_datetime': 1609707942.857562,
    'id': 8491002,
    'images': [   {   'file_name': 'd7e7e5ed1774425395c59982739eb4b4.jpg',
                      'url': 'https://plant.id/media/images/d7e7e5ed1774425395c59982739eb4b4.jpg'}],
    'meta_data': {   'date': '2021-01-03',
                     'datetime': '2021-01-03',
                     'latitude': None,
                     'longitude': None},
    'modifiers': [],
    'secret': '2ksfZHt1GeJozkG',
    'suggestions': [   {   'confirmed': False,
                           'id': 62955282,
                           'plant_details': {   'common_names': [   'Camellia',
                                                                    'Japanese '
                                                                    'camellia',
                                                                    'Common '
                                                                    'camellia',
                                                                    'Tsubaki',
                                                                    'Rose of '
                                                                    'winter',
                                                                    'Japonica'],
                                                'name_authority': 'Camellia '
                                                                  'japonica L.',
                                                'scientific_name': 'Camellia '
                                                                   'japonica',
                                                'structured_name': {   'genus': 'camellia',
                                                                       'species': 'japonica'},
                                                'taxonomy': {   'class': 'Magnoliopsida',
                                                                'family': 'Theaceae',
                                                                'genus': 'Camellia',
                                                                'kingdom': 'Plantae',
                                                                'order': 'Ericales',
                                                                'phylum': 'Tracheophyta'},
                                                'url': 'http://en.wikipedia.org/wiki/Camellia_japonica'},
                           'plant_name': 'Camellia japonica',
                           'probability': 0.21745800378612892},
                       {   'confirmed': False,
                           'id': 62955283,
                           'plant_details': {   'common_names': [   'Rose',
                                                                    'De rosa'],
                                                'name_authority': None,
                                                'scientific_name': 'Rosa',
                                                'structured_name': {   'genus': 'rosa'},
                                                'taxonomy': {   'class': 'Magnoliopsida',
                                                                'family': 'Rosaceae',
                                                                'genus': 'Rosa',
                                                                'kingdom': 'Plantae',
                                                                'order': 'Rosales',
                                                                'phylum': 'Tracheophyta'},
                                                'url': 'http://en.wikipedia.org/wiki/Rosa'},
                           'plant_name': 'Rosa',
                           'probability': 0.15403643894196734},
                       {   'confirmed': False,
                           'id': 62955284,
                           'plant_details': {   'common_names': [   'Paeony',
                                                                    'Paionia'],
                                                'name_authority': None,
                                                'scientific_name': 'Paeonia',
                                                'structured_name': {   'genus': 'paeonia'},
                                                'taxonomy': {   'class': 'Magnoliopsida',
                                                                'family': 'Paeoniaceae',
                                                                'genus': 'Paeonia',
                                                                'kingdom': 'Plantae',
                                                                'order': 'Saxifragales',
                                                                'phylum': 'Tracheophyta'},
                                                'url': 'http://en.wikipedia.org/wiki/Paeonia'},
                           'plant_name': 'Paeonia',
                           'probability': 0.10401217950351851},
                       {   'confirmed': False,
                           'id': 62955285,
                           'plant_details': {   'common_names': [   'China '
                                                                    'rose',
                                                                    'Chinese '
                                                                    'rose'],
                                                'name_authority': 'Rosa '
                                                                  'chinensis '
                                                                  'Jacq.',
                                                'scientific_name': 'Rosa '
                                                                   'chinensis',
                                                'structured_name': {   'genus': 'rosa',
                                                                       'species': 'chinensis'},
                                                'taxonomy': {   'class': 'Magnoliopsida',
                                                                'family': 'Rosaceae',
                                                                'genus': 'Rosa',
                                                                'kingdom': 'Plantae',
                                                                'order': 'Rosales',
                                                                'phylum': 'Tracheophyta'},
                                                'url': 'http://en.wikipedia.org/wiki/Rosa_chinensis'},
                           'plant_name': 'Rosa chinensis',
                           'probability': 0.06035186881000735},
                       {   'confirmed': False,
                           'id': 62955286,
                           'plant_details': {   'common_names': [   'Wild '
                                                                    'peony',
                                                                    'Common '
                                                                    'peony',
                                                                    'Garden '
                                                                    'peony'],
                                                'name_authority': 'Paeonia '
                                                                  'officinalis '
                                                                  'L.',
                                                'scientific_name': 'Paeonia '
                                                                   'officinalis',
                                                'structured_name': {   'genus': 'paeonia',
                                                                       'species': 'officinalis'},
                                                'taxonomy': {   'class': 'Magnoliopsida',
                                                                'family': 'Paeoniaceae',
                                                                'genus': 'Paeonia',
                                                                'kingdom': 'Plantae',
                                                                'order': 'Saxifragales',
                                                                'phylum': 'Tracheophyta'},
                                                'url': 'http://en.wikipedia.org/wiki/Paeonia_officinalis'},
                           'plant_name': 'Paeonia officinalis',
                           'probability': 0.05461902940073029},
                       {   'confirmed': False,
                           'id': 62955287,
                           'plant_details': {   'common_names': [   'Shrub '
                                                                    'althea',
                                                                    'Rose of '
                                                                    'sharon',
                                                                    'Korean '
                                                                    'rose',
                                                                    'Syrian '
                                                                    'ketmia',
                                                                    'Rose '
                                                                    'mallow'],
                                                'name_authority': 'Hibiscus '
                                                                  'syriacus L.',
                                                'scientific_name': 'Hibiscus '
                                                                   'syriacus',
                                                'structured_name': {   'genus': 'hibiscus',
                                                                       'species': 'syriacus'},
                                                'taxonomy': {   'class': 'Magnoliopsida',
                                                                'family': 'Malvaceae',
                                                                'genus': 'Hibiscus',
                                                                'kingdom': 'Plantae',
                                                                'order': 'Malvales',
                                                                'phylum': 'Tracheophyta'},
                                                'url': 'http://en.wikipedia.org/wiki/Hibiscus_syriacus'},
                           'plant_name': 'Hibiscus syriacus',
                           'probability': 0.02330138696669},
                       {   'confirmed': False,
                           'id': 62955288,
                           'plant_details': {   'common_names': [   'China '
                                                                    'rose',
                                                                    'Chinese '
                                                                    'hibiscus',
                                                                    'Hawaiian '
                                                                    'hibiscus',
                                                                    'Shoeblackplant',
                                                                    'Rose '
                                                                    'mallow'],
                                                'name_authority': 'Hibiscus '
                                                                  'rosa-sinensis '
                                                                  'L.',
                                                'scientific_name': 'Hibiscus '
                                                                   'rosa-sinensis',
                                                'structured_name': {   'genus': 'hibiscus',
                                                                       'species': 'rosa-sinensis'},
                                                'taxonomy': {   'class': 'Magnoliopsida',
                                                                'family': 'Malvaceae',
                                                                'genus': 'Hibiscus',
                                                                'kingdom': 'Plantae',
                                                                'order': 'Malvales',
                                                                'phylum': 'Tracheophyta'},
                                                'url': 'http://en.wikipedia.org/wiki/Hibiscus_rosa-sinensis'},
                           'plant_name': 'Hibiscus rosa-sinensis',
                           'probability': 0.023200246135538286},
                       {   'confirmed': False,
                           'id': 62955289,
                           'plant_details': {   'common_names': [   'Peony',
                                                                    'Chinese '
                                                                    'peony',
                                                                    'Common '
                                                                    'garden '
                                                                    'peony'],
                                                'name_authority': 'Paeonia '
                                                                  'lactiflora '
                                                                  'Pall.',
                                                'scientific_name': 'Paeonia '
                                                                   'lactiflora',
                                                'structured_name': {   'genus': 'paeonia',
                                                                       'species': 'lactiflora'},
                                                'taxonomy': {   'class': 'Magnoliopsida',
                                                                'family': 'Paeoniaceae',
                                                                'genus': 'Paeonia',
                                                                'kingdom': 'Plantae',
                                                                'order': 'Saxifragales',
                                                                'phylum': 'Tracheophyta'},
                                                'url': 'http://en.wikipedia.org/wiki/Paeonia_lactiflora'},
                           'plant_name': 'Paeonia lactiflora',
                           'probability': 0.022470811666973775},
                       {   'confirmed': False,
                           'id': 62955290,
                           'plant_details': {   'common_names': [   'Hollyhock',
                                                                    'Common '
                                                                    'hollyhock'],
                                                'name_authority': 'Alcea rosea '
                                                                  'L.',
                                                'scientific_name': 'Alcea '
                                                                   'rosea',
                                                'structured_name': {   'genus': 'alcea',
                                                                       'species': 'rosea'},
                                                'taxonomy': {   'class': 'Magnoliopsida',
                                                                'family': 'Malvaceae',
                                                                'genus': 'Alcea',
                                                                'kingdom': 'Plantae',
                                                                'order': 'Malvales',
                                                                'phylum': 'Tracheophyta'},
                                                'url': 'http://en.wikipedia.org/wiki/Alcea_rosea'},
                           'plant_name': 'Alcea rosea',
                           'probability': 0.010949768602862753}],
    'uploaded_datetime': 1609707941.380085}