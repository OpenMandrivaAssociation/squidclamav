Summary:	A Clamav Antivirus Redirector for Squid
Name:		squidclamav
Version:	5.3
Release:	%mkrel 1
Group:		System/Servers
License:	GPLv2
URL:		http://sourceforge.net/projects/%{name}/
Source0:	http://kent.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-mdv_conf.diff
BuildRequires:	curl-devel
Requires:	squid curl clamav clamd
Suggests:	squidGuard
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SquidClamAv is a dedicated ClamAV antivirus redirector for Squid. It can run
antivirus checks based on filename regex, content-type regex, and more. It is
easy to install and works even with heavy Squid access. 

%prep

%setup -q
%patch0 -p0

#chmod 644 ChangeLog README clwarn.cgi*

%build

%configure2_5x

%make

%install
rm -rf %{buildroot}

%{__install} -d -m 0755 %{buildroot}%{_sysconfdir}
%{__install} -d -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d
%{__install} -d -m 0755 %{buildroot}/var/log/%{name}
%{__install} -d -m 0755 %{buildroot}/%{_libexecdir}

%makeinstall_std


#install -m0644 {name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf
#install -m0755 clwarn.cgi %{buildroot}/var/www/cgi-bin/

# fix logrotate entries
cat > %{name}.logrotate << EOF
/var/log/%{name}/%{name}.log {
    rotate 5
    monthly
    missingok
    notifempty
}
EOF
install -m0644 %{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

rm -f %{buildroot}%{_datadir}/%{name}/README

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_libexecdir}/%{name}/*
%attr(0755,root,root) %{_mandir}/man1/*1*
%attr(0755,squid,squid) %dir /var/log/%{name}
