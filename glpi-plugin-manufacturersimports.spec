%define name glpi-plugin-manufacturersimports
%define version 1.3.0
%define release %mkrel 2

Summary: Financials informations from manufacturers web site plugin
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Monitoring
Url: https://forge.indepnet.net/projects/show/manufacturersimports
Source0: https://forge.indepnet.net/attachments/download/296/glpi-manufacturersimports-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
This plugin allows you to inject financials informations from manufacturers web site files in GLPI.

%prep
%setup -q -n manufacturersimports

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/manufacturersimports
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/manufacturersimports
rm -f %{buildroot}%{_datadir}/glpi/plugins/manufacturersimports/prerequis.txt

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc prerequis.txt
%{_datadir}/glpi/plugins/manufacturersimports
