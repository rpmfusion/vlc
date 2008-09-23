# TODO: libdc1394(juju), java-vlc, modularization (vlc-plugin-foo)
# Patches needed: wxGTK28 - libdc1394-2.0.1
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}


%define with_intern_ffmpeg		0
%define with_ffmpeg_compat		1
%define ffmpeg_date	20080113
%define with_internal_live555 		0
%define live555_date	2008.04.03
%define with_mozilla	 		1
%define with_python_vlc			1
%define with_dc1394			0
%define with_directfb			1
%define with_dirac			1
%define with_vlvc			1


Summary:	Multi-platform MPEG, DVD, and DivX player
Name:		vlc
Version:	0.8.7
%define _version 0.8.6i
Release:	0.4%{?dist}
License:	GPLv2+
Group:		Applications/Multimedia
URL:		http://www.videolan.org/
Source0:	http://download.videolan.org/pub/videolan/vlc/%{_version}/vlc-%{_version}.tar.bz2
%if %with_intern_ffmpeg
Source1:	http://rpm.greysector.net/livna/ffmpeg-%{ffmpeg_date}.tar.bz2
%endif
%if %with_internal_live555
Source2:	http://www.live555.com/liveMedia/public/live.%{live555_date}.tar.gz
%endif
%if %with_vlvc
Source3:        https://pfe.epitech.net/frs/download.php/747/vlvc_source-0.8.tgz
%endif
Patch3:         vlc-0.8.6-wx28compat.patch
Patch4:         vlc-0.8.6f-shared_live555.patch
Patch5:         vlc-0.8.6f-all_plugin.patch
Patch7:         vlc-0.8.6f-wx28iccfixes.patch
Patch9:         vlc-0.8.6c-python_destdir.patch
Patch10:        vlc-0.8.6c-python_libtool.patch
Patch12:        vlc-0.8.6-font_dejavu.patch
Patch16:        vlc-trunk-dirac_0_8_0-api.patch
Patch17:        vlc-0.8.6c-dts_to_dca_api.patch
Patch19:        vlc-0.8.6e-pulse.patch
Patch20:        vlc-0.8.6e-pulse_default.patch
Patch50:        vlc-0.8.6i-ffmpeg-compat.patch
Patch63:        vlc-trunk-dirac_0_9_0-api.patch
Patch80:        vlc-0.8.6e-xulrunner.patch
Patch90:        vlc-0.8.6-vlvc_0.8.patch
Patch91:        vlc-0.8.6-vlvcfix.patch
# git-diff tags/vlc-0.8.6i HEAD > vlc-0.8.7-git_head-$(date +%Y%m%d ).patch
# tar cjvf vlc-0.8.7-git_head-$(date +%Y%m%d ).patch.tar.bz2
Patch99:        vlc-0.8.7-git_head-20080908.patch.tar.bz2
Patch100:       vlc-0.8.7-rpmfusion2_head.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libtool

