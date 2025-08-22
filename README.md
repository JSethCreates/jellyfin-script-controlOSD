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


## Features

 While the advanced visual adjustmetns  


## Installation

1. Download controlOSD.html to a 'UI' folder you create in the directory \Server\jellyfin-web\ 

2. Go to your \Server\jellyfin-web\ directory and search for 'index.html'. 

3. Open that file with notepad and right after you see "splashLogo{background-image:url(assets/img/banner-light.png)}}</style>" place this line:

<iframe src="/web/ui/SethsUI.html" style="display:none;"></iframe>

Then save the index.html file, hard reload your jellyfin page (Ctrl-Shift R  x2), and you should be able to navigate with the arrow keys.

## Usage

Most USB remotes send keyboard inputs 


## License

This project is licensed under the MIT License.
