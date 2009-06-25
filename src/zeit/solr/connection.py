# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import lxml.etree
import lxml.html
import pysolr
import urllib2
import zeit.solr.interfaces
import zope.app.appsetup.product
import zope.interface


class SolrConnection(pysolr.Solr):

    zope.interface.implements(zeit.solr.interfaces.ISolr)

    def update_raw(self, xml):
        data = lxml.etree.tostring(xml, pretty_print=True, encoding='utf8')
        response = self._update(data)
        if response.status != 200:
            raise pysolr.SolrError(self._extract_error(response))

    def _extract_error(self, response):
        # patched to use HTML instead of XML parser, so it does not choke
        # on <hr>-Tags, for example
        et = lxml.html.parse(response)
        return "[%s] %s" % (response.reason, et.findtext('body/h1'))

    def _send_request(self, method, path, body=None, headers=None):
        """Override to use urllib2 instead of httplib directly for file urls.

        This is used for testing only.

        """
        if self.url.startswith('file://'):
            assert method == 'GET' and not headers
            url = 'file://%s' % path
            return urllib2.urlopen(url).read()
        return super(SolrConnection, self)._send_request(
            method, path, body, headers)


@zope.interface.implementer(zeit.solr.interfaces.ISolr)
def solr_connection_factory():
    config = zope.app.appsetup.product.getProductConfiguration('zeit.solr')
    url = config.get('solr-url')
    return SolrConnection(url)