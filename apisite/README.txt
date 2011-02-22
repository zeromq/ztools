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

* syntax: apisite [ [ zmq_dir ] branch category ]
* Without arguments, assumes 0MQ is in ../../zeromq2, and processes the versions released from that git (2.1.0 back to 2.0.6).
* With arguments, processes a single branch/tag from a specified git repository location. E.g. "apisite ../../zeromq2 master master".

## Site Admin and CSS

To change the look and feel of the site you need edit access, and then you can edit http://api.zero.mq/admin:css. The site manager is at http://api.zero.mq/admin:manage.
