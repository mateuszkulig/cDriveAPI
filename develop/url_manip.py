def combineUrlParams(url:str, params:dict):
    resultUrl = f"{url}?"
    for k in params:
        resultUrl += f"{k}={params[k]}&"
    return resultUrl
