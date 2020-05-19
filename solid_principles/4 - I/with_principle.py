import abc

# абстрактные классы / интерфейсы
class CloudHostingProvider(abc.ABC):
    @abc.abstractmethod
    def createServer(region):
        pass

    @abc.abstractmethod
    def listServer(region):
        pass

class CDNProvider(abc.ABC):
    @abc.abstractmethod
    def getCDNAddress():
        pass


class CloudStorageProvider(abc.ABC):
    @abc.abstractmethod
    def storeFile(name):
        pass

    @abc.abstractmethod
    def getFile(name):
        pass


# настоящие классы
class Amazon(CloudHostingProvider, CloudStorageProvider, CDNProvider):
    def __init__(self, name, region):
        self.name = name
        self.region = region

    def createServer(self, region):
        return 'server was created'

    def listServer(self, region):
        return ['a', 'b', 'c']

    def getCDNAddress(self):
        return 'someaddress'

    def storeFile(self, name):
        return self.name
    
    def getFile(self, name):
        return self.name
    
class Dropbox(CloudStorageProvider):
    def __init__(self, name):
        self.name = name

    def getFile(self, name):
        return self.name

    def storeFile(self, name):
        return self.name
        

if __name__ == "__main__":
    amazon = Amazon('amazon', 'UK')
    dropbox = Dropbox('dropbox')