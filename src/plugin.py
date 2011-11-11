from Plugins.Plugin import PluginDescriptor
import CurlyTx
 
def main(session, **kwargs):
    reload(CurlyTx)
    try:
        session.open(CurlyTx.CurlyTx)
    except:
        import traceback
        traceback.print_exc()

def menuHook(menuid):
    if menuid == "mainmenu": 
        return [(_("CurlyTx"), main, "curlytx", 1)]
    return [ ]

 
def Plugins(**kwargs):
    return [
        PluginDescriptor(name = "CurlyTx",
                         description = "View remote text files",
                         where = [PluginDescriptor.WHERE_PLUGINMENU],
                         fnc = main),
        PluginDescriptor(name = "CurlyTx",
                         description = "View remote text files",
                         where=PluginDescriptor.WHERE_MENU,
                         fnc = menuHook),
        ]        
