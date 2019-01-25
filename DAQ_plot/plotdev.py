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
COLS_2 = [[0.9,0,0],[0,0,0.9]]
COLS_4 = [[0.85,0,0],[0,0.85,0],[0,0,0.85],[0,0,0]]
COLS_8 = [[0,192],[0,192],[0,192]]
C_G27  = [[0,100,200],[0,100,200],[0,100,200]]
C_G18  = [[0,128,256],[0,100,200],[0,255]]




CWD    = os.getcwd()
FOLDERS  = 'trial{}'
TRIALS   = ["051118","131118","141118","151118","161118","191118","201118","211118","271118","051218","071218"]
PFOLDERS = 'RUN_{}_{}_plots'

FILE   = 'rms_summary_sca_1.txt'

RUNS_T0 = {
	'1446':'500v, no fn, trial 1',
	'1457':'500v, no fn, trial 2',
	'1557':'500v, tray cable floating',
	'1600':'500v, fn gen off',
	'1603':'500v, fn gen output off',
	'1608':'500v, 100Hz 25mv',
	'1610':'500v, 100Hz 250mv',
	'1612':'500v, 10KHz 25mv',
	'1614':'500v, 10KHz 250mv',
	'1616':'500v, 1MHz 25mv',
	'1618':'500v, 1MHz 250mv',
	'1621':'500v, 1Hz 25mv',
	'1623':'500v, 1Hz 250mv',
	'1628':'900v, output off',
	'1630':'900v, 100Hz 250mv',
	'1632':'900v, 10KHZ 250mv',
	'1635':'700v, output off',
	'1637':'700v, 100Hz 250mv',
	'1638':'700v, 10KHZ 250mv',
	'1641':'500v, output off',
	'1643':'500v, 100Hz 250mv',
	'1644':'500v, 10KHZ 250mv',
	'1647':'300v, output off',
	'1648':'300v, 100Hz 250mv',
	'1650':'300v, 10KHZ 250mv',
}

RUNS_T1 = {
	"1346":"cable floating",
	"1354":"generator off",
	"1359":"generator output off",
	"1401":"1Hz 250mV",
	"1402":"3Hz 250mV",
	"1407":"10Hz 250mV",
	"1410":"30Hz 250mV",
	"1413":"60Hz 250mV",
	"1415":"100Hz 250mV",
	"1418":"120Hz 250mV",
	"1424":"300Hz 250mV",
	"1427":"1KHz 250mV",
	"1432":"3KHz 250mV",
	"1436":"10KHz 250mV",
	"1439":"30KHz 250mV",
	"1440":"100KHz 250mV",
	"1442":"300KHz 250mV",
	"1445":"600KHz 250mV",
	"1446":"1MHz 250mV",
	"1448":"2MHz 250mV",
	"1453":"2mV 1MHz",
	"1455":"4mV 1MHz",
	"1457":"8mV 1MHz",
	"1458":"16mV 1MHz",
	"1500":"32mV 1MHz",
	"1502":"64mV 1MHz",
	"1504":"128mV 1MHz",
	"1505":"250mV 1MHz",
	"1512":"2mV 1KHz",
	"1514":"4mV 1KHz",
	"1517":"8mV 1KHz",
	"1519":"16mV 1KHz",
	"1522":"32mV 1KHz",
	"1524":"64mV 1KHz",
	"1525":"128mV 1KHz",
	"1527":"250mV 1KHz",
}

RUNS_T2 = {
	"1101":"generator output off",
	"1104":"3MHz 250mV",
	"1106":"5MHz 250mV",
	"1107":"8MHz 250mV",
	"1109":"13MHz 250mV",
	"1113":"20MHz 250mV",
	"1114":"32MHz 250mV",
	"1116":"50MHz 250mV",
	"1117":"80MHz 250mV",
	"1424":"600KHz consistency test",
	"1428":"1MHz consistency test",
	"1430":"2MHz consistency test",
	"1433":"3MHz consistency test",
	"1436":"5MHz consistency test",
	"1536":"100KHz consistency test",
	"1538":"300KHz consistency test",
}

