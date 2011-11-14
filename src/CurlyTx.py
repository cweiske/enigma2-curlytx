from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Components.Label import Label
from Components.ScrollLabel import ScrollLabel
from Components.ActionMap import NumberActionMap
from Components.Sources.StaticText import StaticText
from twisted.web import client

from . import config
from Components.config import config

class CurlyTx(Screen):
    skin = """
        <screen name="CurlyTx" position="center,center" size="560,400" title="CurlyTx" >
	  <ePixmap position="0,0" size="140,40" pixmap="skin_default/buttons/red.png" transparent="1" alphatest="on" />
	  <ePixmap position="140,0" size="140,40" pixmap="skin_default/buttons/green.png" transparent="1" alphatest="on" />
	  <ePixmap position="280,0" size="140,40" pixmap="skin_default/buttons/yellow.png" transparent="1" alphatest="on" />
	  <ePixmap position="420,0" size="140,40" pixmap="skin_default/buttons/blue.png" transparent="1" alphatest="on" />
	  <widget source="key_red" render="Label" position="0,0" zPosition="1" size="140,40" valign="center" halign="center" font="Regular;21" transparent="1" foregroundColor="white" shadowColor="black" shadowOffset="-1,-1" />
	  <widget source="key_green" render="Label" position="140,0" zPosition="1" size="140,40" valign="center" halign="center" font="Regular;21" transparent="1" foregroundColor="white" shadowColor="black" shadowOffset="-1,-1" />
	  <widget source="key_yellow" render="Label" position="280,0" zPosition="1" size="140,40" valign="center" halign="center" font="Regular;21" transparent="1" foregroundColor="white" shadowColor="black" shadowOffset="-1,-1" />
	  <widget source="key_blue" render="Label" position="420,0" zPosition="1" size="140,40" valign="center" halign="center" font="Regular;21" transparent="1" foregroundColor="white" shadowColor="black" shadowOffset="-1,-1" />
	  <widget name="text" position="5,45" size="550,350" font="Console;20" />
        </screen>"""

    currentUrl = None

    def __init__(self, session, args = None):
        #self.skin = CurlyTx.skin
        Screen.__init__(self, session)
        #self.skinName = [ "CurlyTx", "Setup" ]

        self["text"] = ScrollLabel("foo")

        self["key_red"]    = StaticText(_("Settings"))
        self["key_green"]  = StaticText(_("Reload"))
        self["key_yellow"] = StaticText(_("Prev"))
        self["key_blue"]   = StaticText(_("Next"))


        self["actions"] = NumberActionMap(["WizardActions", "ColorActions", "InputActions"], {
                "ok": self.close,
                "back": self.close,
                "up": self.pageUp,
                "down":	self.pageDown,

                "red": self.showSettings,
                "green": self.reload
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

    def reload(self):
        self.loadUrl(self.currentUrl)

    def loadUrl(self, url):
        self["text"].setText("Loading ...\n" + url);
        self.currentUrl = url

        client.getPage(url).addCallback(self.urlLoaded).addErrback(self.urlFailed, url)

    def urlLoaded(self, html):
        self["text"].setText(html)

    def urlFailed(self, error, url):
        self["text"].setText(
            "Error fetching URL:\n " + error.getErrorMessage()
            + "\n\nURL: " + url
            )

    def showSettings(self):
        #self.session.openWithCallback(self.setConf ,Pic_Setup)
        from CurlyTxSettings import CurlyTxSettings
        self.session.openWithCallback(self.onSettingsChanged, CurlyTxSettings)

    def onSettingsChanged(self):
        "fixme"
