import os
import requests
import time
import urllib
from django.conf import settings


class SiteMapGenerator(object):
    """
    Class that is to be extended from to allow custom build outs for different sitemaps
    """
    # to be set by the developer when they extend this class
    MODULE = ''
    NAME = ''

    # internal variables
    _file_location = None
    _file_pointer = None
    _locations = []
    _sitemaps = []
    _site_url = 'SITE URL HERE'

    # Choices for the "build" method
    LOCATIONS = 1
    SITEMAPS = 2

    def _get_locations(self):
        raise NotImplementedError

    def _get_sitemaps(self):
        raise NotImplementedError

    def _add_location(self, location, last_modified):
        """
        Method to add a location to be written out

        :location The location of the item that you are wanting to add
        """
        if last_modified is None:
            last_modified = time.strftime("%Y-%m-%d")

        self._locations.append({
            'location': '{0}{1}'.format(self._site_url, location),
            'last_modified': last_modified
        })

    def _add_sitemap(self, location, last_modified=None):
        """
        Method to add a sitemap to be written out

        :location Full URL to the location of the sitemap
        :last_modified Example format 2014-04-15
        """
        if last_modified is None:
            last_modified = time.strftime("%Y-%m-%d")

        self._sitemaps.append({
            'location': '{0}{1}'.format(self._site_url, location),
            'last_modified': last_modified
        })

    def _open_file(self):
        """
        Method to open a connection to write the file out
        """
        if not os.path.exists(self._file_location):
            os.makedirs(self._file_location)

        full_file_path = os.path.join(self._file_location, '{0}_{1}.xml'.format(self.MODULE, self.NAME))

        try:
            os.remove(full_file_path)
        except OSError:
            pass

        self._file_pointer = open(full_file_path, 'w')

    def _close_file(self):
        """
        Method to close the connection to the file we are writing out
        """
        self._file_pointer.close()

    def _build_locations(self):
        """
        Method to build out all the locations that have been requested
        """
        self._get_locations()

        self._file_pointer.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        self._file_pointer.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        self._file_pointer.write('<url>\n')

        for location in self._locations:
            # build the entry
            entry = '<loc>{0}</loc><lastmod>{1}</lastmod>\n'.format(location.get('location'),
                                                                    location.get('last_modified'))
            # write out the entry to the file
            self._file_pointer.write(entry)

        self._file_pointer.write('</url>\n')
        self._file_pointer.write('</urlset>\n')

    def _build_sitemaps(self):
        """
        Method to build out all the sitemaps that have been requested
        """
        self._get_sitemaps()

        self._file_pointer.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        self._file_pointer.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

        for sitemap in self._sitemaps:
            # build the entry
            entry = '<sitemap><loc>{0}</loc><lastmod>{1}</lastmod></sitemap>\n'.format(sitemap.get('location'),
                                                                                       sitemap.get('last_modified'))
            # write out the entry to the file
            self._file_pointer.write(entry)

        self._file_pointer.write('</sitemapindex>\n')

    def get_sitemap_name(self):
        """
        Method to get back the sitemap name that would be generated from this class
        """
        return '{0}_{1}.xml'.format(self.MODULE, self.NAME)

    def get_sitemap_url(self):
        """
        Method to get back the sitemap name that would be generated from this class
        """
        return '/assets/sitemaps/{0}'.format(self.get_sitemap_name())

    def send_sitemap_to_google(self):
        """
        Method to send the sitemap to google
        """
        full_sitemap_url = urllib.urlencode({
            'sitemap': '{0}{1}'.format(self._site_url, self.get_sitemap_url())
        })

        response = requests.get('http://www.google.com/webmasters/tools/ping?{0}'.format(full_sitemap_url))

    def build(self, type):
        """
        Method to build out the sitemap based on the type requested

        :type Type of sitemap that you are wanting to build out
        """
        if self._file_location is None:
            self._file_location = os.path.join(settings.PROJECT_PATH, '/assets/sitemaps/')

        # open the file up to write
        self._open_file()

        if type == self.LOCATIONS:
            self._build_locations()
        elif type == self.SITEMAPS:
            self._build_sitemaps()

        # close the file down
        self._close_file()

        # self.send_sitemap_to_google()
