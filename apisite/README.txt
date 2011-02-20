.set GIT=http://github.com/zeromq/ztools/apisite
.sub 0MQ=ØMQ

ztools/apisite - Rebuild api.zero.mq site
=========================================

.toc

## What?

Automates the conversion and uploading of 0MQ man pages to this Wikidot site. Using a Wikidot site makes it easy for us to change the CSS and administer the site without access to any server.

## How?

To use, you need Wikidot API access. This means a Wikidot login (your own, normally) and a corresponding API key.

To install:

* export APISITE_USER=_login_
* export APISITE_KEY=_key_
* if the zeromq2 repository is not at ../../zeromq2 (from the apisite directory), export ZMQ_DIR=_zeromq-dir_

To run *apisite*:

* run ./apisite from the ztools/apisite directory and watch what happens.

## Site Admin and CSS

To change the look and feel of the site you need edit access, and then you can edit http://api.zero.mq/admin:css. The site manager is at http://api.zero.mq/admin:manage.
