#chose 10 random pixels

#pixel 1
P1 = c.data[20111 ,340]
P1.shape
plt.plot(P1)
Pders10 = signal.savgol_filter(P1, window_length=9, polyorder=2,deriv=0)
plt.plot(Pders10)
Pders12 = signal.savgol_filter(P1, window_length=7, polyorder=2,deriv=2)
plt.plot(Pders12)


#pixel 2
P2 = c.data[2014 ,120]
plt.plot(P2)
Pders20 = signal.savgol_filter(P2, window_length=3, polyorder=2,deriv=0)
plt.plot(Pders20)
Pders22 = signal.savgol_filter(P2, window_length=3, polyorder=2,deriv=2)
#plt.plot(Pders22)


#pixel 3
P3 = c.data[1026 ,81]
P3.shape
plt.plot(P3)

Pders30 = signal.savgol_filter(P3, window_length=3, polyorder=2,deriv=0)
plt.plot(Pders30)
Pders32 = signal.savgol_filter(P3, window_length=3, polyorder=2,deriv=2)
#plt.plot(Pders32)

#pixel 4
P4 = c.data[761 ,53]
P4.shape
plt.plot(P4)

Pders40 = signal.savgol_filter(P4, window_length=3, polyorder=2,deriv=0)
plt.plot(Pders40)
Pders42 = signal.savgol_filter(P4, window_length=3, polyorder=2,deriv=2)
#plt.plot(Pders42)

#pixel 5
P5 = c.data[151,189]
P5.shape
plt.plot(P5)

Pders50 = signal.savgol_filter(P5, window_length=3, polyorder=2,deriv=0)
plt.plot(Pders50)
Pders52 = signal.savgol_filter(P5, window_length=3, polyorder=2,deriv=2)
#plt.plot(Pders52)

#pixel 6
P6 = c.data[7191 ,13]
P6.shape
plt.plot(P6)

Pders60 = signal.savgol_filter(P6, window_length=3, polyorder=2,deriv=0)
plt.plot(Pders60)
Pders62 = signal.savgol_filter(P6, window_length=3, polyorder=2,deriv=2)
#plt.plot(Pders62)

#pixel 7
P7 = c.data[421 ,223]
P7.shape


#pixel 8
P8 = c.data[7191 ,13]
P8.shape
plt.plot(P8)

Pders80 = signal.savgol_filter(P8, window_length=3, polyorder=2,deriv=0)
plt.plot(Pders80)
Pders82 = signal.savgol_filter(P8, window_length=3, polyorder=2,deriv=2)
#plt.plot(Pders82)


#pixel 9
P9 = c.data[10 ,130]
P9.shape
plt.plot(P9)

Pders90 = signal.savgol_filter(P9, window_length=3, polyorder=2,deriv=0)
plt.plot(Pders90)
Pders92 = signal.savgol_filter(P9, window_length=3, polyorder=2,deriv=2)
#plt.plot(Pders92)

#pixel 10
P10 = c.data[563 ,454]
P10.shape
plt.plot(P10)

Pders100 = signal.savgol_filter(P10, window_length=17, polyorder=16,deriv=0)
plt.plot(Pders100)
Pders102 = signal.savgol_filter(P10, window_length=3, polyorder=2,deriv=2)
#plt.plot(Pders102)


# plotting x y axis
ax = plt.gca()
ax.set_xlabel("Wavelength, nm")
ax.set_ylabel("Reflectance")



#comparing window length 3, 5, 7, 9,

P7 = c.data[10765 ,339]
P7.shape
plt.plot(P10)

#raw data
plt.plot(P7,'-r', label='raw data', linewidth=2)

#SG filter
Pders70 = signal.savgol_filter(P7, window_length=9, polyorder=2,deriv=0)
plt.plot(Pders70,'-k', label='wl=9 polyorder=2 der=0')
Pders73 = signal.savgol_filter(P7, window_length=7, polyorder=2,deriv=0)
plt.plot(Pders73,'-g', label='wl=7 polyorder=2 der=0')
Pders75 = signal.savgol_filter(P7, window_length=5, polyorder=2,deriv=0)
plt.plot(Pders75,'-y', label='wl=5 polyorder=2 der=0')
Pders79 = signal.savgol_filter(P7, window_length=3, polyorder=2,deriv=0)
plt.plot(Pders79,'--b', label='wl=3 polyorder=2 der=0')


#Pders715 = signal.savgol_filter(P7, window_length=15, polyorder=2,deriv=2)
#plt.plot(Pders715,'-g', label='wl=15 polyorder=2 der=2')
plt.legend()

#creating function to explore the analysis of candidate spectra


# calculating second derivative ONLY AT 675NM
# select only 675nm in cube data to cl
cl= c[: ,: ,275]
#check dimension
cl.shape
cl.shape
Pder675= np.zeros((2000 ,640 ,1))
# calculate dericative
Pder675= signal.savgol_filter(cl, window_length=9, polyorder=3, deriv=2)
Pder675
#clip
Pder675=Pder675.clip(0)
#to check maximum
Pder675.shape
#to check maximum
np.amax(Pder675)
ax=plt.gca()
# plot
plt.imshow(Pder675, cmap ='Greens_r')
#show image
shw=ax.imshow(Pder675)
#make bar
bar=plt.colorbar(shw)
#show label
plt.xlabel('X')
plt.ylabel('Y')
bar.set_label('ColorBar')
plt.show()

#END



#wa = c.data


#def my_function(wa):
 #   print(my_function)



# calculating chl-a in 1 pixel
#Pder = np.zeros((1 ,1 ,400))
#for x in range (0, 1):
    #for y in range (0, 1):
        #P = c.data[y ,x]
        #Pder[y ,x] = signal.savgol_filter(P, window_length=9, polyorder=3, deriv=2)


#P = c.data[1 ,1]
#Pder = signal.savgol_filter(P, window_length=9, polyorder=3, deriv=2)

# plotting spectral reflectance
#plt.plot(c.W.data ,Pder)
#ax = plt.gca()
#ax.set_xlabel("Wavelength, nm")
#ax.set_ylabel("Reflectance")

# getting value at 675 nm

#Pder[275]

# calculating second derivative on Y=0-2000 X=0-640
#Pder = np.zeros((2000 ,640 ,400))
#for y in range (0, 2000)
    #for x in range (0, 640):
        #P = c.data[y ,x]
        #Pder[y ,x] = signal.savgol_filter(P, window_length=9, polyorder=3, deriv=2)
        #plt.show()

#Pder.shape


#Pder
# checking Pder dimension
#Pder.shape

# filtering 675nm only
#m = Pder[: ,: ,275]

# checking dimension
#m.shape

# plot
#m = Pder[: ,: ,275]
#plt.imsh\
# ow(m, cmap ='Greens_r')


#check a single spectrum of 10 pixel
#s1=c[399:400,310:311,:];s1.shape
#s2=c[399:400,311:312,:]
#s3=c[399:400,312:313,:]
#s4=c[399:400,313:314,:]
#s5=c[399:400,314:315,:]
#s6=c[399:400,315:316,:]
#s7=c[399:400,316:317,:]
#s8=c[399:400,317:318,:]
#s9=c[399:400,318:319,:]
#s10=c[399:400,319:320,:]




# Function to calculate the exponential with constants a and b
def exponential(x, a, b):
    return a*np.exp(b*x)
# Generate dummy dataset
x_dummy = np.linspace(start=5, stop=15, num=50)
x_dummy.shape
# Calculate y-values based on dummy x-values
y_dummy = exponential(x_dummy, 0.5, 0.5)
y_dummy.shape