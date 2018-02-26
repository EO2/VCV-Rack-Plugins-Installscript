import json
#from pprint import pprint
import os
import sys

repos = list()
clone = "git clone "
#git clone --recursive # to get submodules in one go..
# ..community/plugins/
os.chdir('plugins')

for file in os.listdir('.'):
    data = json.load(open(file))
    #pprint(data)
    #print(data['slug'])
    source = data.get('source')
    if source: 
	print(source)
	repos.append(source)


os.chdir('../../plugins')

for repo in repos:
    os.system(clone + repo)


'''
{
  "slug": "AudibleInstruments",
  "name": "Audible Instruments",
  "author": "VCV",
  "license": "BSD 3-clause",
  "version": "0.5.0",
  "homepage": "https://vcvrack.com/",
  "donation": "https://www.paypal.me/",
  "manual": "https://vcvrack.com/manual/AudibleInstruments.html",
  "source": "https://github.com/VCVRack/AudibleInstruments",
  "downloads": {
    "win": {
      "download": "https://example.com/AudibleInstruments-0.5.0-win.zip",
      "sha256": "9372ce3f8ef42d7e874beda36f7c051b3d7de9c904e259a5fc9dba8dc664bf65"
    },
    "lin": {
      "download": "https://example.com/AudibleInstruments-0.5.0-lin.zip",
      "sha256": "238145156cc4e11b3ca6d750df38ca2daf3e09648d9c7db5f23e9518c1ccf5dc"
    },
    "mac": {
      "download": "https://example.com/AudibleInstruments-0.5.0-mac.zip",
      "sha256": "c19fcdfd07dc6184ce30953bf9adb2b4a77d20ef66d2b1c6a6024c2ca4ff505b"
    }
  }
}
'''
