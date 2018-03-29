###
# APP NAME: mom

# APPID: 29778R-Q4T2Q759RR

# USAGE TYPE: Personal/Non-commercial Only
###


import wolframalpha

# app_id = ''
client = wolframalpha.Client('29778R-Q4T2Q759RR')

question = raw_input('Q: ')
result = client.query(question)
ans = next(result.results).text

print ans
