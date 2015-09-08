import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
from numpy import loadtxt
import time



totalStart = time.time()

date,bid,ask = np.loadtxt('GBPUSD1d.txt', unpack=True,
                              delimiter=',',
                              converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})






def percentChange(startPoint,currentPoint):
    try:
        x = ((float(currentPoint)-startPoint)/abs(startPoint))*100.00
        if x == 0.0:
            return 0.000000001
        else:
            return x
    except:
        return 0.0001


def patternStorage():
    '''
    The goal of patternFinder is to begin collection of %change patterns
    in the tick data. From there, we also collect the short-term outcome
    of this pattern. Later on, the length of the pattern, how far out we
    look to compare to, and the length of the compared range be changed,
    and even THAT can be machine learned to find the best of all 3 by
    comparing success rates.'''

    startTime = time.time()
    
    
    x = len(avgLine)-30
    y = 31
    currentStance = 'none'
    
    while y < x:
        pattern = []
        
        p1 = percentChange(avgLine[y-30], avgLine[y-29])
        p2 = percentChange(avgLine[y-30], avgLine[y-28])
        p3 = percentChange(avgLine[y-30], avgLine[y-27])
        p4 = percentChange(avgLine[y-30], avgLine[y-26])
        p5 = percentChange(avgLine[y-30], avgLine[y-25])
        p6 = percentChange(avgLine[y-30], avgLine[y-24])
        p7 = percentChange(avgLine[y-30], avgLine[y-23])
        p8 = percentChange(avgLine[y-30], avgLine[y-22])
        p9 = percentChange(avgLine[y-30], avgLine[y-21])
        p10= percentChange(avgLine[y-30], avgLine[y-20])
		
        p11 = percentChange(avgLine[y-30], avgLine[y-19])
        p12 = percentChange(avgLine[y-30], avgLine[y-18])
        p13 = percentChange(avgLine[y-30], avgLine[y-17])
        p14 = percentChange(avgLine[y-30], avgLine[y-16])
        p15 = percentChange(avgLine[y-30], avgLine[y-15])
        p16 = percentChange(avgLine[y-30], avgLine[y-14])
        p17 = percentChange(avgLine[y-30], avgLine[y-13])
        p18 = percentChange(avgLine[y-30], avgLine[y-12])
        p19 = percentChange(avgLine[y-30], avgLine[y-11])
        p20= percentChange(avgLine[y-30], avgLine[y-10])
		
        p21 = percentChange(avgLine[y-30], avgLine[y-9])
        p22 = percentChange(avgLine[y-30], avgLine[y-8])
        p23 = percentChange(avgLine[y-30], avgLine[y-7])
        p24 = percentChange(avgLine[y-30], avgLine[y-6])
        p25 = percentChange(avgLine[y-30], avgLine[y-5])
        p26 = percentChange(avgLine[y-30], avgLine[y-4])
        p27 = percentChange(avgLine[y-30], avgLine[y-3])
        p28 = percentChange(avgLine[y-30], avgLine[y-2])
        p29 = percentChange(avgLine[y-30], avgLine[y-1])
        p30= percentChange(avgLine[y-30], avgLine[y])


        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]

        try:
            avgOutcome = reduce(lambda x, y: x + y, outcomeRange) / len(outcomeRange)
        except Exception, e:
            print str(e)
            avgOutcome = 0
        futureOutcome = percentChange(currentPoint, avgOutcome)

        '''
        print 'where we are historically:',currentPoint
        print 'soft outcome of the horizon:',avgOutcome
        print 'This pattern brings a future change of:',futureOutcome
        print '_______'
        print p1, p2, p3, p4, p5, p6, p7, p8, p9, p10
        '''

        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)

        pattern.append(p11)
        pattern.append(p12)
        pattern.append(p13)
        pattern.append(p14)
        pattern.append(p15)
        pattern.append(p16)
        pattern.append(p17)
        pattern.append(p18)
        pattern.append(p19)
        pattern.append(p20)

        pattern.append(p21)
        pattern.append(p22)
        pattern.append(p23)
        pattern.append(p24)
        pattern.append(p25)
        pattern.append(p26)
        pattern.append(p27)
        pattern.append(p28)
        pattern.append(p29)
        pattern.append(p30)



        patternAr.append(pattern)
        performanceAr.append(futureOutcome)
        
        y+=1

    endTime = time.time()
    # print len(patternAr)
    # print len(performanceAr)
    print 'Pattern storing took:', endTime-startTime


