import json

def python_to_json(
    value, 
    skipkeys=False, 
    ensure_ascii=True,
    check_circular=True, 
    allow_nan=True, 
    cls=None, 
    indent=None,
    separators=None, 
    default=None, 
    sort_keys=False, **kw) -> json:
    '''
    将Python对象编码成json字符串
    '''
    if not isinstance(value, (dict, list)):
        from ast import literal_eval
        v = literal_eval(value)
        _value = json.dumps(v,
            skipkeys=skipkeys, 
            ensure_ascii=ensure_ascii,
            check_circular=check_circular, 
            allow_nan=allow_nan, 
            cls=cls,
            indent=indent, 
            separators=separators, 
            default=default, 
            sort_keys=sort_keys, **kw)
    else:
        _value = json.dumps(value,
            skipkeys=skipkeys, 
            ensure_ascii=ensure_ascii,
            check_circular=check_circular, 
            allow_nan=allow_nan, 
            cls=cls,
            indent=indent, 
            separators=separators, 
            default=default, 
            sort_keys=sort_keys, **kw)
    return _value

def json_to_python(
    value: str, 
    cls=None, 
    object_hook=None, 
    parse_float=None,
    parse_int=None, 
    parse_constant=None, 
    object_pairs_hook=None, **kw) -> dict:
    '''
    将已编码的 JSON 字符串解码为 Python 对象 
    '''
    _value = json.loads(
        value, 
        cls=cls, 
        object_hook=object_hook, 
        parse_float=parse_float,
        parse_int=parse_int, 
        parse_constant=parse_constant, 
        object_pairs_hook=object_pairs_hook, **kw)
    return _value
