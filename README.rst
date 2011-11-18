=======
CurlyTx
=======
Enigma2 (Dreambox) plugin that lets you view the contents of remote
plain text files, e.g. HTTP.

Multiple URLs can be configured and navigated.



Open issues
===========
- hide default page selection when no page defined
- menu title setting has hard coded length?
- help screens
- page import via atom feed/opml
- move mode to re-order pages
- show current page when multiple ones are defined: "2/6"
- configurable text size per page
- show in plugin/extension menu (blue button)
- is position 1 correct?
- include ``.py`` files?
- include ``.po`` files?


License
=======
The plugin is subject to the GPLv3 or later.



Translation
===========
Beginning a new translation
---------------------------
Replace ``$lang_code`` with your two-letter language code::

    $ cd po
    $ cp messages.po $lang_code.po
    ... edit $lang_code.po now
    $ ./compile.sh


Building
========
ipkg-build:
 http://reichholf.net/files/dreambox/tools/ipkg-build

http://dream.reichholf.net/wiki/Howto:IPK_Pakete_erstellen
