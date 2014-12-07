#! /bin/python
#
#   Hack a set of redirects from the old API pages to the new ones

site = "0mq-api"

#   Get authentication credentials
import os
user = os.environ ['APISITE_USER']
key  = os.environ ['APISITE_KEY']

#   Create XML/RPC connection to Wikidot
from xmlrpclib import ServerProxy
server = ServerProxy ('https://' + user + ':' + key + '@www.wikidot.com/xml-rpc-api.php')

server.pages.save_one ({ "site": site, "page":        "zmq-setsockopt-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_setsockopt\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-bind-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_bind\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-close-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_close\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-connect-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_connect\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-cpp-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_cpp\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-epgm-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_epgm\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-forwarder-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_forwarder\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-init-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_init\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-inproc-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_inproc\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-ipc-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_ipc\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-msg-close-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_msg_close\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-msg-copy-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_msg_copy\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-msg-data-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_msg_data\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-msg-init-data-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_msg_init_data\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-msg-init-size-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_msg_init_size\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-msg-init-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_msg_init\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-msg-move-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_msg_move\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-msg-size-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_msg_size\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-pgm-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_pgm\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-poll-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_poll\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-queue-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_queue\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-recv-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_recv\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-send-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_send\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-setsockopt-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_setsockopt\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-socket-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_socket\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-streamer-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_streamer\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-strerror-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_strerror\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-tcp-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_tcp\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-term-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_term\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-version-html",
    "content": " [[module redirect destination=\"2-1-1:zmq_version\"]]" })
server.pages.save_one ({ "site": site, "page":        "zmq-html",
    "content": " [[module redirect destination=\"2-1-1:zmq\"]]" })
