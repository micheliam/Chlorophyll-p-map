def look(name,label):
    cd = classmap.data
    obj = cd== label
    unique_array = np.unique(obj, return_counts=True)
    objcount = np.sum(obj)
    #obj = obj*1
    cdim = 27345 * 640
    coverage = objcount / cdim*100
    coverage1=round(coverage,2)
    #plt.figure()
    #plt.title(name+" Coverage: "+str(coverage1)+"%")
    #plt.imshow(obj, cmap='Greens')
    #plt.legend(handles=patches, loc=2, borderaxespad=0.)
    #plt.xlabel("X axis")
    #plt.ylabel("Y axis")
    return coverage, objcount,unique_array


a= classmap.data==40
a

#try with np.unique
turf = classmap.data==40
turf
count = np.sum(turf)
count
count/cdim*100
unique_array=np.unique(turf,return_counts=True)
unique_array
tape.shape
cdim
1249920/17500800*100

tape = classmap.data==48
unique_array=np.unique(tape,return_counts=True)
unique_array.shape

x = np.array([True,False,True])
unique, counts = np.unique(x, return_counts=True)


print np.asarray((unique, counts)).T



tapecount = tape * 1
tapecount.shape
tapecount = np.sum(tapecount)
tapecount
tape

cdim = 27345 * 640
coverage = objcount / cdim * 100
unique_array=np.unique(a,return_index=True)
unique_array