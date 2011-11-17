#!/bin/sh
xgettext -kT_ -L Python ../src/*.py

for i in ??.po; do
    msgmerge --update --backup=off "$i" messages.po
done
