%define Werror_cflags	%nil
%define name         quakeforge
%define namegl       %{name}gl
%define namesw       %{name}sw
%define version      0.6.0
%define major        0
%define majorgl      0
%define majorsw      0
#
%define libname      %mklibname %name %major
%define libnamedevel %{libname}-devel
#
%define libnamegl    %mklibname %{namegl} %{majorgl}
%define libnamesw    %mklibname %{namesw} %{majorsw}

Summary:	QuakeForge 3D game engine
Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
Source:		%{name}-%{version}.tar.bz2
Source1:	%{name}16.png.bz2
Source2:	%{name}32.png.bz2
Source3:	%{name}48.png.bz2
Group:		Games/Arcade
License:	GPL
URL:		http://www.quakeforge.net/
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:  bison flex
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:  xmms-devel >= 0.9.5.1
BuildRequires:	GL-devel
BuildRequires:	svgalib-devel

%description
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

This package is in PLF because it requires non free data.

%package -n %libname
Summary: QuakeForge 3D game engine - common files and shared libraries
Group:	 Games/Arcade
Provides: lib%{name} = %{version}

%description -n %libname
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

This package contains shared libraries common to all QuakeForge packages.

%package -n %libnamedevel
Summary:  QuakeForge 3D game engine - headers and devel libs
Group:	  Games/Arcade
Requires: %{libname} = %{version}
Requires: %{libnamegl} = %{version}
Requires: %{libnamesw} = %{version}
Provides: lib%{name}-devel = %{version}

%description  -n %libnamedevel
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

This package contains headers and static libraries for the development of
utilities and applications for QuakeForge.

%package -n %libnamegl
Summary: QuakeForge 3D game engine - OpenGL renderer libraries
Group:	 Games/Arcade
Provides: lib%{name}-gl = %{version}

%description -n %libnamegl
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

This package contains the shared libraries needed to use the OpenGL
rendering targets.

%package -n %libnamesw
Summary: QuakeForge 3D game engine - Software renderer libraries
Group:	 Games/Arcade
Provides: lib%{name}-devel

%description -n %libnamesw
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

This package contains the shared libraries needed to use the software
rendering targets.

%package qfcc-devel
Summary:   QuakeForge QC/Ruamoko compiler
Group:	   Games/Arcade
Requires:  %libname-devel = %{version}
Provides:  qfcc
Obsoletes: qfcc

%description qfcc-devel
QFCC is an optimizing byte-code compiler for the Ruamoko language, a language
based strongly on Id Software's QuakeC. The bytecode interpreter for QuakeC
and Ruamoko is located inside the Quake engine (though there is a standalone
interpreter available).

QFCC is designed to work with the QuakeForge engines, but will work with
most non-QuakeForge servers with a couple of changes to its command-line
options.

#
# Quakeforge 3DFX clients
%package clients-3dfx
Summary:  QuakeForge 3D game engine - glx client
Group:	  Games/Arcade
Requires: quakeforge-common = %{version}
Requires: quakeforge-plugins = %{version}
Requires: %libname = %{version}
Requires: %libnamegl = %{version}

%description clients-3dfx
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

This package contains the 3DFX versions of the QuakeForge client and
standalone engine.

# Quakeforge framebuffer clients
%package clients-fbdev
Summary:  QuakeForge 3D game engine - framebuffer client
Group:	  Games/Arcade
Requires: quakeforge-common = %{version}
Requires: quakeforge-plugins = %{version}
Requires: %libname = %{version}
Requires: %libnamegl = %{version}
Requires: %libnamesw = %{version}

%description clients-fbdev
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

This package contains the FB versions of the QuakeForge client and
standalone engine.

# Quakeforge GLX clients
%package clients-glx
Summary:  QuakeForge 3D game engine - glx client
Group:	  Games/Arcade
Requires: quakeforge-common = %{version}
Requires: quakeforge-plugins = %{version}
Requires: %libname = %{version}
Requires: %libnamegl = %{version}

%description clients-glx
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

This package contains the GLX versions of the QuakeForge client and
standalone engine.

# Quakeforge SDL clients
%package clients-sdl
Summary:  QuakeForge 3D game engine - SDL client
Group:    Games/Arcade
Requires: quakeforge-common = %{version}
Requires: quakeforge-plugins = %{version}
Requires: %libname = %{version}
Requires: %libnamesw = %{version}

