#!/usr/bin/python
# -*- coding: utf-8 -*-

from contextlib import contextmanager
import os
import re
import sys
import tempfile


# see http://en.wikipedia.org/wiki/ANSI_escape_code for more ANSI escape codes
class textColors( object ):
    grey        = '37m'
    white       = '97m'
    cyan        = '36m'
    lightcyan   = '96m'
    pink        = '35m'
    lightpink   = '95m'
    blue        = '34m'
    lightblue   = '94m'
    yellow      = '33m'
    lightyellow = '93m'
    green       = '32m'
    lightgreen  = '92m'
    red         = '31m'
    lightred    = '91m'
    black       = '30m'
    darkgrey    = '90m'

    def get( self, sColor, isBold = False ):

        if ( isBold ):
            return '\033[1;' + vars( textColors )[sColor]
        else:
            return '\033[0;' + vars( textColors )[sColor]

    def end( self ):
        return '\033[0m'


@contextmanager
def namedTempfile():
    tmpFile = tempfile.NamedTemporaryFile( delete = False )

    try:
        yield tmpFile
    finally:
        tmpFile.close()
        os.unlink( tmpFile.name )


class showText( object ):
    def help( self ):
        print 'Usage:   gist [-b] [-c] [-h] [-l] [-o] [-s <search string>] [-t <GitHub API token>]'
        print 'Options:'
        print '         -h                      Show this help'
        print '         -b                      Open a selected Gist in the Webbrowser'
        print '         -c                      Copy a selected Gist into your clipboard'
        print '         -l                      List all your Gists'
        print '         -s <search string>      Search for a string in all Gist descriptions'
        print '         -t <GitHub API token>   Set your GitHub API token to access your Gists'
        print '\r'
        print 'Legend: ' + textColors().get( 'yellow' ) + 'private Gist' + textColors().end() + ', ' + textColors().get( 'green' ) + 'public Gist' + textColors().end() + ', ' + textColors().get( 'red' ) + 'error' + textColors().end()


class SimpleHTTPError( Exception ):
    def __init__( self, code, response ):
        response = json.loads( response.decode( 'utf8', 'ignore' ) )
        print helpers.textColors().get( 'red' ) + response['message'] + ' (' + str( code ) + ')' + helpers.textColors().end()
        sys.exit()
