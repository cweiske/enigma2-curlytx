from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Components.Label import Label
from Components.ScrollLabel import ScrollLabel
from Components.ActionMap import NumberActionMap
from twisted.web import client

class CurlyTx(Screen):
    skin = """
        <screen position="100,100" size="550,400" title="CurlyTx" >
	    <widget name="text" position="0,0" size="550,400" font="Console;20" />
        </screen>"""

    def __init__(self, session, args = None):
        self.skin = CurlyTx.skin
        Screen.__init__(self, session)

        self["text"] = ScrollLabel("foo")

        self["actions"] = NumberActionMap(["WizardActions", "InputActions"], {
                "ok": self.close,
                "back": self.close,
                "up": self.pageUp,
                "down":	self.pageDown
            }, -1)

        self.loadUrl("http://monitoring.home.cweiske.de/wetter/plain.txt")

    def pageUp(self):
        self["text"].pageUp()

    def pageDown(self):
        self["text"].pageDown()


    def mycallback(self, answer):
        print "answer:", answer
        if answer:
            raise Exception("test-crash")
        self.close()

    def loadUrl(self, url):
        self["text"].setText("Loading ...\n" + url);

        client.getPage(url).addCallback(self.urlLoaded).addErrback(self.urlFailed, url)

    def urlLoaded(self, html):
        self["text"].setText(html)

    def urlFailed(self, error, url):
        self["text"].setText(
            "Error fetching URL:\n " + error.getErrorMessage()
            + "\n\nURL: " + url
            )
