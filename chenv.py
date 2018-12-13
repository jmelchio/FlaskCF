import os
import json

vcapservices = json.loads(os.environ['VCAP_SERVICES'])

print 'before password:' + vcapservices['p-redis'][0]['credentials']['password']

vcapservices['p-redis'][0]['credentials']['password'] = 'madeuppassword'

print 'after password:' + vcapservices['p-redis'][0]['credentials']['password']
print json.dumps(vcapservices)

os.environ['ALT_SERVICES'] = json.dumps(vcapservices)

print os.environ['ALT_SERVICES']

# That's All Folks !!
