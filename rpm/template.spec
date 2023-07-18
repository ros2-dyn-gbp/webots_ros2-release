%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-webots-ros2-importer
Version:        2023.1.1
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS webots_ros2_importer package

License:        Apache License 2.0
URL:            http://wiki.ros.org/webots_ros2
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-collada
Requires:       python%{python3_pkgversion}-lark-parser
Requires:       ros-rolling-builtin-interfaces
Requires:       ros-rolling-xacro
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-pycodestyle
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python3-pillow
BuildRequires:  ros-rolling-ament-copyright
%endif

%description
This package allows to convert URDF and XACRO files into Webots PROTO files.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Tue Jul 18 2023 Cyberbotics <support@cyberbotics.com> - 2023.1.1-2
- Autogenerated by Bloom

* Tue Jul 11 2023 Cyberbotics <support@cyberbotics.com> - 2023.1.1-1
- Autogenerated by Bloom

* Thu Jun 29 2023 Cyberbotics <support@cyberbotics.com> - 2023.1.0-1
- Autogenerated by Bloom

* Tue May 23 2023 Cyberbotics <support@cyberbotics.com> - 2023.0.4-1
- Autogenerated by Bloom

* Wed Apr 12 2023 Cyberbotics <support@cyberbotics.com> - 2023.0.3-1
- Autogenerated by Bloom

* Wed Mar 22 2023 Cyberbotics <support@cyberbotics.com> - 2023.0.2-2
- Autogenerated by Bloom