RUNS_T3 = {
	"1140":"All leads floating",
	"1145":"BNC in function generator (off)",
	"1147":"BNC in function generator (output off)",
	"1149":"1Hz 250mV",
	"1151":"100Hz 250mV",
	"1154":"10KHz 250mV",
	"1155":"1MHz 250mV",

	"1232":"All leads floating",
	"1235":"BNC in fn gen; GND on keithley GND",
	"1239":"function generator on, output off",
	"1241":"1Hz 250mV",
	"1246":"100Hz 250mV",
	"1249":"10KHz 250mV",
	"1251":"1MHz 250mV",

	"1546":"output off",
	"1549":"1MHz 250mV",
}

RUNS_T4 = {
	"1055":"Output off", # cable BNC-Al 1
	"1106":"2MHz 2mV",   # (old cable setup)
	"1108":"2MHz 4mV",   #
	"1111":"2MHz 8mV",   #
	"1118":"2MHz 16mV",  #
	"1123":"2MHz 32mV",  #
	"1124":"2MHz 64mV",  #
	"1126":"2MHz 128mV", #
	"1128":"2MHz 250mV", #

	"1312":"old cable, Floating",      # cable BNC-Al 1
	"1315":"old cable, Generator off", # (old cable setup)
	"1318":"old cable, Output off",
	"1321":"old cable, 1Hz 250mV",
	"1323":"old cable, 100Hz 250mV",
	"1328":"old cable, 10KHz 250mV",
	"1332":"old cable, 1MHz 250mV",

	"1416":"new cable, Floating",      # cables (BNC M-M AH 1) + (BNCF-Al 1) 
	"1419":"new cable, Generator off", # (new cable setup)
	"1423":"new cable, Output off",
	"1426":"new cable, 1Hz 250mV",
	"1428":"new cable, 100Hz 250mV",
	"1430":"new cable, 10KHz 250mV",
	"1435":"new cable, 1MHz 250mV",

	"1518":"no cable attached", # no cable attached	
}

RUNS_T5 = {
	"1404":"Other leads floating", # cable BNC M-M SH 2
	"1408":"Attached; f’n off",    # 
	"1410":"function output off",  # 
	"1412":"10KHz 250mV",
	"1413":"100KHz",
	"1415":"300KHz",
	"1417":"600KHz",
	#"1419":"1MHz", # corrputed
	"1421":"2MHz",
	"1423":"3MHz",
	"1424":"5MHz",
	"1426":"8MHz",
	"1429":"13MHz",
	"1431":"20MHz",
	"1434":"Other leads floating", # cable BNC M-M SH 3
	"1437":"Attached; f’n off",    # 
	"1439":"function output off",  # 
	"1501":"10KHz 250mV",
	"1503":"100KHz",
	"1504":"300KHz",
	"1506":"600KHz",
	"1507":"1MHz",
	"1509":"2MHz",
	"1511":"3MHz",
	"1513":"5MHz",
	"1514":"8MHz",
	"1516":"13MHz",
	"1518":"20MHz",
}

RUNS_T6 = {
	"1641":"Cable floating", # cable BNC M-M SH 1
	"1643":"f’n unplugged",
	"1645":"f’n off",
	"1649":"f’n on; output off",

	"1652":"Cable floating", # cable BNC M-M SH 2
	"1654":"f’n unplugged",
	"1657":"f’n off",
	"1701":"f’n on; output off",

	"1705":"Cable floating", # cable BNC M-M SH 3
	"1709":"f’n unplugged",
	"1711":"f’n off",
	"1713":"f’n on; output off",
}

