import requests, json
from requests.auth import HTTPBasicAuth

def create_record(folder,data,USER,API_KEY):
    URL='https://nethunt.com/api/v1/zapier/actions/create-record/'+folder
    y=requests.post(URL, json=data,auth=HTTPBasicAuth(USER, API_KEY))
    print(y.request.body)
    print(y.request.headers)
    print(y.json)

def list_folders(USER,API_KEY):
    URL='https://nethunt.com/api/v1/zapier/triggers/readable-folder'
    y=requests.get(URL, auth=HTTPBasicAuth(USER, API_KEY))
    print(y.request.headers)
    print(y.json)
    y=json.dumps(y.text)
    print(y)

def list_permission_folders(USER,API_KEY):
    URL='https://nethunt.com/api/v1/zapier/triggers/writable-folder'
    y=requests.get(URL, auth=HTTPBasicAuth(USER, API_KEY))
    print(y.request.headers)
    print(y.json)
    y=json.dumps(y.text)
    print(y)

def query_search(folder,USER,API_KEY,query,field,limit):
    limit=str(limit)
    URL='https://nethunt.com/api/v1/zapier/searches/find-record/'+folder+'?query='+field+'%3A'+query+'&limit='+limit
    y=requests.get(URL, auth=HTTPBasicAuth(USER, API_KEY))
    print(y.request.headers)
    print(y.json)
    y=json.dumps(y.text)
    print(y)

def recent_records(folder,USER,API_KEY,YYYY_MM_DD,limit):
    limit=str(limit)
    date=YYYY_MM_DD.replace("_","-")
    URL='https://nethunt.com/api/v1/zapier/triggers/new-record/'+folder+'?since='+date+'T00%3A00%3A00.000Z&limit='+limit
    y=requests.get(URL, auth=HTTPBasicAuth(USER, API_KEY))
    print(y.request.headers)
    print(y.json)
    y=json.dumps(y.text)
    print(y)

def recent_comments(folder,USER,API_KEY,YYYY_MM_DD,limit):
    limit=str(limit)
    date=YYYY_MM_DD.replace("_","-")
    URL='https://nethunt.com/api/v1/zapier/triggers/new-comment/'+folder+'?since='+date+'T00%3A00%3A00.000Z&limit='+limit
    y=requests.get(URL, auth=HTTPBasicAuth(USER, API_KEY))
    print(y.request.headers)
    print(y.json)
    y=json.dumps(y.text)
    print(y)

def recently_updated(folder,USER,API_KEY,fields,YYYY_MM_DD,limit):
    limit=str(limit)
    date=YYYY_MM_DD.replace("_","-")
    all_fields=''
    for item in fields:
        item=item.replace(" ","%20")
        all_fields+='fieldName='+item+'&'
    URL='https://nethunt.com/api/v1/zapier/triggers/updated-record/'+folder+'?'+all_fields+'since='+date+'T00%3A00%3A00.000Z&limit='+limit
    y=requests.get(URL, auth=HTTPBasicAuth(USER, API_KEY))
    print(y.request.headers)
    print(y.json)
    y=json.dumps(y.text)
    print(y)

def recent_changes_in_record(folder,USER,API_KEY,fields,YYYY_MM_DD,limit):
    limit=str(limit)
    date=YYYY_MM_DD.replace("_","-")
    all_fields=''
    for item in fields:
        item=item.replace(" ","%20")
        all_fields+='fieldName='+item+'&'
    URL='https://nethunt.com/api/v1/zapier/triggers/updated-record/'+folder+'?'+all_fields+'since='+date+'T00%3A00%3A00.000Z&limit='+limit
    y=requests.get(URL, auth=HTTPBasicAuth(USER, API_KEY))
    print(y.request.headers)
    print(y.json)
    y=json.dumps(y.text)
    print(y)

def recent_call_logs(folder,USER,API_KEY,YYYY_MM_DD,limit):
    limit=str(limit)
    date=YYYY_MM_DD.replace("_","-")
    URL='https://nethunt.com/api/v1/zapier/triggers/new-call-log/'+folder+'?since='+date+'T00%3A00%3A00.000Z&limit='+limit
    y=requests.get(URL, auth=HTTPBasicAuth(USER, API_KEY))
    print(y.request.headers)
    print(y.json)
    y=json.dumps(y.text)
    print(y)

def recent_drive_files(folder,USER,API_KEY,YYYY_MM_DD,limit):
    limit=str(limit)
    date=YYYY_MM_DD.replace("_","-")
    URL='https://nethunt.com/api/v1/zapier/triggers/new-gdrivefile/'+folder+'?since='+date+'T00%3A00%3A00.000Z&limit='+limit
    y=requests.get(URL, auth=HTTPBasicAuth(USER, API_KEY))
    print(y.request.headers)
    print(y.json)
    y=json.dumps(y.text)
    print(y)

def list_fields(folder,USER,API_KEY):
    URL='https://nethunt.com/api/v1/zapier/triggers/folder-field/'+folder
    y=requests.get(URL, auth=HTTPBasicAuth(USER, API_KEY))
    print(y.request.headers)
    print(y.json)
    y=json.dumps(y.text)
    print(y)
