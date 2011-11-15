from Screens.Screen import Screen
from Components.ActionMap import ActionMap, NumberActionMap
from Components.Sources.StaticText import StaticText

from . import config
from config import createPage
from Components.config import config, getConfigListEntry
from Components.ConfigList import ConfigList, ConfigListScreen

class CurlyTxSettings(ConfigListScreen, Screen):
    skin = """
	<screen name="Setup" position="center,center" size="560,430" title="Setup">
	  <ePixmap pixmap="skin_default/buttons/red.png"    position="0,0"   size="140,40" transparent="1" alphatest="on" />
	  <ePixmap pixmap="skin_default/buttons/green.png"  position="140,0" size="140,40" transparent="1" alphatest="on" />
	  <ePixmap pixmap="skin_default/buttons/yellow.png" position="280,0" size="140,40" transparent="1" alphatest="on" />
	  <ePixmap pixmap="skin_default/buttons/blue.png"   position="420,0" size="140,40" transparent="1" alphatest="on" />
	  <widget source="key_red"    render="Label" position="0,0"   zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1" />
	  <widget source="key_green"  render="Label" position="140,0" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#1f771f" transparent="1" />
	  <widget source="key_yellow" render="Label" position="280,0" zPosition="1" size="140,40" font="Regular;20" valign="center" halign="center" backgroundColor="#a08500" transparent="1" />
	  <widget source="key_blue"   render="Label" position="420,0" zPosition="1" size="140,40" font="Regular;20" valign="center" halign="center" backgroundColor="#18188b" transparent="1" />
	  <widget name="config" position="5,50" size="550,325" scrollbarMode="showOnDemand" />
	</screen>"""

    def __init__(self, session):
        self.skin = CurlyTxSettings.skin
        Screen.__init__(self, session)
        #self.skinName = [ "CurlyTxSettings", "Setup" ]
        self.setup_title = _("Settings")

        self["actions"] = ActionMap(["SetupActions","ColorActions"],
            {
                "cancel": self.keyCancel,
                "save": self.keySave,
                #"ok": self.ok,
                "blue": self.deletePage,
                "yellow": self.newPage
            }, -2)

        self["key_red"]    = StaticText(_("Cancel"))
        self["key_green"]  = StaticText(_("OK"))
        self["key_yellow"] = StaticText(_("New"))
        self["key_blue"]   = StaticText(_("Delete"))

        ConfigListScreen.__init__(self, self.getConfigList(), session = self.session)

    def getConfigList(self):
        list = [
            getConfigListEntry(_("Page"), x.uri)
                for x in config.plugins.CurlyTx.pages
            ]
        list.append(getConfigListEntry(_("Show in main menu"), config.plugins.CurlyTx.menuMain))
        list.append(getConfigListEntry(_("Menu title"), config.plugins.CurlyTx.menuTitle))
        return list

    def keyLeft(self):
        ConfigListScreen.keyLeft(self)

    def keyRight(self):
        ConfigListScreen.keyRight(self)

    def deletePage(self):
        from Screens.MessageBox import MessageBox
        self.session.openWithCallback(
            self.deletePageConfirm,
            MessageBox,
            _("Really delete this page?\nIt cannot be recovered!")
        )

    def deletePageConfirm(self, result):
        if not result:
            return

        id = self["config"].getCurrentIndex()
        del config.plugins.CurlyTx.pages[id]

        self["config"].setList(self.getConfigList())

    def newPage(self):
        from CurlyTxSettings import CurlyTxSettings
        self.session.openWithCallback(self.newPageCreated, CurlyTxPageEdit, createPage(), True)

    def newPageCreated(self, page, new):
        if new:
            config.plugins.CurlyTx.pages.append(page)

        self["config"].setList(self.getConfigList())
        pass



class CurlyTxPageEdit(Screen, ConfigListScreen):
    def __init__(self, session, page, new = False):
        Screen.__init__(self, session)
        self.skinName = [ "CurlyTxPageEdit", "Setup" ]

        self["key_red"]   = StaticText(_("Cancel"))
        self["key_green"] = StaticText(_("OK"))

        self["setupActions"] = ActionMap(["SetupActions"],
            {
                "save": self.save,
                "cancel": self.keyCancel
	    }, -1)

        self.page = page
        self.new = new
        list = [
            getConfigListEntry(_("Page URL"), page.uri),
            getConfigListEntry(_("Title"), page.title),
            ]
        ConfigListScreen.__init__(self, list, session = self.session)

    def save(self):
        self.close(self.page, self.new)
        #FIXME: pass page to parent

    def keyCancel(self):
        self.close()
