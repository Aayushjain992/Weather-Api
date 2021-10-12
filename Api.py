import json
import requests
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Temperature"]
mycol = mydb["mumbai"]
my = mydb["indore"]
my1 = mydb["delhi"]

#mumbai
complete_api_link ='http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=b2ee53cbfd294ff3a92172115210710&q=Mumbai&date=2021-10-07&enddate=2021-10-07&tp=24&format=json'
api_link = requests.get(complete_api_link)
api_data = api_link.json()
m=api_data['data']['weather'][0]['date']
m1=api_data['data']['weather'][0]['mintempC']
m2=api_data['data']['weather'][0]['maxtempC']

complete_api_link ='http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=b2ee53cbfd294ff3a92172115210710&q=Mumbai&date=2021-10-08&enddate=2021-10-08&tp=24&format=json'
api_link = requests.get(complete_api_link)
api_data1= api_link.json()
mu=api_data1['data']['weather'][0]['date']
mu1=api_data1['data']['weather'][0]['mintempC']
mu2=api_data1['data']['weather'][0]['maxtempC']

complete_api_link ='http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=b2ee53cbfd294ff3a92172115210710&q=Mumbai&date=2021-10-09&enddate=2021-10-09&tp=24&format=json'
api_link = requests.get(complete_api_link)
api_data1= api_link.json()
mum=api_data1['data']['weather'][0]['date']
mum1=api_data1['data']['weather'][0]['mintempC']
mum2=api_data1['data']['weather'][0]['maxtempC']

#delhi
complete_api_link ='http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=b2ee53cbfd294ff3a92172115210710&q=Delhi&date=2021-10-07&enddate=2021-10-07&tp=24&format=json'
api_link = requests.get(complete_api_link)
api_data = api_link.json()
d=api_data['data']['weather'][0]['date']
d1=api_data['data']['weather'][0]['mintempC']
d2=api_data['data']['weather'][0]['maxtempC']

complete_api_link ='http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=b2ee53cbfd294ff3a92172115210710&q=Delhi&date=2021-10-08&enddate=2021-10-08&tp=24&format=json'
api_link = requests.get(complete_api_link)
api_data1= api_link.json()
de=api_data1['data']['weather'][0]['date']
de1=api_data1['data']['weather'][0]['mintempC']
de2=api_data1['data']['weather'][0]['maxtempC']

complete_api_link ='http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=b2ee53cbfd294ff3a92172115210710&q=Delhi&date=2021-10-09&enddate=2021-10-09&tp=24&format=json'
api_link = requests.get(complete_api_link)
api_data1= api_link.json()
delh=api_data1['data']['weather'][0]['date']
delh1=api_data1['data']['weather'][0]['mintempC']
delh2=api_data1['data']['weather'][0]['maxtempC']


#indore
complete_api_link ='http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=b2ee53cbfd294ff3a92172115210710&q=Indore&date=2021-10-07&enddate=2021-10-07&tp=24&format=json'
api_link = requests.get(complete_api_link)
api_data = api_link.json()
i=api_data['data']['weather'][0]['date']
i1=api_data['data']['weather'][0]['mintempC']
i2=api_data['data']['weather'][0]['maxtempC']

complete_api_link ='http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=b2ee53cbfd294ff3a92172115210710&q=Indore&date=2021-10-08&enddate=2021-10-08&tp=24&format=json'
api_link = requests.get(complete_api_link)
api_data1= api_link.json()
ind=api_data1['data']['weather'][0]['date']
ind1=api_data1['data']['weather'][0]['mintempC']
ind2=api_data1['data']['weather'][0]['maxtempC']

complete_api_link ='http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=b2ee53cbfd294ff3a92172115210710&q=Indore&date=2021-10-09&enddate=2021-10-09&tp=24&format=json'
api_link = requests.get(complete_api_link)
api_data1= api_link.json()
indo=api_data1['data']['weather'][0]['date']
indo1=api_data1['data']['weather'][0]['mintempC']
indo2=api_data1['data']['weather'][0]['maxtempC']





mydict = {"id":"1" ,"date": m, "mintemp": m1 , "maxtemp": m2 }
mydict1 = {"id":"2" ,"date": mu, "mintemp": mu1 , "maxtemp": mu2 }
mydict2= {"id":"3" ,"date": mum, "mintemp": mum1 , "maxtemp": mum2 }

mydictd = {"id":"1" ,"date": d, "mintemp": d1 , "maxtemp": d2 }
mydictd1 = {"id":"2" ,"date": de, "mintemp": de1 , "maxtemp": de2 }
mydictd2= {"id":"3" ,"date": delh, "mintemp": delh1 , "maxtemp": delh2 }

mydicti = {"id":"1" ,"date": i, "mintemp": i1 , "maxtemp": i2 }
mydicti1 = {"id":"2" ,"date": ind, "mintemp": ind1 , "maxtemp": ind2 }
mydicti2= {"id":"3" ,"date": indo, "mintemp": indo1 , "maxtemp": indo2 }
print("hi")



# x = mycol.insert_one(mydict)
# y = mycol.insert_one(mydict1)
# z = mycol.insert_one(mydict2)

# x1 = my1.insert_one(mydictd)
# y1 = my1.insert_one(mydictd1)
# z1 = my1.insert_one(mydictd2)


# x2 = my.insert_one(mydicti)
# y2 = my.insert_one(mydicti1)
# z2 = my.insert_one(mydicti2)



