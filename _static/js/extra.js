

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

    //feed to parse
    var feed = 'https://cors.io?https://research.computing.yale.edu/current-system-status';
    var status = [];
    $.get(feed, function (data) {

        $(data).find("item").each(function () {
            var result = $(this);
            status.push("<a href='https://research.computing.yale.edu/system-status'>" + result.find("title").text() + "</a>");
        });

        if (status.length > 0){

            var status_color = '#ffcc00'; // yellow
            document.getElementById("system-status-message").innerHTML = "System Status: " + status.join(', ');
            document.getElementById("system-status-message").setAttribute("style", "display: block");

        } else{
            var status_color = '#52BA5D'; // green
        }

            document.getElementById("status-icon").setAttribute("style", "background:"+ status_color);

    });
};
