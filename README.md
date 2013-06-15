lonely_buildings
================

PostGIS scripts to find clusters of buildings in OSM with no nearby road. This is common, for example, in areas with recent building imports where roads mapping has not caught up with new developments.


## Prerequisites

* PostGIS database with OSM data (osm2pgsql schema)
* Pystache  (```pip install pystache```)


## To Run

* Edit the ```config``` section of generate_sql.py to match your database/preferences.

* Create SQL from template: ```python ./generate_sql.py```

* Run the SQL script: ```psql -f find_buildings.sql gis```

* Results are in the <prefix>_points table


## Author

Lars Ahlzen

lars@ahlzen.com
