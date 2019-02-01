

// Autoexpand Sidebar
document.addEventListener("DOMContentLoaded", function() {
    load_navpane();
    display_system_status()
});

function load_navpane() {
    var width = window.innerWidth;
    if (width <= 1200) {
        return;
    }

    var nav = document.getElementsByClassName("md-nav");
    for(var i = 0; i < nav.length; i++) {
        if (typeof nav.item(i).style === "undefined") {
            continue;
        }

        if ((nav.item(i).getAttribute("data-md-level") <= 2) && nav.item(i).getAttribute("data-md-component")) {
            nav.item(i).style.display = 'block';
            nav.item(i).style.overflow = 'visible';
        }
    }

    var nav = document.getElementsByClassName("md-nav__toggle");
    for(var i = 0; i < nav.length; i++) {
       if(nav.item(i).getAttribute("data-md-toggle").length <= 7){
            nav.item(i).checked = true;
        }
    }
};

// display system status
function display_system_status() {

    var url = 'http://research.computing.yale.edu/current-system-status';

    feednami.load(url,function(result){
        if(result.error) {
            console.log(result.error);
        } else {

            var entries = result.feed.entries;
            if (entries.length) {
                var status_color = '#ffcc00'; // yellow

                for(var i = 0; i < entries.length; i++){
                    entry = entries[i];

                    var status = "System Status: <a href='" + entry.link + "'>" + entry.title + "</a>";
                    document.getElementById("system-status-message").innerHTML = status;
                    document.getElementById("system-status-message").setAttribute("style", "display: block");
                }

            }  else{
                var status_color = '#52BA5D'; // green
            }
        }

        document.getElementById("status-icon").setAttribute("style", "background:"+ status_color);

    });
};