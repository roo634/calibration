#! /bin/bash
set -e

RELEASE=calibration-release

rm -rf "$RELEASE"
mkdir "$RELEASE"

# Copy required files
cp *.py           "$RELEASE/"
rm "$RELEASE/test.py"
cp setup-calibration.sh              "$RELEASE/"
cp config.txt       "$RELEASE/"
cp -r services      "$RELEASE/"


# Create zip
zip -r "$RELEASE.zip" "$RELEASE"

echo "Created $RELEASE.zip"