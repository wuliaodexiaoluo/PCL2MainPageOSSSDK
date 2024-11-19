import requests
import json
import pathlib
import hashlib

# 响应状态码
http_ok = range(200,300)   

#基本请求头
def _BaseHeader():
    return {
    "User-Agent":"PCL2PlazaAlistSDK/0.0.2",
    "Accept":"application/json",
    "Content-Type":"application/json;charset=utf-8",
    "X-Project-Url":"https://github.com/wuliaodexiaoluo/PCL2MainPageOSSSDK"
    }

# 并发请求
async def multirequest(methods,uris,headers,data,max=16):
    tasks = []
    result = []
    sem = asyncio.Semaphore(max)
    for x in range(len(data)):
        task = request(method=methods[x],data=[x],uri=uri,header=headers[x])
        tasks.append(task)
    async with sem:
        result.append(await asyncio.gather(*tasks))
    return result

async def request(method:str,uri:str,header,data=None):
    match method.lower():
        case "get":
            return requests.get(url=uri,headers=headers)
        case "head":
            return requests.head(url=uri,headers=headers)
        case "post":
            if not data is None:
                return requests.post(url=uri,data=data,headers=headers)
            else:
                raise KeyError("请求数据无效")
        case "put":
            if not data is None:
                return requests.put(url=uri,data=data,headers=header)
            else:
                raise KeyError("请求数据无效")
        case "delete":
            return requests.delete(url=uri,headers=header)

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

    response = await asyncio.run(request(method="POST",uri=BaseUri+"/api/auth/login/hash",header=h,data=json.dumps(data)))
    if response.status_code in http_ok:
        apitoken = json.loads(response.content)
        apitoken = apitoken["data"]["token"]
        return apitoken,response
    else:
        return None,response

async def fsmkdir(dir,accessToken,BaseUri):
    h = _BaseHeader()
    h["Authorization"] = accessToken
    postdata = {
    "path":dir
    }
    response = await asyncio.run(request(method="POST",uri=BaseUri+"/api/fs/mkdir",data=json.dumps(postdata),header=h))
    if response.status_code in http_ok:
        return True,response
    else:
        return False,response

async def fsrename(newname,path:list,accessToken,BaseUri):
    h = _BaseHeader()
    h["Authorization"] = accessToken
    postdata = {
        "name":newname,
        "path":path
        }
    response = request(url=BaseUri+"/api/fs/rename",headers=h,data=json.dumps(postdata))
    if response.status_code in http_ok:
        return True,response
    else:
        return False,response

async def fsfrom(filepath:list,accessToken,BaseUri):
        h = _BaseHeader()
        putdatas = []
        h["Authorization"] = accessToken
        h["Content-Type"] = "multipart/form-data;charset=utf-8"
        putdata = {}
        for file in path:
            with open(file,"rb",encoding="utf-8") as f:
                data = f.read()
                filesize = len(data)
                putdata["file"] = data
                putdatas.append(putdata)
        uris = ["{BaseUri}/api/fs/from"]
        result = await asyncio.run(multirequest(uris=uris))
