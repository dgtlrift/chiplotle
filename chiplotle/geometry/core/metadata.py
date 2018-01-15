from autologging import logged, traced

@traced
@logged
class MetaData(object):

    def __init__(self):
        self.name = None
        self.tags = set( )

