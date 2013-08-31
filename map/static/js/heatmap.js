Heatmap = function(apiUrl) {
  this.apiUrl_ = apiUrl;
  var mapOptions = {
    center: new google.maps.LatLng(39.808536, -99.059326),
    zoom: 5,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  this.map_ = new google.maps.Map(document.getElementById('map_canvas'),
      mapOptions);
};

Heatmap.prototype.loadData = function() {
  var self = this;
  $.getJSON(this.apiUrl_, {}, function(data) {
    var pointArray = new google.maps.MVCArray();
    $.each(data, function(i, item) {
      pointArray.push(new google.maps.LatLng(item.latitude, item.longitude));
    });
    heatmap = new google.maps.visualization.HeatmapLayer({
      data: pointArray
    });
    heatmap.setMap(this.map_);
  });
};
