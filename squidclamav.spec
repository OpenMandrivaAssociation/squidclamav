Summary:	A Clamav Antivirus Redirector for Squid
Name:		squidclamav
Version:	6.10
Release:	2
Group:		System/Servers
License:	GPLv2
URL:		http://sourceforge.net/projects/%{name}/
Source0:	https://sourceforge.net/projects/squidclamav/files/squidclamav/6.10/%{name}-%{version}.tar.gz
BuildRequires:	curl-devel
BuildRequires:	c-icap-devel
Requires:	squid curl clamav clamd
Suggests:	squidGuard
Patch0:		squidclamav-mdv_conf.diff

%description
SquidClamAv is a dedicated ClamAV antivirus redirector for Squid. It can run
antivirus checks based on filename regex, content-type regex, and more. It is
easy to install and works even with heavy Squid access. 

%prep

%setup -q
%patch0 -p1
#chmod 644 ChangeLog README clwarn.cgi*

%build

%configure2_5x

%make

%install
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

%files
%doc ChangeLog README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
#%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_libexecdir}/%{name}/*
%attr(0755,root,root) %{_libdir}/c_icap/%{name}.so
%attr(0755,root,root) %{_mandir}/man1/*1*
%attr(0755,squid,squid) %dir /var/log/%{name}


%changelog
* Fri Jul 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 6.8-1
+ Revision: 811264
- version update 6.8

* Fri Jul 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 6.7-1
+ Revision: 811229
- version update  6.7
- version update  6.7

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 5.3-3mdv2011.0
+ Revision: 614973
- the mass rebuild of 2010.1 packages

* Thu May 06 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 5.3-2mdv2010.1
+ Revision: 542744
- Rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - rise from the dead, there is a volonteer to maintain it

* Sun Apr 25 2010 Emmanuel Andry <eandry@mandriva.org> 5.3-1mdv2010.1
+ Revision: 538730
- New version 5.3
- rediff config patch
- update files list

* Wed Jan 27 2010 Frederik Himpe <fhimpe@mandriva.org> 4.3-1mdv2010.1
+ Revision: 497393
- Update to new version 4.3

* Wed Jan 27 2010 Frederik Himpe <fhimpe@mandriva.org> 4.2-1mdv2010.1
+ Revision: 497392
- Update to new version 4.2
- Rediff configuration patch

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 3.9-2mdv2010.0
+ Revision: 445227
- rebuild

* Wed Dec 17 2008 Oden Eriksson <oeriksson@mandriva.com> 3.9-1mdv2009.1
+ Revision: 315152
- 3.9

* Mon Dec 08 2008 Oden Eriksson <oeriksson@mandriva.com> 3.8-1mdv2009.1
+ Revision: 311855
- 3.8
- rediffed P0

* Fri Oct 24 2008 Oden Eriksson <oeriksson@mandriva.com> 3.7-1mdv2009.1
+ Revision: 296937
- added more fixes
- import squidclamav


