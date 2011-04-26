#!/bin/bash

#
# Simple shell-script to ensure things are run in serial
#

if test "x${LOCK_FILE}" = "x"; then
	echo "LOCK_FILE environment variable must be set"
	exit 1
fi

WAIT_FOR_LOCK=10
HAS_LOCK="no"

n=0
while [ $n -lt ${WAIT_FOR_LOCK} ]; do
	if test -f "${LOCK_FILE}"; then
		echo "${LOCK_FILE} exists, sleeping.."
		sleep 1
	else
		echo "Created ${LOCK_FILE}"
		echo -n "$$" > "${LOCK_FILE}"
		HAS_LOCK="yes"
		break
	fi
	let "n=n+1"
done

if test "x${HAS_LOCK}" != "xyes"; then
	echo "Failed to acquire lock. Forcing execution."
	echo -n "$$" > "${LOCK_FILE}"
fi

$@

echo "Removing ${LOCK_FILE}"
rm "${LOCK_FILE}"


