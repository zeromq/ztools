#!/bin/sh
#
#

if [ "x$1" = "x" ] || [ "x$2" = "x" ]; then
    echo "Usage: $0 <source directory> <output xml>"
    exit 1
fi

if test ! -d "$1"; then
    echo "Source directory does not exist"
    exit 1
fi

CURRENT_DIR=$( pwd )
SOURCE_DIR="$1"
OUTPUT_XML="$2"

create_coverage() {
    BASENAME=$( basename $1 $2 )
    find ".libs/" -name "*${BASENAME}.gcno" -exec gcov --branch-probabilities --no-output --object-directory {} "$1" \;
}

cd "$SOURCE_DIR"

for i in *.c; do
    create_coverage "$i" ".c"
done

for i in *.cpp; do
    create_coverage "$i" ".cpp"
done

cd $CURRENT_DIR

# from https://software.sandia.gov/trac/fast/wiki/gcovr
gcovr --xml --output="$OUTPUT_XML" -r "$SOURCE_DIR"