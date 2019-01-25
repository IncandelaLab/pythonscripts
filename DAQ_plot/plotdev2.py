import os
import numpy
import matplotlib.pyplot as plt
import math

PLOTFUNCS = [plt.plot, plt.semilogx, plt.semilogy, plt.loglog]

def cg_perm(C):
	"""Iterator for generating colors from permutations of RGB values"""
	indicies = [0,0,0]
	done = False
	while not done:
		yield [C[0][indicies[0]]/256., C[1][indicies[1]]/256., C[2][indicies[2]]/256.]
		indicies[0] += 1
		if indicies[0] >= len(C[0]):
			indicies[0]=0
			indicies[1] += 1
		if indicies[1] >= len(C[1]):
			indicies[1]=0
			indicies[2] += 1
		if indicies[2] >= len(C[2]):
			done=True
	return

def cg_list(L,rep=True):
	"""Iterator for generating colors from a simple list of colors"""
	done=False
	i=0
	while not done:
		if i >= len(L):
			if rep:
				i = 0
			else:
				return
		yield L[i]
		i+=1

CJ = [[0,1,0],[0,0,1],[0.8,0,0.8]]

CBLACK = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
CRED   = [[1,0,0],[1,0,0],[1,0,0],[1,0,0]]
CGREEN = [[0,1,0],[0,1,0],[0,1,0],[0,1,0]]
CBLUE  = [[0,0,1],[0,0,1],[0,0,1],[0,0,1]]
CM     = [[0.8,0,0.8],[0.8,0,0.8],[0.8,0,0.8]]
CC     = [[0.4,0.7,1],[0.4,0.7,1],[0.4,0.7,1]]
COLS_2 = [[0.9,0,0],[0,0,0.9]]
COLS_4 = [[0.85,0,0],[0,0.85,0],[0,0,0.85],[0,0,0]]
COLS_8 = [[0,192],[0,192],[0,192]]
COLS_12 = [[0,129],[0,100,200],[0,192]]
C_G27  = [[0,100,200],[0,100,200],[0,100,200]]
C_G18  = [[0,128,256],[0,100,200],[0,255]]




CWD    = os.getcwd()
FOLDERS  = 'trial{}'
PFOLDERS = 'RUN_{}_plots'

FILE   = 'rms_summary_sca_1.txt'

RUNS_T0 = {
	"131118_1346":"cable floating",
	"131118_1354":"generator off",
	"131118_1359":"generator output off",

	"131118_1401":"1Hz 250mV",
	"131118_1402":"3Hz 250mV",
	"131118_1407":"10Hz 250mV",
	"131118_1410":"30Hz 250mV",
	"131118_1413":"60Hz 250mV",
	"131118_1415":"100Hz 250mV",
	"131118_1418":"120Hz 250mV",
	"131118_1424":"300Hz 250mV",
	"131118_1427":"1KHz 250mV",
	"131118_1432":"3KHz 250mV",
	"131118_1436":"10KHz 250mV",
	"131118_1439":"30KHz 250mV",
	"131118_1440":"100KHz 250mV",
	"131118_1442":"300KHz 250mV",
	"131118_1445":"600KHz 250mV",
	"131118_1446":"1MHz 250mV",
	"131118_1448":"2MHz 250mV",
	"131118_1453":"2mV 1MHz",
	"131118_1455":"4mV 1MHz",
	"131118_1457":"8mV 1MHz",
	"131118_1458":"16mV 1MHz",
	"131118_1500":"32mV 1MHz",
	"131118_1502":"64mV 1MHz",
	"131118_1504":"128mV 1MHz",
	"131118_1505":"250mV 1MHz",
	"131118_1512":"2mV 1KHz",
	"131118_1514":"4mV 1KHz",
	"131118_1517":"8mV 1KHz",
	"131118_1519":"16mV 1KHz",
	"131118_1522":"32mV 1KHz",
	"131118_1524":"64mV 1KHz",
	"131118_1525":"128mV 1KHz",
	"131118_1527":"250mV 1KHz",


	"141118_1101":"generator output off",

	"141118_1104":"3MHz 250mV",
	"141118_1106":"5MHz 250mV",
	"141118_1107":"8MHz 250mV",
	"141118_1109":"13MHz 250mV",
	"141118_1113":"20MHz 250mV",
	"141118_1114":"32MHz 250mV",
	"141118_1116":"50MHz 250mV",
	"141118_1117":"80MHz 250mV",
	"141118_1424":"600KHz consistency test",
	"141118_1428":"1MHz consistency test",
	"141118_1430":"2MHz consistency test",
	"141118_1433":"3MHz consistency test",
	"141118_1436":"5MHz consistency test",
	"141118_1536":"100KHz consistency test",
	"141118_1538":"300KHz consistency test",

}

RUNS_T11 = {
	"171218_1048":"V2 PCB1",# - 171218_1048",
	"171218_1045":"V2 PCB2",# - 171218_1045",
	"171218_1028":"V2 PCB3",# - 171218_1028",
	"171218_1051":"V2 PCB4",# - 171218_1051",
	"171218_1054":"V2 PCB5",# - 171218_1054",
	"171218_1042":"V2 PCB6",# - 171218_1042",
	"181218_1658":"V1 PCB1",# - 181218_1658",
	"181218_1653":"V1 PCB3",# - 181218_1653",
	"181218_1643":"V1 PCB4",# - 181218_1643",
	"181218_1648":"V1 PCB5",# - 181218_1648",
	"181218_1638":"V1 PCB6",# - 181218_1638",
}

