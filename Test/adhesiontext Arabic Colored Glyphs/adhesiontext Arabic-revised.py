#MenuTitle: adhesiontext Arabic Colored Glyphs
# -*- coding: utf-8 -*-
__doc__="""
adhesiontext Arabic that is sensitive to positional forms. Choose which charcters to include by giving them a color in the Glyphs UI or include all.
"""

import vanilla
import GlyphsApp
from random import shuffle
import codecs

theScriptLoc = os.path.dirname(os.path.abspath(__file__))
dicFileLocation = os.path.join(theScriptLoc, 'adhesiontext Arabic Dictionary.txt')

class adhesiontextArabic( object ):
    def __init__( self ):
        # Window 'self.w':
        edY = 22
        txX = 128
        txY = 17
        sp = 12
        btnX = 80
        btnY = 22
        windowWidth  = sp*4+txX+224+btnX
        windowHeight = sp*6.5+txY 

        self.w = vanilla.FloatingWindow(
            ( windowWidth, windowHeight ), # default window size
            "adhesiontext Arabic, Layer Color", # window title
            autosaveName = "com.simonthi.adhesiontextArabic.mainwindow" # stores last window position and size
            )
        
        arabicDic = open(dicFileLocation, 'r')

        # UI elements:
        self.w.text1 = vanilla.TextBox( (sp, sp*1+txY*0, txX, txY), "Words: 25", sizeStyle='regular' )
        self.w.words = vanilla.Slider( (sp+txX, sp*1+txY*0, 195, txY), value=25, minValue=5, maxValue=200, callback=self.sliderCallback)

        #UI check color
        self.w.check = vanilla.CheckBox( (sp, sp*1+txY*1.5, txX, txY), "Include color", sizeStyle='regular')
        
        # UI color elements:
        self.w.text2 = vanilla.TextBox( (sp, sp*1+txY*3, txX, txY), "Color: red", sizeStyle='regular' )
        self.w.color = vanilla.Slider( (sp+txX, sp*1+txY*3, 195, txY), value=0, minValue=0, maxValue=11, callback=self.sliderCallback1)
        
        # Run Button:
        self.w.runButton = vanilla.Button( (-sp-btnX, sp+txY*3, -sp, btnY), "Get text", sizeStyle='regular', callback=self.typeset)
        self.w.setDefaultButton( self.w.runButton)
        
        # Load Settings:
        if not self.LoadPreferences():
            print "Note: 'adhesiontext Arabic' could not load preferences. Will resort to defaults"

        # Open window and focus on it:
        self.w.open()
        self.w.makeKey()
        
    def SavePreferences( self, sender ):
        try:
            Glyphs.defaults["com.simonthi.adhesiontextArabic.words"] = int(self.w.words.get())
            Glyphs.defaults["com.simonthi.adhesiontextArabic.check"] = int(self.w.check.get())
            Glyphs.defaults["com.simonthi.adhesiontextArabic.color"] = int(self.w.color.get())
        except:
            return False
            
        return True

    def LoadPreferences( self ):
        try:
            self.w.text1.set( "Words: %s" % Glyphs.defaults["com.simonthi.adhesiontextArabic.words"] )
            self.w.words.set(Glyphs.defaults["com.simonthi.adhesiontextArabic.words"])
            self.w.check.set(Glyphs.defaults["com.simonthi.adhesiontextArabic.check"])
            colorChanger = ["red", "orange", "brown", "yellow", "light green", "dark green", "light blue", "dark blue", "purple", "magenta", "light gray", "charcoal"]
            self.w.text2.set( "Color: %s" % colorChanger[Glyphs.defaults["com.simonthi.adhesiontextArabic.color"]] )
            self.w.color.set(Glyphs.defaults["com.simonthi.adhesiontextArabic.color"])
        except:
            return False
            
        return True

    def sliderCallback( self, sender ):
        try:
            self.w.text1.set( "Words: %s" % int(sender.get()) )
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


    def sliderCallback1( self, sender ):
        try:
            colorChanger = ["red", "orange", "brown", "yellow", "light green", "dark green", "light blue", "dark blue", "purple", "magenta", "light gray", "charcoal"]
            self.w.text2.set( "Color: %s" %  colorChanger[int(sender.get())])
            self.SavePreferences(sender)
        except:
            return False

    
    def typeset( self, sender ):
        try:
            f = Glyphs.font # frontmost font
            m = f.selectedFontMaster # active master

            f.disableUpdateInterface() # suppresses UI updates in Font View

            necessaryWords = int(self.w.words.get())
            sourceWordsCount = 10000 # the dictionary will be random-shrunk to this number of words
            
            colorUI = int(self.w.color.get())

            includeColor = int(self.w.check.get())

            arabicDic = codecs.open(dicFileLocation, 'r', encoding='utf-8')
            arabicWords = [l[:-1] for l in arabicDic.readlines()]
            shuffle(arabicWords)
            arabicWords = arabicWords[:sourceWordsCount]

            breakers = ['alef-ar', "alefHamzaabove-ar", "alefHamzabelow-ar", "alefMadda-ar", "alefWasla-ar", 'waw-ar', 'dal-ar', 'thal-ar', 'reh-ar', 'zain-ar', "noonghunna-ar", "tehMarbuta-ar", "waw-ar", "wawHamzaabove-ar","lam_alef-ar", "lam_alefHamzaabove-ar", "lam_alefHamzabelow-ar", "lam_alefMadda-ar", "lam_alefWasla-ar",]
            if includeColor == 1:
                arabGlyphs = [g.name for g in f.glyphs if g.script=='arabic' and g.category=='Letter' and g.color==colorUI and (len(g.layers[m.id].paths)>0 or len(g.layers[m.id].components)>0)]
            else:
                arabGlyphs = [g.name for g in f.glyphs if g.script=='arabic' and g.category=='Letter' and (len(g.layers[m.id].paths)>0 or len(g.layers[m.id].components)>0)]
            # clean arabGlyphs further by removing empty components
            removeFromArabGlyphs = []
            for g in arabGlyphs:
                l = f.glyphs[g].layers[m.id]
                if len(l.components) > 0:
                    for c in l.components:
                        if f.glyphs[c.componentName] is None:
                            removeFromArabGlyphs.append(g)
                        elif len(f.glyphs[c.componentName].layers[m.id].paths) == 0:
                            removeFromArabGlyphs.append(g)
            removeFromArabGlyphs = list(set(removeFromArabGlyphs))
            arabGlyphs = [g for g in arabGlyphs if g not in removeFromArabGlyphs]

            arabGlyphsUnicode = [] # the list of unique Arabic letters, not glyphs. Used for initial filtering of the words list.
            for g in arabGlyphs:
                if 'init' in g or 'medi' in g or 'fina' in g:
                    arabGlyphsUnicode.append( g[:-5] )
            arabGlyphsUnicode = list(set(arabGlyphsUnicode))

            # filtering 1
            arabicWordsSimpler1 = []
            for w in arabicWords:
                niceNameList = [Glyphs.niceGlyphName(l) for l in w]
                if len(set(niceNameList) - set(arabGlyphsUnicode) ) == 0:
                    arabicWordsSimpler1.append(niceNameList)

            # filtering 2
            arabicWordsSimpler2 = []
            for niceNameList in arabicWordsSimpler1:
                newWord = []
                preJoining = False
                for nn in niceNameList:
                    if preJoining is False:
                        if nn in breakers:
                            newWord.append(nn)
                            preJoining = False
                        else:
                            newWord.append(nn+'.init')
                            preJoining = True
                    else: 
                        if nn in breakers:
                            newWord.append(nn+'.fina')
                            preJoining = False
                        else:
                            newWord.append(nn+'.medi')
                            preJoining = True
                newWord[-1] = newWord[-1][:-5]+'.fina' if 'medi' in newWord[-1] else newWord[-1]
                newWord[-1] = newWord[-1][:-5] if 'init' in newWord[-1] else newWord[-1]
                # newWord is made, now evaluate
                if len( set(newWord) - set(arabGlyphs) ) == 0:
                    arabicWordsSimpler2.append(newWord)

            shuffle(arabicWordsSimpler2)
            if len(arabicWordsSimpler2) < necessaryWords:
                arabicWordsSimpler2 = arabicWordsSimpler2 * ((necessaryWords / len(arabicWordsSimpler2)) + 1)
                shuffle(arabicWordsSimpler2)
            arabicWordsSimpler2 = arabicWordsSimpler2[:necessaryWords]
            if f.currentTab == None:
                f.newTab()
            f.currentTab.text = '  '.join(['/'+'/'.join(w) for w in arabicWordsSimpler2])

            f.enableUpdateInterface() # re-enables UI updates in Font View
        except Exception, e:
            if arabGlyphs == []:
                Glyphs.showMacroWindow()
                print "No glyphs matching that color"
            else:
            # brings macro window to front and reports fallback error:
                Glyphs.showMacroWindow()
                print "adhesiontext Arabic Error: %s" % e

adhesiontextArabic()