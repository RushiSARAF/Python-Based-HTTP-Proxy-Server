import fileinput
class ResponseManager:
    def __init__(self):
        self.filename = ""

    def getBlockedUserPage(self):
        f =open("blockedip.html","r")
        str = f.read()
        return str;

    def getBlockedKeywordPage(self):
        f =open("blockedkeyword.html","r")
        str = f.read()
        return str;

    def getBlockedWebsitePage(self):
        f =open("blockedwebsite.html","r")
        str = f.read()
        return str;