def currentPattern():
    mostRecentPoint = avgLine[-1]

    curPatStartTime = time.time()

    cp1 = percentChange(avgLine[-31],avgLine[-30])
    cp2 = percentChange(avgLine[-31],avgLine[-29])
    cp3 = percentChange(avgLine[-31],avgLine[-28])
    cp4 = percentChange(avgLine[-31],avgLine[-27])
    cp5 = percentChange(avgLine[-31],avgLine[-26])
    cp6 = percentChange(avgLine[-31],avgLine[-25])
    cp7 = percentChange(avgLine[-31],avgLine[-24])
    cp8 = percentChange(avgLine[-31],avgLine[-23])
    cp9 = percentChange(avgLine[-31],avgLine[-22])
    cp10= percentChange(avgLine[-31],avgLine[-21])
	
	
    cp11 = percentChange(avgLine[-31],avgLine[-20])
    cp12 = percentChange(avgLine[-31],avgLine[-19])
    cp13 = percentChange(avgLine[-31],avgLine[-18])
    cp14 = percentChange(avgLine[-31],avgLine[-17])
    cp15 = percentChange(avgLine[-31],avgLine[-16])
    cp16 = percentChange(avgLine[-31],avgLine[-15])
    cp17 = percentChange(avgLine[-31],avgLine[-14])
    cp18 = percentChange(avgLine[-31],avgLine[-13])
    cp19 = percentChange(avgLine[-31],avgLine[-12])
    cp20= percentChange(avgLine[-31],avgLine[-11])
	
    cp21 = percentChange(avgLine[-31],avgLine[-10])
    cp22 = percentChange(avgLine[-31],avgLine[-9])
    cp23 = percentChange(avgLine[-31],avgLine[-8])
    cp24 = percentChange(avgLine[-31],avgLine[-7])
    cp25 = percentChange(avgLine[-31],avgLine[-6])
    cp26 = percentChange(avgLine[-31],avgLine[-5])
    cp27 = percentChange(avgLine[-31],avgLine[-4])
    cp28 = percentChange(avgLine[-31],avgLine[-3])
    cp29 = percentChange(avgLine[-31],avgLine[-2])
    cp30= percentChange(avgLine[-31],avgLine[-1])

    patForRec.append(cp1)
    patForRec.append(cp2)
    patForRec.append(cp3)
    patForRec.append(cp4)
    patForRec.append(cp5)
    patForRec.append(cp6)
    patForRec.append(cp7)
    patForRec.append(cp8)
    patForRec.append(cp9)
    patForRec.append(cp10)
    patForRec.append(cp11)
    patForRec.append(cp12)
    patForRec.append(cp13)
    patForRec.append(cp14)
    patForRec.append(cp15)
    patForRec.append(cp16)
    patForRec.append(cp17)
    patForRec.append(cp18)
    patForRec.append(cp19)
    patForRec.append(cp20)
    patForRec.append(cp21)
    patForRec.append(cp22)
    patForRec.append(cp23)
    patForRec.append(cp24)
    patForRec.append(cp25)
    patForRec.append(cp26)
    patForRec.append(cp27)
    patForRec.append(cp28)
    patForRec.append(cp29)
    patForRec.append(cp30)

    currentPatEndTime = time.time()

    print 'CurrentPattern took:', currentPatEndTime -curPatStartTime



def graphRawFX():
    
    fig=plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
    ax1.plot(date,bid)
    ax1.plot(date,ask)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    plt.grid(True)
    for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask-bid), facecolor='g',alpha=.3)

    plt.subplots_adjust(bottom=.23)
    plt.show()



    