%description clients-sdl
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

This package contains the SDL versions of the QuakeWorld client and
standalone engine.

# Quakeforge SDL-GL clients
%package clients-sgl
Summary:   QuakeForge 3D game engine - SDL-GL client
Group:     Games/Arcade
Requires:  quakeforge-common = %{version}
Requires:  quakeforge-plugins = %{version}
Requires:  %libname = %{version}
Requires:  %libnamegl = %{version}
Provides:  quakeforge-clients-sdlgl
Obsoletes: quakeforge-clients-sdlgl

%description clients-sgl
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

This package contains the SDL-GL versions of the QuakeForge client and
standalone engine.

# Quakeforge SVGA clients
%package clients-svga
Summary:  QuakeForge 3D game engine - SVGAlib client
Group:	  Games/Arcade
Requires: quakeforge-common = %{version}
Requires: quakeforge-plugins = %{version}
Requires: libquakeforge = %{version}
Requires: libquakeforge-sw = %{version}

%description clients-svga
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

This package contains the SVGAlib versions of the QuakeWorld client and
standalone engine.

# Quakeforge X11 clients
%package clients-x11
Summary:  QuakeForge 3D game engine - X11 client
Group:    Games/Arcade
Requires: quakeforge-common = %{version}
Requires: quakeforge-plugins = %{version}
Requires: %libname = %{version}
Requires: %libnamesw = %{version}
Requires: svgalib

%description clients-x11
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

This package contains the X11 versions of the QuakeForge client and
standalone engine.

# Quakeforge common files
%package common
Summary: QuakeForge 3D game engine - common files and shared libraries
Group:	 Games/Arcade

%description common
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

This package contains common to all QuakeForge packages.

# Maptools
%package maptools
Summary:  QuakeForge 3D game engine - headers and devel libs
Group:	  Games/Arcade
Requires: %libname = %{version}

%description maptools
This package contains QuakeForge's versions of the tools Id Software used
to create maps for the Quake engine. Included are:

* qfbsp, a program for compiling a map file into a BSP tree.
* qflight, a program for generating lightmaps from the static lights in a
  BSP file.
* qfvis, a program for generating the Possibly-Visible Set information from
  a BSP and a portal information file (generated by qfbsp).

# Plugins
%package plugins
Summary: Plugins for QuakeForge
Group:	   Games/Arcade
Provides:  quakeforge-plugins-oss, quakeforge-plugins-alsa.
Obsoletes: quakeforge-plugins-oss, quakeforge-plugins-alsa.

%description plugins
Sound and CD driver plugins for Quakeforge.

%package servers
Summary:  QuakeForge 3D game engine - Server
Group:    Games/Arcade
Requires: %libname = %{version}

%description servers
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

This package contains both the QuakeWorld-compatible and
NetQuake-compatible dedicated servers, as well as a simple
QuakeWorld-compatible master server.

# Tools
%package utils
Summary:  QuakeForge 3D game engine - utility programs
Group:	  Games/Arcade
Requires: %libname = %{version}

%description utils
This package contains several tools for use with QuakeForge:
* pak, a pakfile management tool.
* zpak, a script for compressing pakfiles.
* qfdefs, a tool for fixing up progs data files so they can be used with
  QuakeForge-based servers.
* qfprogs, a "nm" tool for examining progs data files.
* qfwavinfo, a tool to assist in converting "looped" WAV files to Ogg Vorbis.

# Extract, compile and install
%prep
%setup -q


%build
autoconf

# Do not use the --with-svga switch if you want to build the SVGA
# clients, it will fail. Building the SVGA client just depends on
# having libsvgalib-devel installed yes or no...

CFLAGS="%{optflags}" \
./configure --prefix="%{_prefix}" \
	    --bindir="%{_gamesbindir}" \
	    --datadir="%{_datadir}" \
	    --includedir="%{_includedir}" \
	    --libdir="%{_libdir}/games/quakeforge" \
	    --mandir="%{_mandir}" \
	    --sysconfdir="%{_sysconfdir}" \
	    \
	    --with-global-cfg="%{_sysconfdir}/quakeforge.conf" \
	    --with-user-cfg="~/.quakeforge/quakeforgerc" \
	    --with-plugin-path="%{_libdir}/games/quakeforge/plugins" \
	    --with-sharepath="%{_gamesdatadir}/quakeforge" \
	    \
	    --disable-debug \
	    --with-arch="%{_target_cpu}" \
	    --without-fbdev \
	    --without-svga

