1: Get the latest Raspbian Jessie image from raspberry pi website

2: Copy the image to an SD card

3: Steps to turning on your pi 
  a: connect your pi to a tv
  b: connect a usb keyboard/mouse
  c: if you're using a pi2 connect a wifi device as well (you may have problems with your setup pi3 is highly recommended)

4: Go to the Raspberry Pi config settings in the menu
  a: First, lets make sure we set up our wifi for internet access
      in the top right there is a network icon, click it and enter your password for your wifi
  b: Next, make sure you click 'Expand File System'
      this allows your pi to use all the space on the SD card
  c: We wont need the GUI after this, so lets also click to select 'CLI'
      this makes the pi boot without starting X-window
  d: finally, reboot the pi
  
5: run these commands / do these things
  a: sudo apt-get install isc-dhcp-server
  b: sudo nano /etc/dhcp/dhcpd.conf
    I: find these lines and comment them out with #
        option domain-name "example.org";
        option domain-name-servers ns1.example.org, ns2.example.org;
    II: uncomment this line
        #authoritative;
    III: add these lines to the end of the file
          subnet 192.168.10.0 netmask 255.255.255.0 {
            range 192.168.10.10 192.168.10.20;
            option broadcast-address 192.168.10.255;
            option routers 192.168.10.1;
            default-lease-time 600;
            max-lease-time 7200;
            option domain-name "local-network";
            option domain-name-servers 8.8.8.8, 8.8.4.4;
          }
    IV: exit nano by pressing Ctrl+X.
          When nano asks if you want to Save press “Y” 
          then hit enter to confirm the filename.
  c: sudo nano /etc/default/isc-dhcp-server
    I: go to the end of the file and edit the last line like so
        INTERFACES="wlan0"
    II: exit nano
  d: sudo ifdown wlan0
  e: sudo nano /etc/network/interfaces
    I: change this file so it looks like the following:
          
      auto lo
      iface lo inet loopback
      iface eth 0 inet dhcp
      allow-hotplug wlan0
      iface wlan0 inet static
	      address 192.168.10.1
	      netmask 255.255.255.0
	     
    II: exit nano
  f: sudo nano /etc/hostapd/hostapd.conf
    i: in this file you will want to change your SSID and PassPhrase
    ii: exit nano
  g: sudo ifup wlan0
  h: sudo service isc-dhcp-server start
  i: sudo service hostapd start

6: WOW, that was a lot of work, at this point you should be able to see your wifi on another device
    if you can't find it, try rebooting the pi and running steps 5-h and 5-i again
    if that doesn't work, please let me know, it means i missed a step

7: auto run
  a: run these two commands which should tell your pi to start these services on boot
      sudo update-rc.d hostapd enable 
      sudo update-rc.d isc-dhcp-server enable

NOTES:

  most of these steps come from: http://raspberrypihq.com/how-to-turn-a-raspberry-pi-into-a-wifi-router/
  you can continue for a few more steps if you want your pi to connect to the internet
  this requires a few more file changes and iptable setup / forwarding
  also, the newest raspbian jessie image doesn't need a custom hostapd to run wifi on the pi3
  so i skipped this step
  
TODO:
  
  I realize that this doesn't show you the steps to run bottle or use the GPIO pins via connecting to the pi over wifi
  these steps are comming soon, I just have to look over what all i did exactly and make sure I don't miss anything
  the git repo for bottle/foundation and the website files will be up here in a few days
  there is also a bash script that i use to start everything and a file change to get you into root on boot
  these will all be up by this weekend
  
For now, please enjoy having fun turning your pi into a wireless router / access point.
if you do anything with this info, please share it with us / the world / someone

UPDATE:
  all the files are now on github. you can simply copy the confing files to thier correct locations after setting up your pi.
  You will still need to follow the install instructions, but now you have a reference for the configs. 
  The only other thing you will need to do is add 'sudo -i' to the end of your users (default is Pi) .bashrc file.
  and './start_up.sh &' to the end of your root users .bashrc file.
  Be sure to double check that you have executable permisions on start_up.sh and server.py if not run 'chmod +x' on each file that needs it.
  You will need to install python bottle for this to work as well.
  Just run 'pip install bottle' and you should be all set.




