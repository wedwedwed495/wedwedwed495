try:
 import http.client
 import json
 import time
 import urllib.request

 headers = None

 def get2(url, ggg, slach, to__do, headers2):
    if to__do == 'headers.self':
        try:
            global g
            g = http.client.HTTPConnection(url, headers2)
            try:
           
                g.connect()
            
                g.request(ggg, slach)
                global gggg
                gggg = g.getresponse()
            except:
            
                g.request(ggg, slach)
            
                gggg = g.getresponse()
        except:
        
            g = http.client.HTTPSConnection(url, headers2)
            try:
            
                g.connect()
            
                g.request(ggg, slach)
            
                gggg = g.getresponse()
            except:
            
                g.request(ggg, slach)
            
                gggg = g.getresponse()
        global f
        headerss = gggg.headers
        print(headerss)
    if to__do == 'headers.self_pro':
        try:
            g = http.client.HTTPConnection(url)
            try:
           
                g.connect()
            
                g.request(ggg, slach, headers2)
                gggg = g.getresponse()
            except:
            
                g.request(ggg, slach, headers2)
            
                gggg = g.getresponse()
        except:
        
            g = http.client.HTTPSConnection(url)
            try:
            
                g.connect()
            
                g.request(ggg, slach, headers2)
            
                gggg = g.getresponse()
            except:
            
                g.request(ggg, slach, headers2)
            
                gggg = g.getresponse()
        headerss = gggg.headers
        print(headerss)
  def get(url, ggg, slach, to__do):
    try:
        global g
        g = http.client.HTTPConnection(url)
        try:
           
            g.connect()
            
            g.request(ggg, slach)
            global gggg
            gggg = g.getresponse()
        except:
            
            g.request(ggg, slach)
            
            gggg = g.getresponse()
    except:
        
        g = http.client.HTTPSConnection(url)
        try:
            
            g.connect()
            
            g.request(ggg, slach)
            
            gggg = g.getresponse()
        except:
            
            g.request(ggg, slach)
            
            gggg = g.getresponse()
    global f
    if to__do == ".txt/decode":
        
        if gggg:
            
            f = gggg.read()
            f = f.decode()
            print(f)
    elif to__do == ".txt":
        if gggg:
            
            f = gggg.read()
            print(f)
    elif to__do == ".json/decode":
        
        if gggg:
         data = gggg.read()
         data2 = data.decode()
         print(json.loads(data2))  
    elif to__do == ".json":
        
        if gggg:
         data = gggg.read()
         print(json.loads(data2))
    elif to__do == ".status":
        if gggg:
            data = gggg.status
            print(data)
    elif to__do == ".reason":
        if gggg:
            data = gggg.reason
            print(data)  
    elif to__do == ".save.jpg":
        if gggg:
             def download_image(url, save_as):
                 urllib.request.urlretrieve(url, save_as)
                 print(urllib.request.urlretrieve(url, save_as))
             uwehfuiwhefui = url, slach
             image_url = uwehfuiwhefui
             save_as = 'image.jpg'

             download_image(image_url, save_as)
    elif to__do == ".save.pkg":   
        if gggg:
             def download_image(url, save_as):
                 urllib.request.urlretrieve(url, save_as)
                 print(urllib.request.urlretrieve(url, save_as))
             uwehfuiwhefui =url, slach
             image_url = uwehfuiwhefui
             save_as = 'image.pkg'

             download_image(image_url, save_as)
    elif to__do == ".html":
        uwehfuiwhefui = url, slach
        with urllib.request.urlopen(uwehfuiwhefui) as response:
           
           html = response.read()
           html2 = html.decode()
           print(html2)
        
    elif to__do == ".headers":
        hgghh = gggg.headers
        print(hgghh)


 to_do = ".save.pkg"
 get('http://python.org', 'GET', "/ftp/python/3.13.2/python-3.13.2-macos11.pkg", to_do)
except:
 print("error")
