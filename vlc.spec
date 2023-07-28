%global commit0 dfdc90c30a50a7e4fbdddeac2c06d51ade7ab385
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global vlc_rc		-rc2
%global vlc_setup vlc-%{?commit0}

%global _with_bootstrap 1

%if 0%{?!_without_freeworld:1}
%global _with_x264 1
%global _with_x265 1
%global _with_live555 1
%endif

%global _with_a52dec 1
%global _with_aom     1
%global _with_dav1d   1
%global _with_faad2 1
%global _with_ffmpeg 1
%global _with_fluidsynth 1
%global _with_freerdp 1
%global _with_libdca 1
%global _with_libdvbpsi 1
%global _with_libmad 1
%global _with_libmpeg2 1
%global _with_schroedinger 1
%global _with_twolame 1
%global _with_vaapi 1
%global _with_xvidcore 1
%ifarch x86_64 ppc64le aarch64
%if ! (0%{?fedora} >= 37)
%global _with_asdcp   1
%endif
%endif

%if 0%{?rhel} && 0%{?rhel} >= 9
%global _without_libdc1394 1
%endif

%if ! 0%{?el7}
%global _with_bluray  1
%global _with_wayland 1
%endif

%if 0%{?fedora}
%global _with_lirc 1
%ifarch x86_64 i686
%global _with_crystalhd 1
%endif
%endif

%if 0%{?el7}
%global _with_opencv  1
# Developper toolset version
%global dts_ver       8
%endif


Summary:	The cross-platform open-source multimedia framework, player and server
Epoch:		1
Name:		vlc
Version:	3.0.19
Release:	0.5%{?dist}
License:	GPLv2+
URL:		https://www.videolan.org
Source0: https://code.videolan.org/videolan/vlc/-/archive/%{commit0}/vlc-%{shortcommit0}.tar.gz
Patch3:	0001-Use-SYSTEM-wide-ciphers-for-gnutls.patch
Patch4: vlc-onevpl.patch
Patch5:	Lower-libgcrypt-to-1.5.3.patch
Patch6:	Restore-support-for-thread-callbacks-for-older-gcryp.patch
# lua-5.1 is used by default for vlc build
Patch7: Switch-to-Fedora-lua-5.1.patch
# Backport for 3.0 notifyd without gtk3
Patch9: notify-don-t-depend-on-any-GTK-version.patch

BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	fontpackages-devel

%{?_with_bootstrap:
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	libtool
}
BuildRequires:	gcc-c++

%{?_with_a52dec:BuildRequires: a52dec-devel}
%{?_with_aom:BuildRequires: libaom-devel}
BuildRequires:	aalib-devel
BuildRequires:	alsa-lib-devel
%{?_with_asdcp:BuildRequires: asdcplib-devel}
BuildRequires:	avahi-devel
BuildRequires:	cdparanoia-devel
%{?_with_dav1d:BuildRequires: libdav1d-devel}
BuildRequires:	pkgconfig(dbus-1)
%{?_with_faad2:BuildRequires: faad2-devel}
# vlc-3 works with ffmpeg <= 4 for vaapi support
#https://code.videolan.org/videolan/vlc/-/issues/26772
%if 0%{?fedora} >= 36 || 0%{?rhel} >= 9
%{?_with_ffmpeg:BuildRequires: compat-ffmpeg4-devel}
%else
%{?_with_ffmpeg:BuildRequires: ffmpeg-devel >= 0.4.9-0}
%endif
BuildRequires:	flac-devel
%{?_with_fluidsynth:BuildRequires: fluidsynth-devel}
BuildRequires:	fribidi-devel
BuildRequires:	gnutls-devel >= 1.0.17
BuildRequires:	hostname
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	game-music-emu-devel
%ifarch %{arm} aarch64
BuildRequires:	pkgconfig(gstreamer-app-1.0)
BuildRequires:	pkgconfig(gstreamer-video-1.0)
%endif
BuildRequires:	libavc1394-devel
BuildRequires:	libass-devel >= 0.9.7
%{?_with_bluray:BuildRequires: libbluray-devel >= 0.2.1}
BuildRequires:	libcaca-devel
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-devel >= 0.77-3
BuildRequires:	pkgconfig(libchromaprint)
%{?_with_crystalhd:BuildRequires: libcrystalhd-devel}
BuildRequires:	pkgconfig(daaladec)
BuildRequires:	pkgconfig(daalaenc)
%{!?_without_libdc1394:BuildRequires: libdc1394-devel}
%{?_with_libdca:BuildRequires: libdca-devel}
%{?_with_libdvbpsi:BuildRequires: libdvbpsi-devel}
BuildRequires:	libdvdnav-devel
BuildRequires:	libebml-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libkate-devel
%{?_with_libmad:BuildRequires: libmad-devel}
BuildRequires:	libmatroska-devel >= 0.7.6
%ifarch x86_64 i686
BuildRequires:	libmfx-devel
%endif
BuildRequires:	libmodplug-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libmpg123-devel
BuildRequires:	libmtp-devel >= 1.0.0
%{?_with_projectm:BuildRequires: libprojectM-devel}
BuildRequires:	libproxy-devel
BuildRequires:	librsvg2-devel >= 2.9.0
BuildRequires:	libssh2-devel
BuildRequires:	libsysfs-devel
BuildRequires:	libshout-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtiger-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig(libidn)
BuildRequires:	pkgconfig(libjpeg)
# Not Yet in EL - libplacebo-6 incompatible
# https://code.videolan.org/videolan/vlc/-/merge_requests/3950
%if 0%{?fedora} && 0%{?fedora} < 39
BuildRequires:	pkgconfig(libplacebo)
%endif
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libvncclient)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	libupnp-devel
BuildRequires:	libv4l-devel
%{?_with_vaapi:BuildRequires: libva-devel}
BuildRequires:  pkgconfig(vdpau)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(vpx)
BuildRequires:	pkgconfig(libxml-2.0)
%{?_with_lirc:BuildRequires: lirc-devel }
%{?_with_live555:BuildRequires: live555-devel >= 0-0.33}
BuildRequires:  kernel-headers
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	libsamplerate-devel
BuildRequires:	libshout-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:	lua5.1-devel, lua5.1
%else
BuildRequires:	lua-devel
%endif
%{?_with_libmpeg2:BuildRequires: libmpeg2-devel >= 0.3.2}
BuildRequires:	ncurses-devel
%{?_with_opencv:BuildRequires: pkgconfig(opencv)}
BuildRequires:	openslp-devel
Buildrequires:	opus-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig(libarchive) >= 3.1.0
BuildRequires:	pkgconfig(libpulse) >= 0.9.8
BuildRequires:	pkgconfig(libsecret-1) >= 0.18
BuildRequires:	pkgconfig(microdns) >= 0.1.2
BuildRequires:	pkgconfig(protobuf-lite) >= 2.5
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:	qt5-qtbase-private-devel
%endif
BuildRequires:	pkgconfig(Qt5Core) >= 5.5
BuildRequires:	pkgconfig(Qt5Gui) >= 5.5
BuildRequires:	pkgconfig(Qt5Svg) >= 5.5
BuildRequires:	pkgconfig(Qt5X11Extras) >= 5.5
BuildRequires:	pkgconfig(soxr)
BuildRequires:	pkgconfig(spatialaudio)
BuildRequires:	pkgconfig(speexdsp) >= 1.0.5
BuildRequires:	pkgconfig(srt)
%{?_with_wayland:
BuildRequires:	pkgconfig(wayland-client) >= 1.5.91
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(wayland-protocols)
}
%{?_with_schroedinger:BuildRequires: pkgconfig(schroedinger-1.0)}
BuildRequires:	pkgconfig(sqlite3)
%{?_with_sidplay:BuildRequires: pkgconfig(libsidplay2)}
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(taglib)
%{?_with_twolame:BuildRequires: pkgconfig(twolame)}
%{?_with_vcdimager:BuildRequires: vcdimager-devel >= 0.7.21}
%{?_with_x264:BuildRequires: x264-devel >= 0-0.8.20061028}
%{?_with_x265:BuildRequires: x265-devel}
%{?_with_xvidcore:BuildRequires: xvidcore-devel}
BuildRequires:	zlib-devel
BuildRequires:	zvbi-devel

# X-libs
BuildRequires:	libXt-devel
BuildRequires:	libXv-devel
BuildRequires:	libXxf86vm-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXinerama-devel
BuildRequires:	libXpm-devel
%{!?_without_xcb:
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
BuildRequires:  pkgconfig(xcb-keysyms)
}
BuildRequires:	xorg-x11-proto-devel

%{?_with_rpi:
ExclusiveArch:  armv7hnl
BuildRequires:  raspberrypi-vc-devel
BuildRequires:  raspberrypi-vc-static
}

%if 0%{?el7}
BuildRequires: devtoolset-%{dts_ver}-toolchain, devtoolset-%{dts_ver}-libatomic-devel
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  phonon-qt5-devel
BuildRequires:  phonon-qt5-backend-gstreamer
%else
# phonon is unmaintained on EL7
Obsoletes: phonon-backend-vlc < 0.6.2-3
Provides: phonon-backend-vlc = 0.6.2-3
%endif

%{?_with_wayland:
# Fedora 25 Workstation default to wayland but not all
# Boolean deps will handle this better when allowed
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends: qt5-qtwayland%{_isa}
%endif
}

#Merge back jack plugin into main
Obsoletes: vlc-plugin-jack < %{version}-%{release}
Provides: vlc-plugin-jack = %{version}-%{release}

Provides: %{name}-xorg%{_isa} = %{epoch}:%{version}-%{release}
Requires: vlc-core%{_isa} = %{epoch}:%{version}-%{release}

Requires: dejavu-sans-fonts
Requires: dejavu-sans-mono-fonts
Requires: dejavu-serif-fonts

#For xdg-sreensaver
Requires: xdg-utils

Requires:       hicolor-icon-theme

%if 0%{?el7:1}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
%endif


%description
VLC media player is a highly portable multimedia player and multimedia framework
capable of reading most audio and video formats as well as DVDs, Audio CDs VCDs,
and various streaming protocols.
It can also be used as a media converter or a server to stream in uni-cast or 
multi-cast in IPv4 or IPv6 on networks.


