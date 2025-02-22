Name:		texlive-astro
Version:	15878
Release:	2
Summary:	Astronomical (planetary) symbols
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/astro
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/astro.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/astro.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Astrosym is a font containing astronomical symbols, including
those used for the planets, four planetoids, the phases of the
moon, the signs of the zodiac, and some additional symbols. The
font is distributed in MetaFont format.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/astro/astrosym.cal
%{_texmfdistdir}/fonts/source/public/astro/astrosym.cmn
%{_texmfdistdir}/fonts/source/public/astro/astrosym.mac
%{_texmfdistdir}/fonts/source/public/astro/astrosym.mf
%{_texmfdistdir}/fonts/source/public/astro/astrosym.uni
%{_texmfdistdir}/fonts/source/public/astro/astrosym.xtr
%{_texmfdistdir}/fonts/tfm/public/astro/astrosym.tfm
%doc %{_texmfdistdir}/doc/fonts/astro/astrosym.tex
%doc %{_texmfdistdir}/doc/fonts/astro/astrosym.txt

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
