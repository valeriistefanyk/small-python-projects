class Document:
    def __init__(self, data, filename):
       self.data = data
       self.filename = filename

    def load(self):
        print(f'load document {self.filename}')

    def save(self):
        print(f'save document {self.filename}')

class ReadOnlyDocument(Document):
    def save():
        raise Exception("Can't save read-only document!")

class Project:
    def __init__(self, documents):
        self.documents = documents

    def loadAll(self):
        for doc in self.documents:
            doc.load()
    
    def saveAll(self):
        for doc in self.documents:
            # if read-only - raise exception, so:
            if not isinstance(doc, ReadOnlyDocument):
                doc.save()
            else:
                print('this is readonly document!')


if __name__ == "__main__":
    doc1 = Document('some data', 'somefile1.doc')
    doc2 = Document('some data 2', 'somefile2.doc')
    doc3 = ReadOnlyDocument('some data 3', 'somefile3.doc')

    project = Project([doc1, doc2, doc3])
    project.loadAll()
    project.saveAll()