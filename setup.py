from distutils.core import setup
setup(
  name = 'rest_framework_borderkeeper',
  packages = ['rest_framework_borderkeeper'],
  version = '0.0.2',
  description = 'Django Rest Framework Library to manage user filters and permissions with different entities',
  author = 'Marcelo Cueto',
  author_email = 'yo@marcelocueto.cl',
  url = 'https://github.com/mcueto/djangorestframework-borderkeeper',
  download_url = 'https://github.com/mcueto/djangorestframework-borderkeeper/tarball/0.0.2',
  keywords = ['rest framework', 'django', 'security'],
  classifiers=[
      'Environment :: Web Environment',
      'Framework :: Django',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Topic :: Internet :: WWW/HTTP',
  ],
  install_requires = [
      'djangorestframework>=1.9.0',
      'django-filter',
  ],
)