RUNS_T12 = {
	"160119_1506":"interposer",
	"160119_1623":"no interposer", # all runs below this are without interposer

	"170119_1107":"generator disconnected", # below runs are no HPF, 250mV noise
	"170119_1112":"generator off",          #
	"170119_1114":"generator output off",   #
	"170119_1117":"1Hz",                    #
	"170119_1119":"10Hz",                   #
	"170119_1121":"100Hz",                  #
	"170119_1122":"1kHz",                   #
	"170119_1124":"10kHz",                  #
	"170119_1126":"100kHz",                 #
	"170119_1128":"1MHz",                   #
	"170119_1129":"10MHz",                  #

	"170119_1555":"generator disconnected", # below runs are 159.2Hz HPF, 250mV noise
	"170119_1557":"generator off",          #
	"170119_1559":"generator output off",   #
	"170119_1601":"1Hz",                    #
	"170119_1604":"10Hz",                   #
	"170119_1607":"100Hz",                  #
	"170119_1611":"1kHz",                   #
	"170119_1613":"10kHz",                  #
	"170119_1615":"100kHz",                 #
	"170119_1616":"1MHz",                   #
	"170119_1618":"10MHz",                  #

	"180119_1021":"No f’n gen cxn",      # 5kHz BNC in-line HPF
	"180119_1026":"F’n gen off",         # set 1
	"180119_1028":"F’n gen output off",  #
	"180119_1035":"1Hz",                 #
	"180119_1037":"10Hz",                #
	"180119_1039":"100Hz",               #
	"180119_1041":"1kHz",                #
	"180119_1043":"10kHz",               #
	"180119_1045":"1MHz",                #
	"180119_1047":"10MHz",               #

	"180119_1023":"No f’n gen cxn",      # set 2
	"180119_1027":"F’n gen off",         #
	"180119_1034":"F’n gen output off",  #
	"180119_1036":"1Hz",                 #
	"180119_1038":"10Hz",                #
	"180119_1040":"100Hz",               #
	"180119_1042":"1kHz",                #
	"180119_1044":"10kHz",               #
	"180119_1046":"1MHz",                #
	"180119_1048":"10MHz",               #
}

RUNS_T13 = {
	"180119_1216":"Function generator not connected; Alligator GND lead floating",
	"180119_1217":"Function generator not connected; Alligator GND lead floating",

	"180119_1219":"F'n gen off",        # No filter
	"180119_1220":"F'n gen off",        #
	"180119_1221":"F'n gen output off", #
	"180119_1222":"F'n gen output off", #
	"180119_1223":"1Hz",                # 250mV noise
	"180119_1224":"1Hz",                #
	"180119_1225":"100Hz",              #
	"180119_1226":"100Hz",              #
	"180119_1227":"10kHz",              #
	"180119_1228":"10kHz",              #
	"180119_1229":"33kHz",              #
	"180119_1230":"33kHz",              #
	"180119_1231":"100kHz",             #
	"180119_1232":"100kHz",             #
	"180119_1234":"330kHz",             #
	"180119_1235":"330kHz",             #
	"180119_1236":"1MHz",               #
	"180119_1237":"1MHz",               #
	"180119_1238":"3.3MHz",             #
	"180119_1239":"3.3MHz",             #
	"180119_1240":"10MHz",              #
	"180119_1241":"10MHz",              #
	"180119_1242":"20MHz",              #
	"180119_1243":"20MHz",              #

	"180119_1245":"F'n gen off",        # 5kHz BNC HPF
	"180119_1246":"F'n gen off",        #
	"180119_1247":"F'n gen output off", #
	"180119_1248":"F'n gen output off", #
	"180119_1249":"1Hz",                # 250mV noise
	"180119_1250":"1Hz",                #
	"180119_1251":"100Hz",              #
	"180119_1252":"100Hz",              #
	"180119_1253":"10kHz",              #
	"180119_1254":"10kHz",              #
	"180119_1255":"33kHz",              #
	"180119_1256":"33kHz",              #
	"180119_1257":"100kHz",             #
	"180119_1258":"100kHz",             #
	"180119_1259":"330kHz",             #
	"180119_1300":"330kHz",             #
	"180119_1301":"1MHz",               #
	"180119_1302":"1MHz",               #
	"180119_1303":"3.3MHz",             #
	"180119_1304":"3.3MHz",             #
	"180119_1305":"10MHz",              #
	"180119_1306":"10MHz",              #
	"180119_1307":"20MHz",              #
	"180119_1308":"20MHz",              #

	"180119_1346":"F'n gen off",        # 159.2 Hz RC breadboard HPF
	"180119_1347":"F'n gen off",        #
	"180119_1348":"F'n gen output off", #
	"180119_1349":"F'n gen output off", #
	"180119_1350":"1Hz",                # 250mV noise
	"180119_1351":"1Hz",                #
	"180119_1352":"100Hz",              #
	"180119_1353":"100Hz",              #
	"180119_1354":"10kHz",              #
	"180119_1355":"10kHz",              #
	"180119_1356":"33kHz",              #
	"180119_1357":"33kHz",              #
	"180119_1358":"100kHz",             #
	"180119_1359":"100kHz",             #
	"180119_1400":"330kHz",             #
	"180119_1401":"330kHz",             #
	"180119_1402":"1MHz",               #
	"180119_1403":"1MHz",               #
	"180119_1404":"3.3MHz",             #
	"180119_1405":"3.3MHz",             #
	"180119_1406":"10MHz",              #
	"180119_1407":"10MHz",              #
	"180119_1408":"20MHz",              #
	"180119_1409":"20MHz",              #
}

RUNS_T14 = {
	"161117_1016":"6-inch v3_20",
	"161117_1014":"6-inch v3_32",
	"161117_1011":"6-inch v3_33",
	"161117_1008":"6-inch v3_34",
	"161117_1005":"6-inch v3_35",
	"161117_1003":"6-inch v3_36",
	"161117_1001":"6-inch v3_37",
	"161117_0958":"6-inch v3_38",
	"161117_0955":"6-inch v3_40",
	"161117_0952":"6-inch v3_43",
	"161117_0945":"6-inch v3_44",
	"161117_0947":"6-inch v3_46",
	"161117_0949":"6-inch v3_48",
	"161117_0156":"6-inch v3_49",
	"161117_0114":"6-inch v3_51",
	"161117_0116":"6-inch v3_52",
	"271117_0744":"6-inch v3_16",
	"271117_0734":"6-inch v3_17",
	"271117_0740":"6-inch v3_18",
	"161117_0125":"6-inch v3_22",
	"161117_0121":"6-inch v3_30",
}

