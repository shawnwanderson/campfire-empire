from generic_scaffold import CrudManager
from events import  models

class EventCrudManager(CrudManager):
    model = models.Event
    prefix = 'events/'
