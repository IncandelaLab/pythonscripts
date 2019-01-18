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
COLS_12 = [[0,129],[0,100,200],[0,192]]
C_G27  = [[0,100,200],[0,100,200],[0,100,200]]
C_G18  = [[0,128,256],[0,100,200],[0,255]]




CWD    = os.getcwd()
FOLDERS  = 'trial{}'
PFOLDERS = 'RUN_{}_plots'

FILE   = 'rms_summary_sca_1.txt'

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

RUNS = [None]*11 + [RUNS_T11, RUNS_T12]

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


usemeans = False
show_errorbars = True


plot_runs(RUNS_T12_INTER, cg_list(COLS_2), plot_raw=False, xlist=[0,1], means=usemeans, mean_marker='o',show_errorbars=show_errorbars,xlabel='',suptitle='interposer coparison',labels=True,trial=12)

plot_runs(RUNS_T12_NOHPF[:3], cg_list(CBLACK ), plot_raw=False, xlist=[0.0,1.0,2.0], means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='', suptitle='antenna effect', labels=False, xlog=False, ylog=False, cxn=True, cxnlabel='no HPF'         , trial=12, show=False)
plot_runs(RUNS_T12_HPF[:2]  , cg_list(CRED   ), plot_raw=False, xlist=[0.1,    2.1], means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='', suptitle='antenna effect', labels=False, xlog=False, ylog=False, cxn=True, cxnlabel='160Hz HPF'      , trial=12, show=False)
plot_runs(RUNS_T12_5K_1[:3] , cg_list(CGREEN ), plot_raw=False, xlist=[0.2,1.2,2.2], means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='', suptitle='antenna effect', labels=False, xlog=False, ylog=False, cxn=True, cxnlabel='5kHz HPF, Set 1', trial=12, show=False)
plot_runs(RUNS_T12_5K_2[:3] , cg_list(CBLUE  ), plot_raw=False, xlist=[0.3,1.3,2.3], means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='', suptitle='antenna effect', labels=False, xlog=False, ylog=False, cxn=True, cxnlabel='5kHz HPF, Set 2', trial=12)

plot_runs(RUNS_T12_NOHPF[3:], cg_list(CBLACK ), plot_raw=False, xlist=T12_FRQ_NOHPF, means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='frequency', suptitle='250mV noise', labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='no HPF'   , trial=12, show=False)
plot_runs(RUNS_T12_HPF[2:]  , cg_list(CRED   ), plot_raw=False, xlist=T12_FRQ_HPF  , means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='frequency', suptitle='250mV noise', labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='160Hz HPF', trial=12, show=False)
plot_runs(RUNS_T12_5K_1[3:] , cg_list(CGREEN ), plot_raw=False, xlist=T12_FRQ_HPF  , means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='frequency', suptitle='250mV noise', labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='5kHz HPF, Set 1', trial=12,show=False)
plot_runs(RUNS_T12_5K_2[3:] , cg_list(CBLUE  ), plot_raw=False, xlist=T12_FRQ_HPF  , means=usemeans, mean_marker='o', show_errorbars=show_errorbars, xlabel='frequency', suptitle='250mV noise', labels=False, xlog=True, ylog=True, cxn=True, cxnlabel='5kHz HPF, Set 2', trial=12)



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
