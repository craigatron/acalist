Heatmap = function(apiUrl) {
  this.apiUrl_ = apiUrl;
  var mapOptions = {
    center: new google.maps.LatLng(39.808536, -99.059326),
    zoom: 5,
    mapTypeId: google.maps.MapTypeId.HYBRID
  }
  this.map_ = new google.maps.Map(document.getElementById('map_canvas'),
      mapOptions);
  var self = this;
  $.getJSON(this.apiUrl_, {}, function(data) {
    var pointArray = new google.maps.MVCArray();
    $.each(data, function(i, item) {
      if (item.latitude && item.longitude) {
        pointArray.push({
          location: new google.maps.LatLng(item.latitude, item.longitude),
          weight: 1});
      }
    });
    var heatmap = new google.maps.visualization.HeatmapLayer({
      data: pointArray,
      map: self.map_,
      radius: 1,
      dissipating: false,
    });
  });
};