BuildRequires:	a52dec-devel
BuildRequires:	aalib-devel
BuildRequires:	alsa-lib-devel
%{?_with_amr:BuildRequires: amrnb-devel amrwb-devel}
BuildRequires:	avahi-devel
BuildRequires:  cdparanoia-devel
%{?_with_clinkcc:BuildRequires:  clinkcc}
%if %with_dirac
BuildRequires:	dirac-devel >= 0.6.0
%endif
%if %with_directfb
BuildRequires:  directfb-devel
%endif
%if 0%{?fedora} < 9
BuildRequires:	esound-devel
BuildRequires:	arts-devel
%endif
BuildRequires:	faac-devel
BuildRequires:	faad2-devel
BuildRequires:	flac-devel
BuildRequires:	fribidi-devel
# Broken with 0.8.6x
#BuildRequires:  Glide3-devel
#BuildRequires:  Glide3-libGL
BuildRequires:  gnome-vfs2-devel
BuildRequires:	gnutls-devel >= 1.0.17
BuildRequires:	gsm-devel
BuildRequires:  gtk2-devel
BuildRequires:	hal-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lame-devel
BuildRequires:  libavc1394-devel
BuildRequires:	libcaca-devel
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-devel >= 0.77-3
BuildRequires:	libdca-devel
BuildRequires:	libdv-devel
BuildRequires:	libdvbpsi-devel
BuildRequires:	libdvdnav-devel
BuildRequires:  libebml-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmatroska-devel >= 0.7.6
BuildRequires:	libmodplug-devel
BuildRequires:	libmp4v2-devel
BuildRequires:	libmpcdec-devel
BuildRequires:  libnotify-devel
BuildRequires:  libopendaap-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg2-devel >= 2.5.0
BuildRequires:	libsysfs-devel
BuildRequires:  libshout-devel
BuildRequires:	libtar-devel
BuildRequires:	libtheora-devel
BuildRequires:  libtiff-devel
BuildRequires:  libupnp-devel
BuildRequires:	libvorbis-devel
BuildRequires:  libxml2-devel
BuildRequires:	lirc-devel
%if %with_internal_live555
BuildConflicts: live-devel
BuildConflicts: live555-devel
%else
BuildRequires:	live555-devel >= 0-0.19.2008.04.03
%endif
BuildRequires:  kernel-headers >= 2.6.20
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:	mpeg2dec-devel >= 0.3.2
BuildRequires:	ncurses-devel
BuildRequires:	openslp-devel
%if %with_python_vlc
BuildRequires:	python-devel
%endif
BuildRequires:	SDL_image-devel
BuildRequires:	speex-devel >= 1.1.5
%ifarch %{ix86} x86_64
BuildRequires:  svgalib-devel
%endif
BuildRequires:	twolame-devel
BuildRequires:	vcdimager-devel >= 0.7.21
BuildRequires:	wxGTK-devel >= 2.6
BuildRequires:	x264-devel >= 0-0.8.20061028
BuildRequires:	xosd-devel
BuildRequires:	xvidcore-devel
BuildRequires:	zlib-devel

# X-libs
BuildRequires:	libXt-devel
BuildRequires:	libXv-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel

%if 0%{?fedora} > 6
BuildRequires:  libsmbclient-devel
%else 
BuildRequires:  samba-common
%endif

%if 0%{?fedora} > 7
BuildRequires:  pulseaudio-libs-devel >= 0.9.8
BuildRequires:  portaudio-devel
%endif

%if %with_mozilla
BuildRequires:  gecko-devel
BuildRequires:  nspr-devel
%else
Obsoletes: mozilla-vlc < %{version}-%{release}
%endif

%if %with_intern_ffmpeg
## Static version already bundle it
BuildConflicts:	ffmpeg-devel
%else
%if %{with_ffmpeg_compat}
BuildRequires:	ffmpeg-compat-devel >= 0.4.9-0
%else
BuildRequires:	ffmpeg-devel >= 0.4.9-0
%endif
%endif


# Now obsoleted as it will be built externally
Obsoletes: java-vlc < %{version}

#Not in repos
#BuildRequires:  libgoom2-devel
#BuildRequires:  libggi-devel


%if %with_dc1394
BuildRequires:  compat-libdc1394-devel
BuildRequires:  compat-libraw1394-devel
%else
BuildRequires:  libraw1394-devel
%endif

Requires: vlc-core = %{version}-%{release}
Requires: dejavu-fonts


%package devel
Summary:	Development package for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}


%description
VLC (initially VideoLAN Client) is a highly portable multimedia player
for various audio and video formats (MPEG-1, MPEG-2, MPEG-4, DivX,
mp3, ogg, ...) as well as DVDs, VCDs, and various streaming protocols.
It can also be used as a server to stream in unicast or multicast in
IPv4 or IPv6 on a high-bandwidth network.

!!!BIG FAT WARNING!!!
This vlc-0.8.7 pre-version is based on vlc-0.8.6-bugfix branch 
See http://mailman.videolan.org/pipermail/vlc/2008-August/015827.html


%description devel
This package contains development files for VLC Media Player.

VLC (initially VideoLAN Client) is a highly portable multimedia player
for various audio and video formats (MPEG-1, MPEG-2, MPEG-4, DivX,
mp3, ogg, ...) as well as DVDs, VCDs, and various streaming protocols.
It can also be used as a server to stream in unicast or multicast in
IPv4 or IPv6 on a high-bandwidth network.