RUNS_T7 = {
	# Cables: BNC M-M SH 2 + BNCF-AL 1
	"0939":"f’n off",
	"0944":"1KHz 250mV",
	"0947":"10KHz",
	"0950":"100KHz",
	"0952":"300KHz",
	"0955":"600KHz",
	"0958":"1MHz",
	"1000":"2MHz",
	"1006":"5MHz",
	"1009":"10MHz",

	# Cables: BNCF-Al 1 + breadboard & adapters
	"1036":"f’n off",
	"1037":"1KHz 250mV",
	"1040":"10KHz",
	"1042":"100KHz",
	"1046":"300KHz",
	"1048":"600KHz",
	"1050":"1MHz",
	"1052":"2MHz",
	"1055":"5MHz",
	"1057":"10MHz",

	"1342":"No cable",

	"1344":"Attached to BNCF-AL 1; all other leads floating",
	"1346":"All connections made; f’n gen unplugged",
	"1348":"All connections made; f’n gen off but plugged in",
	"1349":"All connections made; f’n gen on, output off",
	"1351":"10kHz",
	"1353":"30kHz",
	"1354":"100kHz",
	"1356":"200kHz",
	"1358":"500kHz",
	"1400":"1MHz",
	"1401":"2MHz",
	"1403":"5MHz",
	"1405":"10MHz",

	"1408":"Attached to BNCF-AL 1; all other leads floating",
	"1411":"All connections made; f’n gen unplugged",
	"1413":"All connections made; f’n gen off but plugged in",
	"1416":"All connections made; f’n gen on, output off",
	"1419":"10kHz",
	"1420":"30kHz",
	"1423":"100kHz",
	"1424":"200kHz",
	"1426":"500kHz",
	"1428":"1MHz",
	"1429":"2MHz",
	"1431":"5MHz",
	"1433":"10MHz",

	"1940":"Attached to BNCF-AL 1; all other leads floating",
	"1942":"All connections made; f’n gen unplugged",
	"1943":"All connections made; f’n gen off but plugged in",
	"1945":"All connections made; f’n gen on, output off",
	"1947":"10kHz",
	"1948":"30kHz",
	"1950":"100kHz",
	"1951":"200kHz",
	"1953":"500kHz",
	"1954":"1MHz",
	"1956":"2MHz",
	"1958":"5MHz",
	"1959":"10MHz",

	"2002":"Attached to BNCF-AL 1; all other leads floating",
	"2004":"All connections made; f’n gen unplugged",
	"2006":"All connections made; f’n gen off but plugged in",
	"2007":"All connections made; f’n gen on, output off",
	"2009":"10kHz",
	"2011":"30kHz",
	"2012":"100kHz",
	"2014":"200kHz",
	"2015":"500kHz",
	"2017":"1MHz",
	"2019":"2MHz",
	"2021":"5MHz",
	"2023":"10MHz",

	"2027":"Attached to BNCF-AL 1; all other leads floating",
	"2029":"All connections made; f’n gen unplugged",
	"2032":"All connections made; f’n gen off but plugged in",
	"2034":"All connections made; f’n gen on, output off",
	"2036":"10kHz",
	"2038":"30kHz",
	"2040":"100kHz",
	"2042":"200kHz",
	"2043":"500kHz",
	"2045":"1MHz",
	"2046":"2MHz",
	"2048":"5MHz",
	"2050":"10MHz",
}

RUNS_T8 = {
	"1510":"No GLI",            # Regular setup with BNC M-M SH 1
	"1516":"GLI on f'n output", # GLI in two places, or not present
	"1524":"GLI on tray clip adapter",  #
	"1530":"Cable floating", # Cable on BNCF-AL 1, all other leads floating 
	"1535":"No cable", # No cable attached

	"1611":"f'n ground floating",        # Regular setup, generator off
	"1613":"f'n ground on keithley",     # BNCF-AL 1 ground varied
	"1621":"f'n ground on quiet ground", # 

	"1627":"output off",   # Normal setup
	"1629":"10kHz 250mV",  #
	"1632":"300kHz 250mV", #

	"1634":"output off",   # GLI
	"1636":"10kHz 250mV",  #
	"1639":"300kHz 250mV", #

	"1642":"output off",   # GLI + quiet ground
	"1645":"10kHz 250mV",  #
	"1646":"300kHz 250mV", #

	"1649":"output off",   # Quiet ground
	"1652":"10kHz 250mV",  #
	"1655":"300kHz 250mV", #
}

RUNS_T9 = {
	#"1105":"0V",
	"1116":"0V (before)",
	#"1119":"50V",
	"1121":"100V",
	"1126":"150V",
	"1128":"200V",
	"1132":"250V",
	"1137":"300V",
	"1140":"350V",
	"1145":"400V",
	"1149":"450V",
	"1152":"500V",
	"1154":"600V",
	"1218":"0V (after)",

	"1249":"0V (before, trial 1)",
	"1254":"0V (before, trial 2)",
	"1258":"50V",
	"1302":"100V",
	"1305":"150V",
	"1307":"200V",
	"1309":"250V",
	"1312":"300V",
	"1318":"350V",
	"1322":"400V",
	"1325":"450V",
	"1327":"500V",
	"1331":"600V",
	"1341":"0V (after)",
	"1343":"No connection to keithley",

	"1629":"M58 no connection",
	"1633":"M58 keithley off",
	"1637":"M58 0V trial 1",
	"1646":"M58 0V trial 2",
	"1650":"M58 10V",
	"1652":"M58 20V",
	"1656":"M58 30V",
	"1702":"M58 40V",
	"1707":"M58 50V",
}

