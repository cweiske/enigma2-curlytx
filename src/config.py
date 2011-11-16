from Components.config import config, ConfigYesNo, ConfigSelection, ConfigNumber, ConfigText, ConfigSubsection, ConfigSubList

def createPage():
    s = ConfigSubsection()
    s.uri   = ConfigText(default="http://", fixed_size=False)
    s.title = ConfigText(
        default = "Page #" + str(len(config.plugins.CurlyTx.pages) + 1),
        fixed_size = False
        )
    return s

#configuration setup
config.plugins.CurlyTx = ConfigSubsection()
config.plugins.CurlyTx.menuMain = ConfigYesNo(default = True)
config.plugins.CurlyTx.menuTitle = ConfigText(default = "CurlyTx")
config.plugins.CurlyTx.pageCount = ConfigNumber(default = 0)
config.plugins.CurlyTx.pages = ConfigSubList()

for id,value in config.plugins.CurlyTx.pages.stored_values.iteritems():
    config.plugins.CurlyTx.pages.append(createPage())

#config.plugins.CurlyTx.defaultPage = ConfigNumber(default=0)
