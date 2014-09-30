"""Tests for emission of high-level markup, as by templates"""

from dxr.testing import DxrInstanceTestCase, run

from nose.tools import eq_, ok_


class MarkupTests(DxrInstanceTestCase):
    def test_autofocus_root(self):
        """Autofocus the query field at the root of each tree but not
        elsewhere."""
        response = self.client().get('/code/source/')
        ok_('<input type="text" name="q" autofocus' in response.data)

        response = self.client().get('/code/source/%26folder%26')
        eq_(response.status_code, 200)
        ok_('<input type="text" name="q" autofocus' not in response.data)

    def test_folder_name_escaping(self):
        """Make sure folder names are HTML-escaped."""
        response = self.client().get('/code/source/')
        ok_('&folder&' not in response.data)
        ok_('&amp;folder&amp;' in response.data)

    def test_analytics_snippet_empty( self ):
        """Make sure google analytics snippet doesn't show up
        in when the key isn't configured"""
        response = self.client().get( '/code/source' )
        ok_( '.google-analytics.com' not in response.data )

