from setuptools import setup, find_packages


setup(
    name='zeit.solr',
    version='2.6.1.dev0',
    author='gocept, Zeit Online',
    author_email='zon-backend@zeit.de',
    url='http://www.zeit.de',
    description='Solr interface',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='BSD',
    namespace_packages=['zeit'],
    install_requires=[
        'gocept.async>=0.3.1',
        'grokcore.component',
        'httplib2',
        'mock',
        'plone.testing',
        'pysolr > 2.0.5',
        'setuptools',
        'zeit.cms>=2.50.0.dev0',
        'zeit.connector>=1.24.0dev',
        'zeit.content.article>=2.8.1',
        'zeit.content.cp >= 2.6.0.dev0',
        'zeit.content.image',
        'zeit.content.portraitbox',
        'zope.index',
    ],
    entry_points="""
        [console_scripts]
        solr-reindex-object=zeit.solr.update:update_main
        solr-reindex-query=zeit.solr.reindex:reindex
        """
)