%make

%install
rm -rf ${RPM_BUILD_ROOT}

make install DESTDIR="${RPM_BUILD_ROOT}" \
	     PLUGINDIR="${RPM_BUILD_ROOT}%{_libdir}/games/quakeforge/plugins"

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}
cp RPM/quakeforge.conf ${RPM_BUILD_ROOT}%{_sysconfdir}
bzip2 -c doc/man/quakeforge.1 > ${RPM_BUILD_ROOT}%{_mandir}/man1/quakeforge.1.bz2
cp tools/qwaq/.libs/qwaq ${RPM_BUILD_ROOT}%{_gamesbindir}

# Icons
install -d ${RPM_BUILD_ROOT}{%_miconsdir,%_liconsdir}
bzcat %{SOURCE1} > ${RPM_BUILD_ROOT}%{_miconsdir}/%name.png
bzcat %{SOURCE2} > ${RPM_BUILD_ROOT}%{_iconsdir}/%name.png
bzcat %{SOURCE3} > ${RPM_BUILD_ROOT}%{_liconsdir}/%name.png

# Menus
install -d ${RPM_BUILD_ROOT}%{_menudir}
install -d ${RPM_BUILD_ROOT}%{_datadir}/applications

for QFCLIENT in fbdev glx sdl sgl x11 ;do

    case ${QFCLIENT} in

	fbdev) TITLE="Framebuffer";;
	glx)   TITLE="GL";;
	sdl)   TITLE="SDL";;
	sgl)   TITLE="SDL-GL";;
	x11)   TITLE="X11";;

    esac

cat << EOF > ${RPM_BUILD_ROOT}%{_menudir}/%{name}-clients-${QFCLIENT}
?package(%{name}-clients-${QFCLIENT}): needs="x11" \\
				 section="More Applications/Games/Arcade" \\
				 title="QF QuakeWorld ${TITLE}" \\
				 longtitle="QuakeForge 3D game engine" \\
				 icon="%{name}.png" \\
				 command="%{_gamesbindir}/qfpaktest && %{_gamesbindir}/qw-client-${QFCLIENT}" \\
                		 xdg="true"

?package(%{name}-clients-${QFCLIENT}): needs="x11" \\
				 section="More Applications/Games/Arcade" \\
				 title="QF NQuake ${TITLE}" \\
				 longtitle="QuakeForge 3D game engine" \\
				 icon="%{name}.png" \\
				 command="%{_gamesbindir}/qfpaktest && %{_gamesbindir}/nq-${QFCLIENT}" \\
                		 xdg="true"
EOF

cat > ${RPM_BUILD_ROOT}%{_datadir}/applications/mandriva-%{name}-qw-${QFCLIENT}.desktop << EOF
[Desktop Entry]
Name=QF QuakeWorld ${TITLE}
Comment=QuakeForge 3D game engine
Exec=%{_gamesbindir}/qfpaktest && %{_gamesbindir}/qw-client-${QFCLIENT}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Encoding=UTF-8
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

cat > ${RPM_BUILD_ROOT}%{_datadir}/applications/mandriva-%{name}-nq-${QFCLIENT}.desktop << EOF
[Desktop Entry]
Name=QF NQuake ${TITLE}
Comment=QuakeForge 3D game engine
Exec=%{_gamesbindir}/qfpaktest && %{_gamesbindir}/nq-${QFCLIENT}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Encoding=UTF-8
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

for QFPACK in hipnotic rogue ; do

[ "${QFPACK}" = "hipnotic" ] && QFPACKTITLE="Mission Pack 1 - Scourge of Armagon"
[ "${QFPACK}" = "rogue" ] && QFPACKTITLE="Mission Pack 2 - Dissolution of Eternity"

