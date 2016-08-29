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

from caesar import encrypt

form = """
<form action = "/encoder">

  <label>Code<input type = "text" name ="code"></label>
  <label>Rotation Amount (1-26)<input type = "text" name ="amount"></label>
  <input type ="submit" value = "encrypt me">

</form>

"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

class Encode(webapp2.RequestHandler):
    def get(self):
    #def post(self):
        q = self.request.get("code")
        n = self.request.get("amount")
        n = int(n)
        code2 = encrypt(q, n)
        self.response.write(code2)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/encoder', Encode)
], debug=True)
