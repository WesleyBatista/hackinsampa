# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Global configuration for all WSGI apps.
"""
import os
import sys
import logging


IS_DEVSERVER = os.environ.get('SERVER_SOFTWARE', '').lower().startswith('devel')
CUR_DIR = os.path.dirname(__file__)
LIB_DIR = os.path.join(CUR_DIR, 'lib')


if IS_DEVSERVER:
    logging.getLogger().handlers[0].setLevel(logging.DEBUG)


def fix_path():
    if LIB_DIR not in sys.path:
        sys.path.append(LIB_DIR)

fix_path()


def webapp_add_wsgi_middleware(app):
    # from google.appengine.ext.appstats import recording
    # app = recording.appstats_wsgi_middleware(app)

    if IS_DEVSERVER:
        logging.debug('\n\n\n')  # space on console between requests
    
    return app


from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
vendor.add('lib')
