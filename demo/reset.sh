#!/usr/bin/env bash

echo Resetting demo app
rm db.sqlite  # remove DB
rm -rf govuk_template/  # remove old build files
./manage.py startgovukapp govuk_template  # download and build components
./manage.py migrate  # just in case
./manage.py buildscss  # to create all css
./manage.py shell --command "
from govuk_template_base.models import ServiceSettings, Link
service_settings = ServiceSettings.default_settings()
service_settings.name = 'Demo service'
service_settings.phase = 'alpha'
service_settings.header_links.add(Link.objects.create(name='Sample form', link='demo:empty', link_is_view_name=True))
service_settings.header_links.add(Link.objects.create(name='Non-empty', link='demo:with-data', link_is_view_name=True))
service_settings.save()
"