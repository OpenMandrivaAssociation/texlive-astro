%global tl_name astro
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.20
Release:	%{tl_revision}.1
Summary:	Astronomical (planetary) symbols
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/astro
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/astro.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/astro.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Astrosym is a font containing astronomical symbols, including those used
for the planets, four planetoids, the phases of the moon, the signs of
the zodiac, and some additional symbols. The font is distributed as
Metafont source.