RUNS_T15 = {
	"220119_1932":"No connection",
	"220119_1934":"No connection",
	"220119_1937":"F'n gen off",
	"220119_1938":"F'n gen off",
	"220119_1939":"F'n gen output off",
	"220119_1940":"F'n gen output off",

	"220119_1942":"1Hz",    # 250mV no filter
	"220119_1943":"1Hz",    #
	"220119_1944":"100Hz",  #
	"220119_1945":"100Hz",  #
	"220119_1946":"10kHz",  #
	"220119_1947":"10kHz",  #
	"220119_1948":"33kHz",  #
	"220119_1949":"33kHz",  #
	"220119_1950":"100kHz", #
	"220119_1951":"100kHz", #
	"220119_1952":"330kHz", #
	"220119_1953":"330kHz", #
	"220119_1954":"1MHz",   #
	"220119_1955":"1MHz",   #
	"220119_1956":"3.3MHz", #
	"220119_1957":"3.3MHz", #
	"220119_1958":"10MHz",  #
	"220119_1959":"10MHz",  #
	"220119_2000":"20MHz",  #
	"220119_2001":"20MHz",  #

	"220119_2003":"1Hz",    # 250mV 5kHz BNC HPF
	"220119_2004":"1Hz",    #
	"220119_2005":"100Hz",  #
	"220119_2006":"100Hz",  #
	"220119_2007":"10kHz",  #
	"220119_2008":"10kHz",  #
	"220119_2009":"33kHz",  #
	"220119_2010":"33kHz",  #
	"220119_2011":"100kHz", #
	"220119_2012":"100kHz", #
	"220119_2013":"330kHz", #
	"220119_2014":"330kHz", #
	"220119_2015":"1MHz",   #
	"220119_2016":"1MHz",   #
	"220119_2017":"3.3MHz", #
	"220119_2018":"3.3MHz", #
	"220119_2019":"10MHz",  #
	"220119_2020":"10MHz",  #
	"220119_2021":"20MHz",  #
	"220119_2022":"20MHz",  #
}

RUNS_T16 = {
	"240119_1538":"Tray cable floating",
	"240119_1539":"Tray cable floating",
	"240119_1540":"F'n gen off",
	"240119_1541":"F'n gen off",
	"240119_1542":"F'n gen output off",
	"240119_1543":"F'n gen output off",
	
	"240119_1544":"1Hz",
	"240119_1545":"1Hz",
	"240119_1546":"1kHz",
	"240119_1547":"1kHz",
	"240119_1548":"100kHz",
	"240119_1549":"100kHz",
	"240119_1550":"300kHz",
	"240119_1551":"300kHz",
	"240119_1552":"600kHz",
	"240119_1553":"600kHz",
	"240119_1554":"1MHz",
	"240119_1555":"1MHz",
	"240119_1556":"2MHz",
	"240119_1557":"2MHz",
	"240119_1558":"3MHz",
	"240119_1559":"3MHz",
	"240119_1600":"5MHz",
	"240119_1601":"5MHz",
	"240119_1602":"8MHz",
	"240119_1603":"8MHz",
	"240119_1604":"13MHz",
	"240119_1605":"13MHz",
	"240119_1606":"20MHz",
	"240119_1607":"20MHz",
	"240119_1608":"32MHz",
	"240119_1609":"32MHz",
	"240119_1610":"50MHz",
	"240119_1611":"50MHz",
	"240119_1612":"80MHz",
	"240119_1613":"80MHz",	
}

RUNS = [RUNS_T0] + [None]*10 + [RUNS_T11, RUNS_T12, RUNS_T13, RUNS_T14, RUNS_T15, RUNS_T16]

#IGNORE_CHANNELS = [[0,0],[1,0],[2,2],[0,28],[3,60],[2,0],[2,4]]
IGNORE_CHANNELS = [
	[0,0],[0,28],[0,22],
	[1,0],[1,2],[1,4],
	[2,2],[2,0],[2,4],
	[3,60],[3,32],[3,44],
	]

def load_rms_dist(run,trial=0):
	file = os.sep.join([CWD,FOLDERS.format(trial),PFOLDERS.format(run),FILE])
	try:
		cont = numpy.loadtxt(file,skiprows=2)
	except:
		print("FAILED AT {}".format(run))
		raise
	active_channels = []
	for channel in cont:
		if int(channel[1]) & 1:
			continue
		else:
			if [int(channel[0]),int(channel[1])] in IGNORE_CHANNELS:
				continue
			else:
				active_channels.append(channel)
	channels = numpy.array(active_channels)
	#channels_conc = numpy.zeros([channels.shape[0],2])
	#channels_conc[...,1] = channels[...,2]
	#channels_conc[...,0] = channels[...,1] + channels[...,0]*64
	return channels

def rms_mean_and_rms(run,col=2,trial=0):
	channels = load_rms_dist(run,trial)[...,col]
	mean = channels.mean()
	rms  = numpy.std(channels)
	return mean,rms


YLABEL_RMS  = "channel RMS values, high gain"
YLABEL_MEAN = "channels means, high gain"

def plot_runs(runs,color_gen,xlist=None,plot_raw=False,means=False,mean_marker=5,show_errorbars=True,xlabel='trial number',suptitle="",ncol=1,trial=0,show=True,xlog=False,basex=10,ylog=False,basey=10,labels=True,cxn=False,cxnlabel=None):
	#plot = PLOTFUNCS[plotfunc]
	col = 3 if means else 2

	xp = []
	yp = []

	for i,run in enumerate(runs):
		mean_rms,rms_rms = rms_mean_and_rms(run,col,trial)
		#print(mean_rms, rms_rms)
		if plot_raw:
			channels = load_rms_dist(run,trial)[...,col]
		color = next(color_gen)

		xval  = i if xlist is None else xlist[i]
		label = '{} - {}'.format(i,RUNS[trial][run]) if xlist is None else '{}'.format(RUNS[trial][run])
		if labels is False:
			label = None
		elif labels is True:
			pass
		else:
			label = labels
		if xlog:plt.xscale("log",basex=basex)
		if ylog:plt.yscale("log",basey=basey)
		if show_errorbars:
			plt.errorbar(xval,mean_rms,yerr=rms_rms,color=color,marker=mean_marker,label=label,capsize=4)
		else:
			pass
			#plt.errorbar(xval,mean_rms,color=color,marker=mean_marker,label=label)
		xp.append(xval)
		yp.append(mean_rms)
		if plot_raw:
			plt.plot([xval]*len(channels),channels,marker='.',color=color,linestyle='')

	#if not show_errorbars:
	if cxn:
		plt.plot(xp,yp,color=color,marker=mean_marker,label=cxnlabel,linestyle='--')

	if show:
		plt.xlabel(xlabel)
		plt.ylabel(YLABEL_MEAN if means else YLABEL_RMS)
		plt.suptitle(suptitle)
		plt.legend(ncol=ncol)
		plt.show()

