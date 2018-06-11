<<<<<<< HEAD
# '''A = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
# bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
# sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
# # print(A)'''
A='map'
B = ''
for i in A:
    if i.isalpha() is True:
        if ord(i) < 121:
            B += (chr(ord(i)+2))
        else:
            B += (chr(ord(i) - 26 + 2))
    else:
        B += i
print(B)


# Second Method

D = "abcdefghijklmnopqrstuvwxyz"
E = "cdefghijklmnopqrstuvwxyzab"
TT = str.maketrans(D, E)
C = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
 sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. '''
print(C.translate(TT))
=======
# '''A = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
# bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
# sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
# # print(A)'''
A='map'
B = ''
for i in A:
    if i.isalpha() is True:
        if ord(i) < 121:
            B += (chr(ord(i)+2))
        else:
            B += (chr(ord(i) - 26 + 2))
    else:
        B += i
print(B)


# Second Method

D = "abcdefghijklmnopqrstuvwxyz"
E = "cdefghijklmnopqrstuvwxyzab"
TT = str.maketrans(D, E)
C = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
 sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. '''
print(C.translate(TT))
>>>>>>> e098262d7bc0c5023aab1e18d9bedf7f221006de
