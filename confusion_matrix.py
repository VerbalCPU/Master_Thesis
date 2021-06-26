from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from pycm import *




#Individual Items high
# cm3 = ConfusionMatrix(matrix={"Gun": {"Gun": 0, "Knife":0,"Wrench":0,"Pliers":0,"Scissors":0},
#                             "Knife": {"Gun": 8, "Knife":0,"Wrench":0,"Pliers":4,"Scissors":12},
#                             "Wrench": {"Gun": 0, "Knife":0,"Wrench":0,"Pliers":0,"Scissors":0},
#                             "Pliers":{"Gun": 0, "Knife":5,"Wrench":0,"Pliers":12,"Scissors":4},
#                             "Scissors":{"Gun": 0, "Knife":0,"Wrench":0,"Pliers":0,"Scissors":0}},transpose=False)
#
# cm3.plot(cmap=plt.cm.Blues,normalized=True,title='Low Energy Channels Individual Items',number_label=True,plot_lib="seaborn")

#Individual Items mid
# cm3 = ConfusionMatrix(matrix={"Gun": {"Gun": 0, "Knife":0,"Wrench":0,"Pliers":0,"Scissors":0},
#                             "Knife": {"Gun": 0, "Knife":0,"Wrench":0,"Pliers":6,"Scissors":18},
#                             "Wrench": {"Gun": 0, "Knife":0,"Wrench":0,"Pliers":0,"Scissors":0},
#                             "Pliers":{"Gun": 0, "Knife":12,"Wrench":0,"Pliers":0,"Scissors":0},
#                             "Scissors":{"Gun": 0, "Knife":0,"Wrench":0,"Pliers":0,"Scissors":0}},transpose=False)
#
# cm3.plot(cmap=plt.cm.Blues,normalized=True,title='Medium Energy Channels Individual Items',number_label=True,plot_lib="seaborn")

#Individual Items high
# cm3 = ConfusionMatrix(matrix={"Gun": {"Gun": 0, "Knife":0,"Wrench":0,"Pliers":0,"Scissors":0},
#                             "Knife": {"Gun": 0, "Knife":0,"Wrench":0,"Pliers":6,"Scissors":18},
#                             "Wrench": {"Gun": 0, "Knife":0,"Wrench":0,"Pliers":0,"Scissors":0},
#                             "Pliers":{"Gun": 0, "Knife":5,"Wrench":0,"Pliers":3,"Scissors":4},
#                             "Scissors":{"Gun": 0, "Knife":0,"Wrench":0,"Pliers":0,"Scissors":0}},transpose=False)
#
# cm3.plot(cmap=plt.cm.Blues,normalized=True,title='High Energy Channels Individual Items',number_label=True,plot_lib="seaborn")

#Clustered Items Low
# cm3 = ConfusionMatrix(matrix={"Gun": {"Gun": 0, "Knife":0,"Wrench":0,"Pliers":0,"Scissors":0},
#                             "Knife": {"Gun": 0, "Knife":4,"Wrench":0,"Pliers":1,"Scissors":16},
#                             "Wrench": {"Gun": 0, "Knife":0,"Wrench":0,"Pliers":0,"Scissors":0},
#                             "Pliers":{"Gun": 0, "Knife":0,"Wrench":0,"Pliers":1,"Scissors":15},
#                             "Scissors":{"Gun": 0, "Knife":0,"Wrench":0,"Pliers":10,"Scissors":14}},transpose=False)
#
# cm3.plot(cmap=plt.cm.Blues,normalized=True,title='Low Energy Channels Clustered Items',number_label=True,plot_lib="seaborn")

# #Clustered Items medium
# cm3 = ConfusionMatrix(matrix={"Gun": {"Gun": 0, "Knife":0,"Wrench":0,"Pliers":0,"Scissors":0},
#                             "Knife": {"Gun": 0, "Knife":27,"Wrench":0,"Pliers":12,"Scissors":1},
#                             "Wrench": {"Gun": 0, "Knife":0,"Wrench":0,"Pliers":0,"Scissors":0},
#                             "Pliers":{"Gun": 0, "Knife":6,"Wrench":0,"Pliers":8,"Scissors":0},
#                             "Scissors":{"Gun": 0, "Knife":5,"Wrench":0,"Pliers":0,"Scissors":1}},transpose=False)
#
# cm3.plot(cmap=plt.cm.Blues,normalized=True,title='Medium Energy Channels Clustered Items',number_label=True,plot_lib="seaborn")

cm3 = ConfusionMatrix(matrix={"Gun": {"Gun": 0, "Knife":0,"Wrench":0,"Pliers":0,"Scissors":0},
                            "Knife": {"Gun": 0, "Knife":9,"Wrench":0,"Pliers":9,"Scissors":8},
                            "Wrench": {"Gun": 0, "Knife":0,"Wrench":0,"Pliers":0,"Scissors":0},
                            "Pliers":{"Gun": 0, "Knife":0,"Wrench":0,"Pliers":14,"Scissors":8},
                            "Scissors":{"Gun": 0, "Knife":5,"Wrench":0,"Pliers":6,"Scissors":4}},transpose=False)

cm3.plot(cmap=plt.cm.Blues,normalized=True,title='High Energy Channels Clustered Items',number_label=True,plot_lib="seaborn")



print(cm3)
plt.show()
