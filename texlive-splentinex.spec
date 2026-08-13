%global tl_name splentinex
%global tl_revision 77682
%global tl_version 1.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Splentinex fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/splentinex
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/splentinex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/splentinex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This is a serif font family designed for body text. This typeface design
was originally crated by Frank Pierpont and Fritz Stelzer in 1913 and
released by Monotype as Plantin. In 2025, Ben Byram-Wigfield created
Splentino, a new digitization of the Plantin design, for inclusion with
the music software Dorico. Splentinex is a modified repackaging of
Splentino.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from splentinex:
Map Splentinex.map
TL_DROPIN_EOF
