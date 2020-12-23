from model.proxyModel import ProxyModel
import urllib.request
import socket
import urllib.error

class ProxyChecker:
    def __init__(self, proxies: list) -> None:        
        self.proxies=proxies              

    def check(self):
        checked_proxies=list()
        socket.setdefaulttimeout(120)               
        for index, currentProxy in enumerate(self.proxies):
            print(f"checking: {self.proxies[index]}")
            _ = currentProxy.get("proxy").split("://")
            proxy = _[1]
            uri = _[0]
            if not ProxyChecker.is_bad_proxy(uri, proxy):                
                print(f"worked proxy: {proxy}")
                checked_proxies.append(self.proxies[index])
        return checked_proxies

            
    @staticmethod
    def is_bad_proxy(uri, proxy):
        try:
            proxy_handler = urllib.request.ProxyHandler({uri: proxy})
            opener = urllib.request.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            req=urllib.request.Request('https://www.google.com')
            req1=urllib.request.Request('https://www.facebook.com')
            req2=urllib.request.Request('https://script.google.com/macros/s/AKfycby9S1Vx3ipI0DhQvZU5hJXOLyFpKErT9NPZwIUEI0RgssJVyV8/exec')
            sock=urllib.request.urlopen(req)
            sock=urllib.request.urlopen(req1)
            sock=urllib.request.urlopen(req2)
        except urllib.error.HTTPError as e:
            print('Error code: ', e.code)
            return e.code
        except Exception as detail:
            print("ERROR:", detail)
            return True
        return False


if __name__ == "__main__":
    pm = ProxyModel("proxy_pool")   
    data =list(pm.get_all_data())    
    pc = ProxyModel("proxy_checked")
    data1=list(pc.get_all_data())   
    pc.drop_collection()    
    data = data + data1   
    print(data)
    checked_list = ProxyChecker(proxies=data).check()    
    pc = ProxyModel("proxy_checked").insert(checked_list)
    pm.drop_collection()



