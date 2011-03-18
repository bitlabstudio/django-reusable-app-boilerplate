#!/bin/sh
echo "Name of your reusable app:"
read APPNAME
echo "Keywords for your app:"
read KEYWORDS
echo "Author of your app:"
read AUTHOR
echo "Author email of your app:"
read AUTHOREMAIL
echo "URL for your app:"
read URL

echo "Deleting .git folder"
rm -rf .git

echo "Replacing README.rst"
rm README.rst
mv lib/README.rst .
rm -rf lib

echo "Replacing strings in files..."
sed -i "s/the_keywords/$KEYWORDS/g" setup.py
sed -i "s/the_author/$AUTHOR/g" setup.py
sed -i "s/the_email/$AUTHOREMAIL/g" setup.py
sed -i "s@the_url@$URL@g" setup.py
find . -type f -exec sed -i "s/appname/$APPNAME/g" {} +

echo "Renaming folders..."
mv appname/templates/appname/ appname/templates/$APPNAME
mv appname $APPNAME

echo "Deleting bin folder..."
rm -rf bin

echo "Initialize new git repository..."
git init
git add .
git commit -am "Initial commit"

echo "Done! Please edit AUTHORS, DESCRIPTION and README.rst now."
