from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Components.Label import Label
from Components.ScrollLabel import ScrollLabel
from Components.ActionMap import NumberActionMap
import urllib

class CurlyTx(Screen):
    skin = """
        <screen position="100,100" size="550,400" title="Test" >
	    <widget name="text" position="0,0" size="550,400" font="Regular;20" />
        </screen>"""

    def __init__(self, session, args = None):
        self.skin = CurlyTx.skin
        Screen.__init__(self, session)

        self["text"] = ScrollLabel("foo")
        #self.session.openWithCallback(self.mycallback, MessageBox, _("Test-Messagebox?"))

        self["actions"] = NumberActionMap(["WizardActions", "InputActions"], {
                "ok": self.close,
                "back": self.close,
                "up": self.pageUp,
                "down":	self.pageDown
            }, -1)
        self.loadUrl()

    def pageUp(self):
        self["text"].pageUp()

    def pageDown(self):
        self["text"].pageDown()


    def mycallback(self, answer):
        print "answer:", answer
        if answer:
            raise Exception("test-crash")
        self.close()

    def loadUrl(self):
        #sample = file(test).read()
        #import urllib
        ##req = urllib2.Request(url)
        r = urllib.urlopen("http://www.bogo/tagebuch/tagebuch.css")
        self["text"].setText(r.read())
        r.close()
        # f.write(r.read())
        # webFile.close()
