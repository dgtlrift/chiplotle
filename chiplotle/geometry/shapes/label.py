from chiplotle.geometry.core.label import Label

def label(text,
            charwidth,
            charheight,
            charspace = None,
            linespace = None,
            origin = 'bottom-left'):
    return Label(text, charwidth, charheight, charspace, linespace, origin)

def labelCat(label,
            text,
            charwidth,
            charheight,
            charspace = None,
            linespace = None,
            origin = 'bottom-left'):
    if label is None:
        return Label(text, charwidth, charheight, charspace, linespace, origin)
    else:
	return label.cat(text, charwidth, charheight, charspace, linespace, origin)
