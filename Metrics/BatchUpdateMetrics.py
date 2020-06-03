#MenuTitle: Batch update Glyphs Metrics
# -*- coding: utf-8 -*-
__doc__="""
Update Glyph Metric on all Glyphs by given amount.
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
            "Batch update Glyphs Metrics", # window title
            autosaveName = "com.simonthi.BatchUpdateMetrics.mainwindow" # stores last window position and size
            )

        # UI elements:
        self.w.text1 = vanilla.TextBox( (sp, sp*1+txY*0, txX, txY), "Font units: 25", sizeStyle='regular' )
        self.w.units = vanilla.Slider( (sp+txX, sp*1+txY*0, 195, txY), value=0, minValue=-100, maxValue=100, callback=self.sliderCallback)

        # Run Button:
        self.w.runButton = vanilla.Button( (-sp-btnX, sp*0.75+txY*0, -sp, btnY), "Update Metrics", sizeStyle='regular', callback=self.updateMetrics)
        self.w.setDefaultButton( self.w.runButton)
        
        # Load Settings:
        if not self.LoadPreferences():
            print "Note: No preferences found. Will resort to defaults"

        # Open window and focus on it:
        self.w.open()
        self.w.makeKey()
        
    def SavePreferences( self, sender ):
        try:
            Glyphs.defaults["com.simonthi.BatchUpdateMetrics.units"] = int(self.w.units.get())
        except:
            return False
            
        return True

    def LoadPreferences( self ):
        try:
            self.w.text1.set( "Font units: %s" % Glyphs.defaults["com.simonthi.BatchUpdateMetrics.units"] )
            self.w.units.set(Glyphs.defaults["com.simonthi.BatchUpdateMetrics.units"])
        except:
            return False
            
        return True

    def sliderCallback( self, sender ):
        try:
            self.w.text1.set( "Font units: %s" % int(sender.get()) )
            self.SavePreferences(sender)
        except:
            return False

    def textCallback( self, sender ):
        try:
            theValue = int(sender.get())
            if not self.SavePreferences(sender):
                pass
        except:
            Glyphs.showMacroWindow()
            print "ENTER A NUMBER!"
    ## Truncate solution from https://realpython.com/python-rounding/#the-decimal-class
    def truncate( n, decimals ):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier

    def reSync( self ):
        font = Glyphs.font
        updateUnits = truncate(int(self.w.units.get()), 0)
        for myGlyph in Glyphs.font.glyphs:
            if myGlyph.leftMetricsKey != None and myGlyph.rightMetricsKey == None:
                myGlyph.layers[font.selectedLayers[0].layerId].syncMetrics()
            elif myGlyph.leftMetricsKey == None and myGlyph.rightMetricsKey != None:
                myGlyph.layers[font.selectedLayers[0].layerId].syncMetrics()
            elif myGlyph.leftMetricsKey != None and myGlyph.rightMetricsKey != None:
                myGlyph.layers[font.selectedLayers[0].layerId].syncMetrics()
        Glyphs.showMacroWindow()
        print "Glyph metrics updated by", updateUnits, "units" 

    def updateMetrics( self, sender ):
        font = Glyphs.font
        updateUnits = truncate(int(self.w.units.get()), 0)
        for myGlyph in Glyphs.font.glyphs:
            if myGlyph.leftMetricsKey == None and myGlyph.rightMetricsKey == None:
                myGlyph.layers[font.selectedLayers[0].layerId].LSB = myGlyph.layers[font.selectedLayers[0].layerId].LSB + updateUnits
                myGlyph.layers[font.selectedLayers[0].layerId].RSB = myGlyph.layers[font.selectedLayers[0].layerId].RSB + updateUnits
            elif myGlyph.leftMetricsKey != None and myGlyph.rightMetricsKey == None:
                myGlyph.layers[font.selectedLayers[0].layerId].RSB = myGlyph.layers[font.selectedLayers[0].layerId].RSB + updateUnits
            elif myGlyph.leftMetricsKey == None and myGlyph.rightMetricsKey != None:
                myGlyph.layers[font.selectedLayers[0].layerId].LSB = myGlyph.layers[font.selectedLayers[0].layerId].LSB + updateUnits
        self.reSync()


batchUpdate()