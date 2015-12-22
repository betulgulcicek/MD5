####################################################################################
#       
#	BIL 470 Kriptografi ve Ag Guvenligi
#	Odev 1
#		Verilen resimler arasinda ayni md5 e sahip olanlari bulma
#
#       BETUL GULCICEK
#       101044025
#
####################################################################################


import hashlib
import Image
import io
import glob


# md5 leri bulan fonksiyon
def Ayni_Ozet_Koda_Sahip_Dosyalari_Bul(fname):
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()



# md5 leri karsilastiran fonksiyon
def compare(item1, item2):
    if item1 == item2:
        return 0
    elif item1 > item2:
        return 1
    else:
        return -1




# md5 ve pathlerin ekrana basilmasi
path_list = []
print '\n\n', "\t\tMD5\t\t\t\t\t\t\t PATH \n\n**************************************************************************************************************\n\n",
for name in glob.glob("/home/betulgulcicek/Desktop/BIL470_101044025_Betul_Gulcicek/Resimler/*.jpg"):
	print Ayni_Ozet_Koda_Sahip_Dosyalari_Bul(fname = name) , '\t\t', name

# pathler path_list e append ediliyor
for name in glob.glob("/home/betulgulcicek/Desktop/BIL470_101044025_Betul_Gulcicek/Resimler/*.jpg"):
    path_list.append(name)


md5_list = []
# md5ler md5_list e append ediliyor
for name in glob.glob("/home/betulgulcicek/Desktop/BIL470_101044025_Betul_Gulcicek/Resimler/*.jpg"):
	md5_list.append(Ayni_Ozet_Koda_Sahip_Dosyalari_Bul(fname = name))
 

# ayni md5 e sahip olan resimler bulunup consola basiliyor
for i in range(len(md5_list)):
    for j in range(i + 1, len(md5_list)):
        if compare(md5_list[i], md5_list[j]) == 0:
            print "\n**************************************************************************************************************\n\n\t\t\tMD5 Degeri Ayni Olan Resimler \n\n", md5_list[i], '\t',path_list[i] , '\n', md5_list[j], '\t', path_list[j], '\n\n'



# end program
