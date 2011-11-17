#!/bin/sh
[ -d tmp ] && rm -r tmp

extdir=usr/lib/enigma2/python/Plugins/Extensions/CurlyTx
mkdir -p tmp/$extdir/locale/
cp -R CONTROL tmp/

for i in po/??.mo; do
    lang=`basename "$i" .mo`
    mkdir -p tmp/$extdir/locale/$lang/LC_MESSAGES
    cp "$i" tmp/$extdir/locale/$lang/LC_MESSAGES/CurlyTx.mo
    cp src/*.py tmp/$extdir/
    python -O -m compileall src/ -d tmp/$extdir
done

ipkg-build tmp/
rm -r tmp
