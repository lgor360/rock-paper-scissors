import gi
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
import os
import random

current_dir = os.path.dirname(os.path.abspath(__file__))

def setulabel(u):
    if u:
        if u == 1:
            userl.set_label("user selection: rock")
        elif u == 2:
            userl.set_label("user selection: scissors")
        elif u == 3:
            userl.set_label("user selection: paper")
    return


def setpclabel(pc):
    if pc:
        if pc == 1:
            pcl.set_label("pc selection: rock")
        elif pc == 2:
            pcl.set_label("pc selection: scissors")
        elif pc == 3:
            pcl.set_label("pc selection: paper")
    return


def infgame(button):
    with open(os.path.join(current_dir, "data/license.txt"), "r", encoding="utf-8") as f:
       license = f.read()

    ab = Gtk.AboutDialog()
    ab.set_program_name("rock-paper-scissors")
    ab.set_comments("some cool game :D\nthe game was made in 2024\ni say hello from Russia!")
    ab.set_authors(["Igor360"])
    ab.set_website("https://github.com/pyminigames/rock-paper-scissors")
    ab.set_license(license)
    ic = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, "data/icon.png"))
    icon = ic.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
    ab.set_logo(icon)
    ab.connect("response", lambda dialog, response: dialog.destroy())
    ab.show()


def check(event, useritem):
    pcitem = random.randint(1, 3)
    if pcitem == useritem:
        p = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/pc/notone.png"))
        pc = p.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
        pcpov.set_from_pixbuf(pc)
        us = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/user/notone.png"))
        user = us.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
        userpov.set_from_pixbuf(user)
    elif pcitem == 1:
        if useritem == 3:
            p = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/pc/sad.png"))
            pc = p.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
            pcpov.set_from_pixbuf(pc)
            us = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/user/happy.png"))
            user = us.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
            userpov.set_from_pixbuf(user)
        if useritem == 2:
            p = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/pc/happy.png"))
            pc = p.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
            pcpov.set_from_pixbuf(pc)
            us = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/user/sad.png"))
            user = us.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
            userpov.set_from_pixbuf(user)
    elif pcitem == 2:
        if useritem == 1:
            p = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/pc/sad.png"))
            pc = p.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
            pcpov.set_from_pixbuf(pc)
            us = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/user/happy.png"))
            user = us.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
            userpov.set_from_pixbuf(user)
        if useritem == 3:
            p = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/pc/happy.png"))
            pc = p.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
            pcpov.set_from_pixbuf(pc)
            us = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/user/sad.png"))
            user = us.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
            userpov.set_from_pixbuf(user)
    elif pcitem == 3:
        if useritem == 2:
            p = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/pc/sad.png"))
            pc = p.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
            pcpov.set_from_pixbuf(pc)
            us = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/user/happy.png"))
            user = us.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
            userpov.set_from_pixbuf(user)
        if useritem == 1:
            p = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/pc/happy.png"))
            pc = p.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
            pcpov.set_from_pixbuf(pc)
            us = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/user/sad.png"))
            user = us.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
            userpov.set_from_pixbuf(user)
    setpclabel(pcitem)
    setulabel(useritem)


def main():
    window = Gtk.Window(title="rock-paper-scissors")
    window.set_icon_from_file(os.path.join(current_dir, "data/icon.png"))
    window.set_default_size(450, 250)
    window.set_resizable(False)
    window.connect("destroy", Gtk.main_quit)

    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    window.add(box)
    
    grid = Gtk.Grid()
    grid.set_row_homogeneous(True)

    about = Gtk.Button(label="about this game")
    about.connect("clicked", infgame)
    about.set_hexpand(True)
    box.pack_end(about, False, True, 0)

    rock = Gtk.Button(label="rock")
    rock.connect("clicked", check, 1)
    rock.set_hexpand(True)
    grid.attach(rock, 0, 0, 1, 1)

    ser = Gtk.Button(label="scissors")
    ser.connect("clicked", check, 2)
    ser.set_hexpand(True)
    grid.attach(ser, 1, 0, 1, 1)

    paper = Gtk.Button(label="paper")
    paper.connect("clicked", check, 3)
    paper.set_hexpand(True)
    grid.attach(paper, 2, 0, 1, 1)

    box.pack_start(grid, False, True, 0)

    label = Gtk.Label(label="pick your item")
    box.pack_start(label, False, True, 0)

    s = Gtk.Separator()
    s.set_size_request(-1, 2.5)
    box.pack_start(s, False, True, 0)

    imbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    imbox.set_homogeneous(True)
    box.pack_start(imbox, False, True, 0)

    pcbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    imbox.pack_start(pcbox, False, True, 0)

    global pcpov
    p = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/pc/happy.png"))
    pc = p.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
    pcpov = Gtk.Image.new_from_pixbuf(pc)
    pcbox.pack_start(pcpov, False, True, 0)
   
    global pcl
    pcl = Gtk.Label(label="pc selection: none")
    pcbox.add(pcl)

    userbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    imbox.pack_start(userbox, False, True, 0)

    global userpov
    us = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, f"data/user/happy.png"))
    user = us.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
    userpov = Gtk.Image.new_from_pixbuf(user)
    userbox.pack_start(userpov, False, True, 0)
   
    global userl
    userl = Gtk.Label(label="user selection: none")
    userbox.add(userl)


    window.show_all()
    Gtk.main()


main()