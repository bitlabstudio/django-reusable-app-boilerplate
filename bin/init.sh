#!/bin/sh

echo "Initialize git repository..."
rm -rf .git
git init
git commit -am "Initial commit"

echo "Done! Please edit AUTHORS, DESCRIPTION and README.rst now."
