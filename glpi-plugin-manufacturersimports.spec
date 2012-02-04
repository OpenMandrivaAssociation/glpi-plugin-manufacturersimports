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
