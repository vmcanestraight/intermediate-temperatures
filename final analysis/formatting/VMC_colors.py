from matplotlib.colors import LinearSegmentedColormap

def get_color(identifier):
    if isinstance(identifier, int):
        return get_color_list()[identifier]
    elif isinstance(identifier, str):
        return get_color_dict()[identifier]
   
def get_color_dict():
    return {'blue': "#2c457d",
                  'light blue': "#50c5db",
                  'orange':"#fe8f06",
                  'teal': "#4b8163",
                  'magenta': "#e30291",
                  'light purple': "#c6c0fe",
                  'purple': "#48006a",
                  'red': "#e60027",
                  'yellow green': "#c0e087"}

def get_color_list():
    return ["#2c457d","#50c5db","#fe8f06","#4b8163","#e30291","#c6c0fe","#48006a","#e60027","#c0e087"]

def get_cmap_dict():
    return {'purple_red' : LinearSegmentedColormap.from_list("custom_cmap", ["#c6c0fe" , "#e60027"]),
            'faux_inferno': LinearSegmentedColormap.from_list("custom_cmap", ['#fff37a', '#f48d5c', '#b53272', '#48006a', '#000000']),
            'faux_viridis': LinearSegmentedColormap.from_list("custom_cmap",  ['#fff37a', '#b1c268', '#669162', '#455871', '#48006a', '#000000'])}

def get_cmap(key):
    return get_cmap_dict()[key]