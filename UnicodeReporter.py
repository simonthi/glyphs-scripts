#MenuTitle: UnicodeReporter
# -*- coding: utf-8 -*-
__doc__="""
Report Glyphs with double and no Unicode assignments.
"""

import GlyphsApp

Glyphs.showMacroWindow()
print('___Glyphs with more than one Unicodes___')
for myGlyph in Glyphs.font.glyphs:
	if myGlyph.unicodes != None:
		if len(myGlyph.unicodes)>1:
			print myGlyph.name myGlyph.unicodes
print('___Glyphs with no Unicode Assigned___')
for myGlyph in Glyphs.font.glyphs:
	if myGlyph.unicodes == None:
		print myGlyph.name