RUNS_T0_NOISE = ["131118_1401","131118_1402","131118_1407","131118_1410","131118_1413","131118_1415","131118_1418","131118_1424","131118_1427","131118_1432","131118_1436","131118_1439","131118_1440","131118_1442","131118_1445","131118_1446","131118_1448","141118_1104","141118_1106","141118_1107","141118_1109","141118_1113","141118_1114","141118_1116","141118_1117"]
T0_FRQ = [1,3,10,30,60,100,120,300,1000,3000,10000,30000,100000,300000,600000,1000000,2000000] + [3000000,5000000,8000000,13000000,20000000,32000000,50000000,80000000]

if False:
	RUNS_T10_ALL = ["1252","1259","1302","1304","1307","1309","1316","1341","1351","1416","1426","1451","1501","1526","1535","1601"]
	RUNS_T10_UNB = ["1252","1259","1302","1304","1307","1309"]
	RUNS_T10_B   = ["1316","1341","1351","1416","1426","1451","1501","1526","1535","1601"]
	RUNS_T10_5m  = RUNS_T10_B[0::2]
	RUNS_T10_30m = RUNS_T10_B[1::2]

RUNS_T11_V1 = ["181218_1658"              ,"181218_1653","181218_1643","181218_1648","181218_1638"]
RUNS_T11_V2 = ["171218_1048","171218_1045","171218_1028","171218_1051","171218_1054","171218_1042"]
RUNS_T11_GOOD = ["181218_1658","181218_1653","181218_1648","171218_1048","171218_1045","171218_1028","171218_1051","171218_1054","171218_1042"]
RUNS_T11_ALL = [_ for _ in RUNS_T11.keys()]

RUNS_T12_INTER = ["160119_1506","160119_1623"]
RUNS_T12_NOHPF = ["170119_1107","170119_1112","170119_1114","170119_1117","170119_1119",              "170119_1122","170119_1124",              "170119_1128","170119_1129"]
RUNS_T12_HPF   = ["170119_1555",              "170119_1559","170119_1601","170119_1604",              "170119_1611","170119_1613","170119_1615","170119_1616","170119_1618"]
RUNS_T12_5K_1  = ["180119_1021","180119_1026","180119_1028","180119_1035","180119_1037","180119_1039","180119_1041","180119_1043","180119_1045","180119_1047"]
RUNS_T12_5K_2  = ["180119_1023","180119_1027","180119_1034","180119_1036","180119_1038","180119_1040","180119_1042","180119_1044","180119_1046","180119_1048"]
T12_FRQ        = [1,10,100,1000,10000,100000,1000000,10000000]
T12_FRQ_NOHPF  = [1,10,    1000,10000,       1000000,10000000]
T12_FRQ_HPF    = [1,10,100,1000,10000,       1000000,10000000]




RUNS_T13_NOCXN   = ["180119_1216","180119_1217"]
RUNS_T13_GENOFF  = ["180119_1219","180119_1220"]
RUNS_T13_OUTPOFF = ["180119_1221","180119_1222"]
RUNS_T13_NOHPF  = ["180119_1219","180119_1220","180119_1221","180119_1222","180119_1223","180119_1224","180119_1225","180119_1226","180119_1227","180119_1228","180119_1229","180119_1230","180119_1231","180119_1232","180119_1234","180119_1235","180119_1236","180119_1237","180119_1238","180119_1239","180119_1240","180119_1241","180119_1242","180119_1243"]
RUNS_T13_BNCHPF = ["180119_1245","180119_1246","180119_1247","180119_1248","180119_1249","180119_1250","180119_1251","180119_1252","180119_1253","180119_1254","180119_1255","180119_1256","180119_1257","180119_1258","180119_1259","180119_1300","180119_1301","180119_1302","180119_1303","180119_1304","180119_1305","180119_1306","180119_1307","180119_1308"]
RUNS_T13_RCHPF  = ["180119_1346","180119_1347","180119_1348","180119_1349","180119_1350","180119_1351","180119_1352","180119_1353","180119_1354","180119_1355","180119_1356","180119_1357","180119_1358","180119_1359","180119_1400","180119_1401","180119_1402","180119_1403","180119_1404","180119_1405","180119_1406","180119_1407","180119_1408","180119_1409"]
T13_FRQ_MUL     = [None,None,None,None,1,1,100,100,10e3,10e3,33e3,33e3,100e3,100e3,330e3,330e3,1e6,1e6,3.3e6,3.3e6,10e6,10e6,20e6,20e6]
T13_FRQ         = [1,100,10e3,33e3,100e3,330e3,1e6,3.3e6,10e6,20e6]

RUNS_T13_NOHPF_GOOD  = ["180119_1224","180119_1226","180119_1228","180119_1230","180119_1232","180119_1235","180119_1237","180119_1238","180119_1241","180119_1243"]
RUNS_T13_BNCHPF_GOOD = ["180119_1250","180119_1252","180119_1254","180119_1255","180119_1258","180119_1300","180119_1301","180119_1304","180119_1306","180119_1308"]
RUNS_T13_RCHPF_GOOD  = ["180119_1351","180119_1353","180119_1355","180119_1357","180119_1359","180119_1401","180119_1403","180119_1405","180119_1407","180119_1409"]

