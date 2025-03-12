#example 1
color = input("fill the target color: ")
class Vehicle:
    def __init__(model, name, color):
        model.name = name
        model.color = color

    def get_name(model):
        print("Vehicle name is %s" % model.name)
 
    def get_color(model):
        print("Vehicle color is %s" % model.color) 

Information = Vehicle("Hossein",color)
Information.get_name()
Information.get_color()


#example 2

class Vehicle:
    color = input()
    def __init__(model, name):
        model.name = name
        model.color = Vehicle.color

    def get_name(model):
        print("Vehicle name is %s" % model.name)
 
    def get_color(model):
        print("Vehicle color is %s" % model.color) 

Information = Vehicle("Hossein")
Information.get_name()
Information.get_color()


# example 3
color = input()

class Vehicle:
    def __init__(model, name):
        model.name = name

    def get_name(model):
        print("Vehicle name is %s" % model.name)
 
    def get_color(model):
        print("Vehicle color is %s" % color) 

Information = Vehicle("Hossein")
Information.get_name()
Information.get_color()