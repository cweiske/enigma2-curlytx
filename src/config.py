from Components.config import config, ConfigYesNo, ConfigSelection, ConfigNumber, ConfigText, ConfigSubsection, ConfigSubList

def createPage():
    s = ConfigSubsection()
    s.uri   = ConfigText(default="http://", fixed_size=False)
    s.title = ConfigText(
        default = "Page #" + str(len(config.plugins.CurlyTx.pages) + 1),
        fixed_size = False
        )
    return s

def loadDefaultPageOptions():
    defaults = []
    for i in range(0, len(config.plugins.CurlyTx.pages)):
        defaults.append((str(i), config.plugins.CurlyTx.pages[i].title.value))
    print "CurlyTx", defaults
    if hasattr(config.plugins.CurlyTx, "defaultPage"):
        config.plugins.CurlyTx.defaultPage.setChoices(defaults, "0")
    else:
        config.plugins.CurlyTx.defaultPage = ConfigSelection(defaults, "0")

#configuration setup
config.plugins.CurlyTx = ConfigSubsection()
config.plugins.CurlyTx.menuMain = ConfigYesNo(default = True)
config.plugins.CurlyTx.menuTitle = ConfigText(default = "CurlyTx")
config.plugins.CurlyTx.pages = ConfigSubList()
for id,value in config.plugins.CurlyTx.pages.stored_values.iteritems():
    config.plugins.CurlyTx.pages.append(createPage())
loadDefaultPageOptions()