RUNS_T14_ALL  = ["161117_1016","161117_1014","161117_1011","161117_1008","161117_1005","161117_1003","161117_1001","161117_0958","161117_0955","161117_0952","161117_0945","161117_0947","161117_0949","161117_0156","161117_0114","161117_0116","271117_0744","271117_0734","271117_0740","161117_0125","161117_0121"]
RUNS_T14_GOOD = ["161117_1016","161117_1014","161117_1011","161117_1008","161117_1005","161117_1003","161117_1001","161117_0958","161117_0955","161117_0952","161117_0945","161117_0947","161117_0949","161117_0156",              "161117_0116","271117_0744","271117_0734","271117_0740","161117_0125","161117_0121"]




RUNS_T15_ALL    = ["220119_1932","220119_1934","220119_1937","220119_1938","220119_1939","220119_1940","220119_1942","220119_1943","220119_1944","220119_1945","220119_1946","220119_1947","220119_1948","220119_1949","220119_1950","220119_1951","220119_1952","220119_1953","220119_1954","220119_1955","220119_1956","220119_1957","220119_1958","220119_1959","220119_2000","220119_2001","220119_2003","220119_2004","220119_2005","220119_2006","220119_2007","220119_2008","220119_2009","220119_2010","220119_2011","220119_2012","220119_2013","220119_2014","220119_2015","220119_2016","220119_2017","220119_2018","220119_2019","220119_2020","220119_2021","220119_2022"]
RUNS_T15_NOCXN   = ["220119_1932","220119_1934"]
RUNS_T15_GENOFF  = ["220119_1937","220119_1938"]
RUNS_T15_OUTPOFF = ["220119_1939","220119_1940"]
RUNS_T15_NOHPF  = ["220119_1942","220119_1943","220119_1944","220119_1945","220119_1946","220119_1947","220119_1948","220119_1949","220119_1950","220119_1951","220119_1952","220119_1953","220119_1954","220119_1955","220119_1956","220119_1957","220119_1958","220119_1959","220119_2000","220119_2001"]
RUNS_T15_BNCHPF = ["220119_2003","220119_2004","220119_2005","220119_2006","220119_2007","220119_2008","220119_2009","220119_2010","220119_2011","220119_2012","220119_2013","220119_2014","220119_2015","220119_2016","220119_2017","220119_2018","220119_2019","220119_2020","220119_2021","220119_2022"]
RUNS_T15_NOHPF_GOOD  = ["220119_1942","220119_1944","220119_1946","220119_1948","220119_1950","220119_1952","220119_1954","220119_1956","220119_1958","220119_2000"]
RUNS_T15_BNCHPF_GOOD = ["220119_2004","220119_2005","220119_2007","220119_2010","220119_2011","220119_2013","220119_2015","220119_2017","220119_2019","220119_2021"]
T15_FRQ         = [1,100,10e3,33e3,100e3,330e3,1e6,3.3e6,10e6,20e6]

RUNS_T16_NOISE = ["240119_1544","240119_1545","240119_1546","240119_1547","240119_1548","240119_1549","240119_1550","240119_1551","240119_1552","240119_1553","240119_1554","240119_1555","240119_1556","240119_1557","240119_1558","240119_1559","240119_1600","240119_1601","240119_1602","240119_1603","240119_1604","240119_1605","240119_1606","240119_1607","240119_1608","240119_1609","240119_1610","240119_1611","240119_1612","240119_1613"]
T16_FRQ = [1,1000,100000,300000,600000,1000000,2000000,3000000,5000000,8000000,13000000,20000000,32000000,50000000,80000000]

um = False
se = False
pr = False


# plot_grounded = True
# if plot_grounded:
# 	suptitle = "Post-grounding\n250mV noise"
# 	plot_runs(RUNS_T15_NOHPF_GOOD , cg_list(CRED ), plot_raw=pr, xlist=T15_FRQ, means=um, mean_marker='o', show_errorbars=se, xlabel='frequency (Hz)', suptitle=suptitle, labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='No filter', trial=15, show=False)
# 	plot_runs(RUNS_T15_BNCHPF_GOOD, cg_list(CBLUE), plot_raw=pr, xlist=T15_FRQ, means=um, mean_marker='o', show_errorbars=se, xlabel='frequency (Hz)', suptitle=suptitle, labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='5kHz HPF', trial=15)

plot80m = True
if plot80m:
	suptitle = "Shield layer grounding comparison\n250mV noise"
	plot_runs(RUNS_T0_NOISE       , cg_list(CBLUE), plot_raw=pr, xlist=T0_FRQ , means=um, mean_marker='o', show_errorbars=se, xlabel='noise frequency (Hz)', suptitle=suptitle, labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='not grounded', trial=0 , show=False)
	plot_runs(RUNS_T16_NOISE[0::2], cg_list(CRED ), plot_raw=pr, xlist=T16_FRQ, means=um, mean_marker='o', show_errorbars=se, xlabel='noise frequency (Hz)', suptitle=suptitle, labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='grounded'    , trial=16, show=True )

