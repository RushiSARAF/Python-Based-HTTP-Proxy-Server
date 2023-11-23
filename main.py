from socket import *
from ResponseManager import *
from RequestParser import *
import requests as req
class PythonProxyServer:
    def __init__(self,port):
        #self.requestStr = None
        self.ip = '0.0.0.0'
        self.port = port
        self.http_header = "HTTP/1.1 200 OK\n\n"
        self.socket = socket (AF_INET,SOCK_STREAM)
        self.socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.socket.bind((self.ip,self.port))
        self.responseManager = ResponseManager()
        self.isValid = True

    def listen(self,backlog):
        self.socket.listen(backlog)
        print("Proxy Server started on port"+str(self.port))


    def accept(self):
        self.resposeWriter,self.clientAddr = self.socket.accept()
        self.requestStr = self.resposeWriter.recv(1024).decode()
        print(self.requestStr)
        reqParser = RequestParser(self.requestStr)

        self.url = reqParser.getReqUrl()
        self.host = reqParser.getReqHost()
        self.isBlockedHost(self.host)
        self.isBlockedKeyword(self.url)
        self.forwardRequest()

    def isBlockedHost(self,hostName):
        if hostName == "yahoo.com":
            msg = self.responseManager.getBlockedWebsitePage()
            self.isValid = False
            self.resposeWriter.sendall(msg.encode("utf-8"))
            self.resposeWriter.close()
    def isBlockedKeyword(self,url):
        if(str(url).__contains__("movies")):
            msg = self.responseManager.getBlockedKeywordPage()
            self.isValid = False
            self.resposeWriter.sendall(msg.encode("utf-8"))
            self.resposeWriter.close()

    def forwardRequest(self):
        if(self.isValid == True):
            try:
                header = {
                'User-Agent':'Mozilla/5.0 (Macintosh: Intel Mac OS X 10.12;rv:55.0)Gecko/20100101 Firefox/55.0'}
                resp = req.get(url=self.url,headers=header)
                #print(resp.content)
                self.resposeWriter.sendall(resp.content)
            except Exception as e:
                print(e)

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    while True:
        proxy = PythonProxyServer(2647)
        proxy.listen(5)
        proxy.accept()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
