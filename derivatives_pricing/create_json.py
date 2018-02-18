

import json

securities = {'1':['AAPL',100,1,'call'],'2':['GOOG',200,1,'call'],'3':['MSFT',200,1,'put']}

with open('options.json', 'w') as fp:
    json.dump(securities, fp)
