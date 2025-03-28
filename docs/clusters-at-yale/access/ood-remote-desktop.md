# Remote Desktop

Occasionally, it is helpful to use a graphical interface to explore data or run certain programs. Remote Desktops are available through our cluster [Web Portals](/clusters-at-yale/access/ood).
Information on accessing the web portal is available on [Access the Web Portal](/clusters-at-yale/access/ood) documentation page. 
From the Web Portal, you are able to launch interactive apps such as Remote Desktops.
In the past options were to use VNC or [X11 forwarding](/clusters-at-yale/access/x11).
These tools can be complex to setup or suffer from reduced performance.
The Remote Desktop app simplifies the configuration of a VNC desktop session on a compute node.

To get started, connect to one of cluster [Web Portals](/clusters-at-yale/access/ood) and choose Remote Desktop from the Interactive Apps menu or the dashboard and then follow the instructions for [launching an interactive app](/clusters-at-yale/access/ood/#launch-an-interactive-app).

## Graphics quality

As shown below, there are sliders for compression and image quality in the remote desktop launch control. These two settings can significantly impact the look and feel of your Remote Desktop. For maximum performance in most modern settings, we recommend sliding the image quality slider all the way to the right ('9', or 'high'). If you don't like how this turns out in the resulting browser tab/window that appears, you can always close the tab, choose a new slider setting, and launch again.

![starting](/img/ood_remote_starting.png){: .medium}

## Copy/Paste

Copy and paste functions in Remote Desktop use a distinct clipboard from your computer's native one. Some web browsers (Edge, Chrome) can automatically sync these two clipboards. However, if this does not work in your browser you can use a special text box to copy and paste to and from the Remote Desktop App. Click the arrow on the left side of your window for a menu, then click the clipboard icon to get access to your Remote Desktop's clipboard.

!!! note "Important note"
Even for browsers like Edge and Chrome that automatically sync the Remote Desktop clipboard, copying and pasting can be glitchy: for example, when pasting from another application to Remote Desktop, you may get the wrong result (clipboard contents out of date) until you use your pointer to click on a window within Remote Desktop.

![clipboard](/img/ood_remote_clipboard.png){: .medium}
