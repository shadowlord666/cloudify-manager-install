Name:           cloudify-manager-install
Version:        %{CLOUDIFY_VERSION}
Release:        %{CLOUDIFY_PACKAGE_RELEASE}%{?dist}
Summary:        Cloudify's Logstash
Group:          Applications/Multimedia
License:        Apache 2.0
URL:            https://github.com/cloudify-cosmo/cloudify-manager
Vendor:         Gigaspaces Inc.
Packager:       Gigaspaces Inc.

BuildRequires:  python, python-setuptools, createrepo
Requires:       python, python-setuptools, PyYAML, python-jinja2, python2-argh = 0.26.1
%define _name cfy-manager


%description
Cloudify common components

-`cfy_manager` helper script


%prep

%build


%install
cd ${RPM_SOURCE_DIR}
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=${RPM_BUILD_DIR}/INSTALLED_FILES
install -m 755 -d ${RPM_BUILD_ROOT}/opt/cloudify/sources
install -m 755 -d ${RPM_BUILD_ROOT}/etc/yum.repos.d/
cp SOURCE_RPMS/*.rpm ${RPM_BUILD_ROOT}/opt/cloudify/sources/
createrepo ${RPM_BUILD_ROOT}/opt/cloudify/sources
cat >${RPM_BUILD_ROOT}/etc/yum.repos.d/Cloudify-local.repo <<EOF
[localrepo]
baseurl=file:///opt/cloudify/sources
gpgcheck=0
EOF


%pre
%post
%preun
%postun


%files

%files -f INSTALLED_FILES
/opt/cloudify/sources
/etc/yum.repos.d/Cloudify-local.repo
