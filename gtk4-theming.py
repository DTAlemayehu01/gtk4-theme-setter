#!/bin/python3

import sys
import os
import subprocess as sp

home_dir = os.getenv('HOME')
xdg_data_home = os.getenv('XDG_DATA_HOME')
if xdg_data_home is None:
    xdg_data_home = os.path.join(home_dir, '.local', 'share')
config_dir = os.getenv('XDG_CONFIG_HOME') 
if config_dir is None:
    config_dir = os.path.join(home_dir, ".config")

themes_dir = [
        os.path.join(os.sep, 'usr','share','themes'), 
        os.path.join(xdg_data_home,"themes"),
        os.path.join(home_dir,".themes")
]

class gtkfiles:
    def __init__(self, path):
        self.gtk_css = os.path.join(path, 'gtk-4.0', 'gtk.css')
        self.gtk_css_dark = os.path.join(path, 'gtk-4.0', 'gtk-dark.css')
        self.gtk_assets = os.path.join(path, 'gtk-4.0', 'assets')
        self.config_assets = os.path.join(path, 'assets')

def uninstall_theme(gtkconfig):
    print(f'\n***\nRemoving set theme!\n***\n')
    sp.run(["rm", gtkconfig.gtk_css]) 
    sp.run(["rm", gtkconfig.gtk_css_dark])
    sp.run(["rm", gtkconfig.gtk_assets])
    sp.run(["rm", gtkconfig.config_assets])
    return

def install_theme(gtktheme, gtkconfig):
    print(f'\n***\nSetting new theme!\n***\n')
    sp.run(["ln", "-s", gtktheme.gtk_css, gtkconfig.gtk_css])
    sp.run(["ln", "-s", gtktheme.gtk_css_dark, gtkconfig.gtk_css_dark])
    sp.run(["ln", "-s", gtktheme.gtk_assets, gtkconfig.gtk_assets])
    sp.run(["ln", "-s", gtktheme.config_assets,gtkconfig.config_assets])

def get_themes():
    all_themes = []
    for theme_dir in themes_dir:
        if not os.path.exists(theme_dir):
            continue
        for theme in os.listdir(theme_dir):
            all_themes.append(os.path.join(theme_dir, theme))
    return all_themes

def menu(all_themes):
    print("Select theme: ")
    for i, theme in enumerate(all_themes):
        print(f'{i+1}. {theme}')
    print("e. Exit")
    chk = input("Your choice: ")
    if chk == "e":
        print("Bye bye!")
        sys.exit()
    return all_themes[int(chk)-1]

if __name__ == "__main__":
    config_files = gtkfiles(config_dir)
    if "--reset" in sys.argv:
        uninstall_theme(config_files)
    else:
        themes = get_themes()
        while True:
            try:
                theme = menu(themes)
                gtk_files = gtkfiles(theme)
                uninstall_theme(config_files)
                install_theme(gtk_files, config_files)
                sys.exit()
            except ValueError as e:
                print("Input a value displayed")

