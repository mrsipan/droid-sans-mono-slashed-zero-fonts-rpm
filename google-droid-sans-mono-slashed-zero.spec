%global fontname google-droid-sans-mono-slashed-zero
%global fontconf 75-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        0.1
Release:        1%{?dist}
Summary:        Google Droid Sans Mono Slashed Zero

Group:          User Interface/X
License:        OFL
URL:            http://www.cosmix.org/software
Source0:        DroidSansMonoSlashed.ttf
Source1:        %{name}-fontconfig.conf
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch
BuildRequires:  fontpackages-devel
#BuildRequires:  fontforge
Requires:       fontpackages-filesystem

%description
Google Droid Sans Mono with 0 slashed

%prep
cp %{SOURCE0} %{SOURCE1} $RPM_BUILD_DIR

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%clean
rm -fr %{buildroot}

%_font_pkg -f %{fontconf} *.ttf

%changelog
* Sun May 25 2014 Ben Sanchez - 0.1
- Initial build

