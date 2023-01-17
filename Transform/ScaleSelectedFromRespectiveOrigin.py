#MenuTitle: Scale selected shapes from respective origin
# -*- coding: utf-8 -*-
__doc__="""
Scale selcted shapes by given factor from their given origin.
"""

import vanilla
import GlyphsApp
import math
            
            
            
class scale( object ):
    def __init__( self ):
        # Window 'self.w':
        edY = 22
        txX = 96
        txY = 17
        sp = 12
        btnX = 128
        btnY = 22
        windowWidth  = sp*4+txX+224+btnX-24
        windowHeight = sp*2+txY+72

        self.w = vanilla.FloatingWindow(
            ( windowWidth, windowHeight ), # default window size
            "Scale selected shapes from center", # window title
            autosaveName = "com.simonthi.Scale.mainwindow" # stores last window position and size
            )

        # UI elements:
        self.w.text1 = vanilla.TextBox( (sp, sp*1+txY*0+1, txX, txY), "Scale factor:", sizeStyle='regular' )
        self.w.units = vanilla.EditText( (sp, txY+sp+8, 48, txY+4), "1", callback=self.inputCallback)
        self.w.text2 = vanilla.TextBox( (128, sp*1+txY*0+1, 256, txY), "Scale origin (Vertical, Horizontal):", sizeStyle='regular' )
        self.w.originY = vanilla.RadioGroup((128, txY+sp+8, -sp, 64), ["Top", "Center", "Bottom"])
        self.w.originX = vanilla.RadioGroup((224, txY+sp+8, -sp, 64), ["Left", "Center", "Right"])

        # Run Button:
        self.w.runButton = vanilla.Button( (-sp-btnX, sp*0.75+txY*0+72, -sp, btnY), "Scale", sizeStyle='regular', callback=self.scale)
        self.w.setDefaultButton( self.w.runButton)
        
        # Load Settings:
        if not self.LoadPreferences():
            print ("Note: No preferences found. Will resort to defaults")

        # Open window and focus on it:
        self.w.open()
        self.w.makeKey()
        
    def SavePreferences( self, sender ):
        try:
            Glyphs.defaults["com.simonthi.Scale.units"] = self.w.units.get()
            Glyphs.defaults["com.simonthi.Origin.originy"] = float(self.w.originY.get())
            Glyphs.defaults["com.simonthi.Origin.originx"] = float(self.w.originX.get())
        except:
            return False
            
        return True

    def LoadPreferences( self ):
        try:
            self.w.text1.set( "Scale factor:" )
            self.w.units.set(Glyphs.defaults["com.simonthi.Scale.units"])
            self.w.originY.set(Glyphs.defaults["com.simonthi.Origin.originy"])
            self.w.originX.set(Glyphs.defaults["com.simonthi.Origin.originx"])
        except:
            return False
            
        return True

    def textCallback( self, sender ):
        try:
            self.w.text1.set( "Scale factor:")
            self.SavePreferences(sender)
        except:
            return False

    def inputCallback( self, sender ):
        try:
            theValue = float(sender.get().replace('', '1'))
            if not self.SavePreferences(sender):
                pass
        except:
            Glyphs.showMacroWindow()
            print ("Please enter a number!")
            

    def reSync( self ):
        selectedLayers = Glyphs.font.selectedLayers
        transformFaktor = float(self.w.units.get())
        flag = False
        for thisLayer in selectedLayers:
            for thisPath in thisLayer.paths:
                if thisPath.selected == True:
                    if(self.w.originY.get() == 1 and self.w.originX.get() == 1):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x+thisPath.bounds.size.width/2)*(1-(transformFaktor)), (thisPath.bounds.origin.y+thisPath.bounds.size.height/2)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 0 and self.w.originX.get() == 0):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x)*(1-(transformFaktor)), (thisPath.bounds.origin.y+thisPath.bounds.size.height)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 0 and self.w.originX.get() == 1):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x+thisPath.bounds.size.width/2)*(1-(transformFaktor)), (thisPath.bounds.origin.y+thisPath.bounds.size.height)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 0 and self.w.originX.get() == 2):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x+thisPath.bounds.size.width)*(1-(transformFaktor)), (thisPath.bounds.origin.y+thisPath.bounds.size.height)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 1 and self.w.originX.get() == 0):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x)*(1-(transformFaktor)), (thisPath.bounds.origin.y+thisPath.bounds.size.height/2)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 1 and self.w.originX.get() == 2):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x+thisPath.bounds.size.width)*(1-(transformFaktor)), (thisPath.bounds.origin.y+thisPath.bounds.size.height/2)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 2 and self.w.originX.get() == 0):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x)*(1-(transformFaktor)), (thisPath.bounds.origin.y)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 2 and self.w.originX.get() == 1):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x+thisPath.bounds.size.width/2)*(1-(transformFaktor)), (thisPath.bounds.origin.y)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 2 and self.w.originX.get() == 2):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x+thisPath.bounds.size.width)*(1-(transformFaktor)), (thisPath.bounds.origin.y)*(1-(transformFaktor))))
                    flag = True
                    
        if (flag == False):
            Glyphs.showMacroWindow()
            print ("Nothing selected. \nPlease select shapes to transform.")

    def scale( self, sender ):
        selectedLayers = Glyphs.font.selectedLayers
        transformFaktor = float(self.w.units.get())
        for thisLayer in selectedLayers:
            for thisPath in thisLayer.paths:
                if thisPath.selected == True:
                    if(self.w.originY.get() == 1 and self.w.originX.get() == 1):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x+thisPath.bounds.size.width/2)*(1-(transformFaktor)), (thisPath.bounds.origin.y+thisPath.bounds.size.height/2)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 0 and self.w.originX.get() == 0):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x)*(1-(transformFaktor)), (thisPath.bounds.origin.y+thisPath.bounds.size.height)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 0 and self.w.originX.get() == 1):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x+thisPath.bounds.size.width/2)*(1-(transformFaktor)), (thisPath.bounds.origin.y+thisPath.bounds.size.height)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 0 and self.w.originX.get() == 2):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x+thisPath.bounds.size.width)*(1-(transformFaktor)), (thisPath.bounds.origin.y+thisPath.bounds.size.height)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 1 and self.w.originX.get() == 0):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x)*(1-(transformFaktor)), (thisPath.bounds.origin.y+thisPath.bounds.size.height/2)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 1 and self.w.originX.get() == 2):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x+thisPath.bounds.size.width)*(1-(transformFaktor)), (thisPath.bounds.origin.y+thisPath.bounds.size.height/2)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 2 and self.w.originX.get() == 0):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x)*(1-(transformFaktor)), (thisPath.bounds.origin.y)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 2 and self.w.originX.get() == 1):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x+thisPath.bounds.size.width/2)*(1-(transformFaktor)), (thisPath.bounds.origin.y)*(1-(transformFaktor))))
                    elif(self.w.originY.get() == 2 and self.w.originX.get() == 2):
                        thisPath.applyTransform(((transformFaktor), 0.0, 0.0, (transformFaktor), (thisPath.bounds.origin.x+thisPath.bounds.size.width)*(1-(transformFaktor)), (thisPath.bounds.origin.y)*(1-(transformFaktor))))
        self.reSync()


scale()