%if %with_python_vlc
%package -n python-vlc
Summary:	VLC Media Player binding for Python
Group:		Applications/Multimedia	
Requires:	%{name}-core = %{version}-%{release}

%description -n python-vlc
VLC Media Player binding for Python
%endif


%if %with_mozilla
%package -n mozilla-vlc
Summary:	VLC Media Player plugin for Mozilla compatible web browsers
Group:		Applications/Multimedia	
Requires:	%{name} = %{version}-%{release}
Requires:	%{_libdir}/mozilla/plugins

%description -n mozilla-vlc
This package contains a VLC Media Player plugin for Mozilla compatible
web browsers.

VLC (initially VideoLAN Client) is a highly portable multimedia player
for various audio and video formats (MPEG-1, MPEG-2, MPEG-4, DivX,
mp3, ogg, ...) as well as DVDs, VCDs, and various streaming protocols.
It can also be used as a server to stream in unicast or multicast in
IPv4 or IPv6 on a high-bandwidth network.
%endif

%package core
Summary:	VLC Media Player without Xorg
Group:		Applications/Multimedia
Provides:       vlc-nox = %{version}-%{release}

%description core
VLC Media Player without X.org for server

%if %with_dc1394
%package plugins-dc1394
Summary:	VLC Media Player Plugins for dc1394
Group:		Applications/Multimedia
Requires:	%{name}-core = %{version}
Requires:       compat-libdc1394-tools

%description plugins-dc1394
VLC plugins for libdc1394
%endif

