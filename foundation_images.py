# -*- coding: utf-8 -*-
"""
Foundation Images
=================

This plugin is mostly for the foundation theme I'm building
which allows one to easily insert centered images with captions
into posts. It's extremely basic and niche for now, but I might
make it more fully-featured later.
"""

from pelican import signals, contents
import re

replacementString = r'''<div class="row image-container">
	<div class="small-12 columns text-center">
		<div class="row">
			<div class="small-12 columns text-center image-image">
				<img src="\1"/>
			</div>
		</div>
		<div class="row image-caption">
			\2
		</div>
	</div>
</div>'''

def processImages(content):
	if isinstance(content, contents.Static):
		return
	
	text = re.sub(r"\{image-caption\[(?P<url>.*?)\]\[(?P<caption>.*?)\]\}", replacementString, content._content)
	content._content = text

def register():
	signals.content_object_init.connect(processImages)
