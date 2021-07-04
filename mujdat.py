#mujdat erenler
# Fill in this file with the code from parsing JSON exercise
import json #json import edildi
with open('mujdat.json','r') as json_dosya:#mujdat.json dosyası json_dosya olarak okuma modunda açıldı
    dosya = json.load(json_dosya)#son_dosya yüklenerek dosya değişkenine atandi
#kimlik ={}#kimlik adında bir sözlük oluşturuldu
#print(dosya)
#for key,value in dosya.items(): #dosyadaki tüm anahtar değer çiftleri için
    #print(type(dosya.items())) #dosyadan alınan veri tipi kontrol edildi
#    if key == 'kimlik': # anahtar kimlik ise
#        kimlik={}
#        kimlik.update(value) #kimlik sözlüğü json dosyadaki değerler ile güncellendi

#for i in kimlik: #kimlik adlı sözlükteki çiftler için
#    print(kimlik.get(i))# değerler yazdırıldı
print("kimlik=",dosya["kimlik"])#mujdat.json dosyasından kimlik anahtarı yazdırıldı
