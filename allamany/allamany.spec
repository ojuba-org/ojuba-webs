Name: allamany
Version: 2.0
Release: 1%{?dist}
Summary: Prophet Mohammad -peace be upon him- teach me
Summary(ar): علمني رسول الله صلى الله عليه وسلم
License: WAQFv2
URL: https://linuxac.org
Source0: %{name}-%{version}.tar.xz
Requires: webkit2gtk3
Requires: islamic-menus
Buildarch: noarch

%description
Prophet Mohammad -peace be upon him- teach me

%description -l ar
علمني رسول الله صلى الله عليه وسلم

%prep
%setup -q -n %{name}
sed -i "s:/usr/share:%{_datadir}:g" %{name}

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/appdata
mkdir -p %{buildroot}%{_datadir}/pixmaps

cp -pr alamany-cards booklet %{buildroot}%{_datadir}/%{name}

install -Dp -m 0644 index.html %{buildroot}%{_datadir}/%{name}
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}
install -Dp -m 0755 %{name}.desktop %{buildroot}%{_datadir}/applications
install -Dp -m 0644 %{name}.appdata.xml %{buildroot}%{_datadir}/appdata
install -Dp -m 0644 %{name}.png %{buildroot}%{_datadir}/pixmaps



%files
%{_datadir}/%{name}/*
%{_datadir}/%{name}/index.html
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png


%changelog
* Mon Sep 21 2020 Mosaab Alzoubi <moceap@hotmail.com> - 2.0-1
- Use Webkit 2G
- Use Python 3

* Fri Sep 18 2020 Mosaab Alzoubi <moceap@hotmail.com> - 1.1-2
- Rebuilt for F32

* Fri Jan 20 2017 Mosaab Alzoubi <moceap@hotmail.com> - 1.1-1
- Initial on Ojuba
