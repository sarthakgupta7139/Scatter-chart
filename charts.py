from matplotlib import pyplot as plt

l1=['sarthak','arjun','aaryan','pulkit','pallav']
l2=[96,95,97,96,96]
plt.plot(l1,l2,'r<')
#plt.bar(l1,l2)
#plt.hist(l2)
#clrs=['r','b','m','g','k']
#plt.scatter(l1,l2,c=clrs)
plt.title('RESULTS')
plt.xlabel('Name')
plt.ylabel('Marks')
plt.show()
