%define __os_install_post %{nil}
%define debug_package %{nil}

Summary:	Free Internet telephony that just works
Name:		skype
Version:	2.2.0.35
Release:	1

Group:		Applications/Internet
License:	Proprietary
URL:		http://www.skype.com
Source0:	http://download.skype.com/linux/%{name}-%{version}-fedora.i586.rpm
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

ExclusiveArch:	i586


%description
Skype - Take a deep breath

Skype is a little piece of software that lets you make free calls
to anyone else on Skype, anywhere in the world. And even though
the calls are free, they are really excellent quality.

 * Make free Skype-to-Skype calls to anyone else, anywhere in the world.
 * Call ordinary phones and mobiles at pretty cheap rates per minute.
 * Group chat with up to 100 people or conference call with up to nine others.
 * See who you are talking to with free video calls.
 * Free to download.

%prep
%setup -q -c -T


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
pushd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -idV --quiet
popd

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mv %{buildroot}%{_datadir}/icons/skype.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/skype.png

sed -i 's!Icon=skype.png!Icon=skype!g' %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor rfremix \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --add-category Telephony			\
  --add-category Qt				\
  --remove-category Application			\
  --delete-original				\
  %{buildroot}%{_datadir}/applications/%{name}.desktop


%post
update-desktop-database &> /dev/null || :
touch --no-create /usr/share/icons/hicolor &>/dev/null || :
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --quiet /usr/share/icons/hicolor || :
fi

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create /usr/share/icons/hicolor &>/dev/null
    gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :

%posttrans
gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root)
%doc %{_docdir}/%{name}-%{version}
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/skype.conf
%config(noreplace) %{_sysconfdir}/prelink.conf.d/skype.conf
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Mon Jul  6 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 2.2.0.35-1
- update to 2.2.0.35

* Thu Apr  7 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 2.2.0.25-1
- update to 2.2.0.25

* Fri Nov 19 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 2.1.0.81-3
- update spec file

* Fri Jan 29 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 2.1.0.81-2
- do not stip anything (rf#121)

* Thu Jan 28 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 2.1.0.81-1
- update to 2.1.0.81

* Tue Nov 24 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 2.1.0.47-1
- initial build for Fedora
