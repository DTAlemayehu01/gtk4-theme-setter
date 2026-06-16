import sys
import os
import subprocess as sp

/usr/share/themes
$XDG_DATA_HOME/themes
~/.themes

home_dir = os.getenv('HOME')
xdg_data_home = os.getenv('XDG_DATA_HOME')
config_dir = ".config"

themes_dir = [
        os.path.join('usr','share','themes'), 
        os.path.join(xdg_data_home,"themes"),
        os.path.join(home_dir,".themes")
]

def uninstall_theme():
    print(f'\n***\nResetting theme to default!\n***\n')
    sp.run(["rm", f'{home_dir}{config_dir}/gtk-4.0/gtk.css'])
    sp.run(["rm", f'{home_dir}{config_dir}/gtk-4.0/gtk-dark.css'])
    sp.run(["rm", f'{home_dir}{config_dir}/gtk-4.0/assets'])
    sp.run(["rm", f'{home_dir}{config_dir}/assets'])
    return

def install_theme():
        sp.run(["ln", "-s", f'{home_dir}{themes_dir}/{chk_theme}/gtk-4.0/gtk.css', f'{home_dir}{config_dir}/gtk-4.0/gtk.css'])
        sp.run(["ln", "-s", f'{home_dir}{themes_dir}/{chk_theme}/gtk-4.0/gtk-dark.css', f'{home_dir}{config_dir}/gtk-4.0/gtk-dark.css'])
        sp.run(["ln", "-s", f'{home_dir}{themes_dir}/{chk_theme}/gtk-4.0/assets', f'{home_dir}{config_dir}/gtk-4.0/assets'])
        sp.run(["ln", "-s", f'{home_dir}{themes_dir}/{chk_theme}/assets', f'{home_dir}{config_dir}/assets'])

def get_themes():
    all_themes = []
    for theme_dir in themes_dir:
        all_themes.append(str(sp.run(["ls", theme_dir], stdout=sp.PIPE).stdout.decode("UTF-8")).split())
    return all_themes

def set_theme(theme_input):
    try:
        theme_idx = int(theme_input)-1
        chk_theme = all_themes[chk_value]
        print(f'\n***\nChoosed {chk_theme}\n***\n')
        print("Removing previous theme...")

        uninstall_themes()

        print("Installing new theme...")


def menu(all_themes):
    print("Select theme: ")
    for i, theme in enumerate(all_themes):
        print(f'{i+1}. {theme}')
    print("e. Exit")
    chk = input("Your choice: ")
    if chk == "e":
        print("Bye bye!")
        sys.exit()
    return chk
