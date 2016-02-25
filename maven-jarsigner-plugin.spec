%global pkg_name maven-jarsigner-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}


%global group_id  org.apache.maven.plugins

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.2
Release:          9.11%{?dist}
Summary:          Signs or verifies a project artifact and attachments using jarsigner
License:          ASL 2.0
URL:              http://maven.apache.org/plugins/%{pkg_name}/
# http://search.maven.org/remotecontent?filepath=org/apache/maven/plugins/maven-jarsigner-plugin/1.2/maven-jarsigner-plugin-1.2-source-release.zip
Source0:          http://search.maven.org/remotecontent?filepath=org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

BuildArch:        noarch

BuildRequires:    %{?scl_prefix}maven-local


%description
This plugin provides the capability to sign or verify
a project artifact and attachments using jarsigner.

If you need to sign a project artifact and all attached artifacts,
just configure the sign goal appropriately in your pom.xml
for the signing to occur automatically during the package phase.

If you need to verify the signatures of a project artifact
and all attached artifacts, just configure the verify goal
appropriately in your pom.xml for the verification to occur
automatically during the verify phase.


%package javadoc
Summary:          API documentation for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x

%mvn_file :%{pkg_name} %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Feb 08 2016 Michal Srb <msrb@redhat.com> - 1.2-9.11
- Fix BR on maven-local & co.

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 1.2-9.10
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.2-9.9
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.2-9.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.2-9.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-9.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-9.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-9.4
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-9.3
- Rebuild to fix incorrect auto-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-9.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-9.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2-9
- Mass rebuild 2013-12-27

* Thu Aug 22 2013 Michal Srb <msrb@redhat.com> - 1.2-8
- Migrate away from mvn-rpmbuild (Resolves: #997477)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Jaromir Capik <jcapik@redhat.com> - 1.2-5
- Introducing NOTICE in the javadoc subpackage
- Minor spec file changes according to the latest guidelines

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May 25 2011 Jaromir Capik <jcapik@redhat.com> - 1.2-2
- Missing runtime deps (maven, plexus-utils) added

* Wed May 18 2011 Jaromir Capik <jcapik@redhat.com> - 1.2-1
- Initial version of the package
