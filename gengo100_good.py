# -*- coding: utf-8 -*-

#1_00
String1 = "stressed"
print String1[::-1]
#desserts

#1_01
String2 = u"パタトクカシーー"
S = String2[0] + String2[2] + String2[4] + String2 [6]
print S
#パトカー

#1_02
a = ""
S1 = u"パトカー"
S2 = u"タクシー"	
S3 = S1 + S2
Rule = [0, 4, 1, 5, 2, 6, 3, 7]
for Pata in Rule:
	a += S3[Pata]
print a

#1_03
aPai_length = []
Pai = r"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
aPai = Pai.split(" ")
#print aPai
for i in aPai:
	if i.find(",") == -1 and i.find(".") == -1:
		aPai_length.append(len(i)) 
	else:	
		aPai_length_normal = len(i)
		aPai_length_normal = aPai_length_normal - i.count(".") - i.count(",") 
		#aPai_length_normal = aPai_length_normal - i.count(",") 
		aPai_length.append(aPai_length_normal) 
		aPai_length_normal = 0
else:
	print aPai_length

#[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
#http://sucrose.hatenablog.com/entry/2014/04/21/000909	

#1_04
a1_04 = r"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
a1_04_Suggest1 = [1, 5, 6, 7, 8, 9, 15, 16, 19]
Num0104_c = []
a1_04_li = []
a1_04_li = a1_04.split(" ")
Num0104_a = len(a1_04_li)
Num0104_a = Num0104_a + 1
Num0104_b = range(1, Num0104_a) 
a1_04_connect = dict(zip(Num0104_b,a1_04_li))
a9 = {}
for key, value in a1_04_connect.iteritems():
	for a8 in a1_04_Suggest1: 
		if key == a8: #一文字だけ抜き出すときの条件
			a9[key] = value[0:1]	
			break #真になった時点で処理を終了させて上書きされないようにする
		else: 
			a9[key] = value[0:2] #何度も同じ内容でアップデートしている
print a9

#{1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mi', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca'}






