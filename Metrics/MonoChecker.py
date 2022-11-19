#MenuTitle: MonoChecker
# -*- coding: utf-8 -*-
__doc__="""
Check if all characters have the same width.
"""

import vanilla
import GlyphsApp
import codecs

class batchUpdate( object ):
    def __init__( self ):
        # Window 'self.w':
        edY = 22
        txX = 128
        txY = 17
        sp = 12
        btnX = 128
        btnY = 22
        windowWidth  = sp*4+txX+224+btnX
        windowHeight = sp*2+txY 

        self.w = vanilla.FloatingWindow(
            ( windowWidth, windowHeight ), # default window size
            "MonoChecker", # window title
            autosaveName = "com.simonthi.MonoChecker.mainwindow" # stores last window position and size
            )

        # UI elements:
        self.w.textAdd = vanilla.TextBox((10, 14, 128, 14), "Width of characters:", sizeStyle='small')
        self.w.text1 = vanilla.EditText((132, 12, 220, 19), "600", sizeStyle='small', callback=self.SavePreferences)

        # Run Button:
        self.w.runButton = vanilla.Button( (-sp-btnX, sp*0.75+txY*0, -sp, btnY), "Show", sizeStyle='regular', callback=self.printChars)
        self.w.setDefaultButton( self.w.runButton)
        
        # Load Settings:
        if not self.LoadPreferences():
            print('Note: No preferences found. Will resort to defaults')

        # Open window and focus on it:
        self.w.open()
        self.w.makeKey()
        
    def SavePreferences( self, sender ):
        try:
            Glyphs.defaults["com.simonthi.MonoChecker.text1"] = int(self.w.text1.get())
        except:
            return False
            
        return True

    def LoadPreferences( self ):
        try:
            self.w.text1.set( "%s" % Glyphs.defaults["com.simonthi.MonoChecker.text1"] )
        except:
            return False
            
        return True


    def textCallback( self, sender ):
        try:
            theValue = int(sender.get())
            if not self.SavePreferences(sender):
                pass
        except:
            Glyphs.showMacroWindow()
            print('ENTER A NUMBER!')
            

    def reSync( self ):
        font = Glyphs.font
        updateUnits = int(self.w.text1.get())
        charStore = []
        for myGlyph in Glyphs.font.glyphs:
            if myGlyph.layers[font.selectedLayers[0].layerId].width != updateUnits:
                charStore.append(myGlyph.string)
        toString = "".join(charStore) 
        print(toString)
        font.newTab(""+toString)

    def printChars( self, sender ):
        font = Glyphs.font
        updateUnits = int(self.w.text1.get())
        charStore = []
        for myGlyph in Glyphs.font.glyphs:
            if myGlyph.layers[font.selectedLayers[0].layerId].width != updateUnits:
                charStore.append(myGlyph.string)
        toString = "".join(charStore)
        print(toString)
        font.newTab(""+toString)


batchUpdate()