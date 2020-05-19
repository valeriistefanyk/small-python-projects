import abc

class CloudProvider(abc.ABC):
    @abc.abstractmethod
    def storeFile(name) -> str:
        pass

    @abc.abstractmethod
    def getFile(name):
        pass

    @abc.abstractmethod
    def createServer(region):
        pass

    @abc.abstractmethod
    def listServers(region) -> list:
        pass

    @abc.abstractmethod
    def getCDNAddress():
        pass


class Amazon(CloudProvider):
    def __init__(self, name, region):
        self.name = name
        self.region = region

    def storeFile(self, name):
        return name

    def getFile(self):
        return f'your file - {name}'

    def createServer(self):
        return "server created"

    def listServers(self):
        return ['a', 'b', 'c']

    def getCDNAddress(self):
        return 'something..'

    


class Dropbox(CloudProvider):
    def __init__(self, name, region):
        self.name = name
        self.region = region

    def storeFile(self, name):
        return name

    def getFile(self, name):
        return f'your file - {name}'

    # нет реализации но все равно приходится реализовывать
    def createServer(self):
        pass

    def listServers(self):
        pass

    def getCDNAddress(self):
        pass

    

if __name__ == "__main__":
    amazon = Amazon('name', 'UK')
    dropbox = Dropbox('name', 'UK')