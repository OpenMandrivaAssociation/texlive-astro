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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Astrosym is a font containing astronomical symbols, including those used
for the planets, four planetoids, the phases of the moon, the signs of
the zodiac, and some additional symbols. The font is distributed as
Metafont source.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/doc/fonts/astro
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/source/public/astro
%dir %{_datadir}/texmf-dist/fonts/tfm/public/astro
%doc %{_datadir}/texmf-dist/doc/fonts/astro/astrosym.tex
%doc %{_datadir}/texmf-dist/doc/fonts/astro/astrosym.txt
%doc %{_datadir}/texmf-dist/fonts/source/public/astro/astrosym.cal
%doc %{_datadir}/texmf-dist/fonts/source/public/astro/astrosym.cmn
%doc %{_datadir}/texmf-dist/fonts/source/public/astro/astrosym.mac
%doc %{_datadir}/texmf-dist/fonts/source/public/astro/astrosym.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/astro/astrosym.uni
%doc %{_datadir}/texmf-dist/fonts/source/public/astro/astrosym.xtr
%{_datadir}/texmf-dist/fonts/tfm/public/astro/astrosym.tfm
