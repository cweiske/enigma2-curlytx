from Components.config import config, ConfigYesNo, ConfigSelection, ConfigNumber, ConfigText, ConfigSubsection, ConfigSubList

#configuration setup
config.plugins.CurlyTx = ConfigSubsection()
config.plugins.CurlyTx.menuMain = ConfigYesNo(default = True)
config.plugins.CurlyTx.menuTitle = ConfigText(default = "CurlyTx")
config.plugins.CurlyTx.pageCount = ConfigNumber(default=0)
config.plugins.CurlyTx.pages = ConfigSubList()
i = 0
while i < config.plugins.CurlyTx.pageCount.value:
    s = ConfigSubsection()
    s.uri = ConfigText(default="http://", fixed_size=False)
    config.plugins.CurlyTx.pages.append(s)
    i += 1
    del s
del i
#config.plugins.CurlyTx.defaultPage = ConfigNumber(default=0)
