from generic_scaffold import CrudManager
from art import models

class ArtCrudManager(CrudManager):
    model = models.Art
    prefix = 'art/'
