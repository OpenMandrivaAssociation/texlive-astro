Name:		texlive-astro
Version:	2.20
Release:	1
Summary:	Astronomical (planetary) symbols
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/astro
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/astro.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/astro.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Astrosym is a font containing astronomical symbols, including
those used for the planets, four planetoids, the phases of the
moon, the signs of the zodiac, and some additional symbols. The
font is distributed in MetaFont format.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}