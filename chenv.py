import os
import json

vcapservices = os.environ.get('VCAPSERVICES')
if vcapservices is None:
    print('Not running in CloudFoundry')
else:
    vcapservices = json.loads(vcapservices)

    print('before password:' + vcapservices['p-redis'][0]['credentials']['password'])

    vcapservices['p-redis'][0]['credentials']['password'] = 'madeuppassword'

    print('after password:' + vcapservices['p-redis'][0]['credentials']['password'])
    print(json.dumps(vcapservices))

    os.environ['ALT_SERVICES'] = json.dumps(vcapservices)

    print(os.environ['ALT_SERVICES'])

# That's All Folks !!
