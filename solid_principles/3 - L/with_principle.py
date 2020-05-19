class Document:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename

    def load(self):
        print(f'load {self.filename} document ...')


class WritableDocument(Document):

    def save(self):
        print(f"save {self.filename} document ...")


class Project:
    def __init__(self, allDocs, writableDocs):
        self.allDocs = allDocs
        self.writableDocs = writableDocs

    def loadAll(self):
        for doc in self.allDocs:
            doc.load()

    def saveAll(self):
        for doc in self.writableDocs:
            doc.save()


if __name__ == "__main__":
    doc1 = Document('some data 1', 'file1.doc')
    doc2 = WritableDocument('some data 2', 'file2.doc')
    doc3 = WritableDocument('some data 3', 'file3.doc')

    project = Project([doc1, doc2, doc3], [doc2, doc3])
    project.loadAll()
    project.saveAll()
