from flask import Flask, render_template, Response
import urllib2
import json
app = Flask(__name__)
app.config['DEBUG'] =  True

API_URL = 'http://www.openaca.org/api/'
LINKS = {
    'email': ('mailto:', 'Mail.png', 'Email'),
    'bajigga_id': ('http://bajigga.com/', 'bajigga.png', 'Bajigga'),
    'facebook_id': ('https://facebook.com/', 'Facebook.png', 'Facebook'),
    'gplus_id': ('https://plus.google.com/', 'Google+.png', 'Google+'),
    'itunes_id': ('https://itunes.apple.com/artist/', 'iTunes.png', 'iTunes'),
    'instagram_id': ('https://instagram.com/', 'Instagram.png', 'Instagram'),
    'loudr_id': ('http://loudr.fm/artist/', 'loudr.png', 'Loudr'),
    'myspace_id': ('https://myspace.com/', 'MySpace.png', 'MySpace'),
    'soundcloud_id': ('https://soundcloud.com/', 'Soundcloud.png',
                      'Soundcloud'),
    'spotify_id': ('https://open.spotify.com/artist/', 'Spotify.png',
                   'Spotify'),
    'tumblr_id': ('https://tumblr.com/', 'Tumblr.png', 'Tumblr'),
    'twitter_id': ('https://twitter.com/', 'Twitter.png', 'Twitter'),
    'youtube_id': ('https://youtube.com/', 'YouTube.png', 'YouTube'),
}
LINK_ORDER = ['email', 'bajigga_id', 'facebook_id', 'gplus_id',
    'instagram_id', 'myspace_id', 'soundcloud_id', 'spotify_id', 'tumblr_id',
    'twitter_id', 'youtube_id', 'loudr_id', 'itunes_id']

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/')
@app.route('/groups/map')
def map():
  return render_template('map.html', include_oms=True, include_clusterer=True)
  
@app.route('/groups/heatmap')
def heatmap():
  return render_template('group_heatmap.html', heatmap=True)
  
@app.route('/groups/location')
def groups():
  return Response(urllib2.urlopen(API_URL + 'groups?loc&format=json'), mimetype='application/json')
  
@app.route('/groups/info/<group_id>')
def group_info(group_id):
  group_dict = json.load(urllib2.urlopen(API_URL + 'groups/' + group_id + '?format=json'))
  links = []
  for field in LINK_ORDER:
    if group_dict.get(field):
        f = LINKS[field]
        links.append((f[0] + group_dict[field], f[1], f[2]))

  return render_template('group_info.html', group=group_dict, links=links)