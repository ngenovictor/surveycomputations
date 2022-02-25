function createMap() {
    var osmlayer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1Ijoibmdlbm92aWN0b3IzMjEiLCJhIjoiY2wwMndqd3VmMDFtYTNrcG93ZjRxN285eCJ9.-Qd_gd0MTNBW2jq03h1ivg', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
        '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="http://mapbox.com">Mapbox</a>',
        id: 'mapbox/satellite-streets-v11'
    });
    var map = L.map('map', {
        center: [-1.0500, 37.0833],
        zoom: 10,
        minZoom: 2,
        maxZoom: 18,
        zoomControl: true,
        layers: [osmlayer,]
    });
    var startPickingbutton = L.Control.extend({
        options: {
            position: 'bottomleft',
        },
        onAdd: function(map){
            var button = L.DomUtil.create("button", "btn btn-primary");
            button.innerHTML = "Start Picking";
            // button.style.width = "100px"
            button.onclick = function(){
                console.log('buttonClicked');
            }
            return button;
        }
    });
    map.addControl(new startPickingbutton());
}
$(document).ready(function(){
    createMap();
});