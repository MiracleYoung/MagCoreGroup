import requests


#创建新玩家，返回玩家类，包含ID、Name、Color、State、Index等
def CreatPlayer(name,color):
    url = "http://test.magcore.clawit.com/api/player"
    payload = "{\"Name\":\"%s\",\"Color\":%d}" % (name,color)
    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:#若name已存在，会返回409，即创建玩家失败
        print("创建玩家失败！")
        return None

#根据id获取玩家信息
def GetPlayer(id):
    url = "http://test.magcore.clawit.com/api/player/" + id
    headers = {
        'Cache-Control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("获取玩家信息失败！")
        return None

#跟据游戏名称创建游戏，返回游戏ID
def CreateGame(name):
    url = "http://test.magcore.clawit.com/api/game"
    payload = "{\"Map\":\"%s\"}" % name
    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("创建游戏失败！")
        return None

#获取游戏列表,返回所有游戏的数组
def GetGameList():
    url = "http://test.magcore.clawit.com/api/game"
    headers = {
        'Cache-Control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("获取游戏列表失败！")
        return None

#加入游戏，需要输入游戏id和玩家id
def JoinGame(gameID,playerID):
    url = "http://test.magcore.clawit.com/api/game/"
    payload = "{\"Game\":\"%s\",\"Player\":\"%s\"}" % (gameID,playerID)
    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
    }
    response = requests.request("PATCH", url, data=payload, headers=headers)
    if response.status_code == 200:
        return True
    else:
        print("加入游戏失败！")
        return False

#根据游戏id开始游戏
def StartGame(gameID):
    url = "http://test.magcore.clawit.com/api/game/" + gameID
    headers = {
        'Cache-Control': "no-cache"
    }
    response = requests.request("PUT", url, headers=headers)
    if response.status_code == 200:
        return True
    else:
        print("开始游戏失败！")
        return False

#根据ID获取游戏信息
def GetGame(id):
    url = "http://test.magcore.clawit.com/api/game/" + id
    headers = {
        'Cache-Control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("获取游戏详情失败！")
        return None

#根据名称获取地图信息
def GetMap(name):
    url = "http://test.magcore.clawit.com/api/map/" + name
    headers = {
        'Cache-Control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("获取地图信息失败！")
        return None

if __name__ == '__main__':
    # playerID = "a9109d9f70c943688178569441f003cb"
    # gameID = "'f99403ddf493435ab4e8c2382f132fd2'"
    gameID = CreateGame("RectSmall")
    gameList = GetGameList()
    player = CreatPlayer("101",2)
    # player1 = GetPlayer(player["Id"])
    # gameID = input("请输入游戏ID：")
    # game = GetGame(gameID)
    # MapName = input("请输入地图名称（rectsmall、rectMid、rectBig）：")
    # Map = GetMap(MapName)
    # JoinGame(gameID,player["Id"])
    # StartGame(gameID)
    I = "wjhui135"