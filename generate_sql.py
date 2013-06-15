#!/usr/bin/python

import pystache

basename = 'find_buildings'
config = {
  'SRC_PREFIX': 'whitman',  # prefix of source table, e.g. "planet_osm"
  'DEST_PREFIX': 'lonely' # prefix of desination tables, e.g. "lonely"
  }
        
# Run template and write sql
with open(basename + '.templ','r') as infile:
  srctext = infile.read()
sql = pystache.render(srctext, config)
with open(basename + '.sql','w') as outfile:
  outfile.write(sql)

