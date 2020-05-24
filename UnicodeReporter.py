#MenuTitle: UnicodeReporter
# -*- coding: utf-8 -*-
__doc__="""
Report Glyphs with double and no Unicode assignments.
"""

import GlyphsApp

Glyphs.showMacroWindow()
print('___Double Unicodes___')
for myGlyph in Glyphs.font.glyphs:
	if myGlyph.unicodes != None:
		if len(myGlyph.unicodes)>1:
			print myGlyph.name
print('___No Unicode Assigned___')
for myGlyph in Glyphs.font.glyphs:
	if myGlyph.unicodes == None:
		print myGlyph.name