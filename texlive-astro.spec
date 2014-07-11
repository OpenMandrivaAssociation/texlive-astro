# revision 15878
# category Package
# catalog-ctan /fonts/astro
# catalog-date 2008-10-03 22:28:15 +0200
# catalog-license lppl
# catalog-version 2.20
Name:		texlive-astro
Version:	2.20
Release:	8
Summary:	Astronomical (planetary) symbols
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/astro
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/astro.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/astro.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.20-2
+ Revision: 749357
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.20-1
+ Revision: 717864
- texlive-astro
- texlive-astro
- texlive-astro
- texlive-astro
- texlive-astro

