# ControlOSD  
*A Jellyfin UI Enhancement script*


![1](https://github.com/JSethCreates/jellyfin-script-controlOSD/blob/main/screenshots/1.PNG?raw=true)
**(Simple OSD with added media logo)**

## Purpose  
While the visual & OSD adjustments will be divisive, the main point of this script is demonstrate how to extend accessibility for users on webview clients (like tablets / Firesticks / Android boxes to use **Adaptive Controllers** ([Eg. Xbox Adaptive Controller](https://www.xbox.com/en-US/accessories/controllers/xbox-adaptive-joystick)) rather than touch input. THe side benefit is this works with common usb remote controls as well, allowing a consistent experience between all devices from PC to TV.

## Features  
This unified script adjusts **navigation accessibility** & simplifies Jellyfin’s **On-Screen Display (OSD)** in any client which uses JFweb by:  

1. **Providing universal adaptive controller/keyboard/remote navigation** by overriding Jellyfin’s (imo broken) ‘TV-mode’, ensuring smooth-ish dynamically updating focus handling on any client (Windows, Linux, Android devices & tvboxes, Firesticks, browsers etc.) which uses a webview wrapper.  

2. **Injecting styles and JavaScript adjustments** beyond Jellyfin’s custom CSS system, removing redundant UI clutter, and reshaping the NowPlaying (Video) OSD into two modes:  
   - **Simple OSD**: minimal, pause + timeline only  
   - **Extended OSD**: extended with plot, artwork, and extras  

This helps users who face neuro or motor challenges with complex UIs. The simple OSD pares it down to just a pause button and timeline, keeping controls clear and easy to manage. This also allows users to enjoy CSS themes and plugins with remote control navigation and thus the experience does not have to be different from PC to an AndroidTV Box or Firestick for example. 


## Installation  
1. Download **controlOSD.html** to a `UI` folder you create, a \Server\jellyfin-web\UI\ directory.  

2. Go back to your `\Server\jellyfin-web\` directory and search for **index.html**.  

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

![2](https://github.com/JSethCreates/jellyfin-script-controlOSD/blob/main/screenshots/2.PNG?raw=true)
**(Extended OSD with Clearart, Plot, and additional metadata)**

## TODO  
- [ ] Currently the script was made for & works best with the [GNAT Theme](https://github.com/JSethCreates/jellyfin-theme-sethstyle). Better, more universal highlighting for other themes coming soon.  
- [ ] Add swipe up to toggle extended OSD in case of a touch-only client.  
- [ ] Fix extras blocking input after OSD fades if untoggled.  

## License  
This project is licensed under the **MIT License**.  