RUNS_T10 = {
	"1252":"No keithley cxn (1)",
	"1259":"No keithley cxn (2)",
	"1302":"Keithley off (1)",
	"1304":"Keithley off (2)",
	"1307":"0V (1)",
	"1309":"0V (2)",
	"1316":"10V 5m",
	"1341":"10V 30m",
	"1351":"30V 5m",
	"1416":"30V 30m",
	"1426":"50V 5m",
	"1451":"50V 30m",
	"1501":"100V 5m",
	"1526":"100V 30m",
	"1535":"150V 5m",
	"1601":"150V 30m",
}

RUNS = [RUNS_T0,RUNS_T1,RUNS_T2,RUNS_T3,RUNS_T4,RUNS_T5,RUNS_T6,RUNS_T7,RUNS_T8,RUNS_T9,RUNS_T10]

#IGNORE_CHANNELS = [[0,0],[1,0],[2,2],[0,28],[3,60],[2,0],[2,4]]
IGNORE_CHANNELS = [
	[0,0],[0,28],[0,22],
	[1,0],[1,2],[1,4],
	[2,2],[2,0],[2,4],
	[3,60],[3,32],[3,44],
	]

def load_rms_dist(run,trial=0):
	file = os.sep.join([CWD,FOLDERS.format(trial),PFOLDERS.format(TRIALS[trial],run),FILE])
	cont = numpy.loadtxt(file,skiprows=2)
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

if True:
	RUNS_T0_ANTENNA_TEST = ['1446','1457','1557','1600','1603']
	RUNS_T0_500V_25MV  = ['1621','1608','1612','1616']
	RUNS_T0_500V_250MV = ['1623','1610','1614','1618']
	RUNS_T0_500V_1HZ   = ['1621','1623']
	RUNS_T0_500V_100HZ = ['1608','1610']
	RUNS_T0_500V_10KHZ = ['1612','1614']
	RUNS_T0_500V_1MHZ  = ['1616','1618']
	RUNS_T0_100HZ = ['1648','1643','1637','1630']
	RUNS_T0_10KHZ = ['1650','1644','1638','1632']
	RUNS_T0_OFF   = ['1647','1641','1635','1628']
	RUNS_T0_NO_CABLE         = ['1446','1457']
	RUNS_T0_500V_250MV_100HZ = ['1610','1643']
	RUNS_T0_500V_250MV_10KHZ = ['1614','1644']
	RUNS_T0_500V_OUTPUT_OFF  = ['1603','1641']
	BV = [300,500,700,900]

if True:
	RUNS_T1_1MHZ_AMP = ["1453","1455","1457","1458","1500","1502","1504","1505"]
	RUNS_T1_1KHZ_AMP = ["1512","1514","1517","1519","1522","1524","1525","1527"]
	RUNS_T1_FRQ      = ["1401","1402","1407","1410","1413","1415","1418","1424","1427","1432","1436","1439","1440","1442","1445","1446","1448"]
	RUNS_T1_ANTENNA  = ["1346","1354","1359"]
	AMPS = [2,4,8,16,32,64,128,250]
	LOGAMPS = [math.log(_,2) for _ in AMPS]
	T1_FRQS = [1,3,10,30,60,100,120,300,1000,3000,10000,30000,100000,300000,600000,1000000,2000000]
	T1_LOGFRQS = [math.log(_,10) for _ in T1_FRQS]

if True:
	RUNS_T2_FRQ = ["1104","1106","1107","1109","1113","1114","1116","1117"]
	T2_FRQS = [3000000,5000000,8000000,13000000,20000000,32000000,50000000,80000000]
	T2_LOGFRQS = [math.log(_,10) for _ in T2_FRQS]

if True:
	RUNS_T3_2LEAD = ["1140","1145","1147","1149","1151","1154","1155"]
	RUNS_T3_1LEAD = ["1232","1235","1239","1241","1246","1249","1251"]
	RUNS_T3_CONF  = ["1546","1549"]

