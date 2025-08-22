<<<<<<< HEAD
# ControlOSD  
*A Jellyfin UI Enhancement script*

## Purpose  
This unified script adjusts **navigation accessibility** & simplifies Jellyfin’s **On-Screen Display (OSD)** in any client which uses JFweb by:  

1. **Providing universal adaptive controller/keyboard/remote navigation** by overriding Jellyfin’s (imo broken) ‘TV-mode’, ensuring smooth-ish dynamically updating focus handling on any client (Windows, Linux, Android devices & tvboxes, Firesticks, browsers etc.) which uses a webview wrapper.  
=======
# ControlOSD

A Jellyfin UI Enhancement script

## Purpose
   This unified script adjusts Jellyfin’s On-Screen Display
   and navigation accessibility in any client which uses JFweb by:


   1. Providing universal keyboard/remote navigation by overriding
     Jellyfin’s (imo broken) TV-mode, ensuring smooth focus handling on
     any client (Windows, Linux, Android boxes, Firesticks etc.).


   2. Injecting styles and java adjustments beyond Jellyfin’s custom CSS system, removing clutter,
     and reshaping the NowPlaying (Video) OSD into two modes:
       • Simple OSD: minimal, pause + timeline only
       • Command OSD: extended with plot, artwork, and extras

>>>>>>> 990f2ada46abcab1596c067f1ec09f01405f66fd

2. **Injecting styles and JavaScript adjustments** beyond Jellyfin’s custom CSS system, removing redundant UI clutter, and reshaping the NowPlaying (Video) OSD into two modes:  
   - **Simple OSD**: minimal, pause + timeline only  
   - **Extended OSD**: extended with plot, artwork, and extras  

<<<<<<< HEAD
This also helps **users who face neuro or motor challenges with complex UIs**. The simple OSD pares it down to just a pause button and timeline, keeping controls clear and easy to manage.  

## Features  
While the visual & OSD adjustments will be divisive, the main point of this script is to extend **accessibility for users on webview clients** (like tablets / Firesticks / Android boxes with sideloaded Android Jellyfin apks) to use **Adaptive Controllers** ([Xbox Adaptive Controller](https://www.xbox.com/en-US/accessories/controllers/xbox-adaptive-joystick)) rather than touch input.  
=======
 While the advanced visual adjustmetns  


## Installation

1. Download controlOSD.html to a 'UI' folder you create in the directory \Server\jellyfin-web\ 

2. Go to your \Server\jellyfin-web\ directory and search for 'index.html'. 

3. Open that file with notepad and right after you see "splashLogo{background-image:url(assets/img/banner-light.png)}}</style>" place this line:

<iframe src="/web/ui/SethsUI.html" style="display:none;"></iframe>

Then save the index.html file, hard reload your jellyfin page (Ctrl-Shift R  x2), and you should be able to navigate with the arrow keys.

## Usage

Most USB remotes send keyboard inputs 

>>>>>>> 990f2ada46abcab1596c067f1ec09f01405f66fd

## Installation  
1. Download **controlOSD.html** to a `UI` folder you create in the directory:  
   ```
   \Server\jellyfin-web   ```  

2. Go to your `\Server\jellyfin-web\` directory and search for **index.html**.  

3. Open that file with Notepad and, right after you see:  
   ```
   splashLogo{background-image:url(assets/img/banner-light.png)}}</style>
   ```  
   place this line:  
   ```html
   <iframe src="/web/UI/controlOSD.html" style="display:none;"></iframe>
   ```  

4. Save the **index.html** file, restart the server, hard reload your Jellyfin page (**Ctrl+Shift+R twice** to clear browser cache), and you should be able to navigate with the arrow keys and enter.  

## Usage  
Most **Adaptive Controllers (or USB remotes)** send inputs as keyboard keystrokes. This script intercepts those keypresses and uses them to navigate the Jellyfin UI (similar to link tab hopping) and attempts to initialize focus on the play/pause, startnext, home buttons on pages where they are most appropriate.  

- **Arrow Keys**: Navigation through cards and links  
- **Enter**: Select Item, Play/Pause Toggle  
- **Arrow Up (in NowPlaying/video mode)**: Toggle extended OSD information and controls  

## TODO  
- [ ] Currently the script works best with [jellyfin-theme-sethstyle](https://github.com/JSethCreates/jellyfin-theme-sethstyle). Better, more universal highlighting for other themes coming soon.  
- [ ] Add swipe up to toggle extended OSD in case of a touch-only client.  
- [ ] Fix extras blocking input after OSD fades if untoggled.  

## License  
This project is licensed under the **MIT License**.  