cat > ${RPM_BUILD_ROOT}%{_datadir}/applications/mandriva-%{name}-nq-${QFCLIENT}-${QFPACK}.desktop << EOF
[Desktop Entry]
Name=QF NQuake ${TITLE}: ${QFPACKTITLE}
Comment=QuakeForge 3D game engine
Exec=%{_gamesbindir}/qfpaktest ${QFPACK} && %{_gamesbindir}/nq-${QFCLIENT} -game ${QFPACK}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Encoding=UTF-8
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

done

done

# Script to test if pakfiles are installed
cat > ${RPM_BUILD_ROOT}%{_gamesbindir}/qfpaktest << EOF
#!/bin/bash

for GAME in hipnotic rogue ; do

    if [ "\$1" = "\${GAME}" ]; then

	if [ ! -f %{_gamesdatadir}/quakeforge/\${GAME}/pak0.pak ]; then

	    if [ -n "\${DISPLAY}" ]; then

		xmessage -center "Error: \"%{_gamesdatadir}/quakeforge/\${GAME}/pak0.pak not found...\" 
       You should first install the Quake PAK file in 
       \"%{_gamesdatadir}/quakeforge/\${GAME}\""

	    else

		echo -e "Error: \"%{_gamesdatadir}/quakeforge/\${GAME}/pak0.pak not found...\""
		echo -e "You should first install the Quake PAK file in"
		echo -e "\"%{_gamesdatadir}/quakeforge/\${GAME}\""

	    fi

	    exit 1

	fi

    elif [ -z "\$1" ]; then

	for PAK in pak0.pak pak1.pak ; do

	    if [ ! -f %{_gamesdatadir}/quakeforge/id1/\${PAK} ]; then

		if [ -n "\${DISPLAY}" ]; then

		    xmessage -center "Error: \"%{_gamesdatadir}/quakeforge/id1/\${PAK} not found...\" 
       You should first install the Quake PAK files in 
       \"%{_gamesdatadir}/quakeforge/id1\""

		else

		    echo -e "Error: \"%{_gamesdatadir}/quakeforge/id1/\${PAK} not found...\""
		    echo -e "You should first install the Quake PAK files in"
		    echo -e "\"%{_gamesdatadir}/quakeforge/id1\""

		fi

		exit 1

	    fi

	done

    fi

done

exit 0
EOF

%clean
rm -rf ${RPM_BUILD_ROOT}

%post clients-fbdev
%{update_menus}

%postun clients-fbdev
%{clean_menus}

%post clients-glx
%{update_menus}

%postun clients-glx
%{clean_menus}

%post clients-sdl
%{update_menus}

%postun clients-sdl
%{clean_menus}

%post clients-sgl
%{update_menus}

%postun clients-sgl
%{clean_menus}

%post clients-x11
%{update_menus}

%postun clients-x11
%{clean_menus}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig


%files -n %libname
%defattr(-,root,root,755)
%dir %{_libdir}/games/quakeforge
%dir %{_libdir}/games/quakeforge/plugins
%{_libdir}/games/quakeforge/libQFcd.so
%{_libdir}/games/quakeforge/libQFcd.so.*
%{_libdir}/games/quakeforge/libQFconsole.so
%{_libdir}/games/quakeforge/libQFconsole.so.*
#%{_libdir}/games/quakeforge/libQFcsqc.so
#%{_libdir}/games/quakeforge/libQFcsqc.so.*
%{_libdir}/games/quakeforge/libQFgamecode.so
%{_libdir}/games/quakeforge/libQFgamecode.so.*
# %{_libdir}/games/quakeforge/libQFgamecode_builtins.so
# %{_libdir}/games/quakeforge/libQFgamecode_builtins.so.*
%{_libdir}/games/quakeforge/libQFgib.so
%{_libdir}/games/quakeforge/libQFgib.so.*
%{_libdir}/games/quakeforge/libQFimage.so
%{_libdir}/games/quakeforge/libQFimage.so.*
%{_libdir}/games/quakeforge/libQFjs.so
%{_libdir}/games/quakeforge/libQFjs.so.*
%{_libdir}/games/quakeforge/libQFmodels.so
%{_libdir}/games/quakeforge/libQFmodels.so.*
%{_libdir}/games/quakeforge/libQFruamoko.so
%{_libdir}/games/quakeforge/libQFruamoko.so.*
%{_libdir}/games/quakeforge/libQFsound.so
%{_libdir}/games/quakeforge/libQFsound.so.*
%{_libdir}/games/quakeforge/libQFutil.so
%{_libdir}/games/quakeforge/libQFutil.so.*

