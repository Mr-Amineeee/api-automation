import requests

class APIClient:

    def get(self,url,headers=None):
        return requests.get(
            url,
            headers=headers
    )


    def put(self,url,data,headers=None):
        return requests.put(
            url,
            json=data,
            headers=headers
    )



    def post(self,url,data,headers=None):
        return requests.post(
            url,
            json=data,
            headers=headers
    )


    def delete(self,url,headers=None):
        return requests.delete(
            url,
            headers=headers
    )
    