if True:
	RUNS_T4_2MHZ = ["1106","1108","1111","1118","1123","1124","1126","1128"]
	RUNS_T4_CABLE_OLD = ["1312","1315","1318","1321","1323","1328","1332"]
	RUNS_T4_CABLE_NEW = ["1416","1419","1423","1426","1428","1430","1435"]
	RUNS_T4_CABLE_NONE = ["1518"]
	RUNS_T4_ANTENNA_C0 = ["1312","1315","1318"]
	RUNS_T4_ANTENNA_C1 = ["1416","1419","1423"]
	T4_LOGFRQS = T2_LOGFRQS

if True:
	RUNS_T5_C2 = ["1404","1408","1410","1412","1413","1415","1417","1421","1423","1424","1426","1429","1431"]
	RUNS_T5_C3 = ["1434","1437","1439","1501","1503","1504","1506","1507","1509","1511","1513","1514","1516","1518"]
	RUNS_T5_ANTENNA_C2 = ["1404","1408","1410"]
	RUNS_T5_ANTENNA_C3 = ["1434","1437","1439"]
	T5_FRQS   = [10000,100000,300000,600000,1000000,2000000,3000000,5000000,8000000,13000000,20000000]
	T5_FRQS_2 = [10000,100000,300000,600000,2000000,3000000,5000000,8000000,13000000,20000000]

if True:
	RUNS_T6_ALL = ["1641","1643","1645","1649","1652","1654","1657","1701","1705","1709","1711","1713"]
	RUNS_T6_UNPLUGGED = ["1643","1654","1709"]

if True:
	RUNS_T7_ALL_R0   = ["0939","0944","0947","0950","0952","0955","0958","1000","1004","1006","1009","1036","1037","1040","1042","1046","1048","1050","1052","1055","1057"]
	RUNS_T7_CABLE_R0 = ["0939","0944","0947","0950","0952","0955","0958","1000","1006","1009"]
	RUNS_T7_BREAD_R0 = ["1036","1037","1040","1042","1046","1048","1050","1052","1055","1057"]
	RUNS_T7_OFF_R0   = ["0939","1036"]
	T7_FRQS_R0 = [1000,10000,100000,300000,600000,1000000,2000000,5000000,10000000]

if True:
	RUNS_T7_NOCABLE  = ["1342"]
	RUNS_T7_SH2      = ["1344","1346","1348","1349","1351","1353","1354","1356","1358","1400","1401","1403","1405"]
	RUNS_T7_BREAD    = ["1408","1411","1413","1416","1419","1420","1423","1424","1426","1428","1429","1431","1433"]
	RUNS_T7_HP_1NF   = ["1940","1942","1943","1945","1947","1948","1950","1951","1953","1954","1956","1958","1959"]
	RUNS_T7_HP_100PF = ["2002","2004","2006","2007","2009","2011","2012","2014","2015","2017","2019","2021","2023"]
	RUNS_T7_HP_10PF  = ["2027","2029","2032","2034","2036","2038","2040","2042","2043","2045","2046","2048","2050"]
	T7_FRQS = [10000,30000,100000,200000,500000,1000000,2000000,5000000,10000000]

if True:
	RUNS_T8_NORMAL = ['1627','1629','1632']
	RUNS_T8_GLI    = ['1634','1636','1639']
	RUNS_T8_BOTH   = ['1642','1645','1646']
	RUNS_T8_QG     = ['1649','1652','1655']
	RUNS_T8_GROUNDS = ['1611','1613']#,'1621'] - 1621 was corrupt file
	RUNS_T8_GLI_ = ['1535','1530','1510','1516','1524']

RUNS_T9_S1 = ["1116","1218","1121","1126","1128","1132","1137","1140","1145","1149","1152","1154"]
V_T9_S1    = [-5,5,100,150,200,250,300,350,400,450,500,600]

RUNS_T9_S2 = ["1249","1254","1341","1258","1302","1305","1307","1309","1312","1318","1322","1325","1327","1331","1343"]
V_T9_S2    = [-5,0,5,50,100,150,200,250,300,350,400,450,500,600,-50]

RUNS_T9_M58 = ["1629","1633","1637","1646","1650","1652","1656","1702","1707"]
V_T9_M58 = [-20,-10,-1,1,10,20,30,40,50]

