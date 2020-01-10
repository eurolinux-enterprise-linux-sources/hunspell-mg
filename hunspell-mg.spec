Name: hunspell-mg
Summary: Malagasy hunspell dictionaries
%define upstreamid 20050109
Version: 0.%{upstreamid}
Release: 10%{?dist}
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/mg_MG.zip
Group: Applications/Text
URL: http://borel.slu.edu/crubadan/apps.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Malagasy hunspell dictionaries.

%prep
%setup -q -c -n hunspell-mg

%build
for i in README_mg_MG.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p mg_MG.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/plt.aff
cp -p mg_MG.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/plt.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
plt_aliases="mg"
for lang in $plt_aliases; do
        ln -s plt.aff $lang.aff
        ln -s plt.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README_mg_MG.txt
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20050109-10
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050109-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050109-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050109-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050109-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 24 2010 Caolán McNamara <caolanm@redhat.com> - 0.20050109-5
- add Malagasy Plateau alias

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050109-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolán McNamara <caolanm@redhat.com> - 0.20050109-3
- tidy spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050109-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 06 2008 Caolán McNamara <caolanm@redhat.com> - 0.20050109-1
- out-by-one

* Tue Sep 30 2008 Caolán McNamara <caolanm@redhat.com> - 0.20050108-1
- initial version
