#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import os
import jinja2
import random
from google.appenfine.api import urlfetch
import urllib
import json

URL = 'https://www.googleapis.com/customsearch/v1?'
KEY = 'AIzaSyBiXlnOqjWbZ5CMc5-K4Lx1RvxwdUWZwtQ'
CX = '016629791439433559366:cr05fhnqi4m'

def get_fortune():
    fortune_list=['Tomorrow, you will meet a life-changing new friend.',
                  'Fame and Instagram followers are headed your way.',
                  'On the Tuesday after next, an odd meeting will lead to a new opportunity.',
                  'Despite dry skies, bring an umbrella tomorrow.',
                  'A thrilling time is in your immediate future.',
                  'Someone has Googled you recently.',
                  'Stay alert. You will be part of a rescue mission.',
                  'You will beat Watson in a game of Jeopardy. Start studying though']
    return(random.choice(fortune_list))


#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        start_template=jinja_current_directory.get_template("templates/fortune_welcome.html")
        self.response.write(start_template.render())


class SimpleURLFetcher(webapp2.RequestHandler):
    def get(self):
        query = 'cat'
        query_params = {'key': KEY, 'cx': CX, 'q': query}
        result = urlfetch.fetch(URL + urllib.urlencode(query_params))
        print result 
        if result.status_code == 200:
            self.response.write(result.status_code)
            self.response.write(result.content)

        else:
            self.response.status_code = result.status_code

#the route mapping
app = webapp2.WSGIApplication([

    ('/simple', SimpleURLFetcher)

], debug=True)





#
#     def post(self):
#         random_fortune = get_fortune()
#         astro_sign = self.request.get('user_astrological_sign')
#         my_dict={'the_fortune':random_fortune, 'the_astro_sign':astro_sign}
#         end_template=jinja_current_directory.get_template("templates/fortune_results.html")
#         #astro_sign = request.form.get('user_astrological_sign')
#         self.response.write(end_template.render(my_dict))
#
#
#
# app = webapp2.WSGIApplication([
#     ('/', FortuneHandler)
# ], debug=True)
