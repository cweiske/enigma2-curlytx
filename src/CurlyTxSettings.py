from Screens.Screen import Screen
from Components.ActionMap import ActionMap, NumberActionMap
from Components.Sources.StaticText import StaticText

from . import config
from Components.config import config, getConfigListEntry
from Components.ConfigList import ConfigList, ConfigListScreen

class CurlyTxSettings(Screen, ConfigListScreen):

    def __init__(self, session):
        Screen.__init__(self, session)
        self.skinName = [ "CurlyTxSettings", "Setup" ]
        self.setup_title = _("Settings")

        self["actions"] = ActionMap(["SetupActions"],
            {
                "cancel": self.keyCancel,
                "save": self.keySave,
                "ok": self.keySave
                #fixme: open page editor
            }, -2)

        self["key_red"] = StaticText(_("Cancel"))
        self["key_green"] = StaticText(_("OK"))

        self.onChangedEntry = [ ]
        ConfigListScreen.__init__(self, self.getConfigList(), session = self.session, on_change = self.changedEntry)

    def getConfigList(self):
        list = []
        list.append(getConfigListEntry(_("Show in main menu"), config.plugins.CurlyTx.menuMain))
        list.append(getConfigListEntry(_("Menu title"), config.plugins.CurlyTx.menuTitle))
        # fixme: automatically set that
        list.append(getConfigListEntry(_("Number of pages"), config.plugins.CurlyTx.pageCount))
        # fixme: other way?
        #list.append(getConfigListEntry(_("Pages"), config.plugins.CurlyTx.pages))
        return list

    def changedEntry(self):
        # fixme: needed?
        for x in self.onChangedEntry:
            x()

    def keyLeft(self):
        ConfigListScreen.keyLeft(self)

    def keyRight(self):
        ConfigListScreen.keyRight(self)


