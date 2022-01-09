#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Optional compilation for OCaml
Summary(pl.UTF-8):	Opcjonalna kompilacja dla OCamla
Name:		ocaml-ppx_optcomp
Version:	0.14.3
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_optcomp/tags
Source0:	https://github.com/janestreet/ppx_optcomp/archive/v%{version}/ppx_optcomp-%{version}.tar.gz
# Source0-md5:	2d012df62dd0bc82d2ea4ab25b628992
URL:		https://github.com/janestreet/ppx_optcomp
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune-devel >= 2.0.0
BuildRequires:	ocaml-ppxlib-devel >= 0.18.0
BuildRequires:	ocaml-stdio-devel >= 0.14
BuildRequires:	ocaml-stdio-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
ppx_optcomp stands for Optional Compilation. It is a tool used to
handle optional compilations of pieces of code depending of the word
size, the version of the compiler, ...

This package contains files needed to run bytecode executables using
ppx_optcomp library.

%description -l pl.UTF-8
ppx_optcomp oznacza Optional Compilation, czyli opcjonalną kompilację.
Jest to narzędzie służące do obsługi opcjonalnej kompilacji fragmentów
kodu w zależności od rozmiaru słowa, wersji kompilatora itd.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_optcomp.

%package devel
Summary:	ppx_optcomp binding for OCaml - development part
Summary(pl.UTF-8):	Wiązania ppx_optcomp dla OCamla - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-dune-devel >= 2.0.0
Requires:	ocaml-ppxlib-devel >= 0.18.0
Requires:	ocaml-stdio-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
ppx_optcomp library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_optcomp.

%prep
%setup -q -n ppx_optcomp-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_optcomp/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_optcomp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_optcomp
%{_libdir}/ocaml/ppx_optcomp/META
%{_libdir}/ocaml/ppx_optcomp/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_optcomp/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_optcomp/*.cmi
%{_libdir}/ocaml/ppx_optcomp/*.cmt
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_optcomp/ppx_optcomp.a
%{_libdir}/ocaml/ppx_optcomp/*.cmx
%{_libdir}/ocaml/ppx_optcomp/*.cmxa
%endif
%{_libdir}/ocaml/ppx_optcomp/dune-package
%{_libdir}/ocaml/ppx_optcomp/opam
