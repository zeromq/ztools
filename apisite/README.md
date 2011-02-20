
<A name="toc1-4" title="ztools/apisite - Rebuild api.zero.mq site" />
ztools/apisite - Rebuild api.zero.mq site
=========================================


**<a href="#toc2-9">What?</a>**

**<a href="#toc2-14">How?</a>**

**<a href="#toc2-29">Site Admin and CSS</a>**

<A name="toc2-9" title="What?" />
## What?

Automates the conversion and uploading of ØMQ man pages to this Wikidot site. Using a Wikidot site makes it easy for us to change the CSS and administer the site without access to any server.

<A name="toc2-14" title="How?" />
## How?

To use, you need Wikidot API access. This means a Wikidot login (your own, normally) and a corresponding API key.

To install:

* export APISITE_USER=_login_
* export APISITE_KEY=_key_
* if the zeromq2 repository is not at ../../zeromq2 (from the apisite directory), export ZMQ_DIR=_zeromq-dir_

To run *apisite*:

* run ./apisite from the ztools/apisite directory and watch what happens.

<A name="toc2-29" title="Site Admin and CSS" />
## Site Admin and CSS

To change the look and feel of the site you need edit access, and then you can edit http://api.zero.mq/admin:css. The site manager is at http://api.zero.mq/admin:manage.
