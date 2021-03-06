#!/usr/bin/env python

__author__ = "Mark Nottingham <mnot@mnot.net>"
__copyright__ = """\
Copyright (c) 2008-2013 Mark Nottingham

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""


import redbot.speak as rs
from redbot.message import headers as rh
from redbot.message import http_syntax as syntax


@rh.GenericHeaderSyntax
def parse(subject, value, red):
    return value.lower()
    
def join(subject, values, red):
    if 'deny' in values:
        red.add_note(subject, rs.FRAME_OPTIONS_DENY)
    elif 'sameorigin' in values:
        red.add_note(subject, rs.FRAME_OPTIONS_SAMEORIGIN)
    else:
        red.add_note(subject, rs.FRAME_OPTIONS_UNKNOWN)
    return values


class DenyXFOTest(rh.HeaderTest):
    name = 'X-Frame-Options'
    inputs = ['deny']
    expected_out = ['deny']
    expected_err = [rs.FRAME_OPTIONS_DENY]
    
class DenyXFOCaseTest(rh.HeaderTest):
    name = 'X-Frame-Options'
    inputs = ['DENY']
    expected_out = ['deny']
    expected_err = [rs.FRAME_OPTIONS_DENY]
    
class SameOriginXFOTest(rh.HeaderTest):
    name = 'X-Frame-Options'
    inputs = ['sameorigin']
    expected_out = ['sameorigin']
    expected_err = [rs.FRAME_OPTIONS_SAMEORIGIN]

class UnknownXFOTest(rh.HeaderTest):
    name = 'X-Frame-Options'
    inputs = ['foO']
    expected_out = ['foo']
    expected_err = [rs.FRAME_OPTIONS_UNKNOWN]

