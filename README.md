<h1>Soundspire</h1>

This is a capstone project that aims to take data from .midi files and translate that to coordinates, edges and faces in a 3D space, hopefully making a 3D model based on how the program interprets the data.<br>

This project is heavily based in Blender and utilizes the Blender API, Python Scripts and external Python Midi Libraries, so you will need to install them onto your computer in order for this program to work...<br>

Playlist is here: https://www.youtube.com/playlist?list=PLg6uxUmvfCjP_n6_9g4Jg76WziWpGKU9A<br>

<h3>Part 1: Install MuseScore</h3>
<ul>
    <li>Musescore is free to download and install on your computer.</li>
    <li>Looking at musescore for the first time might be intimidating, but for our purposes, we'll be making something simple. In the video, I just create a simple C scale, but I discuss other methods to obtain midi files.</li>
    <li>https://youtu.be/xzgx34wspjk</li>
</ul>
<h3>Part 2: Install Blender and Python</h3>
<ul>
    <li>Blender is a game engine, 3D modelling software and renderer. An all-in-one package essentially!</li>
    <li>It can be found here at https://www.blender.org/</li>
    <li>Follow the installation instructions normally, it shouldn't be difficult (or painful) to do.</li>
    <li>Open blender for the first time to verify the version of python it has installed.</li>
        <ol>
            <li>Click anywhere to get rid of the splash screen.</li>
            <li>Press Ctrl+Right Arrow key until you get to a screen that has the python console below</li>
            <li>Record the version of python it states right next to the words "Python Interactive Console" in the black terminal.</li>
            <li>Close Blender</li>
        </ol>
    <li>Navigate to where Blender is installed</li>
        <ol>
            <li>This can be done by left-clicking on the blender icon on your desktop or in the windows menu and select the option to "Open File Location"</li>
            <li>If it opens up to a file explorer window with the shortcuts, just left click on the blender icon in the folder and repeat the same action you did for step 1</li>
            <li>Open the folder that has the Blender version number on it and you'll see a folder labelled "python"</li>
            <li>Move or delete this folder. What this does is it forces Blender to rely on the system to provide the python libraries.</li>
        </ol>
    <li>https://youtu.be/A2xdNfAEBXo</li>
</ul>
    
<h3>Part 3: Install Mido</h3>
<ul>
    <li>Remember that python version you wrote down earlier? Well do a google/bing/whatever internet search like "python 3.5.3 download" on google and you should be taken to the python website that will allow you to install that version of python.</li>
    <li>Once you install python, you will need to open up the command line and type in <code>pip install mido</code></li>
    <li>Once you're done installing the packages, thats it!</li>
    <li>Keep in mind, that if you reinstall blender, you need to make sure that the version of python you have installed on your system matches it! Otherwise things won't work!</li>
    <li>https://youtu.be/IFtT18l6VWQ</li>
</ul>
    

<h3>Part 4: Working with "Soundspire"</h3>
<ul>
    <li>https://youtu.be/Qx8TuhVSNy0</li>
</ul>

Have fun with this :)
