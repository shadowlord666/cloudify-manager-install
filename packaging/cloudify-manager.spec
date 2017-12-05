# psycopg2 ships with its own required shared libraries
%global __requires_exclude_from site-packages/psycopg2
%global __provides_exclude_from site-packages/psycopg2

Name:           cloudify-management-worker
Version:        %{CLOUDIFY_VERSION}
Release:        %{CLOUDIFY_PACKAGE_RELEASE}%{?dist}
Summary:        Cloudify's Management Worker
Group:          Applications/Multimedia
License:        Apache 2.0
URL:            https://github.com/cloudify-cosmo/cloudify-manager
Vendor:         Gigaspaces Inc.
Packager:       Gigaspaces Inc.

BuildRequires:  python >= 2.7, python-virtualenv
Requires:       python >= 2.7
Requires(pre):  shadow-utils


%description
Cloudify's Management worker


%prep


%build
virtualenv /opt/cloudify-manager-installer/env
/opt/cloudify-manager-installer/env/bin/pip install ${RPM_SOURCE_DIR}


%install
install -m 755 -d ${RPM_BUILD_ROOT}/opt
mv /opt/cloudify-manager-installer %{buildroot}/opt/cloudify-manager-installer
install -m 755 -d ${RPM_BUILD_ROOT}/%{_bindir}
ln -s /opt/cloudify-manager-installer/env/bin/cfy_install ${RPM_BUILD_ROOT}/%{_bindir}/cfy_install
ln -s /opt/cloudify-manager-installer/env/bin/cfy_remove ${RPM_BUILD_ROOT}/%{_bindir}/cfy_remove
ln -s /opt/cloudify-manager-installer/env/bin/cfy_config ${RPM_BUILD_ROOT}/%{_bindir}/cfy_config

%pre
%post

%preun
%postun

%files

%defattr(-,root,root)
/opt/cloudify-manager-installer
%{_bindir}/*