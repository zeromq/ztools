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

    export APISITE_USER=_login_
    export APISITE_KEY=_key_
    git clone git://github.com/zeromq/ztools.git
    git clone git://github.com/zeromq/libzmq.git
    git clone git://github.com/zeromq/zeromq2-1.git
    git clone git://github.com/zeromq/zeromq2-2.git

To run on current versions:

    cd ztools/apisite
    ./apiall

To run on one specific version:

    cd ztools/apisite
    ./apione <zmq_dir> <branch> <category>

Where branch is the git branch or tag, and category is the destination on the wiki site. E.g.

    ./apione ../../libzmq master 3-1

## Site Admin and CSS

To change the look and feel of the site you need edit access, and then you can edit http://api.zero.mq/admin:css. The site manager is at http://api.zero.mq/admin:manage.
