# This script contains Monash specific extensions to the omegalib Menu
# to use it import the script into default_init.py
# and call MonashMenu.addMonashMenu() at the end of _onAppStart()


#exporting the monashmenu variable globally
global monmnu

# put in our menu stuff here
def addMonashMenu(mainmnu):
  global monmnu
  monmnu = mainmnu.addSubMenu("Monash")
  #look at function for comments
  mi = monmnu.addButton("echo CameraPreset", "MonashMenu.printCameraSettings(getDefaultCamera())")
  mi.getButton().setCheckable(False) 

#just a helper method to easily create camera presets. 
#This funtion prints the camera position and orientation to the console and one should copy paste from there 
#to add a camera preset button to his application
def printCameraSettings(camera):
  pos=camera.getPosition()
  ori=camera.getOrientation().get_euler()
  print("Add the following line of code to your application script")
  print("mainmnu.addButton(\"PRESETNAME\", \"MonashMenu.SetCamera(getDefaultCamera(),"+str(pos)+",Vector3"+str(ori)+")\")")
  #for example: mi = monmnu.addButton("PresetFoo", "MonashMenu.SetCamera(getDefaultCamera(),Vector3(0.00, 0.00, 0.00),Vector3(-1.7019994854927065, 2.7755575615628914e-17, -0.300000011920929))")

#setting the viewer camera by the viewerposition and viewerorientation. data should be obtained by printCameraSettings
def SetCamera(camera,pos,euler):
  from euclid import Quaternion
  camera.setPosition(pos)
  camera.setOrientation(Quaternion().new_rotate_euler(euler[0],euler[1],euler[2]))
