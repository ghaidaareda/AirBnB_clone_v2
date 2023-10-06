#puppet deployment of server
exec {'update server':
    command => '/usr/bin/env apt update',
}
exec {'install nginx':
    command => '/usr/bin/env apt-get -y install nginx',
}
exec {'create folder shared':
command => '/usr/bin/env mkdir -p /data/web_static/shared/',
}
exec {'create folder tests':
command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
}
exec {'create file index.html':
command => '/usr/bin/env touch /data/web_static/releases/test/index.html',
}
exec {'create test HTML file':
command => '/usr/bin/env echo "<html><body><h1>AirBnB clone</h1></body>" > data/web_static/releases/test/index.html',
}
exec {'create sympolic link':
command => '/usr/bin/env ln -sf /data/web_static/releases/test/ /data/web_static/current',
}
exec {'set ownership':
command => '/usr/bin/env chown -R ubuntu:ubuntu /data/',
}
exec {'Update the Nginx configuration':
command => "/usr/bin/env sed -i '/listen 80 default_server;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default",
}
exec {'restart nginx': 
command => '/usr/bin/env service nginx restart',
}
exec { 'exit 0':
  command => '/usr/bin/env exit 0',
}