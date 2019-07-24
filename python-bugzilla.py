#https://github.com/python-bugzilla/python-bugzilla
#https://github.com/python-bugzilla/python-bugzilla/tree/master/examples

from __future__ import print_function

import pprint

import bugzilla

# public test instance of bugzilla.redhat.com. It's okay to make changes
URL = "https://bugzilla.redhat.com"
api_key = 'uFlE6S9SwJhu3LFtxmnjhzIHbGaCHjcAwqQmeD5l'
bzapi = bugzilla.Bugzilla(URL,api_key)

# getbug() is just a simple wrapper around getbugs(), which takes a list
# IDs, if you need to fetch multiple
#
# Example bug: https://partner-bugzilla.redhat.com/show_bug.cgi?id=427301
bug = bzapi.getbug(1700044)
print("Fetched bug #%s:" % bug.id)
print("  Product   = %s" % bug.product)
print("  Component = %s" % bug.component)
print("  Status    = %s" % bug.status)
print("  Resolution= %s" % bug.resolution)
print("  Summary   = %s" % bug.summary)
print("  comment   = %s" % bug.comment)

# Just check dir(bug) for other attributes, or check upstream bugzilla
# Bug.get docs for field names:
# https://bugzilla.readthedocs.io/en/latest/api/core/v1/bug.html#get-bug

# comments must be fetched separately on stock bugzilla. this just returns
# a raw dict with all the info.
comments = bug.getcomments()
print("\nLast comment data:\n%s" % pprint.pformat(comments[-1]))

#todo make recurse over the bug comments and retrieve the bz_auto_reproducer shell command

# getcomments is just a wrapper around bzapi.get_comments(), which can be
# used for bulk comments fetching
