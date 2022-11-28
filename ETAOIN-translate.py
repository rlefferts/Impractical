import requests, uuid, json
import pprint

# Add your key and endpoint
key = "e0e3004801a74aae8591469ba0c90dbe"
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "westus3"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['es']
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
#body = [{
#    'text': 'I would really like to drive your car around the block a few times!'
#}]

#request = requests.post(constructed_url, params=params, headers=headers, json=body)
#response = request.json()

#print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

TEXT = 'Like the castle in its corner in a medieval game, I foresee terrible \
trouble and I stay here just the same.'

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def count_letters(d, w):

    for l in w:
        l = l.lower()
        if l in ALPHABET:
            if l not in d:
                d[l] = 0
            d[l] += 1

    return(d)

def transate_to_spanish(s):
    body = [{'text': s}]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return(response[0]['translations'][0]['text'])
   

def main():

    d = {}

    new_text = transate_to_spanish(TEXT)

    print("Counting the letters in:\n", new_text, '\n')

    for word in new_text.split():
        count_letters(d, word)

    for (l,x) in sorted(d.items(), key=lambda x:x[1], reverse=True):
            print("%s : %2d : %s" % (l, x, 'X' * x))

if __name__ == "__main__":
    main()