%package devel
Summary:	Development files for %{name}
Requires:	%{name}-core%{_isa} = %{epoch}:%{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package core
Summary:	VLC media player core
Provides:	vlc-nox = %{epoch}:%{version}-%{release}
%{?live555_version:Requires: live555%{?_isa} = %{live555_version}}
%{?lua_version:Requires: lua(abi) = %{lua_version}}

%description core
VLC media player core components

%package extras
Summary:	VLC media player with extras modules
Requires:	vlc-core%{_isa} = %{epoch}:%{version}-%{release}
%if 0%{?el7:1}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
%endif

%description extras
VLC media player extras modules.


%prep
%setup -q -n %{vlc_setup}
%patch -P3 -p1
%if 0%{?fedora} > 37 || 0%{?rhel} > 8
%patch -P4 -p1
%endif
%if 0%{?el7}
%patch -P5 -p1
%patch -P6 -p1
# Lower opus requirement - rfbz#5585
sed -i -e 's/opus >= 1.0.3/opus >= 1.0.2/' configure.ac
sed -i -e 's/opus_multistream_surround_encoder_create/opus_multistream_encoder_create/g' modules/codec/opus.c
sed -i -e 's/ header.channel_mapping,//' modules/codec/opus.c
# Lower taglib
sed -i -e 's/taglib >= 1.9/taglib >= 1.8/' configure.ac
. /opt/rh/devtoolset-%{dts_ver}/enable
%endif
%if 0%{?fedora} || 0%{?rhel} > 7
%patch -P7 -p1
sed -i -e 's/luac/luac-5.1/g' configure.ac
%endif

%patch -P9 -p1

%{?_with_bootstrap:
rm aclocal.m4 m4/lib*.m4 m4/lt*.m4 || :
./bootstrap
}

touch src/revision.txt


%build
%if 0%{?el7}
. /opt/rh/devtoolset-%{dts_ver}/enable
%endif

%configure \
	--disable-dependency-tracking		\
	--disable-optimizations			\
	--disable-silent-rules			\
	--with-default-font=%{_fontbasedir}/dejavu/DejaVuSans.ttf \
	--with-default-font-family=DejaVuSans \
	--with-default-monospace-font=%{_fontbasedir}/dejavu/DejaVuSansMono.ttf \
	--with-default-monospace-font-family=DejaVuSansMono \
	--with-kde-solid=no			\
	--with-pic				\
	--disable-rpath			\
	--with-binary-version=%{version}	\
	--enable-lua				\
%{?_with_live555:--enable-live555} 		\
%{!?_with_opencv:--disable-opencv} \
%{!?el8:--enable-sftp} \
%{?_with_vcdimager:--enable-vcdx}		\
%{?_with_rpi: \
	--enable-omxil				\
	--enable-omxil-vout			\
	--enable-rpi-omxil			\
	--enable-mmal				\
	--enable-mmal-avcodec			\
} \
%{?_with_aom:--enable-aom}                      \
%{!?_with_a52dec:--disable-a52}			\
%{?_with_dav1d:--enable-dav1d}                  \
%{!?_with_ffmpeg:--disable-avcodec --disable-avformat \
	--disable-swscale --disable-postproc} \
%{?_with_faad2:--enable-faad} \
%{!?_with_libmad:--disable-mad} \
%{?_with_twolame:--enable-twolame} \
%{?!_without_freeworld: --enable-realrtsp} \
	--enable-flac				\
	--enable-tremor				\
	--enable-speex				\
	--enable-theora				\
	--enable-libass				\
	--enable-shout				\
%{?_with_wayland: --enable-wayland} 		\
%{!?_without_xcb:--enable-xcb --enable-xvideo} 	\
%{?_without_xcb:--disable-xcb --disable-xvideo} \
	--enable-svg				\
	--enable-aa				\
	--enable-caca				\
	--enable-jack				\
	--enable-pulse				\
	--enable-ncurses			\
	--enable-lirc


%if 0
# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%endif

%if 1
# clean unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%endif



%make_build


%install
%make_install INSTALL="install -p" CPPROG="cp -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

desktop-file-validate %{buildroot}%{_datadir}/applications/vlc.desktop

# Remove installed fonts for skins2
rm -rf %{buildroot}%{_datadir}/vlc/skins2/fonts

#Fix unowned directories
rm -rf %{buildroot}%{_docdir}/vlc

#Ghost the plugins cache
touch %{buildroot}%{_libdir}/vlc/plugins/plugins.dat

#Appdata
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/metainfo/*.appdata.xml || :

#Fixup
rm -rf %{buildroot}/%{_datadir}/macosx

#Disable KDE4 desktop files
rm -rf  %{buildroot}%{_datadir}/kde4


%find_lang %{name}

%check
%if 0%{?el7}
. /opt/rh/devtoolset-%{dts_ver}/enable
%endif
make check || :


%ldconfig_scriptlets core

%post
%{?ldconfig}
if [ $1 == 1 ] ; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins &>/dev/null
fi || :

%{_bindir}/touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi 
%{_bindir}/update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
%{?ldconfig}
%{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins &>/dev/null
%{_bindir}/update-desktop-database %{_datadir}/applications &>/dev/null
%{_bindir}/touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi || :

%posttrans core
%{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins &>/dev/null || :

%post extras
%{?ldconfig}
if [ $1 == 1 ] ; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins &>/dev/null || :
fi

%postun extras
%{?ldconfig}
if [ $1 == 0 ] ; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins &>/dev/null || :
fi

%preun core
if [ $1 == 0 ] ; then
  rm -f %{_libdir}/vlc/plugins*.dat
fi || :


%files
%doc AUTHORS NEWS README THANKS
%license COPYING
%{_datadir}/metainfo/vlc.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/vlc*.png
%{_datadir}/icons/hicolor/*/apps/vlc*.xpm
%{_datadir}/vlc/skins2/
%{_bindir}/qvlc
%{_bindir}/svlc
%{_libdir}/vlc/libvlc_pulse.so*
# qt in main
%{_libdir}/vlc/plugins/gui/libqt_plugin.so
# skin2 in main
%{_libdir}/vlc/plugins/gui/libskins2_plugin.so
%{?_with_projectm:
%{_libdir}/vlc/plugins/visualization/libprojectm_plugin.so
}
#jack in main
%{_libdir}/vlc/plugins/access/libaccess_jack_plugin.so
%{_libdir}/vlc/plugins/audio_output/libjack_plugin.so
#pulseaudio in main
%{_libdir}/vlc/plugins/audio_output/libpulse_plugin.so
%{_libdir}/vlc/plugins/access/libpulsesrc_plugin.so
%{_libdir}/vlc/plugins/services_discovery/libpulselist_plugin.so
%{?_with_fluidsynth:
%{_libdir}/vlc/plugins/codec/libfluidsynth_plugin.so
}

%files core -f %{name}.lang
%{_bindir}/vlc
%{_bindir}/cvlc
%{_bindir}/nvlc
%{_bindir}/rvlc
%{_bindir}/vlc-wrapper
%exclude %{_datadir}/vlc/skins2
%{_datadir}/vlc/
%{_libdir}/*.so.*
%dir %{_libdir}/vlc
%{_libdir}/vlc/lua/
%{_libdir}/vlc/libvlc_vdpau.so*
%{_libdir}/vlc/libvlc_xcb_events.so*
%exclude %{_libdir}/vlc/plugins/access/libaccess_jack_plugin.so
%{?_with_asdcp:
%exclude %{_libdir}/vlc/plugins/access/libdcp_plugin.so
}
%{?_with_vcdimager:
%exclude %{_libdir}/vlc/plugins/access/libvcd_plugin.so
%exclude %{_libdir}/vlc/plugins/access/libvcdx_plugin.so
%exclude %{_libdir}/vlc/plugins/codec/libsvcdsub_plugin.so
}
%{?_with_crystalhd:
%exclude %{_libdir}/vlc/plugins/codec/libcrystalhd_plugin.so
}
%{?_with_fluidsynth:
%exclude %{_libdir}/vlc/plugins/codec/libfluidsynth_plugin.so
}
%exclude %{_libdir}/vlc/plugins/gui/libqt_plugin.so
%exclude %{_libdir}/vlc/plugins/gui/libskins2_plugin.so
%{?_with_opencv:
%exclude %{_libdir}/vlc/plugins/video_filter/libopencv_example_plugin.so
%exclude %{_libdir}/vlc/plugins/video_filter/libopencv_wrapper_plugin.so
}
%{?_with_projectm:
%exclude %{_libdir}/vlc/plugins/visualization/libprojectm_plugin.so
}
%exclude %{_libdir}/vlc/plugins/audio_output/libjack_plugin.so
%exclude %{_libdir}/vlc/plugins/audio_output/libpulse_plugin.so
%exclude %{_libdir}/vlc/plugins/access/libpulsesrc_plugin.so
%exclude %{_libdir}/vlc/plugins/services_discovery/libpulselist_plugin.so
%ghost %{_libdir}/vlc/plugins/plugins.dat
%{_libdir}/vlc/vlc-cache-gen
%{_libdir}/vlc/plugins
%{_mandir}/man1/vlc*.1*


%files extras
%{?_with_opencv:
%{_libdir}/vlc/plugins/video_filter/libopencv_example_plugin.so
%{_libdir}/vlc/plugins/video_filter/libopencv_wrapper_plugin.so
}
%{?_with_vcdimager:
%{_libdir}/vlc/plugins/access/libvcd_plugin.so
%{_libdir}/vlc/plugins/access/libvcdx_plugin.so
%{_libdir}/vlc/plugins/codec/libsvcdsub_plugin.so
}
%{?_with_crystalhd:
%{_libdir}/vlc/plugins/codec/libcrystalhd_plugin.so
}
%{?_with_asdcp:
%{_libdir}/vlc/plugins/access/libdcp_plugin.so
}

%files devel
%dir %{_includedir}/vlc
%{_includedir}/vlc/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/vlc-plugin.pc
%{_libdir}/pkgconfig/libvlc.pc



%changelog
* Fri Jul 28 2023 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.19-0.5
- Update snapshot
- Use onevpl for f38+ and el9+

* Tue Jun 13 2023 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.19-0.4
- Update snapshot

* Mon Apr 10 2023 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.19-0.3.1
- Rebuild for live555

* Sun Mar 26 2023 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.19-0.2.1
- rebuilt

* Thu Mar 23 2023 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.19-0.1.1
- rebuilt

* Wed Mar 22 2023 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.19-0.2
- Update snapshot

* Sun Dec 25 2022 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.18-4
- Add libplacebo-5

* Fri Dec 23 2022 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.18-3
- Update to current snapshot

* Sun Nov 06 2022 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.18-2
- Rebuild for live555

* Sun Oct 16 2022 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.18-1
- Update to 3.0.18

* Fri Sep 30 2022 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.18-0.3.rc
- Update to 3.0.18-rc2

* Mon Sep 26 2022 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.18-0.2.rc
- Rebuild for new flac

* Mon Aug 29 2022 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.18-0.1.rc
- Update to 3.0.18-rc
- Drop mmal downstream (rpi) patches
- Drop merged patches

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:3.0.17.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Fri Jul 22 2022 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.17.4-7
- Rebuild for new ffmpeg

* Fri Jul 15 2022 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.17.4-6
- rebuilt

* Tue Jul 05 2022 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.17.4-5
- rebuilt

* Fri Jun 24 2022 Robert-André Mauchin <zebob.m@gmail.com> - 1:3.0.17.4-4
- Rebuilt for new AOM and dav1d

* Fri Jun 24 2022 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.17.4-3
- Rebuilt

* Sun Jun 12 2022 Sérgio Basto <sergio@serjux.com> - 1:3.0.17.4-2
- Mass rebuild for x264-0.164

* Sun May 15 2022 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.17.4-1
- Update to 3.0.17.4

* Thu Mar 10 2022 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.17.2-1
- Update to 3.0.17.2 (rfbz#6241)

* Tue Feb 22 2022 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.17-7
- Update to 3.0.17

* Fri Feb 04 2022 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.17-6
- rebuilt

* Wed Jan 19 2022 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.17-5
- rebuilt

* Tue Jan 18 2022 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.17-4
- Bump

* Sat Jan 15 2022 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.17-3
- Update 3.x snapshot

* Fri Nov 19 2021 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.17-2
- Rebuilt

* Thu Nov 11 2021 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.17-1
- Update to 3.x snapshot

* Tue Nov 09 2021 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.16-7
- Rebuilt for new ffmpeg snapshot

* Sat Oct 30 2021 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.16-6
- rebuilt

* Thu Aug 19 2021 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.16-5
- Rebuilt

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Sérgio Basto <sergio@serjux.com> - 1:3.0.16-3
- Mass rebuild for x264-0.163

* Wed Jun 30 2021 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.16-2
- Rebuilt

* Sat Jun 19 2021 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.16-1
- Update to 3.0.16

* Wed Jun 16 2021 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.15-3
- Bump

* Sun Jun 13 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1:3.0.15-2
- Rebuild for new aom

* Sat Jun 12 2021 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.15-1
- Update to 3.0.15

* Tue May 11 2021 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.14-1
- Update to 3.0.14

* Mon May 10 2021 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.13-2.1
- rebuilt

* Wed May 05 2021 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.13-1.1
- rebuilt

* Thu Apr 29 2021 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.13-1
- Update to 3.0.13

* Wed Apr 14 2021 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.12.1-9
- Rebuild for new x265

* Fri Apr 02 2021 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.12.1-8
- rebuilt

* Tue Mar 02 2021 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.12.1-7
- Update snapshot

* Thu Feb 11 2021 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.12.1-6
- Rebuilt

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.0.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.12.1-4
- Rebuild

* Wed Jan 20 2021 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.12.1-3
- Rebuild

* Thu Dec 31 2020 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.12.1-2
- Rebuilt for new ffmpeg snapshot

* Mon Dec 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.12.1-1
- Update to 3.0.12.1

* Wed Dec 16 2020 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.12-1
- Update to 3.0.12

* Mon Dec 14 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1:3.0.12-0.4
- Rebuild for dav1d SONAME bump
- Add patch to build with GCC 11.0.0

* Fri Nov 27 2020 Sérgio Basto <sergio@serjux.com> - 1:3.0.12-0.3
- Mass rebuild for x264-0.161

* Fri Oct 30 2020 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.12-0.2
- Backport fix for libnotify - Enable vlc notify

* Fri Oct 30 2020 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.12-0.1
- Update snapshoot
- Switch to lua-5.1

* Wed Oct 21 2020 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.11.1-6
- Rebuild for new libdvdread

* Mon Sep 28 2020 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.11.1-5
- Rebuild for new protobuf

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Aug 02 2020 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.11.1-3
- Revert "Disable LTO"

* Sat Aug 01 2020 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.11.1-2
- Rebuilt for live555

* Mon Jul 27 2020 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.11.1-1
- Update to 3.0.11.1

* Sat Jul 18 2020 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.11-7
- Rebuilt

* Wed Jul 08 2020 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.11-6
- Rebuilt

* Tue Jul 07 2020 Sérgio Basto <sergio@serjux.com> - 1:3.0.11-5
- Mass rebuild for x264

* Wed Jul 01 2020 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.11-4
- Rebuilt for new dav1d and libplacebo

* Tue Jun 30 2020 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.11-3
- Rebuilt

* Wed Jun 24 2020 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.11-2
- rebuilt

* Mon Jun 15 2020 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.11-1
- Update to 3.0.11

* Sun May 31 2020 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.10-3
- Rebuild for new x265 version

* Sun May 24 2020 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.10-2
- Rebuild for dav1d SONAME bump

* Tue Apr 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.10-1
- Update to 3.0.10
- Back to devtoolset-7 for EL7

* Fri Apr 24 2020 Leigh Scott <leigh123linux@googlemail.com> - 1:3.0.9.2-3
- Fix srt issue (rfbz#5614)

* Mon Apr 13 2020 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.9.2-2
- Rebuilt for live555

* Wed Apr 08 2020 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.9.2-1
- Update to 3.0.9.2
- Enable srt
- Enable libssh2 even on el8

* Sun Apr 05 2020 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.9-36
- Lower libopus requirement for el7 - rfbz#5585
- Add patch to build with libdvdread/libdvdnav for rhel

* Sun Apr 05 2020 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.9-35
- Switch to gitlab snapshot
- Switch to devtoolset-8 for el7

* Thu Apr 02 2020 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.9-34
- Update to 20200402
- Enable make tests

* Fri Mar 06 2020 leigh123linux <leigh123linux@googlemail.com> - 1:3.0.9-33
- Update to current snapshot

* Sun Feb 23 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:3.0.9-32
- Rebuild for x265

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:3.0.9-31
- Rebuild for ffmpeg-4.3 git

* Sat Feb 08 2020 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.9-30
- Rebuild for new libplacebo version

* Sat Feb 01 2020 Leigh Scott <leigh123linux@googlemail.com> - 1:3.0.9-29
- rebuilt

* Sat Jan 18 2020 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.9-28
- Update to current snapshot
- Drop libssh2 from el8 - rfbz#5519
- Update mmal patch

* Sun Dec 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:3.0.9-27
- Rebuild for new protobuf version

* Thu Dec 19 2019 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.9-26
- Rebuild for new libplacebo version

* Tue Dec 17 2019 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.9-25
- Mass rebuild for x264

* Thu Nov 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:3.0.9-24
- Rebuild for new x265

* Fri Nov 15 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1:3.0.9-23
- rebuild for libdvdread ABI bump

* Thu Oct 24 2019 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.9-22
- Rebuild for dav1d SONAME bump

* Mon Oct 14 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.9-21
- Update to 20191014
- Update mmal patch to 10

* Tue Sep 17 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.8-20
- Add EL8 support
- Drop kde-filesystem

* Wed Aug 21 2019 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.8-2
- Rebuild for dav1d and aom SONAME bump

* Tue Aug 20 2019 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.8-1
- Update to 3.0.8 - 20190820 snapshot

* Tue Aug 06 2019 Leigh Scott <leigh123linux@gmail.com> - 1:3.0.8-0.5
- Rebuild for new ffmpeg version

* Wed Jul 31 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.8-0.4
- Update snapshot

* Fri Jul 19 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.8-0.3
- Rebuilt for live555

* Thu Jul 18 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.8-0.2
- Update snapshot
- Add system-wide ciphers

* Tue Jul 02 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.8-0.1
- Update to 20190702

* Tue Jun 18 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.7.1-4
- Avoid files listed twice
- Rework with/without options

* Mon Jun 17 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.7.1-3
- Move asdcp plugin to extras

* Wed Jun 12 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:3.0.7.1-2
- Enable asdcplib

* Wed Jun 12 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:3.0.7.1-1
- Update to 3.0.7.1

* Fri Jun 07 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:3.0.7-2
- Enable libplacebo

* Fri Jun 07 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:3.0.7-1
- Update to 3.0.7

* Sat Apr 06 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.7-0.1
- Update to 20190406
- Rebuilt for live555
- Rebuilt for libplacebo
- Update mmal patch

* Tue Mar 26 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.6-24
- Drop projectm until fixed

* Tue Mar 12 2019 Sérgio Basto <sergio@serjux.com> - 1:3.0.6-23
- Mass rebuild for x264

* Tue Mar 05 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.6-22
- Rebuilt for live555/dav1d

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.0.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Feb 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:3.0.6-20
- Rebuild for new x265

* Wed Feb 27 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:3.0.6-19
- Patch for libvpx-1.8.0

* Wed Feb 27 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.6-18
- Rebuilt

* Thu Jan 24 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.6-17
- Drop unmaintained phonon support on el7

* Thu Jan 17 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.6-16
- Update main/core packaging split

* Thu Jan 10 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.6-15
- Update to 3.0.6
- Rework xorg/wayland plugins moved to vlc-core

* Tue Jan 08 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.5-14
- Only enable mmal on rpi
- Fixup vdpau on core

* Fri Jan 04 2019 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.5-12
- Restore Obsoletes/Provides vlc-plugin-jack

* Sun Dec 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:3.0.5-11
- Enable dav1d support

* Thu Dec 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:3.0.5-10
- Update to 3.0.5
- Bump n-v-r to make koji happy

* Thu Dec 20 2018 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.5-0.2
- Add mmal support

* Thu Dec 13 2018 Nicolas Chauvet <kwizart@gmail.com> - 1:3.0.5-0.1
- Bump Epoch
- Update to 20181213

* Thu Nov 29 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.5-7
- Update to 20181129

* Sun Nov 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.5-6
- Rebuild for new x265

* Sun Nov 11 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.5-5
- Update to 20181111

* Sat Oct 20 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.5-4
- Update to 20181020

* Thu Oct 04 2018 Sérgio Basto <sergio@serjux.com> - 3.0.5-3
- Mass rebuild for x264 and/or x265
- Fix build with x264 >= 0.153

* Wed Oct 03 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.5-2
- Update to 20181003 snapshot

* Fri Sep 21 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.5-1
- Update to 3.0.5 snapshot from today
- Enable aom support
- Workaound a bug with vlc-cache-gen on armhfp

* Tue Sep 18 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.4-3
- Expunge qt-devel from buildroot

* Wed Sep 12 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.4-2
- Fix unexpanded ldconfig macro (rfbz#5018)

* Fri Aug 31 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.4-1
- Update to 3.0.4

* Sat Aug 04 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.3-7
- Add patch from vlc mailing list to fix wayland freeze (rfbz#4596)

* Tue Jul 24 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.3-6
- Rebuilt for libplacebo

* Wed Jun 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.3-5
- Revert last commit

* Sat Jun 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.3-4
- Rebuild for new libass version
- Make libplacebo x86 only due to vulkan changes

* Sat Jun 02 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.3-3
- Fix build against Qt 5.11

* Fri Jun 01 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.3-2
- Add missing libjpeg

* Mon May 28 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.3-1
- Update to 3.0.3

* Mon May 14 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.2-3
- Rebuilt

* Mon Apr 23 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.2-2
- Readd lost patch

* Mon Apr 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Tue Apr 17 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.1-6
- Rebuilt for libupnp

* Fri Mar 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.1-5
- Rework version tag
- Add soxr
- Add ldconfig_scriptlets

* Sat Mar 17 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.1-4
- Rebuilt for live555

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 3.0.1-3
- Rebuilt for new ffmpeg snapshot
- Patch for fribidi version 1.0

* Wed Feb 28 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.1-2
- Rebuilt for x265

* Tue Feb 27 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Mon Feb 26 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-3
- Add libplacebo support

* Sun Feb 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-2
- Enable microdns (rfbz#4793)

* Fri Feb 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-1
- Update to 3.0.0 release

* Sun Feb 04 2018 Sérgio Basto <sergio@serjux.com> - 3.0.0-0.53.git20180202.rc9
- Rebuild (live555-2018.01.29)

* Fri Feb 02 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.52.git20180202.rc9
- Update to rc9

* Sat Jan 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-0.51.git20180127.rc8
- Update to 20180127 -rc8
- Rebuild for new libcdio and libvpx

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-0.50.git20180109.rc5
- Rebuilt for ffmpeg-3.5 git

* Mon Jan 15 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.49.git20180109.rc5
- Rebuilt for VA-API 1.0.0

* Tue Jan 09 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.48.git20180109.rc5
- Update to 20180109 -rc5

* Sun Dec 31 2017 Sérgio Basto <sergio@serjux.com> - 3.0.0-0.47.git20171221.rc2
- Mass rebuild for x264 and x265

* Thu Dec 21 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.46.git20171221.rc2
- Update to 20171221
- Drop pre-version
- Set defaults fonts
- Enable gstreamer on %%{arm} and aarch64
- Drop wayland patch

* Sat Dec 16 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0~rc2-0.45.git20171215
- Improve pre-version
- Re-enable i686 mmx/sse (autodetected)

* Fri Dec 15 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.44.git20171215
- Update to 20171215

* Fri Dec 08 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.43.git20171208
- Update to 20171208

* Fri Dec 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-0.42.git20171122
- Rebuild for new protobuf version
- Rebuild against new libmfx (rhbz#1471768)

* Sun Nov 26 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.41.git20171122
- Rebuilt for live555

* Wed Nov 22 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.40.git20171122
- Update to 20171122 snapshot

* Thu Nov 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-0.40.git20171103
- Rebuild for new protobuf version

* Fri Nov 03 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.39.git20171103
- Update to 20171103 snapshoot

* Mon Oct 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-0.38.git20171009
- Rebuild for ffmpeg update

* Mon Oct 09 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-0.37.git20171009
- Update snapshot
- Fix libvlc vdpau issue (rfbz #4678)

* Mon Sep 25 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.36.git20170922
- Rebuilt for live555

* Fri Sep 22 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.35.git20170922
- Update to VDD2017 edition
- https://www.videolan.org/videolan/events/vdd17/

* Wed Aug 23 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.34.git20170823
- Update snapshot

* Mon Jul 31 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.33.git20170717
- Fix lua directory search path

* Tue Jul 25 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.32.git20170717
- Rebuilt for live555

* Mon Jul 17 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.31.git20170717
- Update snapshot

* Tue Jul 04 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.30.git20170704
- Update snapshot
- Use https for downloads - rhbz#4584

* Sat Jun 24 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.29.git20170622
- Restore wayland with a patch - rhbz#4552

* Thu Jun 22 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.28.git20170622
- Update snapshoot
- Disable wayland support for now
- Update release field

* Thu Jun 01 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.2620170601git
- Update to 20170601 snapshot

* Thu May 25 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.25
- Rebuilt for live555

* Tue May 23 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.24
- Update to 20170523 snapshot

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-0.23
- Rebuild for ffmpeg update

* Thu Apr 27 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.22
- Update ot 20170427 snapshot

* Wed Apr 05 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.21
- Update to 20170405 snapshoot
- Rework main -core library split

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 3.0.0-0.20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 16 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.19
- Update to 20170318 snapshoot
- Drop hidpi revert rfbz#4272
- Recommends qt5-qtwayland

* Thu Feb 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-0.18
- Rebuild for libvncserver .so version bump

* Mon Feb 20 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.17
- Update to 20170220 snapshot
- Clean merged patch, unrevert wayland runtime detection
- Switch source url on purpose

* Tue Jan 31 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.16
- Add daala support

* Tue Jan 17 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.15
- Fix lirc activation - rhbz#4420
- Revert upstream commit 785b0f18d7 for wayland detection - rfbz#4380

* Mon Jan 09 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.14
- Update to 20170109
- Disable wayland for now - rhbz#4380
- Move libvlc pulse,vdpau,xcb from -core to main

* Tue Jan 03 2017 Dominik Mierzejewski <rpm@greysector.net> - 3.0.0-0.13
- rebuild for x265

* Mon Dec 12 2016 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.12
- Update to 20161212 snapshot
- Add BR: vpx, mpg123 and mfx

* Tue Nov 22 2016 leigh scott <leigh123linux@googlemail.com> - 3.0.0-0.11
- add patch to disable HIDPI scaling - rfbz#4272

* Tue Nov 08 2016 Sérgio Basto <sergio@serjux.com> - 3.0.0-0.10
- Rebuild for x265-2.1

* Fri Oct 28 2016 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.9
- Updateto 3.0.0 20161026-0238-git
- Merge vlc-plugin-jack into main
- Add support for appdata

* Thu Sep 08 2016 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.8
- Re-enable bootstrap

* Fri Sep 02 2016 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.7
- Bump to 20160901 nightly
- Fix plugins.dat path - rfbz#4184

* Thu Aug 18 2016 Sérgio Basto <sergio@serjux.com> - 3.0.0-0.6
- Clean spec, Vascom patches series, rfbz #4196, add license tag

* Thu Aug 04 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-0.5
- Remove -f from vlc-cache-gen scriptlets rfbz#4167

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 3.0.0-0.4
- Rebuilt for ffmpeg-3.1.1

* Fri Jul 29 2016 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.3
- Update to today snapshoot

* Fri Jul 01 2016 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.2
- Update to today snapshot

* Tue Jun 14 2016 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-0.1
- Update to 3.0.0 - snapshot 20160614
- Switch to qt5
- Update Build Dependencies

* Mon Jun 06 2016 Nicolas Chauvet <kwizart@gmail.com> - 2.2.4-1
- Update to 2.2.4

* Wed May 04 2016 Nicolas Chauvet <kwizart@gmail.com> - 2.2.3-1
- Update to 2.2.3

* Sat Feb 06 2016 Nicolas Chauvet <kwizart@gmail.com> - 2.2.2-1
- Update to 2.2.2

* Tue Oct 06 2015 Nicolas Chauvet <kwizart@gmail.com> - 2.2.2-0.1
- Update to 2.2.2 pre-version

* Sat May 16 2015 Nicolas Chauvet <kwizart@gmail.com> - 2.2.1-6
- Rebuilt for x265

* Wed May 13 2015 Nicolas Chauvet <kwizart@gmail.com> - 2.2.1-5
- Update to current bugfix

* Sat May 09 2015 Nicolas Chauvet <kwizart@gmail.com> - 2.2.1-4
- Recreate the plugins cache on post for main - rfbz#3639
- %%ghost the cache plugins

* Sun Apr 26 2015 Nicolas Chauvet <kwizart@gmail.com> - 2.2.1-3
- Fix build with freerdp for f22
- Disable optimizations
- Disable mmx and sse on fedora >= 22

* Thu Apr 16 2015 Nicolas Chauvet <kwizart@gmail.com> - 2.2.1-2
- Rebuilt for x265

* Mon Apr 13 2015 Nicolas Chauvet <kwizart@gmail.com> - 2.2.1-1
- Update to 2.2.1
- Enable x265 on armhfp
- Add --with rpi conditional for raspberrypi and mmal

* Fri Feb 27 2015 Nicolas Chauvet <kwizart@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Tue Nov 25 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.2.0-0.2
- Update to 2.2.0-rc2

* Fri Nov 14 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.2.0-0.1
- Update to 2.2.0-rc1

* Sun Sep 28 2014 kwizart <kwizart@gmail.com> - 2.1.5-4
- Allow build with ffmpeg24

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.1.5-3
- Rebuilt for FFmpeg 2.4.x

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 2.1.5-2
- Rebuilt for ffmpeg-2.3

* Sat Jul 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.1.5-1
- Update to 2.1.5

* Sat Apr 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.1.4-5
- Rebuilt for libgcrypt

* Sat Mar 29 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.1.4-4
- Rebuilt for ffmpeg

* Sat Mar 22 2014 Sérgio Basto <sergio@serjux.com> - 2.1.4-3
- Rebuilt for x264

* Thu Mar 06 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.1.4-2
- Rebuilt for x264

* Fri Feb 21 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.1.4-1
- Update to 2.1.4

* Thu Feb 06 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.1.3-1
- Update to 2.1.3

* Fri Jan 17 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.1.2-2
- Disable freerdp for f21

* Tue Dec 10 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.1.2-1
- Update to 2.1.2

* Thu Nov 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.1.1-2
- Rebuilt for live555

* Thu Nov 14 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.1.1-1
- Update to 2.1.1

* Tue Nov 05 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-3
- Rebuilt for x264/FFmpeg

* Tue Oct 22 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-2
- Rebuilt for x264

* Tue Oct 01 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Wed Aug 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-0.8.rc1
- Update to 2.1.0-rc1

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-0.6.pre2
- Rebuilt for FFmpeg 2.0.x

* Fri Jul 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-0.5.pre2
- Update to 2.1.0-pre2

* Sat Jul 20 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-0.4.pre1
- Rebuilt for x264

* Fri Jul 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-0.3.pre1
- Use Officially tagged 2.1.0-pre1

* Wed Jun 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-0.2.pre1
- Update to 2.1.0-pre1

* Mon Apr 08 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.6-1
- Update to 2.0.6

* Tue Mar 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.5-6
- Move %%{_datadir}/vlc/lua/http/.hosts to hosts-sample to avoid
  config file - https://bugzilla.rpmfusion.org/2726

* Sat Feb 23 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.5-5
- Fix samba4 detection rfbz#2659

* Wed Jan 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.5-4
- Add new live555 requires

* Sun Jan 20 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.5-3
- Rebuilt for ffmpeg/x264

* Wed Jan 02 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.5-2
- Fix build with FLAC-1.3.x

* Fri Dec 14 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.5-1
- Update to 2.0.5

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.4-3
- Fix build with kernel-3.7

* Fri Nov 23 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.4-2
- Rebuilt for x264

* Fri Oct 19 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.4-1
- Update to 2.0.4
- Enable opus
- Disable x86 loader
- Avoid rpath

* Wed Sep 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.3-3
- Fix --with fluidsynth typo

* Wed Sep 05 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.3-2
- Rebuilt for x264 ABI 125

* Fri Jul 20 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.3-1
- Update to 2.0.3

* Wed Jul 11 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.2-3
- Fix build of xcb
- Switch to pkgconfig(libudev)

* Wed Jul 04 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.2-2
- Rework BR and RPM conditionals
- Drop support for anything below EL-6 and current Fedora.

* Thu Jun 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Sun Jun 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.1-3
- Rebuild for FFmpeg/x264

* Mon Jun 18 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.1-2
- Backport patch for ffmpeg54

* Wed May 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Tue Mar 13 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.0-5
- Rebuilt for x264 ABI 0.120

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.0-4
- Rebuilt for c++ ABI breakage

* Sun Feb 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.0-3
- Reenable skins2 - rfbz#2195
- Disable internal live555 build

* Wed Feb 22 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.0-2
- Rebuilt for x264/FFmpeg

* Sun Feb 19 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.0-1
- Update to 2.0.0 (Final)

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.0-0.9_rc1
- Update to 2.0.0-rc1

* Mon Jan 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-0.7_pre4
- Update to 1.2.0-pre4

* Mon Jan 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-0.6_pre3
- Add BR game-music-emu-devel
- move vcdimager plugin to vlc-extras

* Wed Dec 28 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-0.5_pre3
- Update to 1.2.0-pre3

* Tue Dec 13 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-0.4_pre2
- Rebuild for libbluray

* Sat Dec 10 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-0.3_pre2
- Rebuilt with xz to workaround rfbz#2086

* Wed Dec 07 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-0.2_pre2
- Update to 1.2.0-pre2
- Reverse build conditional to --without freeworld
  So it can be tested with Fedora only (patches welcomed)
- Disable xcb globalhotkeys in Rawhide/F-17

* Fri Oct 07 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.12-1
- Update to 1.1.12
- Add 2 already merged patches

* Tue Sep 20 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.11-2
- Update to current bugfix
- Add patch for FFmpeg-0.8

* Wed Jul 20 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.11-1
- Update to 1.1.11

* Fri Jul 15 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.10-2
- Rebuilt for x264 ABI 115

* Mon Jun 06 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.10-1
- Update to 1.1.10
- backport from 1.1-bugfix
- Re-add mozilla-vlc for f15

* Tue May 10 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.9-2
- Rebuilt for libdvbpsi

* Tue Apr 12 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.9-1
- Update to 1.1.9

* Wed Apr 06 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.8-2
- Backport youtube lua fix - rfbz#1675

* Thu Mar 24 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.8-1
- Update to 1.1.8

* Fri Mar 11 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.8-0.2.1
- Rebuilt for new x264/FFmpeg

* Mon Mar 07 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.8-0.1.1
- Update to pre-1.1.8 bugfix git from today

* Wed Feb 02 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.7-1
- Update to 1.1.7

* Sat Jan 29 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.6.1-1
- Update to 1.1.6.1
- Remove merged patches

* Mon Jan 24 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.6-2
- Update to 1.1.6
- backport lirc and signal fixes

* Sat Dec 18 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.5-2
-  Clear execstack on dmo and real plugin for i686

* Sun Nov 14 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.5-1
- Update to 1.1.5
- Rename nox subpackage to extras
- Move opencv modules to extras
- Move libnotify module to extras until f15

* Wed Nov 10 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.4-6
- Disable notify by f15 - deprecated upstream
- Fix libProjectM crash once selected.
- Fix default CA file for gnutls module.
- xosd not built by default - deprecated upstream

* Tue Nov 09 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.4-5
- Enable VAAPI

* Sun Oct 24 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.4-4
- Workaround for taglib not been tread safe

* Sun Oct 17 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.4-3
- Explicitely use -fPIC compilation even for dmo plugin
- Silence post scriptlet

* Sun Sep 05 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.4-2
- Adds support for vlc-cache-gen
- Drop support for vlc-handlers.schemas
  (will be handled in .desktop file)

* Sat Aug 28 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.4-1
- Update to 1.1.4
- Fix libnotify build on f14
- Obsoletes ffmpeg4vlc
- Raise selinux requirements that fix rhbz#591854

* Sat Aug 21 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.3-1
- Update to 1.1.3
- move some plugin from core to main

* Thu Aug 05 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Thu Jul 01 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Sat Jun 12 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-0.12.rc3
- Update to -rc3

* Tue Jun 08 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-0.11.rc2
- Fix segfault on dlopen

* Mon Jun 07 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-0.10.rc2
- Fix --with a52dec conditional

* Fri Jun 04 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-0.9.rc2
- Update to 1.1.0-rc2

* Sun May  2 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.1.0-0.6.pre3
- Update to 1.1.0-pre3
- Add patch from rdieter

* Fri Apr 16 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.1.0-0.3.pre1
- Update to 1.1.0-pre1
- Built for Fedora
- Changed summary and descriptions

* Sat Feb 27 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.0.5-2
- Add BR libtiger-devel

* Thu Jan 28 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Tue Jan 26 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.0.4-3
- Rebuild

* Sun Jan  3 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.0.4-2
- Add vlc-1.0.4-xulrunner-192.patch

* Tue Dec 15 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4
- Drop patch2 - PulseaAudio is tried first from original sources.

* Sat Oct 31 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Sun Oct 25 2009 kwizart < kwizart at gmail.com > - 1.0.3-0.1_rc
- Update to 1.0.3-rc
- Update bugfix to 20091025
- Clean dc1394 sub-package

* Fri Oct 16 2009 kwizart < kwizart at gmail.com > - 1.0.2-2
- Update to 1.0-bugfix 20091016
- Rebuild for x264/ffmpeg

* Sun Sep 27 2009 kwizart < kwizart at gmail.com > - 1.0.2-1.2
- Disable the workaround for the compiler bug. (rhbz#524439)
- Resync with the fonts requirement.

* Sun Sep 20 2009 kwizart < kwizart at gmail.com > - 1.0.2-1.1
- Workaround the compiler bug on x86 x86_64 by disabling optimization.

* Sat Sep 19 2009 kwizart < kwizart at gmail.com > - 1.0.2-1
- Update to 1.0.2

* Wed Aug 12 2009 kwizart < kwizart at gmail.com > - 1.0.1-2
- Conditionalize libass until stabilized ABI.
- Update to 1.0-bugfix 20090812

* Tue Jul 28 2009 kwizart < kwizart at gmail.com > - 1.0.1-1
- Update to 1.0.1 (Final)
- Improve conditionals
- Backport zip qt4 from 1.0-bugfix
- More %%_isa requirement

* Mon Jul  6 2009 kwizart < kwizart at gmail.com > - 1.0.0-1
- Update to 1.0.0 (Final)

* Thu Jul  2 2009 kwizart < kwizart at gmail.com > - 1.0.0-0.14rc4
- Cherry pick from 1.0-bugfix
- Move xcb modules into main
- Move -devel Requirement from main to -core (Mutlilib fix)

* Wed Jun 17 2009 kwizart < kwizart at gmail.com > - 1.0.0-0.12rc4
- Update to 1.0.0-rc4

* Sun Jun  7 2009 kwizart < kwizart at gmail.com > - 1.0.0-0.11rc3
- Update to 1.0.0-rc3

* Fri Jun  5 2009 kwizart < kwizart at gmail.com > - 1.0.0-0.10rc2
- Move some module to avoid dependency
- Remove previous signal-slot connection(s) if any - vlc trac #2818

* Tue Jun  2 2009 kwizart < kwizart at gmail.com > - 1.0.0-0.9rc2
- Update to current bugfix
- Revert b8f23ea716693d8d07dd8bd0cb4c9ba8ed05f568
- Split plugin-jack

* Wed May 27 2009 kwizart < kwizart at gmail.com > - 1.0.0-0.7rc2
- Update to 1.0.0-rc2
- Rebase xulrunner patch for -rc2
- Add GConf2 support for url-handler (based on totem)

* Wed May 13 2009 kwizart < kwizart at gmail.com > - 1.0.0-0.5rc1
- Fix missing XvMC symbols
- Fix export make_URI

* Tue May 12 2009 kwizart < kwizart at gmail.com > - 1.0.0-0.4rc1
- Update to 1.0.0-rc1
- Add 1.0-bugfix patches

* Fri Apr 17 2009 kwizart < kwizart at gmail.com > - 1.0.0-0.3pre2
- Update to 1.0.0-pre2

* Fri Apr 10 2009 kwizart < kwizart at gmail.com > - 1.0.0-0.2pre1
- Re-enable xxmc
- Remove libmpeg2 out

* Fri Mar 27 2009 kwizart < kwizart at gmail.com > - 1.0.0-0.1pre1
- Update to 1.0.0-pre1
- Add mozilla plugin with xulrunner-1.9.1. Patch from Alexey Gladkov
- Disable xxmc

* Fri Mar  6 2009 kwizart < kwizart at gmail.com > - 0.9.9-0.4rc2
- Update to 0.9.9-rc2

* Fri Feb 27 2009 kwizart < kwizart at gmail.com > - 0.9.9-0.3rc
- Rename the Required font package.

* Fri Feb 13 2009 kwizart < kwizart at gmail.com > - 0.9.9-0.1rc
- Update to 0.9.9rc
- Move Xless binaries to the -core subpackage
- Add support for libxul 1.9.1

* Fri Jan 16 2009 kwizart < kwizart at gmail.com > - 0.9.8a-3
- Add libxul 1.9.1 preliminary support
- backport postproc fixes
- Add pending 0.9-bugfix git branch
- Add lua support by default

* Thu Jan 15 2009 kwizart < kwizart at gmail.com > - 0.9.8a-2
- Disable mozilla-vlc because of libxul 1.9.1 WIP
- Rebuild for libcdio

* Fri Dec  5 2008 kwizart < kwizart at gmail.com > - 0.9.8a-1
- Update to 0.9.8a
Security update:
 * Fixed buffer overflow in Real demuxer (SA-0811, CVE-2008-5276)
- Add pulse0071 Patch
- Fix RPM Fusion bugs:
  https://bugzilla.rpmfusion.org/show_bug.cgi?id=201
  https://bugzilla.rpmfusion.org/show_bug.cgi?id=155

* Thu Nov  6 2008 kwizart < kwizart at gmail.com > - 0.9.6-1
- Update to 0.9.6

* Tue Oct 28 2008 kwizart < kwizart at gmail.com > - 0.9.5-3
- Rebuild for dependency

* Mon Oct 27 2008 kwizart < kwizart at gmail.com > - 0.9.5-2
- Fix ppc/ppc64 build

* Fri Oct 24 2008 kwizart < kwizart at gmail.com > - 0.9.5-1
- Update to 0.9.5
- Use non-default rpmbuild options for dirac kate lua
- Split core/nox (nox bundles directfb/svgalib)
- Fix Selinux denials (patches from gentoo).
- Fix spurious perms on qt4 sources.

* Wed Oct  8 2008 kwizart < kwizart at gmail.com > - 0.9.4-1
- Update to 0.9.4

* Mon Sep 29 2008 kwizart < kwizart at gmail.com > - 0.9.3-2
- Add libv4l2 patch from Hans de Goede

* Fri Sep 26 2008 kwizart < kwizart at gmail.com > - 0.9.3-1
- Update to 0.9.3 (final)
- Few others move from core to main

* Mon Sep 15 2008 kwizart < kwizart at gmail.com > - 0.9.2-1
- Update to 0.9.2 (final)

* Sat Aug  2 2008 kwizart < kwizart at gmail.com > - 0.9.0-0.5.20080802git
- Update to 0.9.0-20080802git

* Sun Jul 13 2008 kwizart < kwizart at gmail.com > - 0.9.0-0.4.20080713git
- Update to 0.9.0-20080713git

* Thu Jul  3 2008 kwizart < kwizart at gmail.com > - 0.9.0-0.3.20080703git
- Update to 0.9.0-20080703git
  http://mailman.videolan.org/pipermail/vlc-devel/2008-July/045911.html
- Conditionalize xvmc to exclude ppc

* Thu Jun 12 2008 kwizart < kwizart at gmail.com > - 0.8.6h-2
- Fix libdvdnav (only) use.

* Fri Jun 6 2008 kwizart < kwizart at gmail.com > - 0.8.6h-1
- Update to 0.8.6h
- Use hicolor icons
- Add patch for new_x-content
  http://bugzilla.livna.org/show_bug.cgi?id=2003
- Fix VLC: HTTP access: cannot seek AVI
  http://bugzilla.livna.org/show_bug.cgi?id=2014
  
* Sun May 18 2008 kwizart < kwizart at gmail.com > - 0.8.6g-2
- Bump for official release

* Wed May 14 2008 kwizart < kwizart at gmail.com > - 0.8.6g-1
- Update to 0.8.6g
Security updates:
 * Removed VLC variable settings from Mozilla and ActiveX (CVE-2007-6683)
 * Removed loading plugins from the current directory (CVE-2008-2147)

Various bugfixes:
 * Fixed various memory leaks, improving stability when running as a server
 * Fixed compilation with recent versions of FFmpeg
 * Correctly parses SAP announcements from MPEG-TS
 * Fixed AAC resampling
 * The Fullscreen Controller appears correctly on Mac OS X,
   if the 'Always-on-top' video option was selected.

* Tue May 13 2008 kwizart < kwizart at gmail.com > - 0.8.6f-6
- Fix ffmpeg-compat with newest ffmpeg interaction

* Mon May 12 2008 kwizart < kwizart at gmail.com > - 0.8.6f-5
- Introduce 180_all_faad.patch
- Re-enable ffmpeg-compat for F-9

* Mon May 12 2008 Thorsten Leemhuis < fedora at leemhuis dot info > - 0.8.6f-4
- disable patch82 temporary

* Fri May  9 2008 kwizart < kwizart at gmail.com > - 0.8.6f-3
- Bugfixes patches for post f version
- Add vlvc 0.8 plugin support
- Add textrel fix from gentoo patch
- Improve libxul patch 

* Mon Apr  7 2008 kwizart < kwizart at gmail.com > - 0.8.6f-2
- Fix for wxGTK28 compatibility.
 Patch from Dominique Leuenberger <dominique@leuenberger.net

* Mon Apr  7 2008 kwizart < kwizart at gmail.com > - 0.8.6f-1
- Update to 0.8.6f (Final)
Security updates:
 * Really fixed subtitle buffer overflow (CVE-2007-6681)
 * Fixed Real RTSP code execution problem (CVE-2008-0073)
 * Fixed MP4 integer overflows (CVE-2008-1489)
 * Fixed cinepak integer overflow
Various bugfixes:
 * Fixed crashes in H264 packetizer
 * Close MMS access on network timeout
 * Fix some problems with AAC decoder & packetizer
- Remove java-vlc (will be built externally)
- Add clinkcc conditional/experimental support.

* Mon Feb 25 2008 kwizart < kwizart at gmail.com > - 0.8.6e-1
- Update to 0.8.6e (Final)
Security updates:
 * Subtitle demuxers overflow (CVE-2007-6681)
 * HTTP listener format string injection (CVE-2007-6682)
 * Fixed buffer overflow in the SDL_image library (CVE-2006-4484)
 * Real RTSP overflows (CVE-2008-0225, CVE-2008-0295,
   CVE-2008-0296, VideoLAN-SA-0801)
 * Arbitrary memory overwrite in the MP4 demuxer (CORE-2008-0130,
   VideoLAN-SA-0802)


* Mon Feb 25 2008 kwizart < kwizart at gmail.com > - 0.8.6e-0.3
- Update to svn20080225 from bugfix (pre 0.8.6e)

* Thu Feb 21 2008 kwizart < kwizart at gmail.com > - 0.8.6e-0.2
- Update to svn20080221 from bugfix (pre 0.8.6e)
- Updated merged pulseaudio patch
- Raise PA to be used by default.

* Mon Feb 18 2008 kwizart < kwizart at gmail.com > - 0.8.6e-0.1
- Update to pre0.8.6e
- Add pre PA patch (not merged yet)

* Sat Jan 19 2008 kwizart < kwizart at gmail.com > - 0.8.6d-4
- Patches from Jens Petersen <juhpetersen at gmail.com>
- Add wxGTK28 wip patch
- Conditionalize directfb and dirac 
- Change the default font to DejaVuSerif.ttf (dejavu-fonts)
- Add BR missing libmpeg4v2

* Thu Jan 10 2008 kwizart < kwizart at gmail.com > - 0.8.6d-3.1
- Remove BR portaudio arts
- Move skins2 to main vlc package
- Enable libopendaap (included within Fedora)

* Mon Dec  3 2007 kwizart < kwizart at gmail.com > - 0.8.6d-3
- Enable java-vlc (developer use only - java-icedtea).
- Fix arch detection for java headers

* Sat Dec  1 2007 kwizart < kwizart at gmail.com > - 0.8.6d-2
- Improve core/nox split

* Thu Nov 29 2007 kwizart < kwizart at gmail.com > - 0.8.6d-1
- Update to vlc 0.8.6d

* Tue Nov  6 2007 kwizart < kwizart at gmail.com > - 0.8.6c-10
- Split to core/nox package for server use.

* Tue Nov  6 2007 kwizart < kwizart at gmail.com > - 0.8.6c-9
- Raise ESD audio_output to be tried by default 
  (used by pulseaudio-esound-compat )

* Tue Nov  6 2007 kwizart < kwizart at gmail.com > - 0.8.6c-8
- Rebuild for libdca and faad2

* Mon Oct 22 2007 kwizart < kwizart at gmail.com > - 0.8.6c-7
- Rebuild for new libdvbpsi5-0.1.6

* Fri Oct 19 2007 kwizart < kwizart at gmail.com > - 0.8.6c-6
- Rebuild with the GPL compatible faad2
- Update the Dirac patch
- Fix livna #1668

* Sun Sep 23 2007 kwizart < kwizart at gmail.com > - 0.8.6c-5
- Prepare svn version
- Drop the python switch default
- Add BR directfb-devel 
- Improve timestamp
- Allow faad2 to be 2.5 (license change is known GPL compatible).

* Thu Aug 23 2007 kwizart < kwizart at gmail.com > - 0.8.6c-4
- Change default font to dejavu-lgc/DejaVuLGCSerif.ttf
  http://bugzilla.livna.org/show_bug.cgi?id=1605
- Remove unneeded fonts provided by skins2

* Tue Aug 14 2007 kwizart < kwizart at gmail.com > - 0.8.6c-3.2
- clean-up with svn
- patch smb.c for call_open (from rdieter advice)
- Update license field to GPLv2

* Sun Aug 12 2007 kwizart < kwizart at gmail.com > - 0.8.6c-3.1
- Fix libtool with shared libs when python-vlc is used
  http://bugzilla.livna.org/show_bug.cgi?id=1590
- Fix desktop file to be GNOME HIG compliant
  http://bugzilla.livna.org/show_bug.cgi?id=1591

* Tue Jul 31 2007 kwizart < kwizart at gmail.com > - 0.8.6c-3
- Switch for python-vlc
- Add bugfix patch pre_d
- Fix version field for desktop file.
- Fix ivtv support with updated patch for new videodev2.h
- Clean old Obsoletes/Provides for name 8.1
- Rebuild with firefox-devel 2.0.0.5
- Patch/rebuild with libcdio 0.78.2
- Add mesa's BR
- Add BR libXvMC-devel for svn

* Tue Jun 26 2007 kwizart < kwizart at gmail.com > - 0.8.6c-2
- Update to new libupnp

* Sat Jun 16 2007 kwizart < kwizart at gmail.com > - 0.8.6c-1
- Update to 0.8.6c (final)
- Add patch to uses v4l2 header for new v4l2 encoder API.

* Sat Jun 16 2007 kwizart < kwizart at gmail.com > - 0.8.6c-0.1
- Update to 0.8.6c (bugfix) 20060616
- Drop FLAC, automake110, wxGTK for 2.8, faad2
- Uses shared ffmpeg.

* Thu Jun  7 2007 kwizart < kwizart at gmail.com > - 0.8.6b-6
- Rebuild for F-7 (compat-wxGTK26)

* Mon Jun  4 2007 kwizart < kwizart at gmail.com > - 0.8.6b-5.3
- Uses only -fPIC to prevent Selinux context problems...
- Uses compat-wxGTK26-devel on Fedora 7
- Leave libcorba for now...
  (libquicktime_plugin seems also broken - confirmed by upstream)
- Change static_live555 to internal_live555.
  needed for testing - uses live-devel for livna releases.

* Sat May 19 2007 kwizart < kwizart at gmail.com > - 0.8.6b-5
- Removed no more needed Selinux Context:
  fixed in http://bugzilla.redhat.com/237473

* Sun May 13 2007 kwizart < kwizart at gmail.com > - 0.8.6b-4
- Disabled pth (broken) and...
- Build ffmpeg static (since shared ffmpeg is pth enabled).
- Add post & postun update-desktop-database
- Update static ffmpeg to 20070503 (same as shared version)

* Sun May 13 2007 kwizart < kwizart at gmail.com > - 0.8.6b-3.3
- Test static updated live555

* Sat May 12 2007 kwizart < kwizart at gmail.com > - 0.8.6b-3.2
- Update to the new ffmpeg with pth (testing - wip )

* Fri May  4 2007 kwizart < kwizart at gmail.com > - 0.8.6b-3.1
- Add BR libebml-devel
- Add BR Glide3-devel
- Add BR gnome-vfs2-devel
- Add BR libxml2-devel
- Fix BR faad2-devel < 2.5
- Add rpmfusion BR libopendaap-devel
- Add rpmfusion BR libgoom2-devel
- Add rpmfusion BR libdc1394-devel
- Exclude corba plugin (broken)
- Add relatives %%configure options
- Comment Glide3 (don't work now - wip)

* Thu May  3 2007 kwizart < kwizart at gmail.com > - 0.8.6b-3
- Enable --enable-pth with ffmpeg
  bump release in case testing take much time.

* Thu May  3 2007 kwizart < kwizart at gmail.com > - 0.8.6b-1.3
- Fix Selinux remain quiet with semanage

* Tue May  1 2007 kwizart < kwizart at gmail.com > - 0.8.6b-1.2
- Few improvements for svn version
- Add missing BR ORBit2-devel and pyorbit-devel
- Improved post preun postun section with help from Anvil.

* Mon Apr 30 2007 kwizart < kwizart at gmail.com > - 0.8.6b-1.1
- Add missing BR libtiff-devel
- Fix Selinux buglet when Selinux is not activated
  was https://bugzilla.livna.org/show_bug.cgi?id=1484

* Sat Apr 21 2007 kwizart < kwizart at gmail.com > - 0.8.6b-1
- Update to Final 8.6b
- Enable Dirac codec
- Fix mozilla-vlc libXt.so loading 
  (removing mozilla-sdk since using firefox sdk >= 1.5)
- Fix SeLinux context for dmo plugin. Was:
  https://bugzilla.livna.org/show_bug.cgi?id=1404
- Enabled cddax only for x86_64 (broken type).

* Wed Apr 18 2007 kwizart < kwizart at gmail.com > - 0.8.6b-0.3
- Fix BR for libsmbclient-devel for Fedora 7
- Update to 0.8.6-bugfix-20070418
- Add BR libraw1394-devel
- Add BR libavc1394-devel

* Mon Apr 16 2007 kwizart < kwizart at gmail.com > - 0.8.6b-0.2
- Fix svgalib-devel only for x86 x86_64
- Fix firefox-devel headers presence/usability. This remains:
 npapi.h: accepted by the compiler, rejected by the preprocessor!
 npapi.h: proceeding with the compiler's result

* Sat Apr 14 2007 kwizart < kwizart at gmail.com > - 0.8.6b-0.1
- Update to rc 0.8.6b (bugfix)
- Hack configure.ac script (it didn't detect firefox headers)
- Add BR libshout-devel
- Add BR svgalib-devel
- Add BR gtk2-devel
- Add BR directfb-devel (wip)
- Add BR libnotify-devel
- Enabled --enable-speex
- Testing --enable-portaudio not usefull (oss is deprecated)
- Enabled --enable-pda
- Testing --enable-directfb (wip)
- Removed patch5 (was format.c)

* Thu Apr  5 2007 kwizart < kwizart at gmail.com > - 0.8.6a-5
- Use system ffmpeg lib (pth and libtool seems to be incompatible with it)
- Dirac seem to compile fine but testing usability for now.
- Cache isn't usefull for now (and won't be since using system libs)
- Exclude %%{_bindir}/vlcwrapper.py? since this is the guideline about python for now.

* Mon Apr  2 2007 kwizart < kwizart at gmail.com > - 0.8.6a-4.6
- Fix %%{_libdir}/advene directory ownership from: #1458
- Fix .py? presence and perm (644)
- Remove .la after make install
- Add --disable-pth (broken for release and svn)
  
* Sat Mar 24 2007 kwizart < kwizart at gmail.com > - 0.8.6a-4.5
- Test dirac (disabled mozilla )
- Test Updated static live555 to 2007.02.22
- Clean up svn to release changes

* Thu Mar 22 2007 kwizart < kwizart at gmail.com > - 0.8.6a-4.4
- WIP changes - ld.conf is unusefull...

* Wed Mar 21 2007 kwizart < kwizart at gmail.com > - 0.8.6a-4.3
- Revert back to the static vlc version 
 ( will explore this with ld.conf later )

* Wed Mar 21 2007 kwizart < kwizart at gmail.com > - 0.8.6a-4.2
- Fix .desktop file
- Disable broken libtool 
- Quick fixes for svn/cache prepare
- Patch format_c
- Fix rpmlint error with python-vlc

* Tue Mar 20 2007 kwizart < kwizart at gmail.com > - 0.8.6a-4.1
- Enable cache for static compilation - wip

* Fri Mar  9 2007 kwizart < kwizart at gmail.com > - 0.8.6a-4
- Enable conditionnal build for
	* mozilla-vlc, java-vlc, dirac
	* ffmpeg and live static
- Enable pth
- Enable gnu_ld

* Thu Mar  8 2007 kwizart < kwizart at gmail.com > - 0.8.6a-3.1
- Fix firefox-devel detection when avaible both i386 and x86_64
  http://bugzilla.livna.org/show_bug.cgi?id=1442

* Thu Mar  8 2007 kwizart < kwizart at gmail.com > - 0.8.6a-3
- Recover patch3 from Ville Skyttä
- Fix FLAC api change see
 http://bugzilla.livna.org/show_bug.cgi?id=1433

* Thu Mar  8 2007 kwizart < kwizart at gmail.com > - 0.8.6a-2
- Update ffmpeg to 20070308
- Enabled static build for internal ffmpeg (x264 vlc modules)
- Fixed: some configure options has changed for ffmpeg

* Sat Mar  3 2007 Thorsten Leemhuis <fedora at leemhuis dot info> - 0.8.6a-1.2
- Rebuild

* Sun Feb  4 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.8.6a-1.1
- Fix aclocal/automake fix for automake 1.10 without breaking it for earlier.

* Sun Feb  4 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.8.6a-1
- Build internal copy of ffmpeg with $RPM_OPT_FLAGS.
- Don't hardcode path to firefox headers.
- Drop Application and X-Livna categories from desktop entry.
- Clean up some unneeded cruft from specfile.
- Fix aclocal/automake calls during bootstrap.
- Let rpmbuild strip MediaControl.so.

* Sat Feb  3 2007 kwizart < kwizart at gmail.com > - 0.8.6a-0.4.static
- Internal static build of ffmpeg from Matthias version.

* Fri Jan 19 2007 kwizart < kwizart at gmail.com > - 0.8.6a-0.3
- Re-enabled mozilla-vlc
- use ifarch ix86

* Sat Jan 13 2007 kwizart < kwizart at gmail.com > - 0.8.6a-0.2
- Import patches from Matthias version
- try to fix firefox includes for mozilla-vlc -> disabled

* Wed Jan 10 2007 kwizart < kwizart at gmail.com > - 0.8.6a-0.1
- Try to Fix run with libavformat.so.51
- disabled

* Mon Jan  8 2007 kwizart < kwizart at gmail.com > - 0.8.6-5
- Update to BR bugzilla infos.
- Fix perms with python and debug headers.
- Cleaned obsolete-not-provided

* Fri Jan  5 2007 kwizart < kwizart at gmail.com > - 0.8.6-4
- Use BuildConflics with libcdio
- Enabled --enable-cddax
- Enabled --enable-vcdx
-  waiting --enable-quicktime (build fails)

* Fri Jan  5 2007 kwizart < kwizart at gmail.com > - 0.8.6-3
  with help from Rathan
- Update to 0.8.6a (security update!)
  from http://www.videolan.org/sa0701.html - #1342
- Add version to desktop file
- Fix dual shortcuts / Add MimeType

* Wed Jan  3 2007 kwizart < kwizart at gmail.com > - 0.8.6-2
 with help from Rathan
- Enabled --enable-shout
- Enabled --enable-quicktime (x86 only !) 
- Enabled --enable-loader (x86 only !)
- Enabled --with-wine-sdk-path (x86 only !)
- Enabled --enable-corba
-  testing --enable-dirac (libdirac-devel reviewing in extra)
   http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=221405
- Enabled --enable-mediacontrol-python-bindings
- Cosmetic changes in BR

* Mon Dec 11 2006 kwizart < kwizart at gmail.com > - 0.8.6-1.fc6
- Update to 8.6 final
- Change deprecated livdotcom to live555
- build shared librairies is default since 8.6
- Enabled --enable-dvdread
- Enabled --enable-faad
- Enabled --enable-twolame
-   waiting --enable-quicktime (problem finding xqtsdk )
- Enabled --enable-real
- Enabled --enable-realrtsp
- Enabled --enable-tremor
- Enabled --enable-tarkin
-   waiting --enable-dirac (TODO libdirac-devel )
- Enabled --enable-snapshot
- Enabled --enable-portaudio
- Enabled --enable-jack
- Enabled --enable-galaktos
-   waiting --enable-mediacontrol-python-bindings (default install error)
-   waiting --enable-cddax (new version of libcdio 0.78.2)
-   waiting --enable-vcdx (new version of libcdio 0.78.2)

* Mon Dec 04 2006 kwizart < kwizart at gmail.com > - 0.8.6-rc1.1.fc6
- Update to 8.6rc1
- disable components in mozilla-vlc
- disable libvlc_pic.a in devel
- Enable x264-devel for static linking.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.8.5-6
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 25 2006 Dams <anvil[AT]livna.org> - 0.8.5-5
- BuildReq:libtool

* Sun Sep 24 2006 Dams <anvil[AT]livna.org> - 0.8.5-4
- Fixed the mozilla plugin damn build 

* Sat Sep  9 2006 Dams <anvil[AT]livna.org> - 0.8.5-3
- sysfsutils-devel -> libsysfs-devel

* Sat Sep  9 2006 Dams <anvil[AT]livna.org> - 0.8.5-1
- Updated to 0.8.5
- Fixed MOZVER value in case more than one mozilla is installed.
- Dropped patches 1, 2 and 3

* Wed Aug 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.8.4a-2
- Adjust for new live package, enable it on all archs.

* Fri Apr 14 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.8.4a-1
- Apply upstream patch to fix linking with newer ffmpeg/postproc.
- Drop no longer needed build conditionals and build dependencies.
- Enable Avahi, Musepack, SLP and sysfs support, fix SDL and Xv.
- Install icon to %%{_datadir}/icons/hicolor.
- Drop zero Epoch remainders.
- Fix -devel obsoletes.
- Specfile cleanups.

* Fri Mar 24 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> 0.8.4-9.a
- rebuild 

* Tue Mar 21 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.4-8.a
- fix #775

* Mon Mar 20 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.4-7.a
- add -fPIC for all arches

* Mon Mar 20 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.4-6.a
- fix build on ppc/i386

* Thu Mar 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.4-5.a
- fix BR

* Wed Mar 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.4-4.a
- make vlc build again

* Tue Mar 14 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> 0.8.4-3.a
- drop "0.lvn" from release

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Mon Jan 09 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.8.4-0.lvn.3.a
- add all BRs the new ffmpeg needs

* Fri Jan 06 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.8.4-0.lvn.2.a
- add buildoption "--without mkv" -- ebml in FC3 is to old
- add buildoption "--without svg" -- does not build with svg on FC3-x86-64

* Thu Jan 05 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.8.4-0.lvn.1.a
- Update to 0.8.4a [with help from che (Rudolf Kastl)]
- Fix x64
- drop Epoch
- drop vlc-0.8.2-test2-altivec.patch, seems they worked on this
- use " --disable-libcdio" until we update to wxGTK2 2.6
- use "--disable-livedotcom" on x86_64 (does not build)

* Sat Aug  6 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.2-0.lvn.4
- Fix "--without cddb" build when libcddb-devel is installed.
- BuildRequire live-devel instead of live.

* Wed Aug  3 2005 Dams <anvil[AT]livna.org> - 0:0.8.2-0.lvn.3
- Rebuilt *without* libcddb
- Rebuilt against new libdvbpsi

* Thu Jul 28 2005 Dams <anvil[AT]livna.org> - 0:0.8.2-0.lvn.2
- Rebuilt against new libcddb/libcdio

* Sat Jul  9 2005 Dams <anvil[AT]livna.org> - 0:0.8.2-0.lvn.1
- Updated to final 0.8.2

* Mon Jun  6 2005 Ville Skyttä <ville.skytta at iki.fi> 0:0.8.2-0.lvn.0.1.test2
- Update to 0.8.2-test2, rename to vlc, improve summaries and descriptions.
- Enable many more modules, many small improvements and cleanups here and there
- Use unversioned install dir for the Mozilla plugin, rename to mozilla-vlc.
- Drop < FC3 compatiblity due to unavailability of required lib versions.
- Fold wx and ncurses to the main package (upstream has retired the
  VLC Gnome and KDE UI's, so separate UI packages don't have a purpose
  any more).

* Sat Sep 11 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.7.2-0.lvn.7
- Remove dependency on libpostproc-devel, it's now in ffmpeg-devel (bug 255).

* Thu Sep  2 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.7.2-0.lvn.6
- BuildRequire alsa-lib-devel, was lost in previous update (bug 258).
- Add libcdio and libmodplug build dependencies.
- Tweak descriptions, remove unnecessary conditional sections.
- Disable dependency tracking to speed up the build.

* Sun Aug 29 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.7.2-0.lvn.5
- Use system ffmpeg (>= 0.4.9), and make it, ALSA, and fribidi unconditional.
- Build with theora by default.
- Change default font to Vera serif bold.
- Enable pvr support for Hauppauge card users (thanks to Gabriel L. Somlo).

* Mon Jul  5 2004 Dams <anvil[AT]livna.org> 0:0.7.2-0.lvn.4
- Enabled libcddb support

* Wed Jun 30 2004 Dams <anvil[AT]livna.org> 0:0.7.2-0.lvn.3
- speex now conditional and default disabled since vlc requires
  development version. 

* Wed Jun 30 2004 Dams <anvil[AT]livna.org> 0:0.7.2-0.lvn.2
- Optional Fribidi and libtheora support (default disabled)

* Tue May 25 2004 Dams <anvil[AT]livna.org> 0:0.7.2-0.lvn.1
- Updated to 0.7.2

* Fri May  7 2004 Dams <anvil[AT]livna.org> 0:0.7.1-0.lvn.1
- BuildConflicts:ffmpeg
- Build against private ffmpeg snapshot

* Tue Mar  9 2004 Dams <anvil[AT]livna.org> 0:0.7.1-0.lvn.1
- Updated to 0.7.1
- Added live.com libraries support
- Added matroska support

* Sun Jan  4 2004 Dams <anvil[AT]livna.org> 0:0.7.0-0.lvn.1
- Updated to 0.7.0
- s/fdr/lvn

* Wed Dec 10 2003 Dams <anvil[AT]livna.org> 0:0.6.2-0.fdr.7
- Conditional ffmpeg build option (default enabled)

* Fri Sep  5 2003 Dams <anvil[AT]livna.org> 0:0.6.2-0.fdr.6
- pth support now default disabled 

* Fri Sep  5 2003 Dams <anvil[AT]livna.org> 0:0.6.2-0.fdr.5
- slp support can now be not-build with '--without slp'

* Thu Sep  4 2003 Dams <anvil[AT]livna.org> 0:0.6.2-0.fdr.4
- Added missing defattr for subpackages
- Fixed permissions on mozilla plugin
- fixed build failure due to typos in ncurses changes
- Removed useless explicit 'Requires:' in subpackages declarations

* Tue Sep  2 2003 Dams <anvil[AT]livna.org> 0:0.6.2-0.fdr.3
- Added builddep for libpng-devel and openslp-devel 
- Added gnome (default:enabled) and ncurses (default:disabled)
  subpackages
- Removed macros (mkdir/install/perl)
- Modified descriptions
- Removed gtk/gnome2 build deps
- Added conditionnal (default-disabled) build option for alsa
- Added conditionnal builddep for pth-devel

* Fri Aug 22 2003 Dams <anvil[AT]livna.org> 0:0.6.2-0.fdr.2
- Added missing BuildRequires for gtk+-devel

* Thu Aug 14 2003 Dams <anvil[AT]livna.org> 0:0.6.2-0.fdr.1
- Updated to 0.6.2
- Hopefully fixed 'if' conditions for optional buildrequires

* Tue Jul  8 2003 Dams <anvil[AT]livna.org> 0:0.6.0-0.fdr.3
- Providing vlc 

* Tue Jul  8 2003 Dams <anvil[AT]livna.org> 0:0.6.0-0.fdr.2
- Moved desktop entry from devel to main package (stupid me)

* Mon Apr 28 2003 Dams <anvil[AT]livna.org> 
- Initial build.