plot_ground_comparison = False
if plot_ground_comparison:
	suptitle = "Shield layer grounding comparison\n250mV noise"
	plot_runs(RUNS_T13_NOHPF_GOOD , cg_list(CBLUE), plot_raw=pr, xlist=T13_FRQ, means=um, mean_marker='o', show_errorbars=se, xlabel='noise frequency (Hz)', suptitle=suptitle, labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='Not grounded; No filter', trial=13, show=False)
	#plot_runs(RUNS_T13_BNCHPF_GOOD, cg_list(CC   ), plot_raw=pr, xlist=T13_FRQ, means=um, mean_marker='o', show_errorbars=se, xlabel='noise frequency (Hz)', suptitle=suptitle, labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='Not grounded; 5kHz HPF' , trial=13, show=False)
	plot_runs(RUNS_T15_NOHPF_GOOD , cg_list(CRED ), plot_raw=pr, xlist=T15_FRQ, means=um, mean_marker='o', show_errorbars=se, xlabel='noise frequency (Hz)', suptitle=suptitle, labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='Grounded; No filter', trial=15, show=True)
	#plot_runs(RUNS_T15_BNCHPF_GOOD, cg_list(CM   ), plot_raw=pr, xlist=T15_FRQ, means=um, mean_marker='o', show_errorbars=se, xlabel='noise frequency (Hz)', suptitle=suptitle, labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='Grounded; 5kHz HPF' , trial=15, show=True)

	plot_runs(RUNS_T13_NOCXN  , cg_list(CBLUE), plot_raw=pr, xlist=[ 0, 1], means=um, mean_marker='o', show_errorbars=se, xlabel='', suptitle='', labels='Not grounded', trial=13, show=False)
	plot_runs(RUNS_T15_NOCXN  , cg_list(CRED ), plot_raw=pr, xlist=[ 2, 3], means=um, mean_marker='o', show_errorbars=se, xlabel='', suptitle='', labels='Grounded'    , trial=15, show=False)

	plot_runs(RUNS_T13_GENOFF , cg_list(CBLUE), plot_raw=pr, xlist=[ 4, 5], means=um, mean_marker='o', show_errorbars=se, xlabel='', suptitle='', labels='Not grounded', trial=13, show=False)
	plot_runs(RUNS_T15_GENOFF , cg_list(CRED ), plot_raw=pr, xlist=[ 6, 7], means=um, mean_marker='o', show_errorbars=se, xlabel='', suptitle='', labels='Grounded'    , trial=15, show=False)

	plot_runs(RUNS_T13_OUTPOFF, cg_list(CBLUE), plot_raw=pr, xlist=[ 8, 9], means=um, mean_marker='o', show_errorbars=se, xlabel='', suptitle='', labels='Not grounded', trial=13, show=False)
	plot_runs(RUNS_T15_OUTPOFF, cg_list(CRED ), plot_raw=pr, xlist=[10,11], means=um, mean_marker='o', show_errorbars=se, xlabel='', suptitle='', labels='Grounded'    , trial=15, show=True)

	RUNS_T13_ANT = RUNS_T13_NOCXN[:1] + RUNS_T13_GENOFF[:1]# + RUNS_T13_OUTPOFF[:1]
	RUNS_T15_ANT = RUNS_T15_NOCXN[:1] + RUNS_T15_GENOFF[:1]# + RUNS_T15_OUTPOFF[:1]
	plot_runs(RUNS_T13_ANT, cg_list(CBLUE), plot_raw=pr, xlist=[0.0,1.0,2.0], means=um, mean_marker='o', show_errorbars=se, xlabel='', suptitle='Antenna effect', labels=False, cxn=True, cxnlabel='Not grounded', trial=13, show=False)
	plot_runs(RUNS_T15_ANT, cg_list(CRED ), plot_raw=pr, xlist=[0.0,1.0,2.0], means=um, mean_marker='o', show_errorbars=se, xlabel='', suptitle='Antenna effect', labels=False, cxn=True, cxnlabel='Grounded'    , trial=15, show=True)




plot_pcb_comp = False
if plot_pcb_comp:
	xl1 = len(RUNS_T11_GOOD)
	xl2 = len(RUNS_T14_GOOD)
	xr1 = range(0,xl1)
	xr2 = range(xl1,xl1+xl2)
	suptitle = 'PCB DAQ comparison\nGood 6" and 8" PCBs'
	#plot_runs(RUNS_T14_GOOD, cg_perm(C_G27), plot_raw=pr, xlist=None, means=um, mean_marker='o',show_errorbars=se,xlabel='',suptitle='6"',labels=True,ncol=3,trial=14)
	plot_runs(RUNS_T11_GOOD[1:], cg_list(CRED ), plot_raw=pr, xlist=xr1[1:], means=um, mean_marker='o',show_errorbars=se,xlabel='',suptitle=suptitle,labels=False,trial=11,show=False)
	plot_runs(RUNS_T14_GOOD[1:], cg_list(CBLUE), plot_raw=pr, xlist=xr2[1:], means=um, mean_marker='o',show_errorbars=se,xlabel='',suptitle=suptitle,labels=False,trial=14,show=False)
	plot_runs(RUNS_T11_GOOD[:1], cg_list(CRED ), plot_raw=pr, xlist=xr1[:1], means=um, mean_marker='o',show_errorbars=se,xlabel='',suptitle=suptitle,labels='8" PCBs',trial=11,show=False)
	plot_runs(RUNS_T14_GOOD[:1], cg_list(CBLUE), plot_raw=pr, xlist=xr2[:1], means=um, mean_marker='o',show_errorbars=se,xlabel='',suptitle=suptitle,labels='6" PCBs',trial=14)


plot_13 = False
if plot_13:
	plot_runs(RUNS_T13_NOHPF_GOOD , cg_list(CBLACK), plot_raw=pr, xlist=T13_FRQ, means=um, mean_marker='o', show_errorbars=se, xlabel='frequency', suptitle='Filter comparison\n250mV noise\n500V bias', labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='No filter', trial=13, show=False)
	plot_runs(RUNS_T13_BNCHPF_GOOD, cg_list(CBLUE ), plot_raw=pr, xlist=T13_FRQ, means=um, mean_marker='o', show_errorbars=se, xlabel='frequency', suptitle='Filter comparison\n250mV noise\n500V bias', labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='BNC HPF (5kHz)', trial=13, show=False)
	plot_runs(RUNS_T13_RCHPF_GOOD , cg_list(CRED  ), plot_raw=pr, xlist=T13_FRQ, means=um, mean_marker='o', show_errorbars=se, xlabel='frequency', suptitle='Filter comparison\n250mV noise\n500V bias', labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='RC HPF (160Hz)', trial=13)

