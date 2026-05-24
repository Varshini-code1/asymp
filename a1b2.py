import matplotlib.pyplot as pt
Names=['Yasa', 'Damian', 'Raji', 'Tanisha', 'Usra', 'Vira', 'Madu' ]
age=[16,20,42,10,80, 54, 61]
pt.plot (Names, age)
pt.xlabel('Name of person')
pt.ylabel('Age of person')
pt.title('Name Vs. Age')
pt.grid()
pt.show()