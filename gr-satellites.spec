Name:           gr-satellites
Version:        5.9.0
Release:        1%{?dist}
Summary:        GNU Radio telemetry decoders for Amateur satellites

License:        GPL-3.0-or-later
URL:            https://github.com/daniestevez/gr-satellites
Source0:        %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  bzip2
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gnuradio-devel >= 3.10
BuildRequires:  libsndfile-devel
BuildRequires:  spdlog-devel
BuildRequires:  orc-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel

Requires:       gnuradio >= 3.10
Requires:       python3-construct
Requires:       python3-pyzmq
Requires:       python3-pyyaml
Requires:       python3-requests
Requires:       python3-websocket-client

%description
gr-satellites is a GNU Radio out-of-tree module encompassing a collection of
telemetry decoders that supports many different Amateur satellites. It
supports most popular protocols, such as AX.25, the GOMspace NanoCom U482C
and AX100 modems, an important part of the CCSDS stack, the AO-40 protocol
used in the FUNcube satellites, and several ad-hoc protocols used in other
satellites.

%prep
%autosetup -p1

%build
%cmake \
    -DENABLE_DOXYGEN:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/gr_satellites
%{_bindir}/gr_satellites_ssdv
%{_bindir}/smog_p_spectrum
%{_libdir}/libgnuradio-satellites.so*
%dir %{_includedir}/satellites
%{_includedir}/satellites/*
%{python3_sitelib}/satellites/
%{_datadir}/gnuradio/grc/blocks/satellites_*.block.yml
%{_mandir}/man1/gr_satellites.1*
%{_mandir}/man1/gr_satellites_ssdv.1*
%{_mandir}/man1/smog_p_spectrum.1*

%changelog
* Thu Oct 08 2026 Jim Howard <xsnrg@users.noreply.github.com> - 5.9.0-1
- Initial Copr build of 5.9.0
