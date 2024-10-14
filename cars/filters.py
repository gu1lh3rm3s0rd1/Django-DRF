from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Brand, Car




class BrandFilterClass(AutoRQLFilterClass):
    MODEL = Brand

class CarFilterClass(AutoRQLFilterClass):
    MODEL = Car
    FILTERS = [
        {
            'filter': 'owner',
            'source': 'brand__name',
        }, 
        {
            'filter': 'brand',
            'source': 'brand__name',
        }
    ]