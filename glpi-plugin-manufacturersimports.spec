%if %mandriva_branch == Cooker
%define release %mkrel 2
%else
%define subrel 1
%define release %mkrel 0
%endif

Summary: Financials informations from manufacturers web site plugin
Name: glpi-plugin-manufacturersimports
Version: 1.4.1
Release: %{release}
License: GPL
Group: Monitoring
Url: https://forge.indepnet.net/projects/show/manufacturersimports
Source0: https://forge.indepnet.net/attachments/download/981/glpi-manufacturersimports-%{version}.tar.gz
BuildArch: noarch

%description
This plugin allows you to inject financials informations from manufacturers web
site files in GLPI.

%prep

%setup -q -n manufacturersimports

find . -type f | xargs chmod 644
find . -type d | xargs chmod 755

%install

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/manufacturersimports
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/manufacturersimports
rm -f %{buildroot}%{_datadir}/glpi/plugins/manufacturersimports/prerequis.txt

%files
%doc prerequis.txt
%{_datadir}/glpi/plugins/manufacturersimports


%changelog
* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-2mdv2012.0
+ Revision: 771129
- various fixes

* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-1
+ Revision: 771090
- 1.4.1

* Fri May 27 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-2
+ Revision: 680285
- rename installation directory to match plugin name

* Fri May 27 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-1
+ Revision: 680282
- new  version

* Sat Jul 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-1mdv2011.0
+ Revision: 554623
- import glpi-plugin-manufacturersimports


