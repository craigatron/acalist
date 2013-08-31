/**
 * @constructor
 */
Map = function(useClusterer, apiUrl, iconFunction, staticUrl) {
  this.useClusterer_ = useClusterer;
  this.apiUrl_ = apiUrl;
  this.iconFunction_ = iconFunction;
  this.staticUrl_ = staticUrl;
  var mapOptions = {
    center: new google.maps.LatLng(39.808536, -99.059326),
    zoom: 5,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  this.map_ = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
  var omsOptions = {
    keepSpiderfied: true
  }
  this.oms_ = new OverlappingMarkerSpiderfier(this.map_, omsOptions);
};

Map.prototype.initialize = function() {
  var self = this;
  var iw = new google.maps.InfoWindow();
  this.oms_.addListener('click', function(marker) {
    iw.setContent(marker.name);
    iw.open(self.map_, marker);
  });
  this.oms_.addListener('spiderfy', function(markers) {
    iw.close();
  });
  this.oms_.addListener('unspiderfy', function(markers) {
    iw.close();
  });
};

Map.prototype.loadMarkers = function() {
  var self = this;
  $.getJSON(this.apiUrl_, {}, function(data) {
    $.each(data, function(i, item) {
      var icon = self.staticUrl_ + self.iconFunction_(item);
      var point = new google.maps.LatLng(item.latitude, item.longitude);
      var marker = new google.maps.Marker({
        map: self.map_,
        title: item.name,
        position: point,
        icon: icon
      });
      marker.name = item.name;
      self.oms_.addMarker(marker);
    });
    if (self.useClusterer_) {
      var mcOptions = {
        averageCenter: true,
        gridSize: 50,
        maxZoom: 8
      };
      var mc = new MarkerClusterer(self.map_, self.oms_.getMarkers(), mcOptions);
    }
  });
};