%prep
%setup -q -n %{name}-%{_version}
%if %with_intern_ffmpeg
%setup -q -D -T -a 1 -n %{name}-%{_version}
%endif
%if %with_internal_live555
%setup -q -D -T -a 2 -n %{name}-%{_version}
%endif
%if %with_vlvc
%setup -q -D -T -a 3 -n %{name}-%{_version}
find vlvc_source-0.8 -type f -exec chmod 644 {} ";"
cp -pR vlvc_source-0.8/* .
cp -p vlvc_readme-0.8_fr.txt vlvc_readme-0.8_fr.txt.noutf8
iconv -f ISO-8859-1 -t UTF-8 vlvc_readme-0.8_fr.txt.noutf8 > vlvc_readme-0.8_fr.txt
touch -r vlvc_readme-0.8_fr.txt.noutf8 vlvc_readme-0.8_fr.txt
%endif


%patch3 -p1 -b .wxGTK28compat
%patch4 -p1 -b .shared_live555
%patch5 -p1 -b .all_plugin
%patch7 -p1 -b .wx28iccfixes
%patch9 -p1 -b .python_destdir
%patch10 -p1 -b .python_libtool
%patch12 -p1 -b .font_dejavu
%if 0%{?fedora} > 7
%patch16 -p1 -b .dirac8
%patch17 -p1 -b .dts_dca
%patch19 -p1 -b .pulse
%patch20 -p1 -b .pulse_default
%endif

%if %{with_ffmpeg_compat}
%patch50 -p1 -b .compat
%endif

%if 0%{?fedora} > 8
%patch63 -p1 -b .dirac9
%patch80 -p1 -b .libxul
%endif

%if %with_vlvc
%patch90 -p1 -b .vlvc
%patch91 -p1 -b .vlvcfix
%endif
%patch99 -p1 -b .vlc87_1
%patch100 -p1 -b .vlc87_2

%{?_with_clinkcc:
#hack for clinkcc support - optional feature - under testing.
mkdir -p clinkcc/{lib/unix,include}
cp -pR %{_includedir}/cybergarage clinkcc/include
cp -pR %{_libdir}/libclink.a clinkcc/lib/unix
sed -i -e 's|MediaServer.h|media/server/MediaServer.h|' configure.ac configure
}

# Fix perms issues
chmod 644 mozilla/control/*
chmod 644 src/control/log.c
sed -i 's/\r//'  mozilla/control/* 


sh bootstrap


%build
%if %with_intern_ffmpeg
export CFLAGS="%{optflags}"
# Build bundeled ffmpeg first
pushd ffmpeg-%{ffmpeg_date}
./configure \
%ifarch x86_64
	--extra-cflags="-fPIC -DPIC" \
%else
	--extra-cflags="-fPIC -DPIC -fomit-frame-pointer" \
%endif
	--disable-static \
	--enable-pthreads \
	--enable-shared \
	--disable-ffmpeg \
	--disable-ffserver \
	--disable-vhook \
	--disable-ffplay \
	--disable-optimizations \
	--disable-strip \
	--disable-protocols \
	--enable-liba52 \
	--enable-libmp3lame \
	--enable-libfaac \
	--enable-libfaad \
	--enable-libgsm \
	--enable-libtheora \
	--enable-libvorbis \
	--enable-libx264 \
	--enable-libxvid \
	--enable-pp \
	--enable-gpl \
%{?_with_amr:--enable-libamr-nb --enable-libamr-wb }

# Watch http://trac.videolan.org/vlc/ticket/865
# Planned to be enabled for 0.9.x

	make %{?_smp_mflags}

# Hack for PKG_CONFIG_PATH
for pc in theora vorbis vorbisenc ogg ;do 
  ln -s %{_libdir}/pkgconfig/${pc}.pc
done

popd
%endif


%if %with_internal_live555
# Then bundled live555 - not needed
pushd live
# Force the use of our CFLAGS
%{__perl} -pi -e 's|-O2|%{optflags} -fPIC -DPIC|g' config.linux
# Configure and build
./genMakefiles linux && make
popd
%endif


# Altivec compiler flags aren't set properly (0.8.2)
%ifarch ppc ppc64
export CFLAGS="$CFLAGS -maltivec -mabi=altivec"
%endif

%if %{with_ffmpeg_compat}
mkdir -p temp
# Fake the ffmpeg installation
ln -sf %{_includedir}/ffmpeg-compat temp/ffmpeg
ln -sf %{_includedir}/postproc-compat temp/postproc
export FFMPEG_CFLAGS="-I%{_builddir}/%{name}-%{_version}/temp -I%{_builddir}/%{name}-%{_version}/temp/ffmpeg"
export POSTPROC_CFLAGS="-I%{_builddir}/%{name}-%{_version}/temp -I%{_builddir}/%{name}-%{_version}/temp/ffmpeg"
export FFMPEG_LDFLAGS="$(pkg-config --libs libpostproc-compat libavcodec-compat libavutil-compat libavformat-compat)"
%endif

%configure \
	--disable-dependency-tracking		\
	--disable-rpath				\
	--enable-shout				\
	--enable-release			\
	--enable-live555 			\
%if %with_internal_live555
	--with-live555-tree=live		\
%endif
%if %with_dc1394
	--enable-dc1394				\
%endif
	--enable-dv				\
	--enable-ffmpeg --with-ffmpeg-mp3lame --with-ffmpeg-faac \
%if %with_intern_ffmpeg
 	--with-ffmpeg-tree=ffmpeg-%{ffmpeg_date} \
%{?_with_amr:--enable-libamr-nb --enable-libamr-wb } \
	--with-ffmpeg-faac --with-ffmpeg-vorbis \
	--with-ffmpeg-theora --with-ffmpeg-ogg --with-ffmpeg-zlib \
	--with-ffmpeg-a52 --with-ffmpeg-x264 \
%endif
	--enable-libtool 			\
	--with-gnu-ld				\
	--with-PIC				\
	--disable-static			\
	--enable-shared				\
 	--disable-pth				\
	--enable-dvdread			\
	--enable-v4l				\
	--enable-pvr				\
	--enable-libcdio			\
	--enable-cddax 				\
	--enable-vcdx				\
	--enable-dvb				\
	--enable-faad				\
	--enable-twolame			\
	--enable-real				\
	--enable-realrtsp			\
	--enable-flac				\
	--enable-tremor				\
	--enable-speex				\
	--enable-tarkin				\
	--enable-theora				\
%if %with_dirac
	--enable-dirac				\
%endif
	--enable-svg				\
	--enable-snapshot			\
%ifarch %{ix86} x86_64
	--enable-svgalib			\
%endif
%if %with_directfb
	--enable-directfb			\
%endif
	--enable-aa				\
	--enable-caca				\
%if 0%{?fedora} < 9
        --enable-esd                            \
	--enable-arts				\
%endif
	--enable-jack				\
%{?_with_clinkcc:--enable-cyberlink --with-cyberlink-tree=clinkcc }	\
	--enable-upnp				\
%if 0%{?fedora} > 7
        --enable-portaudio                      \
	--enable-pulse				\
%endif
	--enable-ncurses			\
	--enable-xosd				\
	--enable-galaktos			\
	--enable-slp				\
	--enable-lirc				\
	--disable-corba				\
%if %with_vlvc
	--enable-vlvc				\
%endif
%if %with_python_vlc
	--enable-mediacontrol-python-bindings	\
%endif
%ifarch %{ix86}
	--enable-loader				\
%endif
	--without-contrib			\
%if %with_mozilla 
	--enable-mozilla			\
%endif
	--with-x264-tree=%{_includedir}


# clean unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%if %{with_ffmpeg_compat}
sed -i -e 's|cflags="${cflags} -I/usr/include/ffmpeg-compat"|cflags="${cflags} -I%{_includedir}/ffmpeg-compat -I%{_includedir}/postproc-compat/"|' vlc-config
%else
sed -i -e 's|cflags="${cflags} -I/usr/include/ffmpeg"|cflags="${cflags} -I%{_includedir}/ffmpeg -I%{_includedir}/postproc/"|' vlc-config
%endif



make %{?_smp_mflags}



%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" CPPROG="cp -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

install -dm 755 $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 644 doc/vlc*.1 $RPM_BUILD_ROOT%{_mandir}/man1

for i in 16x16 32x32 48x48 128x128 ; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}/apps
  install -pm 0644 share/vlc${i}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}/apps/vlc.png
done

desktop-file-install --vendor livna			\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	--delete-original				\
	--mode 644					\
	$RPM_BUILD_ROOT%{_datadir}/applications/vlc.desktop

%if %with_python_vlc
# Fix python shebang
sed -i -e 's|"""Wrapper|#!/usr/bin/python\n"""Wrapper|' $RPM_BUILD_ROOT%{_bindir}/vlcwrapper.py
%endif


%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi 
%{_bindir}/update-desktop-database %{_datadir}/applications || :

%post core -p /sbin/ldconfig

%postun
%{_bindir}/update-desktop-database %{_datadir}/applications
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi || :

%postun core -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog MAINTAINERS NEWS README THANKS
%doc %{_docdir}/vlc/*
%if %with_vlvc
%doc vlvc_readme-0.8_en.txt vlvc_readme-0.8_fr.txt
%endif
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/vlc.png
%{_bindir}/wxvlc
%{_libdir}/vlc/gui/libwxwidgets_plugin.so
%{_libdir}/vlc/access/libaccess_gnomevfs_plugin.so
%{_libdir}/vlc/access/libscreen_plugin.so
%{_libdir}/vlc/misc/libsvg_plugin.so
%{_libdir}/vlc/misc/libnotify_plugin.so
%{_libdir}/vlc/video_output/libaa_plugin.so
%{_libdir}/vlc/video_output/libcaca_plugin.so
%{_libdir}/vlc/video_output/libglx_plugin.so
%{_libdir}/vlc/video_output/libopengl_plugin.so
%{_libdir}/vlc/video_output/libx11_plugin.so
%{_libdir}/vlc/video_output/libxvideo_plugin.so
%{_libdir}/vlc/visualization/libgalaktos_plugin.so
%{_libdir}/vlc/audio_output/libpulse_plugin.so
%{_libdir}/vlc/visualization/libxosd_plugin.so
%{_libdir}/vlc/gui/libskins2_plugin.so
%{_datadir}/vlc/skins2/

%files core -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/vlc
%{_datadir}/vlc/
%{_libdir}/*.so.*
%{_bindir}/svlc
%exclude %{_libdir}/vlc/gui/libwxwidgets_plugin.so
%exclude %{_libdir}/vlc/gui/libskins2_plugin.so
%exclude %{_datadir}/vlc/skins2
%exclude %{_libdir}/vlc/access/libaccess_gnomevfs_plugin.so
%exclude %{_libdir}/vlc/access/libscreen_plugin.so
%exclude %{_libdir}/vlc/misc/libsvg_plugin.so
%exclude %{_libdir}/vlc/misc/libnotify_plugin.so
%exclude %{_libdir}/vlc/video_output/libaa_plugin.so
%exclude %{_libdir}/vlc/video_output/libcaca_plugin.so
%exclude %{_libdir}/vlc/video_output/libglx_plugin.so
%exclude %{_libdir}/vlc/video_output/libopengl_plugin.so
%exclude %{_libdir}/vlc/video_output/libx11_plugin.so
%exclude %{_libdir}/vlc/video_output/libxvideo_plugin.so
%exclude %{_libdir}/vlc/visualization/libgalaktos_plugin.so
%exclude %{_libdir}/vlc/audio_output/libpulse_plugin.so
%exclude %{_libdir}/vlc/visualization/libxosd_plugin.so
%if %with_dc1394
%exclude %{_libdir}/vlc/access/libdc1394_plugin.so
%endif
%{_libdir}/vlc/
%{_mandir}/man1/vlc.1*

%if %with_dc1394
%files plugins-dc1394
%defattr(-,root,root,-)
%{_libdir}/vlc/access/libdc1394_plugin.so
%endif

%files devel
%defattr(-,root,root,-)
%doc HACKING
%dir %{_includedir}/vlc
%{_includedir}/vlc/*
%{_mandir}/man1/vlc-config.1*
%{_libdir}/*.so
%{_bindir}/vlc-config

%if %with_mozilla
%files -n mozilla-vlc
%defattr(-,root,root,-)
%{_libdir}/mozilla/plugins/libvlcplugin.so
%endif

%if %with_python_vlc
%files -n python-vlc
%defattr(-,root,root,-)
%{python_sitearch}/*
%{_bindir}/vlcwrapper.py
%exclude %{_bindir}/vlcwrapper.py?
%endif



%changelog
* Tue Sep 23 2008 kwizart < kwizart at gmail.com > - 0.8.7-0.4
- libaccess_gnomevfs_plugin is no more in -core
- More HEAD bugfixes (live555)

* Mon Sep 15 2008 kwizart < kwizart at gmail.com > - 0.8.7-0.3
- Update to 20080915 from 0.8.6-bugfix
- BR live555-devel only

* Mon Sep  8 2008 kwizart < kwizart at gmail.com > - 0.8.7-0.2
- Update to 0.8.6-bugfix
Security updates:
 * Fixed overflow in TTA demuxer (CVE-2008-3732)
 * Fixed overflow in MMS module (CVE-2008-3794)
 * Fixed overflow in Ogg demuxer
Various bugfixes:
 * Fixed support for large URLs in HTTPd scripts
- Drop vlc-git support from this spec file
- Remove patch11

* Thu Aug 28 2008 kwizart < kwizart at gmail.com > - 0.8.6i-3
- Import for RPMFusion
- Switch for live555

* Thu Jun 12 2008 kwizart < kwizart at gmail.com > - 0.8.6i-2
- Fix compilation with ffmpeg-compat

* Thu Jun 12 2008 kwizart < kwizart at gmail.com > - 0.8.6i-1
- Update to 0.8.6i
Security updates:
 * Fixed integer overflow in WAV demuxer (CVE-2008-2430)

Various bugfixes:
 * Fixed option to use shared memory within the GLX video output module
 * Miscellaneous bugfixes in multiple modules and in libvlc
   (transcode stream output, OSD menu video filter, VCD input,
    SAP services discovery, http control interface)
 * Updated Polish translation

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
- Move skin2 to main vlc package
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
- Remove unneeded fonts provided by skin2

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

* Tue Mar 22 2007 kwizart < kwizart at gmail.com > - 0.8.6a-4.4
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
