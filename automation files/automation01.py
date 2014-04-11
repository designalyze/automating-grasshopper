#Python Workshop Lesson:Automation01
#http://www.designalyze.com/automateGHwithRhinoScript_01

import rhinoscriptsyntax as rs
import Rhino
import time
 
 
#Load Grasshopper plugin as gh
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
 
### This is used to print the method names ###
for func in dir(gh):
    if not func.startswith('_'): print func
