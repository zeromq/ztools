#!/bin/sh

fail() {
	echo "Build failed"
	exit 1
}
trap fail ERR

if test "x$1" = "x"; then
	echo "Usage: $0 <repo url>"
	exit 1
fi

if test -d ./build_tmp_dir; then
    rm -rf ./build_tmp_dir
fi

# Clone the repository
git clone $1 ./build_tmp_dir
cd ./build_tmp_dir

# Prepare build
./autogen.sh
./configure

# Build
make -j2
make check