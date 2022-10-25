#MenuTitle: AllCapFontSubsWriter
# -*- coding: utf-8 -*-
__doc__="""
Write substitution rules for all cap fonts in one batch.
"""

import GlyphsApp

Glyphs.showMacroWindow()
print('___Printing substituion rules___\n')
for myGlyph in Glyphs.font.glyphs:
	if (myGlyph.case == 1 and myGlyph.export == True):
		print ("sub " + myGlyph.name.lower() + " by " + myGlyph.name +";")