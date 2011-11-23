=======
CurlyTx
=======
Enigma2 (Dreambox) plugin that lets you view the contents of remote
plain text files, e.g. HTTP.

Multiple URLs can be configured and navigated.



Open issues
===========
- page import via atom feed/opml
- move mode to re-order pages
- how to show clock in lcd?
- show headers when pressing info button


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
