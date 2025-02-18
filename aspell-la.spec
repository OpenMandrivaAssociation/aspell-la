%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 20020503-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Latin
%define languagecode la
# FIXME:	no locale yet
%define lc_ctype la_

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	20020503.0
Release:	22
Group:		System/Internationalization
Url:		https://aspell.net/
License:	GPLv2
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= %{aspell_ver}
BuildRequires:	make
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
#Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
#Provides:	aspell-%{lc_ctype}
Provides:	spell-%{languagecode}
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

chmod 644 Copyright README* 

%files
%doc README* Copyright 
%{_libdir}/aspell-%{aspell_ver}/*

