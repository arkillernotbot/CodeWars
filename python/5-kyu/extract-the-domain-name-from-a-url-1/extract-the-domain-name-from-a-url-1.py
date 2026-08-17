def domain_name(url):
    a = url.find('/')
    if url.startswith("http"):
        url = url[a+2:]
    url = url.split('.')
    if url[0] != 'www':
        return url[0]
    else:
        return url[1]