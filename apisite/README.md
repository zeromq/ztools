
<A name="toc1-4" title="ztools/apisite - Rebuild api.zero.mq site" />
ztools/apisite - Rebuild api.zero.mq site
=========================================


**<a href="#toc2-9">What?</a>**

**<a href="#toc2-14">How?</a>**

**<a href="#toc2-43">Site Admin and CSS</a>**

<A name="toc2-9" title="What?" />
## What?

Automates the conversion and uploading of ØMQ man pages to this Wikidot site. Using a Wikidot site makes it easy for us to change the CSS and administer the site without access to any server.

<A name="toc2-14" title="How?" />
## How?

To use, you need Wikidot API access. This means a Wikidot login (your own, normally) and a corresponding API key.

To install:

    export APISITE_USER=_login_
    export APISITE_KEY=_key_
    git clone git://github.com/zeromq/ztools.git
    git clone git://github.com/zeromq/zeromq2.git
    git clone git://github.com/zeromq/zeromq2-1.git

Make sure the main and 2.1 gits are in parallel directories to ztools.

To run on all versions from 2.0.6 to master:

    cd ztools/apisite
    ./apiall

To run on one specific version:

    cd ztools/apisite
    ./apione <zmq_dir> <branch> <category>
    
Where branch is the git branch or tag, and category is the destination on the wiki site. E.g.

    ./apione ../../zeromq2 v2.0.10 2-0-10
    
<A name="toc2-43" title="Site Admin and CSS" />
## Site Admin and CSS

To change the look and feel of the site you need edit access, and then you can edit http://api.zero.mq/admin:css. The site manager is at http://api.zero.mq/admin:manage.
