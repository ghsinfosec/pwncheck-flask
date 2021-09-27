import hashlib
import requests


def pwncheck(password):
    # get the sha1 hash of submitted pw
    sha1 = hashlib.sha1(password.encode('utf-8'))
    pw_hash = sha1.hexdigest().upper()  # convert to upper case
    prefix = pw_hash[0:5]  # necessary for the api, ref above

    url = f'https://api.pwnedpasswords.com/range/{prefix}'

    response = requests.get(url).content.decode('utf-8')  # store the response in utf-8 format

    # create a dictionary to store the key/value pairs of returned hashes
    hash_data = dict(i.split(':') for i in response.split('\r\n'))

    # include the prefix to store the full pw hash
    hash_data = dict((prefix + key, value) for (key, value) in hash_data.items())

    # check for the pw hash in the dictionary to find a match
    for k, v in hash_data.items():
        # match found, pw is compromised
        if k == pw_hash:
            status = f'[!!] The password you entered has been seen {v} \
             times in data breaches! Do NOT use this password! [!!]'
            message = 'compromised'
            break

    # no match found, pw is good for now
    if pw_hash != k:
        status = f'The password you entered has not been found \
        in any data breach and is safe to use!'
        message = 'safe'

    return status, message
