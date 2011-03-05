#!/bin/sh

if test "x$1" = "x"; then
    echo "Usage: $0 <git repo>"
    exit 1
fi

if test "x$JENKINS_URI" = "x"; then
    echo "JENKINS_URI must be set"
    exit 1
fi

START_TIME=`date +'%s'`
./execbuild.sh "$1" > ./raw_output.txt 2>&1
BUILD_STATUS=$?
BUILD_OUTPUT=`xxd -p ./raw_output.txt | tr -d '\n'`
END_TIME=`date +'%s'`

ELAPSED_TIME=`expr $END_TIME - $START_TIME`
ELAPSED_TIME=`expr $ELAPSED_TIME \\* 1000`

echo "<run>
        <log encoding='hexBinary'>${BUILD_OUTPUT}</log>
        <result>${BUILD_STATUS}</result>
        <duration>${ELAPSED_TIME}</duration>
      </run>" > ./build_output.txt

curl --insecure -X POST --raw --upload-file ./build_output.txt \
"${JENKINS_URI}/job/${JOB_NAME}/postBuildResult"