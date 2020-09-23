%global rel 2

Name: arabic-writer
Version: 1.4.4
Release: %{rel}%{?dist}
Summary: Arabic Writer
Summary(ar): الكاتب العربي
License: GPLv1
URL: http://omar84.com
Source0: %{name}-%{version}-%{rel}.tar.xz
Requires: webkit2gtk3
Buildarch: noarch

%description
Enables Arabic writing in programs that isn't support

%description -l ar
تمكين الكتابة بالعربية في البرامج غير الداعمة لها

%prep
%setup -q -n %{name}
sed -i "s:/usr/share:%{_datadir}:g" %{name}

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/appdata
mkdir -p %{buildroot}%{_datadir}/pixmaps


install -Dp -m 0644 index.html %{buildroot}%{_datadir}/%{name}
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}
install -Dp -m 0755 %{name}.desktop %{buildroot}%{_datadir}/applications
install -Dp -m 0644 %{name}.appdata.xml %{buildroot}%{_datadir}/appdata
install -Dp -m 0644 %{name}.png %{buildroot}%{_datadir}/pixmaps



%files
%doc ReadMe.txt
%{_datadir}/%{name}/index.html
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png


%changelog
* Wed Sep 23 2020 Mosaab Alzoubi <moceap@hotmail.com> - 1.4.4-2
- Use Webkit 2G
- Use Python3
- Rebuilt for F32

* Fri Jan 27 2017 Mosaab Alzoubi <moceap@hotmail.com> - 1.4.4-1
- Initial on Ojuba