plot_12 = False
if plot_12:
	# plot_runs(RUNS_T12_INTER, cg_list(COLS_2), plot_raw=pr, xlist=[0,1], means=um, mean_marker='o',show_errorbars=se,xlabel='',suptitle='interposer coparison',labels=True,trial=12)

	# plot_runs(RUNS_T12_NOHPF[:3], cg_list(CBLACK ), plot_raw=pr, xlist=[0.0,1.0,2.0], means=um, mean_marker='o', show_errorbars=se, xlabel='', suptitle='antenna effect', labels=False, xlog=False, ylog=False, cxn=True, cxnlabel='no HPF'         , trial=12, show=False)
	# plot_runs(RUNS_T12_HPF[:2]  , cg_list(CRED   ), plot_raw=pr, xlist=[0.1,    2.1], means=um, mean_marker='o', show_errorbars=se, xlabel='', suptitle='antenna effect', labels=False, xlog=False, ylog=False, cxn=True, cxnlabel='160Hz HPF'      , trial=12, show=False)
	# plot_runs(RUNS_T12_5K_1[:3] , cg_list(CGREEN ), plot_raw=pr, xlist=[0.2,1.2,2.2], means=um, mean_marker='o', show_errorbars=se, xlabel='', suptitle='antenna effect', labels=False, xlog=False, ylog=False, cxn=True, cxnlabel='5kHz HPF, Set 1', trial=12, show=False)
	# plot_runs(RUNS_T12_5K_2[:3] , cg_list(CBLUE  ), plot_raw=pr, xlist=[0.3,1.3,2.3], means=um, mean_marker='o', show_errorbars=se, xlabel='', suptitle='antenna effect', labels=False, xlog=False, ylog=False, cxn=True, cxnlabel='5kHz HPF, Set 2', trial=12)

	plot_runs(RUNS_T12_NOHPF[3:], cg_list(CBLACK ), plot_raw=pr, xlist=T12_FRQ_NOHPF, means=um, mean_marker='o', show_errorbars=se, xlabel='frequency', suptitle='Filter comparison\n250mV noise\n300V bias', labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='No filter'   , trial=12, show=False)
	plot_runs(RUNS_T12_5K_1[3:] , cg_list(CGREEN ), plot_raw=pr, xlist=T12_FRQ_HPF  , means=um, mean_marker='o', show_errorbars=se, xlabel='frequency', suptitle='Filter comparison\n250mV noise\n300V bias', labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='BNC HPF (5kHz), Set 1', trial=12,show=False)
	plot_runs(RUNS_T12_5K_2[3:] , cg_list(CBLUE  ), plot_raw=pr, xlist=T12_FRQ_HPF  , means=um, mean_marker='o', show_errorbars=se, xlabel='frequency', suptitle='Filter comparison\n250mV noise\n300V bias', labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='BNC HPF (5kHz), Set 2', trial=12,show=False)
	plot_runs(RUNS_T12_HPF[2:]  , cg_list(CRED   ), plot_raw=pr, xlist=T12_FRQ_HPF  , means=um, mean_marker='o', show_errorbars=se, xlabel='frequency', suptitle='Filter comparison\n250mV noise\n300V bias', labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='RC HPF (160Hz)', trial=12)



#plot_runs(RUNS_T11_GOOD, cg_perm(COLS_12), plot_raw=False, xlist=None, means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='', suptitle='Good 8" PCBs', labels=True, trial=11, ncol=2)
#plot_runs(["171218_1042"], cg_list(CBLACK), plot_raw=False, xlist=None, means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='', suptitle='V2 PCB6', labels=True, trial=11)

# plot_runs(RUNS_T10_ALL, cg_perm(C_G18) , plot_raw=False, xlist=None, means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='Trial', suptitle="Module 58", labels=True, trial=10)


# plot_runs(RUNS_T9_M58, cg_perm(C_G18) , plot_raw=False, xlist=V_T9_M58, means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='bias voltage', suptitle="Module 58", labels=True, trial=9)

# suptitle = 'Channel {} distribution vs. bias voltage'.format("mean" if usemeans else "RMS")

# plot_runs(RUNS_T9_S2[-1:] , cg_list(CBLACK), plot_raw=False, xlist=V_T9_S2[-1:] , means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='bias voltage', suptitle='', labels="No keithley connection", trial=9, show=False)
# plot_runs(RUNS_T9_S2[:3]  , cg_list(CRED), plot_raw=False, xlist=V_T9_S2[:3]  , means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='bias voltage', suptitle='', labels=False, cxn=True, cxnlabel="Zero bias voltage", trial=9, show=False)
# plot_runs(RUNS_T9_S2[3:-1], cg_list(CBLUE) , plot_raw=False, xlist=V_T9_S2[3:-1], means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='bias voltage', suptitle=suptitle, labels=False, cxn=True, cxnlabel='Biased', trial=9)





