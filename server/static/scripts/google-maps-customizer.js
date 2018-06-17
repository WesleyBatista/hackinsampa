var markers = [];
function initMap() {
    var myLatLng = { lat: -23.5517576, lng: -46.6385405 };

    var mapStyles = [
        {
            featureType: 'poi',
            stylers: [{ visibility: 'off' }]
        },
    ];

    var map = new google.maps.Map(document.getElementById('map'), {
        center: myLatLng,
        zoom: 15,
        zoomControl: true,
        mapTypeControl: false,
        scaleControl: true,
        streetViewControl: false,
        rotateControl: true,
        fullscreenControl: false,
        styles: mapStyles
    });

    var types = ["prefeitura", "união", "privado", "governo"];

    for (let i = 0, len = data.length; i < len; i++) {
        var pin = data[i];
        var marker = new google.maps.Marker({
            position: { lat: pin.lat, lng: pin.lng },
            map: map,
            animation: google.maps.Animation.DROP,
            title: pin.Name,
            icon: 'static/images/' + pin.type + '_' + pin.status + '.png',
            category: pin.type + '_' + pin.status,
        });
        marker.addListener('click', function () { toggleBounce(i); });
        marker.addListener('click', function () { onPinClick(i); });
        markers.push(marker);
    }

}

function toggleBounce(i) {
    console.log(i);
    if (markers[i].getAnimation() !== null) {
        markers[i].setAnimation(null);
    } else {
        markers[i].setAnimation(google.maps.Animation.BOUNCE);
        markers.forEach(function (element, index) {
            index !== i && element.setAnimation(null);
        })
    }
}