import requests

url = "http://test.magcore.clawit.com"

class player():

    def __init__(self,url):
        self.url=url
        self.player_id=None
        self.player_index=None
        self.player_bases=None


    #创建新玩家
    def createPlayer(self):
        #玩家输入信息
        username = input('玩家名>>').strip()
        color = int(input('颜色>>').strip())

        url = self.url + '/api/player'
        payload="{\"Name\":%s,\"Color\":%s}"%(username,color)
        headers={
            'Content-Type':'application/json',
            'Cache-Contro':'no-cache'
        }
        response = requests.request("GET",url,data=payload,headers=headers)
        ret_dic = response.text[0]
        #判断是否创建成功
        if ret_dic["State"]==200:
            self.player_id = ret_dic["Id"]
            self.player_index=ret_dic["Index"]
            self.player_bases=ret_dic["Bases"]
            print('创建玩家成功！')
            return 1
        else:
            return 0

    #获取玩家详情
    def getPlayer(self):

        url = self.url + '/api/player/%s' % self.player_id
        headers = {
            'Cache-Contro': 'no-cache'
        }
        response = requests.request("GET", url, headers=headers)
        # print(response)
        return response.text

    #加入游戏
    def joinGame(self,game_obj):
        url = self.url + '/api/game'
        payload ="{\"Game\":%s,\"Player\":%s}"%(game_obj.game_id,self.player_id)
        headers = {
            'Content-type': 'application/json',
            'Cache-Contro': 'no-cache'
        }
        response = requests.request("PATCH", url, data=payload, headers=headers)
        print(response)  # <Response [200]>
        return response.text


    #开始游戏
    def startGame(self,game_obj):
        url = self.url + '/api/game/%s'%game_obj.game_id
        headers = {
            'Cache-Contro': 'no-cache'
        }
        response = requests.request("PUT",url,headers=headers)
        print(response)
        return response.text



class game():
    def __init__(self,url):
        self.url=url
        self.game_lst=None
        self.game_id=None
    #创建游戏  返回游戏列表
    def createGame(self):
        map = input("地图类型>>").strip()
        url = self.url + '/api/game'
        payload ="{\"Map\":%s}"%map
        headers = {
            "Content-Type":"application/json",
            "Cache-Control":"no-cache"
        }
        response = requests.request('GET',url,data=payload,headers=headers)
        # print(response)
        if response.status_code == 200:
            self.geme_lst = response.text
            return 1
        else:
            return 0

    #  [{"id":"23c7b9c92ee94d1c87af26a5c570cf52","map":"RectSmall","state":0}]

    #获取游戏列表
    def gameList(self):

        url = self.url + '/api/game'
        headers = {
            "Content-Type": "application/json",
            "Cache-Contro": "no-cache"
        }
        response = requests.request("GET", url, headers=headers)

        if response.status_code == 200:
            self.geme_lst = response.text
            return 1
        else:
            return 0

    # print(gameList(url))

    #获取游戏详情
    def getGame(self):
        url = self.url + '/api/game/%s' % self.game_id
        headers = {
            'Cache-Contro': 'no-cache'
        }
        response = requests.request("GET",url,headers=headers)
        # print(response)
        return response.text


    #获取地图信息
    def getMap(self,map_name):
        url = self.url + '/api/map/%s' % map_name
        headers = {
            'Cache-Contro': 'no-cache'
        }
        response = requests.request("GET", url, headers=headers)
        # print(response)
        return response.text









