try:
    import requests
    import json
    import pathlib
    import hashlib
    
    def _BaseHeader():
        return {
            "User-Agent":"PCL2PlazaAlistSDK/0.0.1",
            "Accept":"application/json",
            "Content-Type":"application/json"
        }
    
    async def login(username,password,BaseUri):
        
        h = _BaseHeader()
    
        sha256_hash = hashlib.sha256()
    
        input_bytes = password.encode('utf-8') + "-https://github.com/alist-org/alist"
    

        sha256_hash.update(input_bytes)
    

        hashpass = sha256_hash.hexdigest()
    

        data = {
            "username":username,
            "password":hashpass
        }

        response = requests.post(BaseUri+"/api/auth/login/hash",headers=h,data=data)
        if 200 <= response.status_code <=299:
            apitoken = json.loads(response.content)
            apitoken = apitoken["data"]["token"]
            return apitoken
        else:
            return False
        
    async def fsmkdir(dir,accessToken,BaseUri):
        h = _BaseHeader()
        h["Authorization"] = accessToken
        postdata = {
            "path":dir
        }
        response = requests.post(url=BaseUri+"/api/fs/mkdir",data=json.dumps(postdata),headers=h)
        return response
    async def fsrename(newname,path,accessToken,BaseUri):
        h = _BaseHeader()
        h["Authorization"] = accessToken
        postdata = {
            "name":newname,
            "path":path
        }
        response = requests.post(url=BaseUri+"/api/fs/rename",headers=h,data=json.dumps(postdata))
        return response
    async def fsfrom(filepath:list,accessToken,BaseUri):
        h = _BaseHeader()
        h["Auth"]

except KeyError as e:
    exit(1)
except Exception as e:
    exit(1)