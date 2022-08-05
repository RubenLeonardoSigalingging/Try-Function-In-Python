#!/usr/bin/env python3


# Try Function


try:
	print(VarX)
except:
	print("Terjadi Pengecualian")
	print("An Exception Occurred")


# 2
try:
	print(VarX)
except NameError:
	print("Variable X Is Not Defined",end=" ~> ")
	print("Variabel X Tidak Didefinisikan")
except:
	print("Something else went wrong!")
	print("Ada yang salah!")


# 3
try:
	print("\n")
	print("Halo Friend!")
except:
	print("Something Went Wrong!",end=" ~> ")
	print("Ada Yang Salah!")
else:
	print("Nothing Went Wrong!",end=" ~> ")
	print("Tidak Ada yang Salah!")
finally:
	print("The 'Try Except' Is Finished!",end=" ~> ")
	print("'Coba Kecuali' Selesai!")


# 4. Contoh dengan membuka, menulis dan menutup sebuah file.
try:
	File=open("Leonardo.txt","w")
	try:
		Message_Box=str(input("Input A Message Box: "))
		File.write(Message_Box)
	except:
		print("Something Went Wrong, When Writing To The File!")
		print("Ada yang Salah, Saat Menulis ke File!")
	else:
		File=open("Leonardo.txt","r")
		print("\n")
		print(f"Result From Writing The File Is: {File.read()}")
	finally:
		File.close()
except:
	print("Something Went Wrong When Opening The File!")