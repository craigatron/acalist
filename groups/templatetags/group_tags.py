from django import template
from django.conf import settings

register = template.Library()

LINKS = {
    'email': ('mailto:', 'Mail.png', 'Email'),
    'bajigga_id': ('http://bajigga.com/', 'bajigga.png', 'Bajigga'),
    'facebook_id': ('https://facebook.com/', 'Facebook.png', 'Facebook'),
    'gplus_id': ('https://plus.google.com/', 'Google+.png', 'Google+'),
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
    'myspace_id', 'soundcloud_id', 'spotify_id', 'tumblr_id',
    'twitter_id', 'youtube_id']


def social_link(group, field):
  link_info = LINKS[field]
  return '<a href="%s" target="_blank"><img src="%s" title="%s" /></a>' % (
      link_info[0] + getattr(group, field),
      settings.STATIC_URL + 'img/' + link_info[1], link_info[2])


@register.simple_tag
def social_row(group, use_table):
  html = '<tr>' if use_table else '<span>'
  for field in LINK_ORDER:
    if getattr(group, field):
      if use_table:
        html += '<td>'
      html += social_link(group, field)
      if use_table:
        html += '</td>'
  return html + ('</tr>' if use_table else '</span>')

