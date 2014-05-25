#!/bin/bash -vex

rpmbuild -bs --nodeps \
  --define "_sourcedir ." \
  --define "_srcrpmdir ." \
  google-droid-sans-mono-slashed-zero.spec
