from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Components.Label import Label
from Components.Sources.StaticText import StaticText
from Components.ActionMap import NumberActionMap

class CurlyTx(Screen):
    skin = """
        <screen position="100,100" size="550,400" title="Test" >
	    <widget name="text" position="0,0" size="550,25" font="Regular;20" />
        </screen>"""

    def __init__(self, session, args = None):
        self.skin = CurlyTx.skin
        Screen.__init__(self, session)

        self["text"] = StaticText("foo")
        #sample = file(test).read()
        #import urllib
        ##req = urllib2.Request(url)
        # r = urllib2.urlopen(req)
        # f.write(r.read())
        # webFile.close()
        #self.session.openWithCallback(self.mycallback, MessageBox, _("Test-Messagebox?"))

        self["actions"] = NumberActionMap(["WizardActions", "InputActions"], {
                "ok": self.close,
                "back": self.close
                }, -1)


    def mycallback(self, answer):
        print "answer:", answer
        if answer:
            raise Exception("test-crash")
        self.close()
