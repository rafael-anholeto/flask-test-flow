
class Book:
    def __init__(self, id,  title, timestamp):
        self.id = id
        self.title = title
        self.timestamp = timestamp
        
        
    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'timestamp': self.timestamp
        }