RUNS_T10_ALL = ["1252","1259","1302","1304","1307","1309","1316","1341","1351","1416","1426","1451","1501","1526","1535","1601"]
RUNS_T10_UNB = ["1252","1259","1302","1304","1307","1309"]
RUNS_T10_B   = ["1316","1341","1351","1416","1426","1451","1501","1526","1535","1601"]
RUNS_T10_5m  = RUNS_T10_B[0::2]
RUNS_T10_30m = RUNS_T10_B[1::2]


usemeans = False
show_errorbars = True

# plot_runs(RUNS_T10_ALL, cg_perm(C_G18) , plot_raw=False, xlist=None, means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='Trial', suptitle="Module 58", labels=True, trial=10)


# plot_runs(RUNS_T9_M58, cg_perm(C_G18) , plot_raw=False, xlist=V_T9_M58, means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='bias voltage', suptitle="Module 58", labels=True, trial=9)

# suptitle = 'Channel {} distribution vs. bias voltage'.format("mean" if usemeans else "RMS")

# plot_runs(RUNS_T9_S2[-1:] , cg_list(CBLACK), plot_raw=False, xlist=V_T9_S2[-1:] , means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='bias voltage', suptitle='', labels="No keithley connection", trial=9, show=False)
# plot_runs(RUNS_T9_S2[:3]  , cg_list(CRED), plot_raw=False, xlist=V_T9_S2[:3]  , means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='bias voltage', suptitle='', labels=False, cxn=True, cxnlabel="Zero bias voltage", trial=9, show=False)
# plot_runs(RUNS_T9_S2[3:-1], cg_list(CBLUE) , plot_raw=False, xlist=V_T9_S2[3:-1], means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='bias voltage', suptitle=suptitle, labels=False, cxn=True, cxnlabel='Biased', trial=9)





# plot_runs(RUNS_T8_GLI_,     cg_perm(COLS_8), means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='trial number', suptitle='GLI test', trial=8,)
# #plot_runs(RUNS_T8_GROUNDS, cg_list(COLS_4), means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='trial number', suptitle='Ground test', trial=8,)

# plot_runs(RUNS_T8_NORMAL, cg_list(CBLACK), means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='trial', suptitle='', cxn=True, cxnlabel='Normal', labels=False, trial=8, show=False)
# plot_runs(RUNS_T8_GLI   , cg_list(CBLUE ), means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='trial', suptitle='', cxn=True, cxnlabel='GLI', labels=False, trial=8, show=False)
# #plot_runs(RUNS_T8_BOTH  , cg_list(CM    ), means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='trial', suptitle='', cxn=True, cxnlabel='Both', labels=False, trial=8, show=False)
# plot_runs(RUNS_T8_QG    , cg_list(CRED  ), means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='trial', suptitle='', cxn=True, cxnlabel='Qiet ground', labels=False, trial=8)


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

plot_freq_response = True
if plot_freq_response:
	plot_runs(RUNS_T1_FRQ   , cg_list(CBLACK)  , xlist = T1_FRQS  , means=False, trial=1, xlog=True, ylog=True, show_errorbars=False, labels=False, mean_marker='o', cxn=True, cxnlabel=None, show=False)
	plot_runs(RUNS_T2_FRQ   , cg_list(CRED  )  , xlist = T2_FRQS  , means=False, trial=2, xlog=True, ylog=True, show_errorbars=False, labels=False, mean_marker='o', cxn=True, cxnlabel="cable 1", show=False)
	plot_runs(RUNS_T5_C2[3:], cg_list(CGREEN), xlist = T5_FRQS_2, means=False, trial=5, xlog=True, ylog=True, show_errorbars=False, labels=False, mean_marker='o', cxn=True, cxnlabel="cable 3", show=False)
	plot_runs(RUNS_T5_C3[3:], cg_list(CBLUE) , xlist = T5_FRQS  , means=False, trial=5, xlog=True, ylog=True, show_errorbars=False, labels=False, mean_marker='o', cxn=True, cxnlabel="cable 4", suptitle="Mean of Channel RMS - Frequency Dependence", xlabel="signal frequency (Hz)", show=True)

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

# This data may be inaccurate (dry air)
# plot_runs(RUNS_T6_ALL, cg_list(CRED), trial=6)














