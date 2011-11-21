from . import _

from Screens.Screen import Screen
from Screens.HelpMenu import HelpableScreen
from Screens.MessageBox import MessageBox
from Components.Label import Label
from Components.ScrollLabel import ScrollLabel
from Components.ActionMap import ActionMap
from Components.Sources.StaticText import StaticText
from twisted.web import client

from . import config
from Components.config import config

class CurlyTx(Screen,HelpableScreen):
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
    currentPage = None

    def __init__(self, session, args = None):
        #self.skin = CurlyTx.skin
        Screen.__init__(self, session)
        HelpableScreen.__init__(self)
        #self.skinName = [ "CurlyTx", "Setup" ]

        self["text"] = ScrollLabel("foo")

        self["key_red"]    = StaticText(_("Settings"))
        self["key_green"]  = StaticText(_("Reload"))
        self["key_yellow"] = StaticText(_("Prev"))
        self["key_blue"]   = StaticText(_("Next"))


        self["actions"] = ActionMap(
            ["WizardActions", "ColorActions", "InputActions"], {
                "ok":   self.close,
                "back": self.close,
                "up":   self.pageUp,
                "down": self.pageDown,

                "red":    self.showSettings,
                "green":  self.reload,
                "yellow": self.prevPage,
                "blue":   self.nextPage
            }, -1)

        self.loadHelp()
        self.loadUrl(config.plugins.CurlyTx.defaultPage.value)

    def loadHelp(self):
        self.helpList.append((
                self["actions"], "WizardActions",
                [("up", _("Scroll page contents up"))]))
        self.helpList.append((
                self["actions"], "WizardActions",
                [("down", _("Scroll page contents down"))]))
        self.helpList.append((
                self["actions"], "ColorActions",
                [("red", _("Show program settings"))]))
        self.helpList.append((
                self["actions"], "ColorActions",
                [("green", _("Reload current page URL"))]))
        self.helpList.append((
                self["actions"], "ColorActions",
                [("yellow", _("Switch to next configured page URL"))]))
        self.helpList.append((
                self["actions"], "ColorActions",
                [("blue", _("Switch to previous configured page URL"))]))
        self.helpList.append((
                self["actions"], "WizardActions",
                [("ok", _("Close window"))]))
        self.helpList.append((
                self["actions"], "WizardActions",
                [("back", _("Close window"))]))
        self.helpList.append((
                self["actions"], "HelpActions",
                [("displayHelp", _("Show this help screen"))]))

    def pageUp(self):
        self["text"].pageUp()

    def pageDown(self):
        self["text"].pageDown()

    def prevPage(self):
        if self.currentPage == None:
            return

        pageId = self.currentPage - 1
        if pageId < 0:
            pageId = len(config.plugins.CurlyTx.pages) - 1
        self.loadUrl(pageId)

    def nextPage(self):
        if self.currentPage == None:
            return

        pageId = self.currentPage + 1
        if pageId > len(config.plugins.CurlyTx.pages) - 1:
            pageId = 0
        self.loadUrl(pageId)

    def reload(self):
        if self.currentPage == None:
            return

        self.loadUrl(self.currentPage)

    def loadUrl(self, pageId):
        if pageId == None:
            self.loadNoPage()
            return

        pageId = int(pageId)
        if pageId > (len(config.plugins.CurlyTx.pages) - 1):
            if len(config.plugins.CurlyTx.pages) == 0:
                self.loadNoPage()
            else:
                self["text"].setText("Invalid page " + pageId);
            return

        url   = config.plugins.CurlyTx.pages[pageId].uri.value
        title = config.plugins.CurlyTx.pages[pageId].title.value
        self.currentPage = pageId
        self.currentUrl = url

        self.setTitle(title)
        self["text"].setText("Loading ...\n" + url);

        client.getPage(url).addCallback(self.urlLoaded).addErrback(self.urlFailed, url)

    def urlLoaded(self, html):
        self["text"].setText(html)

    def urlFailed(self, error, url):
        self["text"].setText(
            "Error fetching URL:\n " + error.getErrorMessage()
            + "\n\nURL: " + url
            )

    def loadNoPage(self):
        self["text"].setText("Go and add a page in the settings");

    def showSettings(self):
        from CurlyTxSettings import CurlyTxSettings
        self.session.openWithCallback(self.onSettingsChanged, CurlyTxSettings)

    def onSettingsChanged(self):
        if len(config.plugins.CurlyTx.pages) == 0:
            self.currentPage = None
            self.loadUrl(self.currentPage)
        elif self.currentPage == None:
            self.currentPage = 0
            self.loadUrl(self.currentPage)
