class Phone:
     def __init__(self,brand,model,color): # function to initialize car details
         self.brand = brand # Instance attribute for phone brand
         self.model = model # Instance attribute for phone model
         self.color = color # Instance attribute for phone color

samsung_1= Phone("z-fold","fold6","grey")
samsung_2= Phone("galaxy","s21","silver")
samsung_3= Phone("galaxy","s22-ultra","gold")
iphone=   Phone("iphone-16","pro-max","black")
print(f" the brand name is {samsung_1.brand},the model is{samsung_1.model},the color is {samsung_1.color}")
print(f" the brand name is {samsung_2.brand},the model is{samsung_2.model},the color is {samsung_2.color}")
print(f" the brand name is {samsung_3.brand},the model is{samsung_3.model},the color is {samsung_3.color}")
print(f" the brand name is {iphone.brand},the model is{iphone.model},the color is {iphone.color}")