plot_filter_trials=False
if plot_filter_trials:
	plot_runs(RUNS_T7_SH2[4:]     , cg_list(CM)    , xlist=T7_FRQS, means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel = "Noise Frequency (Hz)", trial=7, show=False, xlog=True, ylog=True, labels=False, cxn=True, cxnlabel="Regular cable")
	plot_runs(RUNS_T7_BREAD[4:]   , cg_list(CBLACK), xlist=T7_FRQS, means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel = "Noise Frequency (Hz)", trial=7, show=False, xlog=True, ylog=True, labels=False, cxn=True, cxnlabel="Breadboard (no filter)")
	plot_runs(RUNS_T7_HP_1NF[4:]  , cg_list(CRED)  , xlist=T7_FRQS, means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel = "Noise Frequency (Hz)", trial=7, show=False, xlog=True, ylog=True, labels=False, cxn=True, cxnlabel="159Hz HPF")
	plot_runs(RUNS_T7_HP_100PF[4:], cg_list(CBLUE) , xlist=T7_FRQS, means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel = "Noise Frequency (Hz)", trial=7, show=False, xlog=True, ylog=True, labels=False, cxn=True, cxnlabel="1.59kHz HPF")
	plot_runs(RUNS_T7_HP_10PF[4:] , cg_list(CGREEN), xlist=T7_FRQS, means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel = "Noise Frequency (Hz)", trial=7, show=True , xlog=True, ylog=True, labels=False, cxn=True, cxnlabel="15.9kHz HPF", suptitle="Effect of Filter on Noise")

	plot_runs(RUNS_T7_SH2[:4]     , cg_list(CM)    , means=usemeans, mean_marker='o', show_errorbars=False, xlabel = "Trial Number", trial=7, show=False, xlog=False, ylog=False, labels=False, cxn=True, cxnlabel="Regular cable")
	plot_runs(RUNS_T7_BREAD[:4]   , cg_list(CBLACK), means=usemeans, mean_marker='o', show_errorbars=False, xlabel = "Trial Number", trial=7, show=False, xlog=False, ylog=False, labels=False, cxn=True, cxnlabel="Breadboard (no filter)")
	plot_runs(RUNS_T7_HP_1NF[:4]  , cg_list(CRED)  , means=usemeans, mean_marker='o', show_errorbars=False, xlabel = "Trial Number", trial=7, show=False, xlog=False, ylog=False, labels=False, cxn=True, cxnlabel="159Hz HPF")
	plot_runs(RUNS_T7_HP_100PF[:4], cg_list(CBLUE) , means=usemeans, mean_marker='o', show_errorbars=False, xlabel = "Trial Number", trial=7, show=False, xlog=False, ylog=False, labels=False, cxn=True, cxnlabel="1.59kHz HPF")
	plot_runs(RUNS_T7_HP_10PF[:4] , cg_list(CGREEN), means=usemeans, mean_marker='o', show_errorbars=False, xlabel = "Trial Number", trial=7, show=True , xlog=False, ylog=False, labels=False, cxn=True, cxnlabel="15.9kHz HPF", suptitle="Effect of Filter on Antenna Effect")

plot_amp_response=False
if plot_amp_response:
	plot_runs(RUNS_T4_2MHZ    , cg_list(CBLUE) , xlist=AMPS, trial=4, means=True, xlog=True, labels=False, ylog=True, basex=10, show_errorbars=True, mean_marker='o', cxn=True, cxnlabel="2 MHz noise", show=False)
	plot_runs(RUNS_T1_1MHZ_AMP, cg_list(CRED)  , xlist=AMPS, trial=1, means=True, xlog=True, labels=False, ylog=True, basex=10, show_errorbars=True, mean_marker='o', cxn=True, cxnlabel="1 MHz noise", show=False)
	plot_runs(RUNS_T1_1KHZ_AMP, cg_list(CGREEN), xlist=AMPS, trial=1, means=True, xlog=True, labels=False, ylog=True, basex=10, show_errorbars=True, mean_marker='o', cxn=True, cxnlabel="1 KHz noise", show=True, suptitle="Mean of Channel RMS - Amplitude Dependence", xlabel="Noise Amplitude (mV)")

plot_freq_response = False
if plot_freq_response:
	plot_runs(RUNS_T1_FRQ   , cg_list(CRED)  , xlist = T1_FRQS  , means=True, trial=1, xlog=True, ylog=True, show_errorbars=False, labels=False, mean_marker='o', cxn=True, cxnlabel=None, show=False)
	plot_runs(RUNS_T2_FRQ   , cg_list(CRED)  , xlist = T2_FRQS  , means=True, trial=2, xlog=True, ylog=True, show_errorbars=False, labels=False, mean_marker='o', cxn=True, cxnlabel="cable 1", show=False)
	plot_runs(RUNS_T5_C2[3:], cg_list(CGREEN), xlist = T5_FRQS_2, means=True, trial=5, xlog=True, ylog=True, show_errorbars=False, labels=False, mean_marker='o', cxn=True, cxnlabel="cable 3", show=False)
	plot_runs(RUNS_T5_C3[3:], cg_list(CBLUE) , xlist = T5_FRQS  , means=True, trial=5, xlog=True, ylog=True, show_errorbars=False, labels=False, mean_marker='o', cxn=True, cxnlabel="cable 4", suptitle="Mean of Channel RMS - Frequency Dependence", xlabel="signal frequency (Hz)", show=True)

plot_antenna_test = False
if plot_antenna_test:
	plot_runs(RUNS_T4_CABLE_NONE, cg_list(CBLACK)    , means=False, xlist=[-1.7]           , trial=4, show=False)

	plot_runs(RUNS_T4_ANTENNA_C0[:1], cg_list(CRED)  , means=False, xlist=[-1.0,1.0,2.0][:1], trial=4, show=False, labels="cable 1 (old cable)")
	plot_runs(RUNS_T4_ANTENNA_C0[1:], cg_list(CRED)  , means=False, xlist=[-1.0,1.0,2.0][1:], trial=4, show=False, labels=False)
	plot_runs(RUNS_T4_ANTENNA_C1[:1], cg_list(CGREEN), means=False, xlist=[-0.9,1.1,2.1][:1], trial=4, show=False, labels="cable 2 (new 50-ohm cable)")
	plot_runs(RUNS_T4_ANTENNA_C1[1:], cg_list(CGREEN), means=False, xlist=[-0.9,1.1,2.1][1:], trial=4, show=False, labels=False)
	plot_runs(RUNS_T5_ANTENNA_C2[:1], cg_list(CBLUE) , means=False, xlist=[-0.8,1.2,2.2][:1], trial=5, show=False, labels="cable 3 (new 75-ohm cable)")
	plot_runs(RUNS_T5_ANTENNA_C2[1:], cg_list(CBLUE) , means=False, xlist=[-0.8,1.2,2.2][1:], trial=5, show=False, labels=False)
	plot_runs(RUNS_T5_ANTENNA_C3[:1], cg_list(CM)    , means=False, xlist=[-0.7,1.3,2.3][:1], trial=5, show=False , labels="cable 4 (custom shield cable)")

	# This data may be inaccurate (dry air)
	#plot_runs(RUNS_T6_UNPLUGGED, cg_list(CJ), means=False, xlist=[0.0,0.1,0.2], trial=6, show=False, labels=False)

	plot_runs(RUNS_T5_ANTENNA_C3[1:], cg_list(CM)    , means=False, xlist=[-0.7,1.3,2.3][1:], trial=5, show=True , labels=False, xlabel = "", suptitle = "Cable Comparison - Antenna Test")
