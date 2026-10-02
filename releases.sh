#! /bin/bash
set -e

RELEASE=calibration-release

rm -rf "$RELEASE"
mkdir "$RELEASE"

# Copy required files
cp *.py           "$RELEASE/"
cp setup-calibration.sh              "$RELEASE/"
cp change_pswd.sh              "$RELEASE/"
cp config.txt       "$RELEASE/"
cp -r services      "$RELEASE/"

# Compile python files
python3.13 -m compileall -b -q "$RELEASE/"

# Remove the original Python source
rm -f "$RELEASE"/*.py


# Create zip
zip -r "$RELEASE.zip" "$RELEASE"

echo "Created $RELEASE.zip"