def patternRecognition():
    patRecStartTime = time.time()
    ######
    predictedOutcomesAr = []
    ######
    plotPatAr = []
    patFound = 0

    for eachPattern in patternAr:
        totalSim = 0
        for i in range(0,10):
          sim = 100 - abs(percentChange(eachPattern[i]), patForRec[i])
          totalSim += sim
          if sim <= 50:
            break
        if i >= 10:
          howSim = totalSim / 10.00
        if homSim > 70:
            patFound = 1
            plotPatAr.append(eachPattern)

    patloopEndTime = time.time()
    print 'Pattern loop took:', patloopEndTime - patRecStartTime

    predArray = []
    if patFound == 1:
        #fig = plt.figure(figsize=(10,6))

        for eachPatt in plotPatAr:
            futurePoints = patternAr.index(eachPatt)

            if performanceAr[futurePoints] > patForRec[29]:
                pcolor = '#24bc00'
                #####
                predArray.append(1.000)
            else:
                pcolor = '#d40000'
                #######
                predArray.append(-1.000)

            #plt.plot(xp, eachPatt)
            predictedOutcomesAr.append(performanceAr[futurePoints])
            #plt.scatter(35, performanceAr[futurePoints],c=pcolor,alpha=.4)

        patfutureEndTime = time.time()
        print 'Pattern future loop took:', patfutureEndTime - patloopEndTime

        realOutcomeRange = allData[toWhat+20:toWhat+30]

        if(len(realOutcomeRange) > 0):


            realAvgOutcome = reduce(lambda x, y: x + y, realOutcomeRange) / len(realOutcomeRange)
            predictedAvgOutcome = reduce(lambda x, y: x + y, predictedOutcomesAr) / len(predictedOutcomesAr)

            realMovement = percentChange(allData[toWhat],realAvgOutcome)
            #######
            # print predArray
            predictionAverage = reduce(lambda x, y: x + y, predArray) / len(predArray)
            # print predictionAverage
            if predictionAverage < 0:
                # print 'drop predicted'
                # print patForRec[29]
                # print realMovement
                if realMovement < patForRec[29]:
                    accuracyArray.append(100)
                else:
                    accuracyArray.append(0)

            if predictionAverage > 0:
                # print 'rise predicted'
                # print patForRec[29]
                # print realMovement
                if realMovement > patForRec[29]:
                    accuracyArray.append(100)
                else:
                    accuracyArray.append(0)

    patRecEndTime = time.time()

    print 'Pattern patternRecognition took:', patRecEndTime - patRecStartTime
                                    #######
                                    #plt.scatter(40, realMovement, c='#54fff7',s=25)
                                    #plt.scatter(40, predictedAvgOutcome, c='#008db8',s=25)
                                    #plt.plot(xp, patForRec, '#54fff7', linewidth = 3)
                                    #plt.grid(True)
                                    #plt.title('Pattern Recognition.\nCyan line is the current pattern. Other lines are similar patterns from the past.\nPredicted outcomes are color-coded to reflect a positive or negative prediction.\nThe Cyan dot marks where the pattern went.\nOnly data in the past is used to generate patterns and predictions.')
                                    #plt.show()
            
            


dataLength = int(bid.shape[0])
# print 'data length is', dataLength
allData = ((bid+ask)/2)
toWhat = 55000


avgLine = ((bid+ask)/2)
patternAr = []
performanceAr = []
patternStorage()

######
accuracyArray = []

####
samps = 0
while toWhat < dataLength:
    ######
    
    

    avgLine = avgLine[:toWhat]
    patForRec = []
    currentPattern()
    patternRecognition()

    # print accuracyArray
    accuracyAverage = reduce(lambda x, y: x + y, accuracyArray) / len(accuracyArray)
    
    toWhat += 1
    samps +=1
    print 'Backtested Accuracy is',str(accuracyAverage)+'% after',samps,'actionable trades'

totalEnd = time.time()-totalStart

print 'Entire (18) processing took:',totalEnd,'seconds'