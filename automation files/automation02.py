#Python Workshop Lesson:Automation02
#http://www.designalyze.com/automateGHwithRhinoScript_02

import rhinoscriptsyntax as rs
import Rhino
import time
 
#Load Grasshopper plugin as gh
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
 
#SetSliderValue("GUID",Number)
 
rs.EnableRedraw(True)
 
for i in range(0,3,1):
    gh.SetSliderValue("GUID_FOR_SLIDER_1",i)
    for j in range(0,2,1):
        gh.SetSliderValue("GUID_FOR_SLIDER_2",j)
        gh.RunSolver("FILENAME.gh")
        time.sleep(1)
