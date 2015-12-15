from django.shortcuts import render

# Create your views here.
def konversi(bil):
	bil &= (2 << 31)-1
	formatStr = '{:0'+str(32)+'b}'
	ret = formatStr.format(int(bil))
	return ret