from requests import request, Session

def myrequest(method, url, **kwargs):
    method = method.upper()
    res = request(method=method, url=url, **kwargs)
    return res

def session(method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None):
    method = method.upper()
    with Session() as s:
        res = s.request(method, url, 
        params=params, 
        data=data, 
        headers=headers, 
        cookies=cookies, 
        files=files, 
        auth=auth, 
        timeout=timeout, 
        allow_redirects=allow_redirects, 
        proxies=proxies, 
        hooks=hooks, 
        stream=stream, 
        verify=verify, 
        cert=cert, 
        json=json)
        return res