# Devel
%files -n %libnamedevel
%defattr(-,root,root,755)
%{_libdir}/games/quakeforge/libQFcd.*a
%{_libdir}/games/quakeforge/libQFconsole.*a
#%{_libdir}/games/quakeforge/libQFcsqc.*a
%{_libdir}/games/quakeforge/libQFgamecode.*a
# %{_libdir}/games/quakeforge/libQFgamecode_builtins.*a
%{_libdir}/games/quakeforge/libQFgib.*a
%{_libdir}/games/quakeforge/libQFimage.*a
%{_libdir}/games/quakeforge/libQFjs.*a
%{_libdir}/games/quakeforge/libQFmodels.*a
%{_libdir}/games/quakeforge/libQFmodels_gl.*a
%{_libdir}/games/quakeforge/libQFmodels_sw.*a
%{_libdir}/games/quakeforge/libQFsound.*a
%{_libdir}/games/quakeforge/libQFrenderer_gl.*a
%{_libdir}/games/quakeforge/libQFrenderer_sw32.*a
%{_libdir}/games/quakeforge/libQFruamoko.a
%{_libdir}/games/quakeforge/libQFutil.*a
%{_libdir}/games/quakeforge/plugins/*.a
# %{_libdir}/games/quakeforge/plugins/*.la
%dir %{_includedir}/QF
%{_includedir}/QF/*.h
%dir %{_includedir}/QF/GL
%{_includedir}/QF/GL/*.h
%dir %{_includedir}/QF/plugin
%{_includedir}/QF/plugin/*.h
%{_libdir}/games/quakeforge/qfcc/include/*
%{_libdir}/games/quakeforge/pkgconfig/*
%{_libdir}/games/quakeforge/qfcc/lib/*

# GL libs
%files -n %libnamegl
%defattr(-,root,root,755)
%{_libdir}/games/quakeforge/libQFmodels_gl.so
%{_libdir}/games/quakeforge/libQFmodels_gl.so.*
%{_libdir}/games/quakeforge/libQFrenderer_gl.so
%{_libdir}/games/quakeforge/libQFrenderer_gl.so.*

# Software libs
%files -n %libnamesw
%defattr(-,root,root,755)
%{_libdir}/games/quakeforge/libQFmodels_sw.so
%{_libdir}/games/quakeforge/libQFmodels_sw.so.*
%{_libdir}/games/quakeforge/libQFrenderer_sw32.so
%{_libdir}/games/quakeforge/libQFrenderer_sw32.so.*

# Qfcc compiler
%files qfcc-devel
%defattr(-,root,root,755)
%{_gamesbindir}/qfcc
%{_gamesbindir}/qfpreqcc
%{_mandir}/man1/qfcc.1*
# %dir %{_includedir}/QF/ruamoko
# %{_includedir}/QF/ruamoko/*
# %dir %{_libdir}/games/quakeforge/ruamoko
# %{_libdir}/games/quakeforge/ruamoko/*.a

# 3DFX clients
%files clients-3dfx
%defattr(-,root,root,755)
# %{_gamesbindir}/qw-client-3dfx
# %{_gamesbindir}/nq-3dfx

# Framebuffer clients
%files clients-fbdev
%defattr(-,root,root,755)
#%{_gamesbindir}/qw-client-fbdev
#%{_gamesbindir}/nq-3dfx
%{_menudir}/%{name}-clients-fbdev
%{_datadir}/applications/mandriva-%{name}-*-fbdev.desktop
%{_datadir}/applications/mandriva-%{name}-*-fbdev-*.desktop
# %{_gamesbindir}/nq-fbdev

# GLX clients
%files clients-glx
%defattr(-,root,root,755)
%{_gamesbindir}/qw-client-glx
%{_gamesbindir}/nq-glx
%{_menudir}/%{name}-clients-glx
%{_datadir}/applications/mandriva-%{name}-*-glx.desktop
%{_datadir}/applications/mandriva-%{name}-*-glx-*.desktop

# SDL clients
%files clients-sdl
%defattr(-,root,root,755)
%{_gamesbindir}/qw-client-sdl
%{_gamesbindir}/qw-client-sdl32
%{_gamesbindir}/nq-sdl
%{_gamesbindir}/nq-sdl32
%{_menudir}/%{name}-clients-sdl
%{_datadir}/applications/mandriva-%{name}-*-sdl.desktop
%{_datadir}/applications/mandriva-%{name}-*-sdl-*.desktop

# SDLGL clients
%files clients-sgl
%defattr(-,root,root,755)
%{_gamesbindir}/qw-client-sgl
%{_gamesbindir}/nq-sgl
%{_menudir}/%{name}-clients-sgl
%{_datadir}/applications/mandriva-%{name}-*-sgl.desktop
%{_datadir}/applications/mandriva-%{name}-*-sgl-*.desktop

# SVGA clients
%files clients-svga
%defattr(-,root,root,755)
# %attr(4755,root,root) %{_gamesbindir}/qw-client-svga
# %attr(4755,root,root) %{_gamesbindir}/nq-svga

# X11 clients
%files clients-x11
%defattr(-,root,root,755)
%{_gamesbindir}/qw-client-x11
%{_gamesbindir}/nq-x11
%{_menudir}/%{name}-clients-x11
%{_datadir}/applications/mandriva-%{name}-*-x11.desktop
%{_datadir}/applications/mandriva-%{name}-*-x11-*.desktop

# Common files
%files common
%defattr(-,root,root,755)
%doc COPYING NEWS TODO 
%config(noreplace) %{_sysconfdir}/quakeforge.conf
%attr(755,root,root) %{_gamesbindir}/qfpaktest
%dir %{_gamesdatadir}/quakeforge
%dir %{_gamesdatadir}/quakeforge/QF
%{_gamesdatadir}/quakeforge/QF/menu.dat*
#%{_gamesdatadir}/quakeforge/QF/game.dat
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
%{_mandir}/man1/quakeforge.1.*
%{_mandir}/man1/zpak.1.*
%{_gamesdatadir}/quakeforge/QF/menu.plist
%{_gamesdatadir}/quakeforge/QF/menu.sym.gz

# Maptools
%files maptools
%defattr(-,root,root,755)
%{_gamesbindir}/bsp2img
%{_gamesbindir}/hw-master
%{_gamesbindir}/qfbsp
%{_gamesbindir}/qflight
%{_gamesbindir}/qfvis
%{_gamesbindir}/qflmp
%{_gamesbindir}/qfpc
%{_mandir}/man1/qflight.1*
%{_mandir}/man1/qfvis.1*

# Plugins
%files plugins
%defattr(-,root,root,755)
%{_libdir}/games/quakeforge/plugins/cd_file.so
%{_libdir}/games/quakeforge/plugins/cd_linux.so*
# %{_libdir}/games/quakeforge/plugins/cd_null.so*
%{_libdir}/games/quakeforge/plugins/cd_sdl.so*
# %{_libdir}/games/quakeforge/plugins/cd_xmms.so*
%{_libdir}/games/quakeforge/plugins/console_client.so*
%{_libdir}/games/quakeforge/plugins/snd_output_disk.so*
# %{_libdir}/games/quakeforge/plugins/snd_output_null.so*
# %{_libdir}/games/quakeforge/plugins/snd_output_sdl.so*
# %{_libdir}/games/quakeforge/plugins/snd_render_default.so*
# %{_libdir}/games/quakeforge/plugins/snd_output_alsa.so*
# %{_libdir}/games/quakeforge/plugins/snd_output_oss.so*

# Servers
%files servers
%defattr(-,root,root,755)
%{_gamesbindir}/qw-server
%{_gamesbindir}/nq-server
%{_gamesbindir}/qw-master
%{_gamesbindir}/qtv
%{_libdir}/games/quakeforge/plugins/console_server.so*

# Tools
%files utils
%defattr(-,root,root,755)
%{_gamesbindir}/pak
%{_gamesbindir}/zpak
#%{_gamesbindir}/qfdefs
%{_gamesbindir}/qfmodelgen
%{_gamesbindir}/qfprogs
%{_gamesbindir}/qfwavinfo
%{_gamesbindir}/qwaq
%{_gamesbindir}/wad
%{_mandir}/man1/pak.1*
%{_mandir}/man1/wad.1*

