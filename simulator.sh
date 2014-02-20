#!/bin/bash

pushd prototype;
svn up
find . -name '*.proto' |xargs protoc --python_out=.
touch __init__.py
popd

python simulator.py
