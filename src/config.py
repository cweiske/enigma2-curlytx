from Components.config import config, ConfigYesNo, ConfigSelection, ConfigNumber, ConfigText, ConfigSubsection, ConfigSubList

#configuration setup
config.plugins.CurlyTx = ConfigSubsection()
config.plugins.CurlyTx.menuMain = ConfigYesNo(default = True)
config.plugins.CurlyTx.menuTitle = ConfigText(default = "CurlyTx")
config.plugins.CurlyTx.pages = ConfigSubList()
#i = 0
#while i < len(config.plugins.CurlyTx.pages):
#    config.plugins.CurlyTx.pages.append(createPage)
#    i += 1
#    del s
#del i
#config.plugins.CurlyTx.defaultPage = ConfigNumber(default=0)


def createPage():
    s = ConfigSubsection()
    s.uri   = ConfigText(default="http://", fixed_size=False)
    s.title = ConfigText(
        default = "Page #" + str(len(config.plugins.CurlyTx.pages) + 1),
        fixed_size = False
        )
    return s
