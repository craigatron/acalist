function geocode() {
  var geocodeUrl = 'https://maps.googleapis.com/maps/api/geocode/json';
  var address = django.jQuery('#id_location').val().replace(' ', '+');
  django.jQuery.getJSON(geocodeUrl, { address: address, sensor: false }, function(data) {
    if (data.results && data.results[0] && data.results[0].geometry &&
        data.results[0].geometry.location) {
      geom = data.results[0].geometry.location;
      django.jQuery('#id_latitude').val(geom.lat);
      django.jQuery('#id_longitude').val(geom.lng);
    } else {
      alert('Couldn\'t geocode that address!');
    }
  });
  return false;
}
