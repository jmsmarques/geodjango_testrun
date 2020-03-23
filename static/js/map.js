var mymap;
var currentMarker;

function map_init(map, options) {
    // get point lat and lon
    var lon = "{{ worldborder.lon }}";
    var lat = "{{ worldborder.lat }}";

    // zoom to point & add it to map
    map.setView([lat, lon], 12);
    L.marker([lat, lon]).addTo(map);

    map.on("click", onMapClick);

    mymap = map;
}

function onMapClick(e) {
    //alert("You clicked the map at " + e.latlng);
    var lat = e.latlng.lat;
    var lon = e.latlng.lng;
    //L.marker([lat, lon]).addTo(mymap); //adds marker
    
    if(typeof currentMarker === 'undefined') {
        currentMarker = L.marker([lat, lon], {
            draggable: true
        }).addTo(mymap)
        .bindPopup(
            '<form action={% url \'map\' method="post">' +
            '{% csrf_token %}' +
                    '{{ form }}' +
                '<input type="submit" value="Save" />' +
            '</form>')
        .on('click', function(e) {
            if(currentMarker.getPopup().isPopupOpen()) {
                currentMarker.closePopup();
            }
            else {
                currentMarker.openPopup();
                document.getElementById('id_lat').value = e.latlng.lat ;
                document.getElementById('id_lon').value= e.latlng.lng ;
                document.getElementById('id_lat').readOnly = true;
                document.getElementById('id_lon').readOnly = true;
            }
        })
        .on('dblclick', function(e) {
            currentMarker.remove();
        });  
    }
    else {
        currentMarker.remove();
        currentMarker = L.marker([lat, lon], {
            draggable: true
        }).addTo(mymap)
        .bindPopup(
            '<form action=\"/world/map/create_point/\" method="post">{% csrf_token %}' +
                '<table border="1">' +
                    '<tr>' +
                        '<td> Lat: <input type=\"float\" name=\"lat\" id=\'lat\' readonly></td>' +
                    '</tr>' +
                    '<tr>' +
                        '<td>Lon: <input type=\"float\" name=\"lon\" id=\'lon\'readonly></td>' +
                    '</tr>' +
                    '<tr>' +
                    '   <td>Description: <input type=\"text\" name=\"description\"></td>' +   
                    '</tr>' +                     
                '</table>' +
                '<input type="submit" value="Save" />' +
            '</form>')
        .on('click', function(e) {
            if(currentMarker.getPopup().isPopupOpen()) {
                currentMarker.closePopup();
            }
            else {
                currentMarker.openPopup();
                document.getElementById('lat').value = e.latlng.lat ;
                document.getElementById('lon').value= e.latlng.lng ;
            }
        })
        .on('dblclick', function(e) {
            currentMarker.remove();
        });    
    }       
}